---
id: 1
title: Setup Project Constitution and Principles
stage: constitution
date: 2025-12-06
surface: agent
model: gemini
feature: none
branch: master
user: user
command: /sp.constitution
labels: [constitution, setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- .specify/memory/constitution.md
- .specify/templates/plan-template.md
- .specify/templates/tasks-template.md
tests:
- none
---

## Prompt

/sp.constitution Project Principles:
- **Evolutionary Architecture**: We start as a Console App (Phase I) and evolve into a Cloud-Native System (Phase V).
- **Business First**: Focus on user value. Phase I must be simple and fast; do not over-engineer.
- **No "Magic Code"**: All code must be explicit, typed, and documented.
- **Monorepo Structure**: Eventually separates into /frontend and /backend, but starts simple.

Technical Stack (Phased):
- **Global**: Python 3.13+, `uv` package manager, Conventional Commits.
- **Phase I (Current)**:
    - Interface: CLI (Command Line Interface).
    - Storage: In-Memory (Variables/Classes).
    - Logic: Pure Python (No web frameworks).
- **Phase II+ (Future)**:
    - Frontend: Next.js 16+ (App Router), TypeScript, Tailwind.
    - Backend: FastAPI, SQLModel.
    - Database: Neon Serverless PostgreSQL.

Quality Standards (Immutable):
- **Type Hints**: All Python functions MUST have type hints (e.g., `def add(a: int) -> int:`).
- **Docstrings**: All classes and functions must have docstrings explaining intent.
- **TDD**: Write tests first. Use `pytest` for Python logic.
- **Clean Code**: Use Dataclasses for models. Separate data (Model) from logic (Controller) even in a simple script.

Directories & Structure:
- `/specs`: Stores all spec files (organized by phase, e.g., `specs/phase-1/`).
- `/src`: Source code for Phase I (will move to `/backend` in Phase II).
- `/tests`: Pytest files matching the source structure.

## Response snapshot

I have updated the project constitution and its dependent templates.
- **Version**: 1.0.0
- **Updated Files**:
    - `.specify/memory/constitution.md`
    - `.specify/templates/plan-template.md`
    - `.specify/templates/tasks-template.md`
- A new Prompt History Record has been created at `history/prompts/constitution/001-setup-project-constitution-and-principles.constitution.prompt.md`

## Outcome

- ✅ Impact: The project now has a clear and documented set of principles and standards.
- 🧪 Tests: Not applicable for this command.
- 📁 Files: 3 files were updated.
- 🔁 Next prompts: The user can now proceed with other commands, like `/sp.plan` or `/sp.specify`.
- 🧠 Reflection: The process of updating the constitution and its dependent files was successful. The use of `replace` tool with multiple calls was necessary to handle the updates to the `tasks-template.md` file.

## Evaluation notes (flywheel)

- Failure modes observed: The `replace` tool failed when trying to perform multiple different replacements in a single call.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Use a single `replace` call with a more complex `old_string` that covers all the changes.
