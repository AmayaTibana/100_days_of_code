---

### `todo.py`

```python
#!/usr/bin/env python3
"""
Simple CLI Todo List
Usage:
  python todo.py add "Task description"
  python todo.py list
  python todo.py done <task_number>
  python todo.py delete <task_number>
Data stored in tasks.json
"""

import sys
import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def add_task(description):
    tasks = load_tasks()
    task = {"description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks.")
        return
    for i, t in enumerate(tasks, 1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['description']}")

def mark_done(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    tasks[index-1]["done"] = True
    save_tasks(tasks)
    print(f"Task {index} marked as done.")

def delete_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(index-1)
    save_tasks(tasks)
    print(f"Deleted task: {removed['description']}")

def print_usage():
    print(__doc__)

def main(argv):
    if len(argv) < 2:
        print_usage()
        return 1
    cmd = argv[1].lower()
    if cmd == "add" and len(argv) >= 3:
        add_task(" ".join(argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(argv) == 3:
        mark_done(int(argv[2]))
    elif cmd == "delete" and len(argv) == 3:
        delete_task(int(argv[2]))
    else:
        print_usage()
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))