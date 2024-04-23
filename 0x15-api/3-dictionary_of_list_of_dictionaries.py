#!/usr/bin/python3
"""script that use a REST API for a website
to returns information about all users's TODO list progress,
and export it in json format."""

import json
import requests

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    dic = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()

        dic[user_id] = []
        for todo in todos:
            dic[user_id].append({
                "username": username,
                "task": todo.get("title"),
                "completed": todo.get("completed")
            })

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(dic, json_file)
