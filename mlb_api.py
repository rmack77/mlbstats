import requests


# Get MLB teams return json data from the MLB Stats API
def get_mlb_teams():
    """Fetch MLB teams from the MLB Stats API."""
    return api_call("https://statsapi.mlb.com/api/v1/teams?sportId=1")


# Make an API call, return json data
def api_call(endpoint):
    """Make an API call to fetch MLB teams and print their names."""
    url = endpoint
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.text}")
