#!/usr/bin/env python3
"""
TaskFlow CLI - Professional Task Management Utility
Author: Clythix
"""

import sys
from core import load_tasks, display_tasks

def main():
    print("=== TaskFlow CLI v1.0.0 ===")
    tasks = load_tasks()
    display_tasks(tasks)

if __name__ == "__main__":
    main()
