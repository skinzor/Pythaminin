import os as linux

# Set FOLDER where all repos will be cloned
folder_name = input("Enter Folder Name Where repo's will be cloned: ")
print("All repo's will be saved in the " + repr(folder_name) + " Directory!")

# Printing + The Repos
peppy = ("https://zxq.co/ripple/pep.py")
print("1.pep.py")

lets = ("https://zxq.co/ripple/lets")
print("2.LETS")

hanayo = ("zxq.co/ripple/hanayo")
print("3.Hanayo")

rippleapi = ("zxq.co/ripple/rippleapi")
print("4.Ripple-Api")

avatar_server = ("github.com/Uniminin/avatar-server")
print("5.Avatar-Server")

# Git
git = "git clone "
go = "go get -u "

while True:
    repo = input("Select Repositories To Clone: ")
    if repo == '1':
        print('Cloning pep.py')
        linux.system("mkdir " + folder_name + " && cd " + folder_name)
        linux.system(git + peppy)
        break
    if repo == '2':
        print('Cloning Lets')
        linux.system("mkdir " + folder_name + " && cd " + folder_name)
        linux.system(git + lets)
        break
    if repo == '3':
        print("Cloning Hanayo")
        linux.system(go + hanayo)
        break
    if repo == '4':
        print("Cloning Ripple-Api")
        linux.system(go + rippleapi)
        break
    if repo == '5':
        print("Cloning into Avatar-Server")
        linux.system(go + avatar_server)
        break
    if repo == 'all':
        print("Cloning All Repositories")
        linux.system("mkdir " + folder_name + " && cd " + folder_name)
        linux.system(git + peppy)
        linux.system(git + lets)
        linux.system(go + hanayo)
        linux.system(go + rippleapi)
        linux.system(go + avatar_server)
        break
print("Hanayo, Rippleapi, Avatar-Server has been cloned into the GO-Path!")
print('Done Cloning')
