
import sys
import urllib.error
from github_api import fetch_user_events
from formatter import format_activity_list

if len(sys.argv) < 2:
    print("Usage: python main.py <github_username>")
    sys.exit(1)
    
try:
    username = sys.argv[1]
    events = fetch_user_events(username)
    print(format_activity_list(username, events))
    
except urllib.error.HTTPError as e:
    if e.code == 404:
        print(f"404: Username not found for {username}")

    elif e.code == 403:
        print("403: API rate limit exceeded. Please try again later.")

    else:
        print(f"HTTP error occurred: {e.code} - {e.reason}")

    sys.exit(1)
        
except urllib.error.URLError:
    print("Network error occurred. Please check your internet connection.")
    sys.exit(1)