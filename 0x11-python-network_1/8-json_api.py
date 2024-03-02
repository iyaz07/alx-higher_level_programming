#!/usr/bin/python3
"""Script to send a POST request to search_user endpoint"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"

    # Set q to the provided letter or empty string if not provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Send POST request
    try:
        response = requests.post(url, data={'q': q})
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()

        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print("Error:", e)
    except ValueError:
        print("Not a valid JSON")

