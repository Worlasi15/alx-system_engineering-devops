#!/usr/bin/python3
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively query the Reddit API and return titles of
    all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store titles of hot articles.
        after (str): Parameter used for pagination to get the
        next set of results.

    Returns:
        list or None: List containing titles of hot articles or
        None if no results are found.
    """
    # Initialize hot_list if not provided
    if hot_list is None:
        hot_list = []

    # Set a custom User-Agent to avoid Too Many Requests error
    user_agent = {'User-Agent': 'api_advanced-project'}

    # Reddit API URL for getting hot articles in a subreddit
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Parameters for pagination
    params = {'after': after}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(url, params=params, headers=user_agent, allow_redirects=False)

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
            after_data = data.get('data', {}).get('after')
            if after_data is not None:
                # Recursively call the function for the next page
                recurse(subreddit, hot_list, after_data)
            else:
                # Return the final hot_list when there are no more pages
                return hot_list
        else:
            # If there's an issue, return None
            return None
    except requests.exceptions.RequestException as e:
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
            print(result)
        else:
            print("None")
