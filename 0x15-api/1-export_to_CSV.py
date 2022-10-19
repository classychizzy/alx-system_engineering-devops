#!/usr/bin/python3
"""a file that exports a response from an api in
csv format"""


import requests
import sys
import csv

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(userId)
        )
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(
            f, delimiter=',', quotechar='"',
            quoting=csv.QUOTE_ALL, lineterminator='\n'
            )
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow(
                    [userId, name, str(task.get('completed')),
                        task.get('title')]
                    )
