#!/usr/bin/python3
""" module that contains the function def
recurse(subreddit, hot_list=[], count=0, after=None):
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """recursivley returns a list of titles of all hot articles
    for a given subreddit"""

    response = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},)

    if response.status_code >= 400 or response.status_code >= 300:
        return None

    hot_post = hot_list + [child.get("data").get("title")
                           for child in response.json()
                           .get("data").get("children")]

    fdf = response.json()
    if not fdf.get("data").get("after"):
        return hot_post

    return recurse(subreddit, hot_post, fdf.get("data").get("count"),
                   fdf.get("data").get("after"))
