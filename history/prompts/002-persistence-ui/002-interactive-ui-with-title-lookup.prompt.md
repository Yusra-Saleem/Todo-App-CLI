---
id: 002
title: Interactive Ui With Title Lookup
stage: green
date: 2025-12-07
surface: agent
model: gemini-2.0-flash-exp
feature: 002-persistence-ui
branch: main
user: local
command: /add-interactive-mode
labels: ["ui", "enhancement", "interactive", "python"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - src/todo_manager.py
 - src/main.py
tests:
 - manual verification with send_command_input
---

## Prompt

add user direct for better understanding . add multiple aption for updation with title or id

## Response snapshot

Added `find_task` to `TodoManager` to allow looking up tasks by ID or exact Title string. Updated `main.py` to:
1. Support interactive prompts for `add`, `update`, `delete`, and `done` if arguments are missing.
2. Accept a Title string for `update`, `delete`, and `done` instead of just an ID.

## Outcome

- ✅ Impact: Significantly improved UX. Users can now run `add` and be prompted for details, and can refer to tasks by their human-readable title.
- 🧪 Tests: Manually verified interactive `add` and `update` (by title) using terminal interaction tools.
- 📁 Files: `src/todo_manager.py` (logic), `src/main.py` (UI).
- 🔁 Next prompts: None intended.
- 🧠 Reflection: The interactive loop via `input()` works well with the prompt mechanism.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
