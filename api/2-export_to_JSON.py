
#!/usr/bin/python3
"""Export an employee's TODO tasks to a JSON file."""

import json
import sys
import urllib.request


def main():
    """Fetch employee TODO tasks and export them to JSON."""
    if len(sys.argv) != 2:
        return

    employee_id = int(sys.argv[1])

    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)
    )
    todos_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)
    )

    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode("utf-8"))

    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode("utf-8"))

    username = user.get("username")

    tasks = []

    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {str(employee_id): tasks}

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    main()

