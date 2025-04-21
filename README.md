
# 📝 Task Tracker (JSON-Based)

This is a simple command-line Task Tracker application written in Python. It allows users to manage tasks with options to add, delete, mark as done, and view tasks saved in a JSON file.

---

## 📂 Features

- 📁 Load and save tasks from a `.json` file
- ➕ Add a new task (default status: *pending*)
- ❌ Delete a task by task ID
- ✅ Mark a task as *done*
- 👀 View all tasks
- ✔️ View completed tasks
- 🕓 View pending tasks
- 💾 Changes are automatically saved to the file

---

## ▶️ How to Run

1. Make sure you have Python installed (version 3.6 or higher recommended).
2. Save the script in a `.py` file, e.g., `task_tracker.py`.
3. Run it via terminal or command prompt:

```bash
python task_tracker.py
```

---

## 📘 Usage Instructions

1. **Start the Program**  
   You'll be prompted to either:
   - `1` to open the task tracker
   - `2` to exit

2. **Enter File Name**  
   - Provide a name for your task file. If it doesn't exist, a new `.json` file will be created.

3. **Task Tracker Menu Options:**
   ```
   1. Add task
   2. Delete task
   3. Mark as done
   4. View all tasks
   5. View done tasks
   6. View pending tasks
   7. Quit
   ```

4. **Actions Save Automatically**  
   Every action updates the file so your tasks are never lost.

---

## 📂 JSON File Format

Tasks are stored in JSON format as a list of dictionaries:
```json
[
  {
    "task_id": 1,
    "task_name": "Example Task",
    "status": "pending"
  }
]
```

---

## ✅ Example

```bash
Enter '1' to open task tracker or '2' to exit the program: 1
Enter the name of your file: tasks
Task Tracker Menu:
1. Add task
...
Enter your choice: 1
Enter the task: Complete assignment
Task added. Task ID 1
```

---

## 🛠 Future Improvements

- add the provision for users to not provide .json extension 
- Add due dates or priorities
- Allow editing of task names
- Provide sorting or searching functionality
- GUI version using Tkinter or PyQt

---

## Project URL: https://roadmap.sh/projects/task-tracker

---

## 📄 License

This project is for educational purposes and can be modified or extended freely.
