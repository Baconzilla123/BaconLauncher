import json
import requests
import urllib.request

searchinput = input("search term: ")

searchurl = "https://api.modrinth.com/v2/search?query=" + str(searchinput) + "&filters=categories=%22paper%22"

response = requests.get(searchurl)
searchraw = response.text
searchdict = json.loads(searchraw)
searchlist = searchdict["hits"]
current = 0
for hit in searchdict["hits"]:
    current = current + 1
    print("[" + str(current) + "] " + str(hit["title"]))


print("type a list of plugins. [type number in brackets separated by a ',']")
version = input()

current = 0
for search in searchlist:
    launchname = str(search[current])
    if str(version) == (str(current + 1)):
        selectedversion = search
        print("Found Server")

    current = current + 1
