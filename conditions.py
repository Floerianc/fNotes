from os import listdir
from PyQt5.QtGui import QTextOption

def tmpFileCondition(nameLabel):
    if nameLabel == "":
        return False
    
    noteName = nameLabel.replace(' ', '_')
    
    if "Tmp" not in nameLabel:
        noteName = f"{nameLabel.replace(' ', '_')}Tmp"
    return noteName

def returnPathIfNoteExists(notes, noteName):
    for note in notes:
        if noteName == note[1]:
            path = f"{note[0]}/{note[1]}"
    return path

def IndexOfNoteInList(listWidgets, note):
    for listWidget in listWidgets:
        for i in range(listWidget.count()):
            
            if listWidget.item(i).text() == note:
                return listWidget, i
    return None, None

def PDFNameCondition(name, content):
    if str(name) == "" or str(content) == "":
        return False
    else:
        return True

def getLanguage(index):
    languages = listdir('asset/doc')
    filename = f"asset/doc/{languages[index]}"
    
    with open(filename, "r", encoding="UTF-8") as doc:
        content = doc.read()
        return content

getLanguage(0)

def autoSaveTime(time):
    if time == 0:
        time = 9509509
    return time

def getwordWrapStatus(status):
    
    wraps = {
        '0': QTextOption.WrapMode.NoWrap,
        '2': QTextOption.WrapMode.WrapAnywhere
    }
    return wraps[str(status)]
