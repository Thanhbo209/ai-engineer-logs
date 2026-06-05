# Phase 0 - Orientation & Setup

## Mastery Criteria

- [x] Create an isolated environment
  - Evidence: Created `.venv` in the repo root with `python -m venv .venv`.
  - Note: A project-specific environment keeps installed packages separate from system Python and other projects.

- [x] Install packages
  - Evidence: Installed `requests` inside `.venv` and generated `requirements.txt` with `.venv\Scripts\python.exe -m pip freeze > requirements.txt`.
  - Note: Dependencies are pinned after the environment works so the setup can be reproduced.

- [x] Keep secrets out of GitHub
  - Evidence: Added `.env` to `.gitignore` and created `.env.example` with placeholder values only.
  - Note: Local secrets belong in `.env`; public examples belong in `.env.example`.

- [x] Push branched code to GitHub
  - Evidence: Initialized Git, created branch `phase-0-setup`, and made local commit `550a03b` with message `feat(phase-0): add learning log setup`.
  - Pending: Add a GitHub remote and push `phase-0-setup`.
  - Note: Phase 0 should remain `In progress` until the branch and first commit are pushed to GitHub.
