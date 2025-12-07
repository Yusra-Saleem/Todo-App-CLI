---
id: 1
title: Specify In-Memory Todo CLI
stage: spec
date: 2025-12-06
surface: agent
model: gemini
feature: 001-in-memory-todo-cli
branch: 001-in-memory-todo-cli
user: user
command: /sp.specify
labels: [spec, feature]
links:
  spec: specs/001-in-memory-todo-cli/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/001-in-memory-todo-cli/spec.md
- specs/001-in-memory-todo-cli/checklists/requirements.md
tests:
- none
---

## Prompt

/sp.specify Phase I: In-Memory Python Console App Context: We are building the first phase of the "Evolution of Todo" project. This is a Command Line Interface (CLI) application written in Python. It must NOT use a database or web framework yet. Data is stored in memory (variables). User Stories (Basic Level): 1. Add Task: User can create a new task with a title and optional description. 2. View List: User can see all tasks with their ID and status. 3. Update Task: User can modify the title or description of an existing task by ID. 4. Delete Task: User can remove a task by ID. 5. Complete Task: User can toggle a task's status to "Completed". Technical Constraints: - Language: Python 3.13+. - Package Manager: uv. - Interface: Console/Terminal input (using `input()` loop). - Storage: In-memory list or dictionary (non-persistent). - Testing: pytest with 100% coverage for core logic. Architecture: - Follow the Constitution: Separate the `Task` data model (dataclass) from the `TodoManager` logic. - The CLI loop should be in a separate entry point (e.g., `main.py`). Acceptance Criteria: - Application starts a loop waiting for user commands. - Invalid inputs (like deleting a non-existent ID) are handled gracefully (print error, don't crash). - "View List" shows indicators for completed tasks (e.g., `[x]` vs `[ ]`).

## Response snapshot

I have created the feature specification for the "In-Memory Todo CLI".
- **Branch**: `001-in-memory-todo-cli`
- **Specification File**: `specs/001-in-memory-todo-cli/spec.md`
- **Checklist**: `specs/001-in-memory-todo-cli/checklists/requirements.md`

## Outcome

- ✅ Impact: The feature is now clearly defined and ready for the planning phase.
- 🧪 Tests: Not applicable for this command.
- 📁 Files: 2 files were created.
- 🔁 Next prompts: The user can now proceed with `/sp.plan`.
- 🧠 Reflection: The initial attempt to run the script failed due to command parsing issues. The manual process was successful.

## Evaluation notes (flywheel)

- Failure modes observed: The `run_shell_command` tool failed to parse the long feature description string correctly.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Investigate alternative ways to pass long strings to shell commands.
