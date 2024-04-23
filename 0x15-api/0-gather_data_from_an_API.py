#!/usr/bin/python3
"""script that use a REST API for a website with a given employee ID,
to returns information about thier TODO list progress."""

import requests
import sys

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [i.get("title") for i in todo if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todo)))
    [print("\t {}".format(c)) for c in completed]
