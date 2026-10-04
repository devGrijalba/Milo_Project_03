# Relocatable package: build, prove, lint

Recipe for a deliverable that must run from any directory. Validated on a
Google Flow image-generation toolchain: 108 files, 51 MB, zero npm dependencies.

## Build it reproducibly from a script

The build script is part of the deliverable. A package assembled by hand cannot
be rebuilt, and the first thing that breaks after an edit is a file nobody
remembered to re-copy.

- **Resolve the root from the script's own location**, never from `pwd`:
  `HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"`. Then assert the
  expected structure exists (`[ ! -d "$SRC/src" ] && exit 1`) before building —
  a wrong root writes to the wrong place and the error surfaces only as an
  empty package.
- **Never silence a copy step.** `cp ... 2>/dev/null || true` converts "did not
  copy" into "looks like it copied". A build can report OK while producing nine
  empty directories.
- **`cp` on a path with a subdirectory copies the CONTENT, not the folder.**
  `cp -r "GOOGLE FLOW/doc" dest/` lands `doc/` at the destination root, so the
  index file ends up outside the folder the docs say it lives in. Use
  `cp --parents -r` to preserve the full path.
- **Allow overriding the destination** (`FLOW_PORTABLE_DEST=...`). A folder with
  the cwd of a live process in it makes `rm -rf` fail with `Device or resource
  busy`; warn and let the caller pick another path instead of building on top of
  a half-cleared tree.
- **Verify a required-file list at the end and exit nonzero** if any entry is
  missing. This is the gate that turns a silent partial package into a loud one.

## The acceptance run

```bash
cd "$TMP" && rm -rf extract && mkdir extract
unzip -q package.zip -d extract/RENAMED_NAME     # new dir, new name
cd extract/RENAMED_NAME
<real entrypoint>                                 # the command users will run
```

Renaming matters: it proves nothing in the artifact points at the build path.
Run it three ways: the real entrypoint, the linter, and the project's own test
suite — all from the extracted copy.

## A portability linter must be correct before it can be trusted

Static scan of the shipped tree for two distinct hazards:

| Hazard | Verdict | Why |
|---|---|---|
| Absolute machine path (`D:\...`) | **FAIL** | breaks on move |
| System path (`C:/Program Files`, `AppData`) | **WARN** | decided by the OS, not the package |
| Relative path written by hand | **FAIL** | depends on cwd; fails silently elsewhere |

The third is the expensive one and the one a regex gets wrong. Six false
positives that each had to be fixed before the linter was trustworthy:

- **A URL is not a path.** `ws://localhost:8765` matches `[A-Za-z]:[/\\]` as
  `s://localhost`. Require a whitespace/quote boundary before the drive letter
  AND a slash immediately after the colon.
- **Spaces are part of the path.** `C:/Program Files/...` captured as
  `C:/Program` never matches the system-prefix list, so a legitimate system path
  reports as a machine path. Capture spaces, trim afterwards.
- **The linter's own whitelist must not trip it.** Exclude the linter file
  itself, and compare paths with both separators — `relative()` yields
  `tools\x.js` on Windows and `tools/x.js` on Linux.
- **Provenance strings are not accesses.** `source: 'knowledge/world_lock.json'`
  exists to be READ as relative, to audit where a value came from. Filtering on
  `source:`/`note:`/`why:`/log calls is correct, not a suppression.
- **A declared constant is not the access.** `const RULES = {a: 'knowledge/...'}` +
  `readFile(fromRoot(p))` is correct. Test the FILE for an anchor applied to a
  disk call, not the shape of the declaration line.
- **A file that never opens a file cannot have unanchored paths.**
  `scene.resolver.js` declares paths purely for provenance and reads nothing
  (a `Catalog` reads). Require an `opensFiles()` check first.

When a linter produces findings that are all wrong, fix the linter's LOGIC.
Never add an exclusion list to make it green — a checker you have to silence is
no longer a checker, and the real defect ships.

## Test regexes in isolation before wiring them in

Every one of the six above was found by running the linter against known-good
and known-bad lines. Print what each captures and compare with what the line
actually says; a regex that looks right in the source is routinely wrong in the
string.

## Ship the rules a foreign session follows

A relocatable package needs its own `START.md` at the root: the current route,
the exact commands, prerequisites, a troubleshooting table ordered by
probability, the folder tree, and the one invariant that explains the design
(the two asset universes: a master carries silhouette, a crop carries one
attribute and nothing else).

State which path CANNOT be made relative and how to override it — typically the
browser's download directory, which the OS decides. An undocumented
un-relativizable path reads as a portability bug to the next person.
