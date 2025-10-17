import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

youtube_api_key = os.getenv("YOUTUBE_API_KEY")
channel_handle = "MrBeast"


def get_playlist_id():
    try:
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={channel_handle}&key={youtube_api_key}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        channel_items = data['items'][0]
        channel_playlist_id = channel_items['contentDetails']['relatedPlaylists']['uploads']

        return channel_playlist_id

    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    get_playlist_id()
