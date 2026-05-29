# ============================================
# CodSoft Internship - Task 1: To-Do List
# ============================================

import json
import os

TODO_FILE = "todos.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("\n📋 Koi task nahi hai abhi!")
        return
    print("\n📋 Your To-Do List:")
    print("-" * 40)
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "⬜"
        print(f"{i}. {status} {task['title']}")
    print("-" * 40)

def add_task(tasks):
    title = input("Naya task likho: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        save_tasks(tasks)
        print(f"✅ Task add ho gaya: '{title}'")
    else:
        print("❌ Task khali nahi hona chahiye!")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Kaunsa task complete karna hai (number likho): "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"🎉 Task complete: '{tasks[num-1]['title']}'")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Sirf number likho!")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Kaunsa task delete karna hai (number likho): "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task delete ho gaya: '{removed['title']}'")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Sirf number likho!")

def update_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Kaunsa task update karna hai (number likho): "))
        if 1 <= num <= len(tasks):
            new_title = input("Naya naam likho: ").strip()
            if new_title:
                old = tasks[num - 1]["title"]
                tasks[num - 1]["title"] = new_title
                save_tasks(tasks)
                print(f"✏️ Task update: '{old}' → '{new_title}'")
        else:
            print("❌ Invalid number!")
    except ValueError:
        print("❌ Sirf number likho!")

def main():
    print("=" * 40)
    print("   📝 CodSoft - To-Do List App   ")
    print("=" * 40)

    tasks = load_tasks()

    while True:
        print("\n📌 Menu:")
        print("1. Tasks dekho")
        print("2. Task add karo")
        print("3. Task complete karo")
        print("4. Task update karo")
        print("5. Task delete karo")
        print("6. Exit")

        choice = input("\nOption choose karo (1-6): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            update_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("👋 Bye! Tasks save ho gaye hain.")
            break
        else:
            print("❌ Invalid option! 1-6 ke beech choose karo.")

if __name__ == "__main__":
    main()
