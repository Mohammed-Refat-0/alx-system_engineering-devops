#!/usr/bin/python3
""" the number of subscribers for a given subreddit.
If an invalid subreddit is given, return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url)
    if response.status_code == 404 or response.status_code >= 300:
        return 0
    else:
        return response.json().get("data", {}).get("subscribers", 0)
