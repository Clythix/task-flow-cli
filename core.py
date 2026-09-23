import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from local JSON storage."""
    if not os.path.exists(DATA_FILE):
        return [{"id": 1, "title": "Setup repository workflow", "status": "Completed"}]
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def display_tasks(tasks):
    """Prints a formatted table of current tasks."""
    print("\nCurrent Tasks:")
    print("-" * 35)
    for t in tasks:
        status_icon = "[x]" if t["status"] == "Completed" else "[ ]"
        print(f"{t['id']}. {status_icon} {t['title']}")
    print("-" * 35)
