
#!/usr/bin/python3
"""Export an employee's TODO tasks to a CSV file."""

import csv
import json
import sys
import urllib.request


def main():
    """Fetch employee TODO tasks and export them to CSV."""
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

    with open("{}.csv".format(employee_id), "w") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL,
                            lineterminator="\n")

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()

