# DEEPSEEK_REAL_GATE_01 — run report

- episode: `EP0001`
- seed: `MILO-S0001`
- role: `script_hook_specialist`
- parallelism: 1 (critic/synthesizer/repair OFF)
- elapsed: 1790765049s
- criteria: 10/11 PASS
- failure class: **CONTRACT**

## Criteria

- PASS — request_built (seed=MILO-S0001)
- PASS — tab_acquired (owner=specialist_script_hook_specialist)
- PASS — composer_present (readyState=complete login_wall=False)
- PASS — prompt_injected (wrote=WROTE)
- PASS — read_back_exact (sent=15517 chars, composer=15517 chars)
- PASS — composer_cleared_after_send
- PASS — response_received (16,071 chars in 1790765049s, 26 polls)
- PASS — json_extracted (dict)
- FAIL — specialist_contract_valid (errors=missing:role,missing:proposals,missing:evidence,missing:risks,missing:handoff,too_large:16110>6000)
- PASS — tab_reset (navigated to a fresh chat)
- PASS — tab_released

## Artifacts

- `request.json` — the built request
- `prompt.txt` — exactly what was typed into the composer
- `raw_response.txt` — DeepSeek's reply, unmodified
- `parsed_response.json` — what the extractor recovered
- `validation.json` — contract check
- `gate_result.json` — machine-readable result

## Failure classification

- JSON parsed but does not satisfy the specialist contract: missing:role,missing:proposals,missing:evidence,missing:risks,missing:handoff,too_large:16110>6000

Prompts were NOT modified. Calibration is a separate step.
