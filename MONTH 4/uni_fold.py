from subprocess import call

folder_name = input("Enter Folder Name: ")
number = 0

while True:
    call(f'mkdir {folder_name}{number}', shell=True)
    print(f"Created {folder_name}{number}")
    number += 1
