# Tasks: In-Memory Todo CLI

**Input**: Design documents from `specs/001-in-memory-todo-cli/`
**Prerequisites**: plan.md, spec.md, data-model.md

**Tests**: Per the constitution, Test-Driven Development (TDD) is mandatory. All implementation tasks must be preceded by a failing test. Use `pytest` for all tests.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directories: `src/` and `tests/`
- [x] T002 Initialize Python project with `uv` in the root directory
- [x] T003 Install `pytest` dependency (`uv pip install pytest`)

---

## Phase 2: Core Model (Task)

**Purpose**: Define and test the fundamental data structure for a Task.

### Tests for Core Model ⚠️

> **NOTE: Per the TDD principle, write these tests FIRST and ensure they FAIL before starting implementation.**

- [x] T004 [P] Write test for `Task` dataclass in `tests/test_task_model.py` (focus on ID generation, title validation, optional description default, completed status)

### Implementation for Core Model

- [x] T005 Implement `Task` dataclass in `src/task_model.py`

---

## Phase 3: Core Manager (TodoManager) - User Stories

**Purpose**: Implement and test the core business logic for managing tasks.

---

## Phase 3.1: User Story 1 - Add a new task (Priority: P1) 🎯 MVP

**Goal**: Allow users to create new tasks with titles and optional descriptions.

**Independent Test**: User can add a task and then view the list to see the newly created task.

### Tests for User Story 1 ⚠️

> **NOTE: Per the TDD principle, write these tests FIRST and ensure they FAIL before starting implementation.**

- [x] T006 [P] [US1] Write test for `TodoManager.add_task` in `tests/test_todo_manager.py` (test adding with/without description, empty title rejection)

### Implementation for User Story 1

- [x] T007 [US1] Implement `TodoManager.add_task` in `src/todo_manager.py`

---

## Phase 3.2: User Story 2 - View all tasks (Priority: P1)

**Goal**: Allow users to view a list of all existing tasks.

**Independent Test**: User can add a few tasks and then view the list to see all of them displayed correctly.

### Tests for User Story 2 ⚠️

> **NOTE: Per the TDD principle, write these tests FIRST and ensure they FAIL before starting implementation.**

- [x] T008 [P] [US2] Write test for `TodoManager.get_all_tasks` in `tests/test_todo_manager.py` (test empty list, list with multiple tasks)

### Implementation for User Story 2

- [x] T009 [US2] Implement `TodoManager.get_all_tasks` in `src/todo_manager.py`

---

## Phase 3.3: User Story 5 - Complete a task (Priority: P1)

**Goal**: Allow users to mark a task as completed.

**Independent Test**: User can add a task, mark it as complete, and then view the list to see its status has changed.

### Tests for User Story 5 ⚠️

> **NOTE: Per the TDD principle, write these tests FIRST and ensure they FAIL before starting implementation.**

- [x] T010 [P] [US5] Write test for `TodoManager.complete_task` in `tests/test_todo_manager.py` (test completing existing, non-existing ID, already completed)

### Implementation for User Story 5

- [x] T011 [US5] Implement `TodoManager.complete_task` in `src/todo_manager.py`

---

## Phase 3.4: User Story 3 - Update an existing task (Priority: P2)

**Goal**: Allow users to modify the title or description of an existing task.

**Independent Test**: User can add a task, update it, and then view the list to see the changes.

### Tests for User Story 3 ⚠️

> **NOTE: Per the TDD principle, write these tests FIRST and ensure they FAIL before starting implementation.**

- [x] T012 [P] [US3] Write test for `TodoManager.update_task` in `tests/test_todo_manager.py` (test updating title/description, non-existing ID, empty title rejection)

### Implementation for User Story 3

- [x] T013 [US3] Implement `TodoManager.update_task` in `src/todo_manager.py`

---

## Phase 3.5: User Story 4 - Delete a task (Priority: P2)

**Goal**: Allow users to remove a task from the list.

**Independent Test**: User can add a task, delete it, and then view the list to confirm it's gone.

### Tests for User Story 4 ⚠️

> **NOTE: Per the TDD principle, write these tests FIRST and ensure they FAIL before starting implementation.**

- [x] T014 [P] [US4] Write test for `TodoManager.delete_task` in `tests/test_todo_manager.py` (test deleting existing, non-existing ID)

### Implementation for User Story 4

- [x] T015 [US4] Implement `TodoManager.delete_task` in `src/todo_manager.py`

---

## Phase 4: CLI Interface

**Purpose**: Implement the command-line interface for user interaction.

- [x] T016 Implement CLI loop and command parsing in `src/main.py`
- [x] T017 Integrate `TodoManager` methods into CLI commands in `src/main.py`
- [x] T018 Implement graceful error handling and user feedback in `src/main.py` (for non-integer IDs, non-existent tasks)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Core Model (Phase 2)**: Depends on Setup completion
- **Core Manager (Phase 3)**: Depends on Core Model completion
- **CLI Interface (Phase 4)**: Depends on Core Manager completion

### User Story Dependencies

- All user stories within Phase 3 can technically be implemented in parallel after Core Model completion, but they are ordered by priority and functional dependencies for a logical workflow.

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services (handled in Phase 2 & 3)
- Services before endpoints (CLI integration)
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T001-T003) can run in parallel if the environment is set up.
- Test writing for each `TodoManager` method (T006, T008, T010, T012, T014) can be parallelized.
- Implementing each `TodoManager` method (T007, T009, T011, T013, T015) can be parallelized once its corresponding test is written.
- CLI implementation tasks (T016-T018) can be parallelized to some extent.

---

## Implementation Strategy

### MVP First (User Stories: Add, View, Complete)

1.  Complete Phase 1: Setup
2.  Complete Phase 2: Core Model (Task)
3.  Complete Phase 3.1: Add Task
4.  Complete Phase 3.2: View all tasks
5.  Complete Phase 3.3: Complete a task
6.  **STOP and VALIDATE**: Test basic Add, View, Complete functionality independently.
7.  Deploy/demo if ready

### Incremental Delivery

1.  Complete Setup + Core Model → Foundation ready
2.  Add User Story 1 (Add Task) → Test independently → Deploy/Demo (MVP!)
3.  Add User Story 2 (View all tasks) → Test independently → Deploy/Demo
4.  Add User Story 5 (Complete a task) → Test independently → Deploy/Demo
5.  Add User Story 3 (Update task) → Test independently → Deploy/Demo
6.  Add User Story 4 (Delete task) → Test independently → Deploy/Demo
7.  Each story adds value without breaking previous stories.
8.  Implement CLI Interface (Phase 4) once core logic is stable.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
