from dataclasses import dataclass, field
import itertools

_task_id_counter = itertools.count(1)

def set_id_counter(start_value):
    global _task_id_counter
    _task_id_counter = itertools.count(start_value)


@dataclass(eq=True)
class Task:
    title: str
    description: str = ""
    completed: bool = False
    id: int = field(default=None, compare=True)

    def __post_init__(self):
        if not self.title or self.title.isspace():
            raise ValueError("Task title cannot be empty")
        if self.id is None:
            self.id = next(_task_id_counter)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
            id=data.get("id")
        )
        return task
