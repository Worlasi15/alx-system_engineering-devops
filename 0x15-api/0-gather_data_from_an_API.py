#!/usr/bin/env python3
"""
Python script that returns information
about his/her TODO list progress.
"""

import requests as req
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user_todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos"
    .format(user_id)
    resp = req.get(url).json()
    user_name = resp.get("name")
    count = 0
    user_todos = req.get(user_todo_url).json()
    total_todos = len(user_todos)

    print(f"Employee {user_name} is done with tasks({count}/{total_todos}):")

    for todo in user_todos:
        if todo.get("completed"):
            count += 1
            print(f"\t{todo.get('title')}")
