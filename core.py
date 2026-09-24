import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from local JSON storage with robust error handling."""
    if not os.path.exists(DATA_FILE):
        # Return default starter task if file doesn't exist yet
        return [{"id": 1, "title": "Setup repository workflow", "status": "Completed"}]
    
    try:
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except json.JSONDecodeError:
        # Handles corrupted JSON gracefully instead of crashing
        print("Warning: tasks.json was corrupted. Initializing empty task list.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading tasks: {e}")
        return []

def display_tasks(tasks):
    """Prints a formatted table of current tasks safely."""
    print("\nCurrent Tasks:")
    print("-" * 35)
    if not tasks:
        print("No tasks found.")
    else:
        for t in tasks:
            status_icon = "[x]" if t.get("status") == "Completed" else "[ ]"
            print(f"{t.get('id', 'N/A')}. {status_icon} {t.get('title', 'Untitled')}")
    print("-" * 35)
