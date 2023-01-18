import os

name = input("Name The Server Folder: ")
version = input("Enter Server Version: ")
type = input("Server Software You Are Using: ")
jar = input("The Name Of The Server Jar: ")
mem = input("Amount Of Allocated Memory (MB): ")

foldername = (str(name) + " [" + type + "] (" + version + ")")

if jar.endswith(".jar"):
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

    