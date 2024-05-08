#!/usr/bin/python3
"""  recursive function that queries the Reddit API"""
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, hot_list=None):
    """recursive function that queries the Reddit API,
      parses the title of all hot articles,
      and prints a sorted count of given keywords
      (case-insensitive, delimited by spaces
    """
    if hot_list is None:
      hot_list = []

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
          return count_words(subreddit, word_list, after, hot_list)
       else:
          keyword_count = Counter()
          for title in hot_list:
             for word in word_list:
                if word.lower() in title.lower().split():
                   keyword_count[word.lower()] += 1

          sorted_counts = sorted(keyword_count.items(), key=lambda x: (-x[1], x[0]))
          for keyword, count in sorted_counts:
             print(f"{keyword}: {count}")
    else:
        print(f"Error: {response.status_code} - {response.reason}")
