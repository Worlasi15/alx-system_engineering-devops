#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers.
    If an invalid subreddit is given, the function returns 0.
    """
    # Reddit API URL for getting subreddit information
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_bot/1.0'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract and return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid or there's an issue, return 0
            return 0
    except Exception as e:
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
