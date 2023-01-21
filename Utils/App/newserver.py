import os
import json
import requests
import urllib.request

class main:
    jarname = ""
    foldername = ""

def makeserverfolder(jar, version, type):
    name = input("Name The Server Folder: ")
    mem = input("Amount Of Allocated Memory (MB): ")

    foldername = (str(name) + " [" + type + "] (" + version + ")")
    main.foldername = foldername
    if str(jar).endswith(".jar"):
        jarname = str(jar)
    else:
        jarname = str(jar) + '.jar'
    os.mkdir(str(foldername))
    os.mkdir((str(foldername) + "/Batches"))
    os.mkdir((str(foldername) + "/Server"))
    os.mkdir(str(foldername) + "/Ngrok")

    with open( str(foldername) + '/Batches/startserver.bat', 'w') as f:
        f.write('cd "./' + foldername + "/Batches" + '"\n')
        f.write('start ngrok.bat\n')
        f.write('cd "../Server"\n')
        f.write('java -Xms' + str(mem) + 'M -Xmx' + str(mem) + 'M -jar ' + jarname + '\n')
        f.write('exit')
        f.close()
    with open( str(foldername) + '/Batches/ngrok.bat', 'w') as f:
        f.write('cd "../Ngrok"\n')
        f.write('ngrok --region au tcp 25565\n')
        f.write('cd "./Batches"\n')
        f.write('exit')
        f.close()
    with open( str(foldername) + '/Batches/stopserver.bat', 'w') as f:
        f.write('taskill /f /im cmd.exe /t')
        f.write('exit')
        f.close()



versions = "https://api.papermc.io/v2/projects/paper"

servertype = "paper"


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

makeserverfolder(file, selectedversion, servertype)

r = requests.get(download, allow_redirects=True)

open(file, 'wb').write(r.content)
os.rename('./' + file, './' + str(main.foldername) + "/Server/" + file)