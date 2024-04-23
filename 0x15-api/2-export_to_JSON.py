#!/usr/bin/python3
"""script that use a REST API for a website with a given employee ID,
to returns information about thier TODO list progress,
and export it in json format."""

import csv
import json
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    dic = {}
    dic[id] = []
    for i in todo:
        dic[id].append({"task": i.get("title"), "completed": i.get(
            "completed"), "username": user.get("username")})

    with open(f'{id}.json', "w") as file:
        json.dump(dic, file)
