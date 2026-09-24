#!/usr/bin/env python3
"""
TaskFlow CLI - Professional Task Management Utility
Author: Clythix
"""

import argparse
from core import load_tasks, display_tasks, save_tasks

VERSION = "1.0.0"

def main():
    parser = argparse.ArgumentParser(description="TaskFlow CLI - Manage tasks from your terminal.")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}")
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # 'list' command
    subparsers.add_parser("list", help="Display all tasks")

    # 'add' command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", type=str, help="The title of the task")

    args = parser.parse_args()

    tasks = load_tasks()

    if args.command == "add":
        new_id = max([t.get("id", 0) for t in tasks], default=0) + 1
        new_task = {"id": new_id, "title": args.title, "status": "Pending"}
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"Successfully added task: '{args.title}' (ID: {new_id})")
    else:
        # Default action: list tasks
        display_tasks(tasks)

if __name__ == "__main__":
    main()
