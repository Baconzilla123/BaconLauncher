import os
import subprocess
import time

batches = []
servernames = []
pluginlist = []
modlist = []

mainpath = "./"

servername = ""
servertype = ""
serververs = ""

for root, dirs, files in os.walk(mainpath):
    for file in files:
        if file.endswith(".bat"):
            if root.__contains__("Utils") == False:
                path = os.path.join(root, file)
                name = root.lstrip(mainpath)
                print("[Found] " + path)
                if file == "startserver.bat":
                    print("[Starter] " + file)
                    print("(ServerName)" + name)
                    batches.append(path)
                    servernames.append(name)

os.system('cls')

current = 0
for batch in batches:
    server = str(servernames[current]).split(" ")

    servername = str(server[0])
    servertype = str(server[1]).strip("[]")
    serververs = str(server[2]).strip("()")
    serververs = serververs.rstrip(")\Batches")

    print("[" + str(current + 1) + "] " + servername + " (" + servertype + " " + str(serververs) + ")")
    current = current + 1

prompt = "\nType the number or the name of the server you want to start.\nor add ' -p' to view the plugins or '-m' to view the mods."

print(prompt)
selected = input()
selectedserver = ""
selectedbatch = ""

launch = True



current = 0
for batch in batches:
    launchname = (str(servernames[current]).split(" "))[0]
    if str(selected).__contains__(str(current + 1)):
        selectedserver = (mainpath + str(servernames[current]).strip("\Batches") + "/Server")
        selectedbatch = batch
        print("Found Server")
    elif (str(launchname).lower()).__contains__(selected.lower().removesuffix(" -m")):
        selectedserver = (mainpath + str(servernames[current]).strip("\Batches") + "/Server")
        selectedbatch = batch
        print("Found Server")

    current = current + 1


if str(selected).__contains__("-p"):
    launch = False
    plugins = (selectedserver + "/plugins")
    print("Scanning Plugins...")
    try:
        for root, dirs, files in os.walk(plugins):
            for file in files:
                if file.endswith(".jar"):
                    path = os.path.join(root, file)
                    name = file
                    
                    pluginlist.append(name)
                    print("[Plugin] " + name)
    except:
        print("No Plugins found :[ \n closing in 3s")
        time.sleep(3)
    if pluginlist == []:
        print("No Plugins found :[ \n closing in 3s")
        time.sleep(3)

if str(selected).__contains__("-m"):
    launch = False
    mods = (selectedserver + "/mods")
    print("Scanning Mods...")
    try:
        for root, dirs, files in os.walk(mods):
            for file in files:
                if file.endswith(".jar"):
                    path = os.path.join(root, file)
                    name = file
                    
                    modlist.append(name)
                    print("[Mod] " + name)
    except:
        print("No Mods found :[ \n closing in 3s")
        time.sleep(3)
    if modlist == []:
        print("No Mods found :[ \n closing in 3s")
        time.sleep(3)

if launch:
    subprocess.call(selectedbatch)

