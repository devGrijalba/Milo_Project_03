"""Scores computed locally from rubric scores; no model supplied overall score trusted.

Revision count is now 1 by default with a conditional second pass. The old gate
required EXACTLY two reviews; it is replaced by a minimum of one plus the
orchestrator's conditional trigger. Thresholds (90 per dimension, per
perspective, and for the composite) are NOT relaxed, and the judge-disagreement
check still applies whenever two reviews actually exist.
"""
import math
from src.common import DIMENSIONS, digest

WEIGHTS = {
    'facebook_viewer': {'hook': .30, 'narrative': .25, 'emotion': .20, 'shareability': .25},
    'cinematic_director': {'narrative': .30, 'visual': .30, 'editing': .25, 'voice': .15},
    'milo_director': {'milo': .60, 'emotion': .20, 'visual': .20},
}


def _review_checks(x, p, c, check):
    """Per-review contract checks. Shared by the one-review and two-review paths."""
    issues = []
    issues.extend(check(x, p, c))
    if x.get('rubric_version') != '1.0.0':
        issues.append('Rubric version missing')
    if x.get('confidence') not in ['medium', 'high']:
        issues.append('Insufficient confidence')
    for k in DIMENSIONS:
        d = x.get('dimensions', {}).get(k, {})
        refs = d.get('beat_ids', [])
        available = {b['beat_id'] for b in p['beats']}
        if not refs or not isinstance(refs, list) or any(v not in available for v in refs):
            issues.append('Invalid beat evidence references ' + k)
        if not isinstance(d.get('improvement'), str):
            issues.append('Improvement explanation missing ' + k)
    for k in ['canon_comparison', 'mining_comparison', 'history_comparison']:
        if not isinstance(x.get(k), str) or not x[k].strip():
            issues.append('Missing comparison ' + k)
    return issues


def aggregate(report, p, c, check):
    if not isinstance(report, dict) or not isinstance(report.get('reviews'), list):
        return ['Review report required'], None
    reviews = report['reviews']
    issues = []

    minimum = int(c.get('min_review_passes') or 1)
    if len(reviews) < minimum:
        return ['At least %d review pass required' % minimum], None
    if len(reviews) > 2:
        return ['At most two review passes'], None

    ids = [x.get('review_id') if isinstance(x, dict) else None for x in reviews]
    if len(set(ids)) != len(ids) or not all(ids):
        issues.append('Distinct review IDs required')
    for x in reviews:
        if not isinstance(x, dict):
            return ['Review must be object'], None
        issues.extend(_review_checks(x, p, c, check))
    if issues:
        return issues, None

    scores = {k: min(x['dimensions'][k]['score'] for x in reviews) for k in DIMENSIONS}

    differences = {}
    if len(reviews) == 2:
        differences = {k: abs(reviews[0]['dimensions'][k]['score'] - reviews[1]['dimensions'][k]['score'])
                       for k in DIMENSIONS}
        for k, d in differences.items():
            if d > c['max_judge_disagreement']:
                issues.append('Review disagreement requires re-evaluation: ' + k)

    perspectives = {role: round(sum(scores[k] * w for k, w in weights.items()), 2)
                    for role, weights in WEIGHTS.items()}
    overall = round(.4 * perspectives['facebook_viewer']
                    + .3 * perspectives['cinematic_director']
                    + .3 * perspectives['milo_director'], 2)
    for k, v in perspectives.items():
        if v < 90:
            issues.append('Perspective below 90: ' + k)
    if overall < 90:
        issues.append('Composite below 90')
    if issues:
        return issues, None

    card = {
        'dimensions': scores,
        'perspectives': perspectives,
        'overall': overall,
        'judge_disagreement': differences,
        'review_passes': len(reviews),
        'minimum': 90,
        'aggregation': ('Minimum per dimension across passes, then weighted scores'
                        if len(reviews) > 1
                        else 'Minimum per dimension across one pass, then weighted scores'),
        'calibration': 'PROVISIONAL_NOT_AUDIENCE_VALIDATED',
    }
    return issues, card
