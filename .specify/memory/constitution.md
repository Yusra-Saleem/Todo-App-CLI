<!--
---
sync_impact_report:
  version_change: "0.0.0 -> 1.0.0"
  modified_principles:
    - "PRINCIPLE_1_NAME -> Evolutionary Architecture"
    - "PRINCIPLE_2_NAME -> Business First"
    - "PRINCIPLE_3_NAME -> No \"Magic Code\""
    - "PRINCIPLE_4_NAME -> Monorepo Structure"
  added_sections:
    - "Technical Stack"
    - "Quality Standards"
    - "Directories & Structure"
  removed_sections:
    - "[SECTION_2_NAME]"
    - "[SECTION_3_NAME]"
  templates_updated:
    - ".specify/templates/plan-template.md"
    - ".specify/templates/spec-template.md"
    - ".specify/templates/tasks-template.md"
  todos: []
---
-->
# Hackathon Phase02 Constitution

## Core Principles

### I. Evolutionary Architecture
We start as a Console App (Phase I) and evolve into a Cloud-Native System (Phase V). This phased approach allows for rapid initial development while planning for future scalability.

### II. Business First
Focus on delivering user value quickly. Phase I must be simple and fast; we must avoid over-engineering and premature optimization. Features should be driven by immediate user needs.

### III. No "Magic Code"
All code must be explicit, typed, and documented. This ensures clarity, maintainability, and reduces cognitive overhead for developers. Implicit behaviors or undocumented side effects are strictly forbidden.

### IV. Monorepo Structure
The project will eventually separate into `/frontend` and `/backend` directories but will start as a single, simple structure. This simplifies initial setup and tooling while providing a clear path for future separation of concerns.

## Technical Stack (Phased)

- **Global**: Python 3.13+, `uv` package manager, and Conventional Commits for version control.
- **Phase I (Current)**:
    - **Interface**: Command Line Interface (CLI).
    - **Storage**: In-Memory (Variables/Classes).
    - **Logic**: Pure Python (No web frameworks).
- **Phase II+ (Future)**:
    - **Frontend**: Next.js 16+ (App Router), TypeScript, Tailwind CSS.
    - **Backend**: FastAPI, SQLModel.
    - **Database**: Neon Serverless PostgreSQL.

## Quality Standards (Immutable)

- **Type Hints**: All Python functions and methods MUST have complete type hints (e.g., `def add(a: int, b: int) -> int:`).
- **Docstrings**: All public classes, functions, and methods MUST have docstrings explaining their purpose, arguments, and return values.
- **Test-Driven Development (TDD)**: Write tests first. Use `pytest` for all Python logic. Every new feature or bug fix must begin with a failing test.
- **Clean Code**: Use Dataclasses for data models. Strictly separate data structures (Models) from business logic (Controllers), even in simple scripts, to maintain a clean architecture.

## Directories & Structure

- **/specs**: Stores all specification files, organized by phase (e.g., `specs/phase-1/`).
- **/src**: Contains the source code for the current phase. This will move to `/backend` in Phase II.
- **/tests**: Contains all `pytest` files, mirroring the source code structure.

## Governance

This constitution is the single source of truth for project standards and supersedes all other practices. Amendments require a documented proposal, team review, and an explicit migration plan for existing code. All code reviews must verify compliance with these principles.

**Version**: 1.0.0 | **Ratified**: 2025-12-06 | **Last Amended**: 2025-12-06