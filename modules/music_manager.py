import urllib
import webbrowser

class MusicManager:
    
    def play_song(self, song):
        print(f"Playing {song}")
        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(song)
        webbrowser.open(url)