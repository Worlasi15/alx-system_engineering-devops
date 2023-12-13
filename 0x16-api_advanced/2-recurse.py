#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    """
    # Reddit API URL for getting hot articles in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Set a custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'my_bot/1.0'}

    # Parameters for pagination
    params = {'limit': 100, 'after': after}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, headers=headers, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract titles and add them to the hot_list
            children = data.get('data', {}).get('children', [])
            for child in children:
                title = child.get('data', {}).get('title', '')
                hot_list.append(title)

            # Check if there are more pages (pagination)
            after = data.get('data', {}).get('after')
            if after is not None:
                # Recursively call the function for the next page
                recurse(subreddit, hot_list, after)
            else:
                # Return the final hot_list when there are no more pages
                return hot_list
        else:
            # If the subreddit is invalid or there's an issue, return None
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
