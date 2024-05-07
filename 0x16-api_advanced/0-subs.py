#!/usr/bin/python3
"""api to check number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Function to check the subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MyBot/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers

    elif response.status_code == 404:
        return 0

    else:
        print(f"Error: {response.status_code} - {response.reason}")
        return 0
