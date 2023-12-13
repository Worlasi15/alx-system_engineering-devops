#!/usr/bin/python3
"""
Printing titles of
the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Check if subreddit is a valid string
    if not isinstance(subreddit, str):
        print("None")
        return

    # Set a custom User-Agent to avoid Too Many Requests error
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Parameters for limiting to the first 10 hot posts
    params = {'limit': 10}

    # Construct the Reddit API URL for hot posts
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=user_agent, params=params)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        results = response.json()

        # Extract and print the titles of the first 10 hot posts
        my_data = results.get('data', {}).get('children', [])
        for post in my_data:
            title = post.get('data', {}).get('title', '')
            print(title)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("None")


# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
