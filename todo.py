import sys
import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    return json.loads(TASKS_FILE.read_text(encoding="utf-8"))


def save_tasks(tasks):
    TASKS_FILE.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")


def cmd_add(task_name):
    tasks = load_tasks()
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    tasks.append({"id": new_id, "task": task_name, "done": False})
    save_tasks(tasks)
    print(f"已添加: {task_name} (id={new_id})")


def cmd_list(done_filter=None):
    tasks = load_tasks()
    if not tasks:
        print("暂无待办事项")
        return
    for t in tasks:
        if done_filter is True and not t["done"]:
            continue
        if done_filter is False and t["done"]:
            continue
        status = "x" if t["done"] else " "
        print(f"  [{status}] {t['id']}. {t['task']}")


def cmd_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"已完成: {t['task']}")
            return
    print(f"错误: 找不到 id={task_id} 的任务")


def cmd_delete(task_id):
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            task_name = t["task"]
            del tasks[i]
            save_tasks(tasks)
            print(f"已删除: {task_name}")
            return
    print(f"错误: 找不到 id={task_id} 的任务")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python todo.py <add|list|done|delete> [参数]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("用法: python todo.py add <任务名>")
            sys.exit(1)
        cmd_add(sys.argv[2])

    elif command == "list":
        if "--done" in sys.argv:
            cmd_list(done_filter=True)
        elif "--undone" in sys.argv:
            cmd_list(done_filter=False)
        else:
            cmd_list()

    elif command == "done":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("用法: python todo.py done <任务id>")
            sys.exit(1)
        cmd_done(int(sys.argv[2]))

    elif command == "delete":
        if len(sys.argv) < 3 or not sys.argv[2].isdigit():
            print("用法: python todo.py delete <任务id>")
            sys.exit(1)
        cmd_delete(int(sys.argv[2]))

    else:
        print(f"未知命令: {command}")
        print("可用命令: add, list, done, delete")


with open("user.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data["name"])

