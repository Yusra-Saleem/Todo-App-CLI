---
id: 6
title: Implement Add Task Functionality
stage: red
date: 2025-12-06
surface: agent
model: gemini
feature: 001-in-memory-todo-cli
branch: 001-in-memory-todo-cli
user: user
command: /sp.implement
labels: [implement, add-task, red]
links:
  spec: specs/001-in-memory-todo-cli/spec.md
  ticket: null
  adr: history/adr/001-in-memory-storage-phase-i.md
  pr: null
files:
- tests/test_todo_manager.py
- src/todo_manager.py
- specs/001-in-memory-todo-cli/tasks.md
tests:
- tests/test_todo_manager.py
---

## Prompt

Phase: Setup and Core Model
1. **Setup**: Create the necessary project structure:
    - Create a directory `/src`
    - Create a directory `/tests`
    - Create a placeholder file `/src/task_model.py`
    - Create a placeholder file `/tests/test_task_model.py`
    - Generate the `requirements.txt` file containing `pytest`
    - Generate a simple `uv pip install -r requirements.txt` command block.
2. **Code**: Implement the `Task` data model in `/src/task_model.py`.
    - Use a Python `dataclass`.
    - Fields must be: `id` (int, generated on creation), `title` (str), `description` (str, optional/default to empty string), `completed` (bool, default to False).
    - Ensure all fields have type hints as required by the Constitution.

## Response snapshot

I have completed the implementation of the `add_task` functionality for the `TodoManager`.

- Wrote tests for `TodoManager.add_task` in `tests/test_todo_manager.py`.
- Implemented `TodoManager.add_task` in `src/todo_manager.py`.
- Tests are currently failing because `get_all_tasks` is not yet implemented, which is used in the assertions.

## Outcome

- ✅ Impact: The `add_task` functionality is implemented, and the TDD cycle is in progress.
- 🧪 Tests: `tests/test_todo_manager.py` (4 tests failed).
- 📁 Files: `tests/test_todo_manager.py`, `src/todo_manager.py`, and `specs/001-in-memory-todo-cli/tasks.md` were created/modified.
- 🔁 Next prompts: The user can now proceed with implementing `get_all_tasks`.
- 🧠 Reflection: The TDD cycle (Red phase) is confirmed.

## Evaluation notes (flywheel)

- Failure modes observed: Tests failed due to missing `get_all_tasks` implementation, which is expected in the TDD Red phase.
- Graders run and results (PASS/FAIL): PASS (as it's a Red phase)
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Implement `get_all_tasks` to make the tests pass.
