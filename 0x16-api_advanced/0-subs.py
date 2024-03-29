#!/usr/bin/python3
"""
Retrieving the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given
    subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
        If the subreddit is invalid, return 0.
    """
    # Check if subreddit is a valid string
    if not isinstance(subreddit, str):
        return 0

    # Set a custom User-Agent to avoid Too Many Requests error
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Construct the Reddit API URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=user_agent)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        results = response.json()

        # Extract and return the number of subscribers
        return results['data']['subscribers']
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0


# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"{subreddit} has {subscribers} subscribers.")
