import requests

def get_mlb_teams():
    """Fetch MLB teams from the MLB Stats API."""
    return api_call("https://statsapi.mlb.com/api/v1/teams?sportId=1")

def get_standings():
    """Fetch MLB standings from the MLB Stats API."""
    return api_call("https://statsapi.mlb.com/api/v1/standings?leagueId=104&season=2025&standingsTypes=regularSeason&date=2025-05-26")

def api_call(endpoint):
    """Make an API call to fetch MLB teams and print their names."""
    url = endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
