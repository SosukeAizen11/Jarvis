import urllib
import webbrowser

class SearchEngine:
    def search_google(self, query):
        print(f"Searching for {query}")
        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
        webbrowser.open(url)