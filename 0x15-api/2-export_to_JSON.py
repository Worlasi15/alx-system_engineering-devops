#!/usr/bin/python3
"""
Python script that returns information
about his/her TODO list progress and exports data to JSON.
"""

import json
import requests as req
import sys


def export_to_json(user_id, user_todos):
    """
    Export user TODOs to JSON file.

    Args:
        user_id (str): User ID.
        user_todos (list): List of user's TODOs.
    """
    filename = "{}.json".format(user_id)

    with open(filename, 'w') as json_file:
        json.dump({user_id: user_todos}, json_file)


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)

    try:
        user_response = req.get(url)
        user_data = user_response.json()
        user_todos = req.get(user_todo_url).json()

        formatted_todos = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user_data.get("username")
            }
            for todo in user_todos
        ]

        print("Employee {} is done with tasks({}/{}):".format(
            user_data.get("name"), len([t for t in formatted_todos if t["completed"]]), len(formatted_todos)
        ))

        for formatted_todo in formatted_todos:
            print("\t{}".format(formatted_todo["task"]))

        export_to_json(user_id, formatted_todos)

    except req.RequestException as e:
        print("Error: {}".format(e))

