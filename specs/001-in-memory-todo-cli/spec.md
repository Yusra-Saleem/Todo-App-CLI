# Feature Specification: In-Memory Todo CLI

**Feature Branch**: `001-in-memory-todo-cli`
**Created**: 2025-12-06
**Status**: Draft
**Input**: User description: "Phase I: In-Memory Python Console App..."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add a new task (Priority: P1)

A user can create a new task by providing a title and an optional description. This is the most fundamental feature.

**Why this priority**: This is the core functionality of a todo application. Without it, the application is useless.

**Independent Test**: The user can add a task and then view the list to see the newly created task.

**Acceptance Scenarios**:

1.  **Given** the application is running, **When** the user chooses to add a task and provides a title "Buy milk", **Then** the task list should contain a new task with the title "Buy milk" and status "Incomplete".
2.  **Given** the application is running, **When** the user chooses to add a task and provides a title "Buy milk" and a description "From the store", **Then** the task list should contain a new task with the title "Buy milk", the description "From the store", and status "Incomplete".

---

### User Story 2 - View all tasks (Priority: P1)

A user can view a list of all existing tasks, including their ID, title, and completion status.

**Why this priority**: This is essential for users to see what they need to do.

**Independent Test**: The user can add a few tasks and then view the list to see all of them displayed correctly.

**Acceptance Scenarios**:

1.  **Given** there are no tasks, **When** the user chooses to view the task list, **Then** the application should display a message indicating that there are no tasks.
2.  **Given** there are two tasks, one completed and one incomplete, **When** the user chooses to view the task list, **Then** the application should display both tasks with their correct IDs and statuses (e.g., `[x]` for completed, `[ ]` for incomplete).

---

### User Story 3 - Update an existing task (Priority: P2)

A user can modify the title or description of an existing task by specifying its ID.

**Why this priority**: Allows for correcting mistakes or adding more detail to tasks.

**Independent Test**: The user can add a task, update it, and then view the list to see the changes.

**Acceptance Scenarios**:

1.  **Given** a task with ID 1 exists, **When** the user chooses to update task 1 with a new title "Buy groceries", **Then** the task with ID 1 should have the title "Buy groceries".
2.  **Given** a task with ID 1 exists, **When** the user chooses to update a non-existent task with ID 99, **Then** the application should display an error message.

---

### User Story 4 - Delete a task (Priority: P2)

A user can remove a task from the list by specifying its ID.

**Why this priority**: Allows users to remove completed or unnecessary tasks.

**Independent Test**: The user can add a task, delete it, and then view the list to confirm it's gone.

**Acceptance Scenarios**:

1.  **Given** a task with ID 1 exists, **When** the user chooses to delete task 1, **Then** the task list should no longer contain the task with ID 1.
2.  **Given** the application is running, **When** the user chooses to delete a non-existent task with ID 99, **Then** the application should display an error message.

---

### User Story 5 - Complete a task (Priority: P1)

A user can mark a task as "Completed".

**Why this priority**: This is a core part of the "todo" workflow.

**Independent Test**: The user can add a task, mark it as complete, and then view the list to see its status has changed.

**Acceptance Scenarios**:

1.  **Given** an incomplete task with ID 1 exists, **When** the user chooses to complete task 1, **Then** the task with ID 1 should have its status changed to "Completed".
2.  **Given** a completed task with ID 1 exists, **When** the user chooses to complete task 1 again, **Then** the task's status should remain "Completed".

## Clarifications

### Session 2025-12-06
- Q: What is the exact output message if the user tries to update or delete a non-existent Task ID? → A: Error: Task with ID <ID> not found.
- Q: How should the CLI handle non-integer input for the Task ID (e.g., if the user types 'A' instead of '1')? → A: Error: Invalid ID. Please provide a number.
- Q: What is the default value for a task's description if it's not provided by the user? → A: An empty string (`''`).
- Q: Should we add a specific requirement to the spec to explicitly reiterate that TDD and Type Hint standards MUST be followed? → A: Yes, add an explicit requirement for TDD and Type Hints.

### Edge Cases

- What happens when the user enters an invalid command?
- If the user tries to update or delete a non-existent task ID, the system will display: `Error: Task with ID <ID> not found.`
- The system will not allow the creation of a task with an empty or whitespace-only title.
- If the user provides non-integer input for a task ID, the system will display: `Error: Invalid ID. Please provide a number.`

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to add a new task with a title and optional description.
- **FR-002**: System MUST allow users to view a list of all tasks with their ID and status.
- **FR-003**: System MUST allow users to update the title or description of an existing task by ID.
- **FR-004**: System MUST allow users to delete a task by ID.
- **FR-005**: System MUST allow users to mark a task as completed.
- **FR-006**: System MUST handle invalid user inputs gracefully by printing a specific error message (e.g., "Error: Task with ID <ID> not found.") and not crashing.
- **FR-007**: System MUST display a visual indicator for completed tasks (e.g., `[x]` vs `[ ]`).
- **FR-008**: System MUST run in a continuous loop, waiting for user commands.
- **FR-009**: System MUST NOT allow the creation of a task with an empty or whitespace-only title.
- **FR-010**: System MUST adhere to Test-Driven Development (TDD) principles and use Python Type Hints for all new code, as per the project constitution.

### Key Entities *(include if feature involves data)*

- **Task**: Represents a single todo item.
  - **Attributes**:
    - `id`: A unique integer identifier.
    - `title`: A string representing the task's name.
    - `description`: An optional string with more details about the task. Defaults to an empty string (`''`) if not provided.
    - `completed`: A boolean indicating whether the task is completed.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can perform all CRUD (Create, Read, Update, Delete) operations on tasks.
- **SC-002**: The application correctly persists the state of the task list in memory for the duration of the session.
- **SC-003**: 100% of the core logic in the `TodoManager` class is covered by `pytest` tests.
- **SC-004**: The application provides clear feedback to the user for both successful operations and errors.