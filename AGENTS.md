# AGENTS.md

## Purpose

This repo is a long-term learning monorepo for becoming a strong software engineer first, then specializing in AI engineering.

Agents should keep the repo useful for two audiences:

- The learner, who needs clear notes, evidence of mastery, and runnable practice code.
- Recruiters or engineers reviewing the repo, who need quick orientation, visible progress, and links to strong projects.

## Strategic Direction

The roadmap has two major tracks:

1. Software Engineering Core
2. AI Engineering Specialization

Software Engineering comes first. AI Engineering comes later after the core is strong enough to support deeper work with ML, LLMs, RAG, agents, evaluation, and AI backend systems.

## Operating Rules

- Keep the repo software-engineering-first unless the user explicitly asks to work on AI specialization.
- Do not create the full roadmap scaffold unless explicitly asked.
- Create only folders needed for the current stage, plus clear placeholders when Git would otherwise lose an important active folder.
- Keep reading notes and runnable code separate.
- Put understanding, summaries, diagrams, explanations, and reading snippets in `notes/`.
- Put small runnable exercises, drills, snippets, and isolated experiments in `practice/`.
- Put larger portfolio-style builds in `projects/`.
- Put reading lists, links, cheatsheets, and references in `resources/`.
- Put outdated roadmap material in `archive/` instead of deleting it.
- Do not delete existing work. Archive old AI-first material under `archive/old-ai-roadmap/` when it no longer fits.
- Do not create full AI track folders unless the user asks for AI-track work.
- Keep changes topic-scoped unless the request is clearly repo-wide.
- Update `progress.md` when topic status changes.
- Do not treat a topic as complete until its `mastery.md` has concrete evidence for the criteria.
- Never commit `.env` files or real secrets. Use `.env.example` with placeholder values.
- Pin dependencies with `pip freeze > requirements.txt` only after a project works.
- Do not polish notes like production code. Notes are for understanding; projects are for execution.

## Canonical Layout

Use this shape as the long-term target. The current repo may only contain part of it; do not scaffold missing folders unless requested.

```text
software-engineering-to-ai-engineering-roadmap/
|-- README.md
|-- AGENTS.md
|-- ROADMAP.md
|-- progress.md
|-- notes/
|   |-- software-engineering/
|   `-- ai-engineering/
|-- practice/
|   |-- software-engineering/
|   `-- ai-engineering/
|-- projects/
|   |-- swe/
|   `-- ai/
|-- resources/
|   |-- software-engineering/
|   |-- ai-engineering/
|   `-- cheatsheets/
`-- archive/
    `-- old-ai-roadmap/
```

## Current Active Stage

Focus on Software Engineering Core:

```text
notes/software-engineering/01-programming-fundamentals/
notes/software-engineering/02-computer-science-foundations/
practice/software-engineering/01-programming-fundamentals/
practice/software-engineering/02-computer-science-foundations/
```

## Notes Rules

Each topic folder under `notes/` should use these files when applicable:

- `notes.md`: personal notes, summaries, and explanations from reading.
- `snippets.md` or `snippets.py`: small examples tested while learning. This is not the place for full projects.
- `mastery.md`: topic mastery criteria plus evidence for completed items.

`mastery.md` should describe what was actually done, not just what was read.

Example:

```markdown
# Backend Engineering Mastery

## Criteria

- [x] Build a small HTTP API
  - Evidence: Built and tested `projects/swe/backend-api`.
- [ ] Add authentication middleware
```

## Practice Rules

Practice work belongs under `practice/track/topic/exercise-name/` when there is runnable code.

Use this structure for runnable practice exercises:

```text
exercise-name/
|-- README.md
|-- src/
|-- tests/
`-- package/dependency file if needed
```

Practice README files should answer:

- What the exercise does.
- Why it was built for this topic.
- What was learned.
- How to run it.

## Project Rules

Portfolio-style projects belong under `projects/swe/` or `projects/ai/`.

Projects should eventually include:

- A clear README.
- Setup and run instructions.
- Tests where useful.
- Architecture or data-flow notes.
- Evidence links from the related `mastery.md`.

## Top-Level README Rules

The top-level `README.md` is recruiter-facing. It should answer quickly:

- What this repo is.
- The current focus.
- How the repo is structured.
- How progress is tracked.
- Where the strongest projects are once they exist.

Do not list tools that were only read about. Only list tools used in notes, snippets, practice, or projects.

## Progress And Mastery

`progress.md` should have one line per topic and a simple status. Use these statuses consistently:

- `Done`
- `In progress`
- `Not started`

Before moving a topic to `Done`:

- Update the topic notes.
- Fill in `mastery.md` with criteria and evidence.
- Link related practice or project work.
- Update `progress.md`.

## Ground Rules

- Notes are not projects. Practice is not scratch notes. Projects are portfolio builds.
- Keep everything in this monorepo until portfolio work requires standalone repos, unless the user asks otherwise.
- Do not create frontend, backend, AI, or deployment apps during a structure-only refactor.
- Preserve existing files and user changes. Do not rewrite unrelated notes, progress files, or project files.
