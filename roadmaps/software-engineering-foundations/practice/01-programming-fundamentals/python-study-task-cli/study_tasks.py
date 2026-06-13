
from typing import TypedDict
from pathlib import Path
import json
import argparse

# Use the tasks.json next to this Python file
TASKS_FILE = Path(__file__).with_name("tasks.json")

# Type
class Task(TypedDict):
    id: int
    title: str
    phase: int
    topic: str
    done: bool

# File I/O functions
def load_tasks() -> list[Task]:
    if not TASKS_FILE.exists():
        return []
    
    try: 
        with TASKS_FILE.open('r', encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("tasks.json is corrupted or empty")
        return []

def save_tasks(tasks: list[Task]) -> None:
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=2, ensure_ascii=False)
    except IOError as e:
        print(f"Failed to write to file: {e}")


# Task logic functions

def get_next_id(tasks: list[Task]) -> int:
    if len(tasks) == 0: 
        return 1
    return max(task['id'] for task in tasks) + 1

def create_task(title: str, phase: int, topic: str, task_id: int) -> Task:
    return {
        "id": task_id,
        "title": title,
        "phase": phase,
        "topic": topic,
        "done": False
    }
    

def add_task(title: str, phase: int, topic: str) -> Task: 
    tasks_list = load_tasks()
    next_id = get_next_id(tasks_list)
    new_task: Task = create_task(title, phase, topic, next_id)
    tasks_list.append(new_task)
    save_tasks(tasks_list)

    return new_task

def find_task_by_id(tasks: list[Task], task_id: int) -> Task | None:
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def mark_done(task_id: int) -> bool:
    tasks = load_tasks()
    task_mark = find_task_by_id(tasks, task_id)
    if task_mark is not None:
        task_mark['done'] = True
        save_tasks(tasks)
        return True
    return False
    
def get_task_stats(tasks: list[Task]) -> dict[str, int | float]:
    total_tasks = len(tasks)
    completed_tasks = 0
    for task in tasks:
        if task['done']:
            completed_tasks = completed_tasks + 1

    remaining_tasks = total_tasks - completed_tasks

    if total_tasks == 0:
        completion_percentage = 0.0
    else:
        completion_percentage = (completed_tasks / total_tasks) * 100

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "remaining_tasks": remaining_tasks,
        "completion_percentage": completion_percentage  
    }

# Display functions
def format_task(task: Task) -> str:
    status: str = "[x]" if task["done"] else "[ ]"
    return f"{status} #{task['id']} Phase {task['phase']} {task['topic']} - {task['title']}"

def display_tasks(tasks: list[Task]) -> None:
    if len(tasks) == 0:
        print("No tasks found.")
        return
    for task in tasks:
        print(format_task(task))

def display_stats(stats: dict[str, int | float]) -> None:
    print(f"Total tasks: {stats['total_tasks']}")
    print(f"Done: {stats['completed_tasks']}")
    print(f"Remaining: {stats['remaining_tasks']}")
    print(f"Completion: {stats['completion_percentage']:.2f}%")

# cli commands
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="study_tasks",
        description="Manage study tasks"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new study task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--phase", type=int, required=True, help="Roadmap phase number")
    add_parser.add_argument("--topic", required=True,help="Task topic")

    # list command
    subparsers.add_parser(
        "list",
        help="List all study tasks"
    )
    # done command
    done_parser = subparsers.add_parser(
        "done",
        help="Mark a task as done"
    )

    done_parser.add_argument(
        "task_id",
        type=int,
        help="Task ID to mark as done"
    )
    # stats command
    subparsers.add_parser(
        "stats",
        help="Show task statistics"
    )

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title, args.phase, args.topic)
        print(f"Added task #{task['id']}: {task['title']}")
    
    elif args.command == "list":
        tasks = load_tasks()
        display_tasks(tasks)
    
    elif args.command == "done":
        updated_task = mark_done(args.task_id)

        if updated_task:
            print(f"Marked task #{args.task_id} as done.")
        else: 
            print(f"Task {args.task_id} not found.")

    elif args.command == "stats":
        tasks = load_tasks()
        stats = get_task_stats(tasks)
        display_stats(stats)

if __name__ == "__main__":
    main()

# CLI COMMANDS

# python study_tasks.py list
# -> Display list of tasks

# python study_tasks.py add "Learn functions" --phase 1 --topic python
# -> Add task to tasks.json

# python study_tasks.py done 3
# -> Marked task with id = 3 to be done

# python study_tasks.py stats
# -> Display stats of all tasks

    












    
        

    
