# Test Cases for Profile README

## Purpose
This directory validates that the profile UI content in `README.md` remains complete, structured, and aligned with the documented tech stack and use-case outcomes.

## Structure
- `test_readme_structure.py`
  - Verifies critical sections exist.
  - Guards against accidental removal of core technologies and AI platforms/tooling mentions (Antigravity, OpenAI Codex, OpenCLAW, ChatGPT, Gemini, Claude).
  - Enforces that the `Featured Projects` section is removed.

## Coverage Summary
- **Positive scenarios:** expected sections and technologies/tooling mentions are present.
- **Negative scenarios:** missing sections or missing key technology mentions will fail tests.
- **Regression guard:** if `## 🌟 Featured Projects` is reintroduced, tests fail.
- **Failure simulation scope:** network-dependent checks are intentionally excluded to keep tests deterministic in offline/CI-constrained environments.

## Run
From repository root:

```bash
python -m unittest tests/test_readme_structure.py
```
