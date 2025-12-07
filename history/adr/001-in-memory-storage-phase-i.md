# ADR 001: Decision to Use In-Memory Storage for Phase I

## Status
Accepted

## Context
During Phase I of the "Evolution of Todo" project, the primary objective is to deliver a Command Line Interface (CLI) application quickly and simply. The project constitution emphasizes "Business First" and avoiding over-engineering in early phases. The initial requirements for the Todo CLI involve basic CRUD operations on tasks within a single user session, with no requirement for data persistence across application runs.

## Decision
For Phase I, the application will use **in-memory storage** (Python lists or dictionaries) to manage task data. No external database or persistent storage mechanism will be implemented.

## Alternatives Considered
-   **No Database (In-Memory)**: Chosen alternative. Simple, fast to implement, aligns with Phase I goals and "Business First" principle.
-   **SQLite Database**: Considered for lightweight persistence. Rejected due to introducing external dependency, file management, and a SQL layer, which would add complexity not required for the immediate Phase I objectives. This would be a form of premature optimization given the current constraints.
-   **Flat File Storage (JSON/CSV)**: Considered for simple persistence. Rejected as it still adds I/O concerns and serialization/deserialization logic beyond the "simplest possible" for Phase I.

## Consequences
### Positive
-   **Rapid Development**: Minimal setup and boilerplate code, allowing for quick iteration and delivery of core CLI functionality.
-   **Simplified Architecture**: Reduces initial complexity, focusing development efforts on application logic rather than database integration.
-   **No External Dependencies**: Keeps the application self-contained for Phase I, avoiding database connection issues or configuration.
-   **Easy Refactoring Path**: The `Task` model and `TodoManager` logic are designed to be decoupled from storage. This will facilitate a smoother transition to a persistent storage solution (e.g., Neon Serverless PostgreSQL with SQLModel) in Phase II, without requiring significant re-architecture of core logic.

### Negative
-   **Data Volatility**: All task data will be lost when the application terminates. This is acceptable for Phase I's scope.
-   **Limited Scale**: Not suitable for multi-user environments or large datasets, but this is a deliberate constraint for Phase I.
-   **Manual Testing Limitations**: Requires re-populating data for each test run if not handled via test fixtures, which is common in unit testing.

## Compliance
This decision aligns with the "Business First" and "Evolutionary Architecture" principles of the project constitution, allowing us to start simple and evolve the storage solution as the project progresses to later phases.
