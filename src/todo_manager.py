import json
import os
from task_model import Task, set_id_counter

class TodoManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self._tasks: list[Task] = []
        self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self._tasks = [Task.from_dict(t) for t in data]
            
            # Sync ID counter
            if self._tasks:
                max_id = max(t.id for t in self._tasks)
                set_id_counter(max_id + 1)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load tasks from {self.filename}: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, 'w') as f:
                data = [t.to_dict() for t in self._tasks]
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving tasks: {e}")

    def find_task(self, identifier: str | int) -> Task | None:
        """Find a task by ID (int) or Title (str case-insensitive match)."""
        # Try finding by ID first
        try:
            target_id = int(identifier)
            for task in self._tasks:
                if task.id == target_id:
                    return task
        except ValueError:
            pass
        
        # If not an ID (or failed to find by ID), try finding by Title
        # We look for an exact case-insensitive match
        search_title = str(identifier).strip().lower()
        for task in self._tasks:
            if task.title.lower() == search_title:
                return task
        return None

    def add_task(self, title: str, description: str = "") -> Task:
        # Task dataclass handles title validation
        task = Task(title=title, description=description)
        # Ensure ID is unique - _task_id_counter in Task ensures this
        self._tasks.append(task)
        self.save_tasks()
        return task

    def get_all_tasks(self) -> list[Task]:
        return list(self._tasks) # Return a copy

    def complete_task(self, identifier: str | int) -> Task:
        task = self.find_task(identifier)
        if task:
            task.completed = True
            self.save_tasks()
            return task
        raise ValueError(f"Error: Task '{identifier}' not found.")

    def update_task(self, identifier: str | int, new_title: str = None, new_description: str = None) -> Task:
        task = self.find_task(identifier)
        if task:
            if new_title is not None:
                # Reuse Task's validation for title
                if not new_title or new_title.isspace():
                    raise ValueError("Task title cannot be empty")
                task.title = new_title
            if new_description is not None:
                task.description = new_description
            self.save_tasks()
            return task
        raise ValueError(f"Error: Task '{identifier}' not found.")

    def delete_task(self, identifier: str | int) -> Task:
        task = self.find_task(identifier)
        if task:
            self._tasks.remove(task)
            self.save_tasks()
            return task
        raise ValueError(f"Error: Task '{identifier}' not found.")
