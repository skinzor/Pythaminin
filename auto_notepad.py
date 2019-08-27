from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("View->Zoom->Zoom In")

app.UntitledNotepad.Edit.type_keys("Hello! This is a test python automation written by uniminin ", with_spaces = True)

app.UntitledNotepad.menu_select("Edit->Time/Date")
