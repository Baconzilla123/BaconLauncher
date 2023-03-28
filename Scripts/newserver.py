import os
import json
import requests

class main:
    instancedir = json.loads(open("./LauncherConfig.json").read())["InstanceDir"]
    jarname = ""
    foldername = ""

    def makeserverfolder(jar, version, type):
        name = input("Name The Server Folder: ")
        mem = str(int(input("Amount Of Allocated Memory (GB): ")) * 1000)

        foldername = (str(name) + " [" + type + "] (" + version + ")")
        main.foldername = foldername
        if str(jar).endswith(".jar"):
            jarname = str(jar)
        else:
            jarname = str(jar) + '.jar'
        path = os.path.join(main.instancedir,str(foldername))
        os.mkdir(path)
        os.mkdir((path + "/Config"))
        os.mkdir((path + "/Server"))
        ##os.mkdir(str(foldername) + "/Scripts")
        with open( path + '/Config/ServerInfo.json', 'x') as f:
            serverinfodict = {
                "JarName":jarname,
                "Mem":mem
            }
            serverinfo = json.dumps(serverinfodict)

            f.write(serverinfo)
            f.close()

    def main():
        ##versions

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


        print("select a server build, enter nothing for the latest. [type number in brackets]")
        build = input()
        if build == "":
            selectedbuild = buildslist[len(buildslist) - 1]
        else:
            current = 0
            for bui in buildslist:
                launchname = str(buildslist[current])
                if str(build) == (str(current + 1)):
                    selectedbuild = bui
                    print("Found Server")

                current = current + 1

        download = "https://api.papermc.io/v2/projects/paper/versions/" + str(selectedversion) + "/builds/" + str(selectedbuild) + "/downloads/paper-" + str(selectedversion) + "-" + str(selectedbuild) + ".jar"
        file = "paper-" + str(selectedversion) + "-" + str(selectedbuild) + ".jar"

        main.makeserverfolder(file, selectedversion, servertype)

        r = requests.get(download, allow_redirects=True)

        open(file, 'wb').write(r.content)
        path = os.path.join(main.instancedir,str(main.foldername))
        os.rename('./' + file, path + "/Server/" + file)