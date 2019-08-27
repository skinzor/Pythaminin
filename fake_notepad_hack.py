from pywinauto.application import Application
import time as hack

fake = input("What is your name: ")
fakel = input("Are you sure you want to run the script? ")
print("I'm running anyways :p")
print("Executing script... Script started")
hack.sleep(1)
print("Hacking You...")
hack.sleep(2)
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("View->Zoom->Zoom In")

app.UntitledNotepad.Edit.type_keys("Hello " + fake + "! You Have been fucked!!!", with_spaces = True)

app.UntitledNotepad.menu_select("Edit->Time/Date")
