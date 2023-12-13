#!/usr/bin/python3
import requests


def count_words(subreddit, word_list, after="", word_counts=None):
    """Count occurrences of words in the titles of hot posts in a subreddit"""

    # Initialize word_counts if not provided
    if word_counts is None:
        word_counts = {word: 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}
    headers = {'user-agent': 'bhalut'}

    try:
        # Make a GET request to the Reddit API
        response = requests.get(
            url,
            params=params,
            allow_redirects=False,
            headers=headers
        )
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        data = response.json()

        for topic in data['data']['children']:
            for word in topic['data']['title'].split():
                normalized_word = word.lower()
                if normalized_word in word_counts:
                    word_counts[normalized_word] += 1

        after = data['data']['after']

        if after is None:
            # Combine counts for case-insensitive identical words
            for i, word in enumerate(word_list):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        word_counts[word_list[i].lower()] += word_counts[word_list[j].lower()]
                        word_counts[word_list[j].lower()] = 0

            # Sort and print the results
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_word_counts:
                if count > 0:
                    print(f"{word}: {count}")
        else:
            count_words(subreddit, word_list, after, word_counts)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Example usage
if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass a subreddit as an argument.")
    elif len(sys.argv) < 3:
        print("Please pass a list of words to count.")
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
