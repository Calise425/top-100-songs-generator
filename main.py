import requests
from bs4 import BeautifulSoup
import lxml
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

# Spotipy setup
scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

# Actually getting the top 100 most popular songs of an era
date = input("What day would you like the top 100 songs of? (YYYY-MM-DD): ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "lxml")
song_title_tags = soup.select(selector="li ul li h3")
song_titles = []
for song in song_title_tags:
    song_titles.append(song.text.strip())

print(song_titles)