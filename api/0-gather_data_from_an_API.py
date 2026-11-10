#!/usr/bin/python3
"""Gather data from an API and display an employee's TODO progress."""

import json
import sys
import urllib.request


def main():
    """Fetch employee information and display completed TODO tasks."""
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

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
