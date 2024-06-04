#!/usr/bin/python3
""" module that contins the function
def count_words(subreddit, words_list, after="", words_dict={}):
"""

import requests

reddit_url = "https://www.reddit.com/"


def count_words(subreddit, words_list, after="", words_dict={}):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function returns None.
    """
    if not words_dict:
        for word in words_list:
            words_dict[word] = 0

    if after is None:
        words_list = [[key, value] for key, value in words_dict.items()]
        words_list = words_list.sort(key=lambda x: (-x[1], x[0]))
        for element in words_list:
            if element[1]:
                print(f"{element[0].lower()}: {element[1]}")
        return None

    url = reddit_url + f"r/{subreddit}/hot/.json"

    response = requests.get(url,  params={
        'limit': 100,
        'after': after
    })

    if response.status_code != 200:
        return None

    try:
        js = response.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower_case = [elem.lower() for elem in title.split(' ')]

            for element in words_list:
                words_dict[element] += lower_case.count(element.lower())

    except Exception:
        return None

    count_words(subreddit, words_list, after, words_dict)
