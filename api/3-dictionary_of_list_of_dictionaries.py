
#!/usr/bin/python3
"""Export all employees' TODO tasks to a JSON file."""

import json
import urllib.request


def main():
    """Fetch all employees and their TODO tasks."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    with urllib.request.urlopen(users_url) as response:
        users = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    data = {}

    for user in users:
        user_id = str(user.get("id"))
        data[user_id] = []

    for task in todos:
        user_id = str(task.get("userId"))

        task_data = {
            "username": next(
                (user.get("username") for user in users
                 if str(user.get("id")) == user_id),
                None
            ),
            "task": task.get("title"),
            "completed": task.get("completed")
        }

        data.get(user_id).append(task_data)

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()

