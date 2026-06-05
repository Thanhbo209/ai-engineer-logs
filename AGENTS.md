# AGENTS.md

## Purpose

This repo is a long-term AI engineering roadmap. It tracks a 28-phase study journey with reading notes, small code snippets, runnable practice projects, resources, progress tracking, and later portfolio work.

Agents should keep the repo useful for two audiences:

- The learner, who needs clear notes, evidence of mastery, and runnable practice code.
- Recruiters or engineers reviewing the repo, who need a quick README, visible progress, and a few strong project links.

## Operating Rules

- Do not create the full 28-phase scaffold unless explicitly asked.
- Keep reading notes and runnable project code separate.
- Put understanding, summaries, and small reading snippets in `notes/`.
- Put runnable mini-projects, experiments, apps, and tests in `practice/`.
- Keep changes phase-scoped unless the request is clearly repo-wide.
- Update `progress.md` when phase status changes.
- Do not treat a phase as complete until its `mastery.md` has concrete evidence for the criteria.
- Never commit `.env` files or real secrets. Use `.env.example` with placeholder values.
- Pin dependencies with `pip freeze > requirements.txt` only after a project works.
- Do not polish notes like production code. Notes are for understanding; projects are for execution.

## Canonical Layout

Use this shape as the target structure. The current repo may only contain part of it; do not scaffold missing folders unless requested.

```text
ai-engineer-roadmap/
|-- notes/
|   |-- phase-01-foundations/
|   |   |-- notes.md
|   |   |-- snippets.py
|   |   `-- mastery.md
|   |-- phase-02-python-advanced/
|   |-- phase-03-data-tools/
|   |-- phase-04-sql-nosql/
|   |-- phase-05-math-stats/
|   |-- phase-06-ml-methodology/
|   |-- phase-07-classical-ml/
|   |-- phase-08-deep-learning/
|   |-- phase-09-computer-vision/
|   |-- phase-10-nlp-basics/
|   |-- phase-11-transformers/
|   |-- phase-12-llms/
|   |-- phase-13-prompt-engineering/
|   |-- phase-14-rag/
|   |-- phase-15-vector-dbs/
|   |-- phase-16-agents/
|   |-- phase-17-fine-tuning/
|   |-- phase-18-evaluation/
|   |-- phase-19-ai-backend/
|   |-- phase-20-mlops/
|   |-- phase-21-deployment/
|   |-- phase-22-cloud/
|   |-- phase-23-security/
|   |-- phase-24-observability/
|   |-- phase-25-system-design/
|   |-- phase-26-portfolio/
|   |-- phase-27-career/
|   `-- phase-28-specialization/
|-- practice/
|   |-- phase-01-foundations/
|   |-- phase-03-data-tools/
|   |-- phase-06-ml-methodology/
|   |-- phase-07-classical-ml/
|   |-- phase-08-deep-learning/
|   |-- phase-09-cv/
|   |-- phase-10-nlp/
|   |-- phase-11-transformers/
|   |-- phase-12-llms/
|   |-- phase-13-prompts/
|   |-- phase-14-rag/
|   |-- phase-15-vector-dbs/
|   |-- phase-16-agents/
|   |-- phase-17-fine-tuning/
|   |-- phase-18-evals/
|   |-- phase-19-ai-backend/
|   |-- phase-20-mlops/
|   |-- phase-21-deployment/
|   |-- phase-22-cloud/
|   `-- phase-26-portfolio/
|-- resources/
|   |-- reading-list.md
|   `-- cheatsheets/
|-- AIEngineer.html
|-- progress.md
`-- README.md
```

## Notes Rules

Each phase folder under `notes/` should use these files when applicable:

- `notes.md`: personal notes, summaries, and explanations from reading.
- `snippets.py`: small code bits tested while reading. This is not the place for full projects.
- `mastery.md`: copied roadmap mastery criteria plus one sentence of evidence for each completed item.

`mastery.md` should describe what was actually done, not just what was read.

Example:

```markdown
# Phase 11 - Transformers mastery

