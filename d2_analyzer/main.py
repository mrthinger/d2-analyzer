import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from open_dota_api_client import Client

opendota_client = Client(base_url="https://api.opendota.com/api")

# Define a default retry configuration
def default_retry(func):
    @retry(stop=stop_after_attempt(3), wait=wait_fixed(5), retry_error_callback=lambda x: print(f"Failed after 3 retries for {func.__name__}."))
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@default_retry
def fetch_recent_matches():
    response = requests.get("https://api.opendota.com/api/publicMatches")
    response.raise_for_status()
    return response.json()

@default_retry
def fetch_replay_info(match_id):
    response = requests.get(f"https://api.opendota.com/api/replays/{match_id}")
    response.raise_for_status()
    return response.json()  # The endpoint returns an array, so we take the first element

def fetch_parsed_matches():
    response = requests.get("https://api.opendota.com/api/parsedMatches")
    response.raise_for_status()
    return response.json()

@default_retry
def download_replay(cluster, match_id, replay_salt):
    replay_url = f"http://replay{cluster}.valve.net/570/{match_id}_{replay_salt}.dem.bz2"
    replay_data = requests.get(replay_url).content
    with open(f"{match_id}.dem.bz2", "wb") as f:
        f.write(replay_data)

# Usage:
matches = fetch_recent_matches()
for match in matches:
    match_id = match['match_id']
    replay_info = fetch_replay_info(match_id)
    cluster = replay_info['cluster']
    replay_salt = replay_info['replay_salt']
    download_replay(cluster, match_id, replay_salt)
