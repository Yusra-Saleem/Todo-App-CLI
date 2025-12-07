from src.task_model import Task
import pytest

def test_task_creation():
    task = Task(title="Buy groceries")
    assert task.id is not None
    assert task.title == "Buy groceries"
    assert task.description == ""
    assert task.completed is False

def test_task_creation_with_description():
    task = Task(title="Walk the dog", description="Remember the leash")
    assert task.id is not None
    assert task.title == "Walk the dog"
    assert task.description == "Remember the leash"
    assert task.completed is False

def test_task_creation_with_completed_status():
    task = Task(title="Finish report", completed=True)
    assert task.id is not None
    assert task.title == "Finish report"
    assert task.description == ""
    assert task.completed is True

def test_task_id_generation():
    task1 = Task(title="Task 1")
    task2 = Task(title="Task 2")
    assert task1.id != task2.id

def test_task_title_cannot_be_empty():
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(title="")

def test_task_title_cannot_be_whitespace():
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        Task(title="   ")

def test_task_description_default():
    task = Task(title="Simple task")
    assert task.description == ""

def test_task_equality():
    task1 = Task(id=1, title="Test", description="Desc", completed=False)
    task2 = Task(id=1, title="Test", description="Desc", completed=False)
    task3 = Task(id=2, title="Test", description="Desc", completed=False)
    assert task1 == task2
    assert task1 != task3