## Criteria

- [x] Explain attention end-to-end
  - Wrote a blog-style explanation in notes.md and reviewed it against diagrams.
- [x] Implement scaled dot-product attention in PyTorch
  - Built and tested practice/phase-11-transformers/attention-scratch/attention.py.
- [ ] Fine-tune a model on a small classification task
```

## Practice Project Rules

Practice projects belong under `practice/phase-XX-topic/project-name/`.

Each runnable mini-project should include:

```text
project-name/
|-- README.md
|-- main.py
|-- requirements.txt
|-- .env.example
`-- tests/
    `-- test_basic.py
```

Project README files should answer:

- What the project does.
- Why it was built for this phase.
- What was learned.
- How to run it.
- The architecture or data flow, in a short paragraph or small diagram.

Keep one commit per mini-project milestone when this repo is under Git. Use commit messages like:

```text
feat(phase-12): add streaming chat with token cost tracking
```

## Top-Level README Rules

The top-level `README.md` is recruiter-facing. It should answer these questions quickly:

- What is this repo?
- How far along is the roadmap?
- Who is the learner?
- Where is the most interesting code?

Use this structure:

- Hero header: repo title and 1-2 sentence description.
- Progress tracker: phase, topic, status.
- Featured projects: 3-4 strongest links with one-line descriptions.
- Tech stack: tools actually used across projects.

Do not list tools that were only read about. Only list tools used in notes, snippets, or projects.

## Progress And Mastery

`progress.md` should have one line per phase and a simple status. Use these statuses consistently:

- `Done`
- `In progress`
- `Not started`

Before moving from Phase N to Phase N+1:

- Update the phase notes.
- Fill in `mastery.md` with criteria and evidence.
- Update `progress.md`.
- Link any related practice project.

## Phase Project Groupings

Some phases are conceptual and should share a practice project instead of forcing a standalone app.

| Phases | Cluster                          | Practice guidance                                                      |
| ------ | -------------------------------- | ---------------------------------------------------------------------- |
| 01-02  | Python core                      | Separate micro-scripts per concept are fine.                           |
| 03-04  | Data + SQL                       | One EDA + SQL query project covers both.                               |
| 05     | Math/stats                       | Notes + Jupyter notebook; no separate project required.                |
| 06-07  | Classical ML                     | One full sklearn project with proper evaluation.                       |
| 08-09  | DL + CV                          | One PyTorch training-loop project plus fine-tuned ResNet.              |
| 10-11  | NLP + Transformers               | Separate TF-IDF baseline and attention-from-scratch projects.          |
| 12-13  | LLMs + Prompts                   | One streaming chat app with eval-backed prompts.                       |
| 14-15  | RAG + Vectors                    | One RAG system with hybrid retrieval and cited answers.                |
| 16     | Agents                           | Standalone bounded tool agent; this is a flagship project.             |
| 17-18  | Fine-tuning + Evals              | One LoRA run plus eval suite against a baseline.                       |
| 19-21  | Backend + Ops                    | One production API with streaming, Docker, and health checks.          |
| 22-24  | Cloud + Security + Observability | Add cloud deploy, tracing, and secrets handling to the production API. |
| 25-26  | Design + Portfolio               | Write ADR docs and build 2-3 flagship repos.                           |

## Ground Rules

- Notes are not code. Practice is not scratch notes. Cross-link between them when needed.
- Keep everything in this monorepo until Phase 26 portfolio work, unless the user asks for standalone repos.
- Portfolio projects should eventually have polished READMEs, live demos when possible, architecture diagrams, and detailed writeups.
- After finishing a phase, add a short public-writing draft or summary if the user asks for blog or LinkedIn material.
- Preserve existing files and user changes. Do not rewrite unrelated notes, progress files, or project files.
