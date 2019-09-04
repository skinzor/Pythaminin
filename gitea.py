import os as ubuntu
import time

while True:
    gitea = input("Do you have go installed? y/n: ")
    if gitea == 'n':
        print("Installing Go!")
        ubuntu.system("sudo apt-get update && sudo apt-get update -y")
        ubuntu.system("sudo add-apt-repository ppa:longsleep/golang-backports -y && sudo apt-get update")
        ubuntu.system("sudo apt-get install golang-go -y")
        ubuntu.system("echo 'export GOPATH=$HOME/go' >> ~/.bashrc")
        ubuntu.system("echo 'export PATH=${PATH}:${GOPATH}/bin' >> ~/.bashrc")
        ubuntu.system("source ~/.bashrc")
        ubuntu.system("go get -d -u code.gitea.io/gitea")
        ubuntu.system("cd go/src/code.gitea.io/gitea")
        ubuntu.system('TAGS="bindata" make generate build')
        ubuntu.system("./gitea web")
        break
    if gitea == 'y':
        print("Cloning Gitea into go path...")
        time.sleep(2)
        ubuntu.system("go get -d -u code.gitea.io/gitea")
        ubuntu.system("cd go/src/code.gitea.io/gitea")
        ubuntu.system('TAGS="bindata" make generate build')
        ubuntu.system("./gitea web")
        break
