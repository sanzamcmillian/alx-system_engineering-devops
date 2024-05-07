#!/usr/bin/python3
"""recursive function that queries the RedditAPI"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """function that queries the Reddit API and
       returns a list containing the titles of
       all hot articles for a given subreddit
    """
    if hot_list:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'MyBot/1.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
