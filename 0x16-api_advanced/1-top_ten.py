#!/usr/bin/python3
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}

    try:
        response = requests.get(url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Check if the subreddit exists
            if 'error' in data:
                print(None)
                return

            # Print titles of the first 10 hot posts
            for post in data['data']['children']:
                print(post['data']['title'])

        else:
            print(None)  # Print None for invalid subreddit or other errors

    except Exception as e:
        print(f"Error: {e}")
        print(None)


# Example usage
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
