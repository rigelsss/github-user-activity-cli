import urllib.request
import json

def fetch_user_events(username):
    """
    Busca os eventos públicos recentes de um usuário do GitHub.
    Pode lançar urllib.error.HTTPError ou urllib.error.URLError.
    """
    
    url = f"https://api.github.com/users/{username}/events"
    request = urllib.request.Request(url, headers={"User-Agent": "github-activity-cli"})
    response = urllib.request.urlopen(request)
    raw_bytes = response.read()
    text = raw_bytes.decode("utf-8")
    events = json.loads(text)
    return events