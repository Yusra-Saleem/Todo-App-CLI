from src.todo_manager import TodoManager
from src.task_model import Task
import pytest

def test_add_task():
    manager = TodoManager()
    task = manager.add_task("Buy groceries")
    assert task.title == "Buy groceries"
    assert task.description == ""
    assert not task.completed
    assert manager.get_all_tasks() == [task]

def test_add_task_with_description():
    manager = TodoManager()
    task = manager.add_task("Walk the dog", "Take a long walk")
    assert task.title == "Walk the dog"
    assert task.description == "Take a long walk"
    assert not task.completed
    assert manager.get_all_tasks() == [task]

def test_add_task_empty_title_rejection():
    manager = TodoManager()
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        manager.add_task("")
    assert manager.get_all_tasks() == []

def test_add_task_whitespace_title_rejection():
    manager = TodoManager()
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        manager.add_task("   ")
    assert manager.get_all_tasks() == []

def test_get_all_tasks_empty():
    manager = TodoManager()
    assert manager.get_all_tasks() == []

def test_get_all_tasks_multiple():
    manager = TodoManager()
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    all_tasks = manager.get_all_tasks()
    assert len(all_tasks) == 2
    assert task1 in all_tasks
    assert task2 in all_tasks

def test_complete_task_existing():
    manager = TodoManager()
    task = manager.add_task("Buy groceries")
    completed_task = manager.complete_task(task.id)
    assert completed_task.completed is True
    assert manager.get_all_tasks()[0].completed is True

def test_complete_task_non_existent():
    manager = TodoManager()
    with pytest.raises(ValueError, match=f"Error: Task with ID 99 not found."):
        manager.complete_task(99)

def test_complete_task_already_completed():
    manager = TodoManager()
    task = manager.add_task("Buy groceries")
    manager.complete_task(task.id)
    completed_task = manager.complete_task(task.id) # Try to complete again
    assert completed_task.completed is True


def test_update_task_title():
    manager = TodoManager()
    task = manager.add_task("Old Title", "Old Description")
    updated_task = manager.update_task(task.id, new_title="New Title")
    assert updated_task.title == "New Title"
    assert updated_task.description == "Old Description"
    assert manager.get_all_tasks()[0].title == "New Title"

def test_update_task_description():
    manager = TodoManager()
    task = manager.add_task("Title", "Old Description")
    updated_task = manager.update_task(task.id, new_description="New Description")
    assert updated_task.title == "Title"
    assert updated_task.description == "New Description"
    assert manager.get_all_tasks()[0].description == "New Description"

def test_update_task_title_and_description():
    manager = TodoManager()
    task = manager.add_task("Old Title", "Old Description")
    updated_task = manager.update_task(task.id, new_title="New Title", new_description="New Description")
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Description"
    assert manager.get_all_tasks()[0].title == "New Title"
    assert manager.get_all_tasks()[0].description == "New Description"

def test_update_task_non_existent():
    manager = TodoManager()
    with pytest.raises(ValueError, match=f"Error: Task with ID 99 not found."):
        manager.update_task(99, new_title="Non Existent")

def test_update_task_empty_title_rejection():
    manager = TodoManager()
    task = manager.add_task("Original Title")
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        manager.update_task(task.id, new_title="")
    assert manager.get_all_tasks()[0].title == "Original Title" # Should not be changed

def test_update_task_whitespace_title_rejection():
    manager = TodoManager()
    task = manager.add_task("Original Title")
    with pytest.raises(ValueError, match="Task title cannot be empty"):
        manager.update_task(task.id, new_title="   ")
    assert manager.get_all_tasks()[0].title == "Original Title" # Should not be changed

def test_delete_task_existing():
    manager = TodoManager()
    task1 = manager.add_task("Task 1")
    task2 = manager.add_task("Task 2")
    deleted_task = manager.delete_task(task1.id)
    assert deleted_task == task1
    assert manager.get_all_tasks() == [task2]

def test_delete_task_non_existent():
    manager = TodoManager()
    manager.add_task("Task 1")
    with pytest.raises(ValueError, match=f"Error: Task with ID 99 not found."):
        manager.delete_task(99)
    assert len(manager.get_all_tasks()) == 1 # Ensure no task was deleted





