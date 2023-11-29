#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Employee ID provided as a command-line argument
    employee_id = sys.argv[1]

    # API endpoint URL for the employee's TODO list
    url = 'https://jsonplaceholder.typicode.com/users
    /{}/todos'.format(employee_id)

    # Fetching data from the API
    response = requests.get(url)
    todos = response.json()

    # Getting employee information from the API
    employee_info_url = 'https://jsonplaceholder.typicode.com
    /users/{}'.format(employee_id)
    employee_info = requests.get(employee_info_url).json()
    employee_name = employee_info.get('name')

    # Counting the number of completed tasks
    completed_tasks = [task for task in todos if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Displaying employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format
            (employee_name, num_completed_tasks, total_tasks))

    # Displaying titles of completed tasks
    for task in completed_tasks:
        print("\t {}".format(task['title']))
