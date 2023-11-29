#!/usr/bin/python3
"""
Python script that returns information
about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    employee_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    try:
        user_response = requests.get(user_url)
        user_data = user_response.json()
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        total_tasks = len(todo_data)
        completed_tasks = [task for task in todo_data if task['completed']]
        num_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            user_data['name'], num_completed_tasks, total_tasks
        ))

        for task in completed_tasks:
            print("\t {}".format(task['title']))

    except requests.RequestException as e:
        print("Error: {}".format(e))
