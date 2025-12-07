# Data Model: In-Memory Todo CLI

## Entity: Task

Represents a single todo item.

### Attributes:
- `id`: Integer, unique identifier. Auto-generated.
- `title`: String. Must not be empty or whitespace-only.
- `description`: String. Optional. Defaults to an empty string (`''`) if not provided.
- `completed`: Boolean. Indicates whether the task is completed. Defaults to `False`.

### Relationships:
- None (standalone entity for Phase I).

### Validation Rules:
- `title`: Required, non-empty, non-whitespace.
- `id`: Must be a positive integer.
- `completed`: Must be a boolean.

### State Transitions:
- An incomplete task can transition to a completed state.
- A completed task can remain in a completed state (no transition back to incomplete in Phase I).
