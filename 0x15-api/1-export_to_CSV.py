#!/usr/bin/python3
"""script that use a REST API for a website with a given employee ID,
to returns information about thier TODO list progress,
and export it in csv format."""

import csv
import requests
import sys

if __name__ == "__main__":

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(id)).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    file_name = id + '.csv'
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todo:
            writer.writerow(
                [id, user.get("username"), i.get("completed"), i.get("title")])
