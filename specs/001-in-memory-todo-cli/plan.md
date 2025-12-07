# Implementation Plan: In-Memory Todo CLI

**Branch**: `001-in-memory-todo-cli` | **Date**: 2025-12-06 | **Spec**: specs/001-in-memory-todo-cli/spec.md
**Input**: Feature specification from `specs/001-in-memory-todo-cli/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This plan outlines the implementation for Phase I of the "Evolution of Todo" project, focusing on a Command Line Interface (CLI) application with in-memory task management. The core functionality includes adding, viewing, updating, deleting, and completing tasks. The technical approach leverages Python 3.13+, `uv` for package management, and `pytest` for testing, adhering strictly to a `Task` dataclass for data modeling, a `TodoManager` for business logic, and a `main.py` entry point for the CLI interaction. All efforts are guided by the project constitution's principles of TDD, explicit typing, and clean code.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: `uv`, `pytest`, `FastAPI`, `SQLModel`, `Next.js`
**Storage**: In-Memory (Phase I), Neon Serverless PostgreSQL (Phase II+)
**Testing**: `pytest`
**Target Platform**: CLI (Phase I), Cloud-Native (Phase V)
**Project Type**: Monorepo (`/src` -> `/backend`, `/frontend`)
**Performance Goals**: Fast and simple for Phase I
**Constraints**: Adherence to phased development.
**Scale/Scope**: Console App (Phase I) -> Cloud-Native System (Phase V)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [ ] **Evolutionary Architecture**: Does this feature align with the current project phase?
- [ ] **Business First**: Is this feature delivering immediate user value? Is it simple and not over-engineered?
- [ ] **No "Magic Code"**: Is all new code explicit, typed, and documented?
- [ ] **Monorepo Structure**: Does the file structure align with the project's phased approach?
- [ ] **Type Hints**: Are all new Python functions and methods fully type-hinted?
- [ ] **Docstrings**: Do all new public classes, functions, and methods have clear docstrings?
- [ ] **TDD**: Were tests written first for this feature?
- [ ] **Clean Code**: Does the code separate data models from logic?

## Project Structure

### Documentation (this feature)

```text
specs/001-in-memory-todo-cli/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
src/
├── task_model.py
├── todo_manager.py
└── main.py

tests/
├── test_task_model.py
└── test_todo_manager.py
```

**Structure Decision**: The single project structure is chosen for Phase I as per the project constitution, with dedicated files for the Task model, TodoManager logic, and the main CLI entry point, along with corresponding unit tests.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
