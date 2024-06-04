#!/usr/bin/python3
""" module that contains the function def top_ten(subreddit).
"""
import requests


def number_of_subscribers(subreddit):
    """prints the titles of the first 10 hot posts listed
    for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url)
    if response.status_code >= 300 or response.status_code >= 400:
        print('None')
    else:
        for post in response.json().get('data').get('childern'):
            print(post.get('data').get('title'))
