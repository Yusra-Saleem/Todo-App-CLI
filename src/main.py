import os
import sys
import shlex
from todo_manager import TodoManager
from task_model import Task

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("=" * 60)
    print(" " * 20 + "TODO LIST MANAGER")
    print("=" * 60)

def print_help():
    print("\n[COMMANDS]")
    print("  add <title> [desc]   : Add a new task (use quotes for spaces)")
    print("  list                 : Show all tasks")
    print("  done <id>            : Mark task as complete (alias: complete)")
    print("  update <id> <title>  : Update task title")
    print("  desc <id> <text>     : Update task description")
    print("  del <id>             : Delete a task (alias: delete)")
    print("  clear                : Clear the screen")
    print("  help                 : Show this menu")
    print("  exit                 : Quit")
    print("-" * 60)

def print_task_list(tasks):
    if not tasks:
        print("\n  (No tasks found. Add one with 'add <title>')\n")
        return

    # ID | Done | Title | Desc
    print(f"\n{'ID'.ljust(4)} | {'Status'.ljust(8)} | {'Title'.ljust(20)} | {'Description'}")
    print("-" * 60)
    for task in tasks:
        status = "[DONE]" if task.completed else "[TODO]"
        # Handing long titles/descriptions
        title = task.title
        if len(title) > 20:
            title = title[:17] + "..."
        
        desc = task.description
        if len(desc) > 25:
            desc = desc[:22] + "..."
            
        print(f"{str(task.id).ljust(4)} | {status.ljust(8)} | {title.ljust(20)} | {desc}")
    print("-" * 60 + "\n")

def run_cli():
    manager = TodoManager()
    clear_screen()
    print_header()
    print("Type 'help' for commands. Tip: Use quotes for multi-word text.\n")

    while True:
        try:
            user_input = input("todo> ").strip()
            if not user_input:
                continue

            # proper parsing of quotes: add "Buy Milk" "From the store"
            try:
                parts = shlex.split(user_input)
            except ValueError:
                print("! Error: Unbalanced quotes.")
                continue

            if not parts:
                continue

            command = parts[0].lower()
            args = parts[1:]

            if command in ["exit", "quit"]:
                print("Goodbye!")
                break

            elif command == "help":
                print_help()
                print("  Note: You can use Task ID or Title for commands like done/update/del.")

            elif command == "clear":
                clear_screen()
                print_header()

            elif command == "add":
                title = ""
                description = ""
                
                if not args:
                    # Interactive mode
                    print("Enter task details (leave empty to cancel):")
                    title = input("  Title: ").strip()
                    if not title:
                        print("Cancelled.")
                        continue
                    description = input("  Description: ").strip()
                else:
                    title = args[0]
                    description = args[1] if len(args) > 1 else ""

                try:
                    t = manager.add_task(title, description)
                    print(f"OK. Added task #{t.id}")
                except ValueError as e:
                    print(f"! {e}")

            elif command == "list":
                print_task_list(manager.get_all_tasks())

            elif command in ["complete", "done"]:
                identifier = args[0] if args else None
                if not identifier:
                     # Interactive mode possible?
                     print("! Usage: done <id or title>")
                     continue
                
                try:
                    t = manager.complete_task(identifier)
                    print(f"OK. Task #{t.id} '{t.title}' marked as DONE.")
                except ValueError as e:
                    print(f"! {e}")

            elif command == "update":
                identifier = None
                new_title = None
                new_desc = None

                if not args:
                     # Full Interactive mode
                     identifier = input("  Enter Task ID or Title to update: ").strip()
                     if not identifier:
                         print("Cancelled.")
                         continue
                else:
                    identifier = args[0]
                
                # If args provided, we might have title/desc in them
                if args and len(args) > 1:
                    new_title = args[1]
                    new_desc = args[2] if len(args) > 2 else ""
                else:
                    # Interactive update details
                    print(f"Update task '{identifier}' (leave empty to keep current):")
                    new_title = input("  New Title: ").strip() or None
                    new_desc = input("  New Description: ").strip() or None

                if new_title is None and new_desc is None:
                    print("No changes specified.")
                    continue

                try:
                    t = manager.update_task(identifier, new_title=new_title, new_description=new_desc)
                    print(f"OK. Updated task #{t.id}")
                except ValueError as e:
                    print(f"! {e}")

            elif command == "desc":
                if len(args) < 2:
                    print("! Usage: desc <id|title> <new_description>")
                    continue
                try:
                    # Logic reuse
                    identifier = args[0]
                    new_desc = args[1]
                    t = manager.update_task(identifier, new_description=new_desc)
                    print(f"OK. Updated description for task #{t.id}")
                except ValueError as e:
                    print(f"! {e}")

            elif command in ["delete", "del", "remove"]:
                if not args:
                    # Interactive
                    identifier = input("  Enter Task ID or Title to DELETE: ").strip()
                    if not identifier:
                         print("Cancelled.")
                         continue
                else:
                    identifier = args[0]

                try:
                    t = manager.delete_task(identifier)
                    print(f"OK. Deleted task #{t.id} '{t.title}'")
                except ValueError as e:
                    print(f"! {e}")

            else:
                print(f"Unknown command '{command}'. Type 'help'.")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"! Unexpected error: {e}")

if __name__ == "__main__":
    run_cli()
