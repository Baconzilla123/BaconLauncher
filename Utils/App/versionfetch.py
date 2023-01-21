import json
import requests
import urllib.request

versions = "https://api.papermc.io/v2/projects/paper"

response = requests.get(versions)
versionsraw = response.text
versionsdict = json.loads(versionsraw)
versionslist = versionsdict["versions"]
print(versionsdict)
current = 0
for version in versionsdict["versions"]:
    current = current + 1
    print("[" + str(current) + "] " + str(version))


print("select a minecraft verion. [type number in brackets]")
version = input()

current = 0
for ver in versionslist:
    launchname = str(versions[current])
    if str(version) == (str(current + 1)):
        selectedversion = ver
        print("Found Server")

    current = current + 1

##builds


builds = "https://api.papermc.io/v2/projects/paper/versions/" + str(selectedversion)

response = requests.get(builds)
buildsraw = response.text
buildsdict = json.loads(buildsraw)
buildslist = buildsdict["builds"]
print(buildsdict)
current = 0
for build in buildslist:
    current = current + 1
    if current == len(buildslist):
        print("[" + str(current) + "] " + str(build) + " (Latest)")
    else:
        print("[" + str(current) + "] " + str(build))


print("select a server build. [type number in brackets]")
build = input()

current = 0
for bui in buildslist:
    launchname = str(buildslist[current])
    if str(build) == (str(current + 1)):
        selectedbuild = bui
        print("Found Server")

    current = current + 1

download = "https://api.papermc.io/v2/projects/paper/versions/" + str(selectedversion) + "/builds/" + str(selectedbuild) + "/downloads/paper-" + str(selectedversion) + "-" + str(selectedbuild) + ".jar"
file = "paper-" + str(selectedversion) + "-" + str(selectedbuild) + ".jar"

r = requests.get(download, allow_redirects=True)

open(file, 'wb').write(r.content)