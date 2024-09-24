import language_tool_python
from locale import getlocale
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QColor

def getLanguage(lang):
    langs = [
        'en-US',
        'de-DE'
    ]
    sysLang = getlocale()[0].replace('_', '-')
    
    if sysLang in langs:
        tool = language_tool_python.LanguageTool(sysLang)
    else:
        tool = language_tool_python.LanguageTool(langs[lang])
    
    return tool

def checkWords(text: str, langTool: language_tool_python.LanguageTool):
    print("Checkpoint 3")
    matches = langTool.check(text)
    matchTupleList = []
    
    for match in matches:
        matchTupleList.append((match.offset, match.errorLength, match.replacements[0:5]))
    
    print(matchTupleList)
    return matchTupleList

def markError(tE: QTextEdit, matches: list):
    cursor = tE.textCursor()
    
    errorCharFormat = QTextCharFormat()
    errorCharFormat.setFontUnderline(True)
    errorCharFormat.setUnderlineColor(QColor('#ff0000'))
    
    for match in matches:
        print(match)
        text_length = len(tE.toPlainText())
        
        if match[0] < 0 or match[0] >= text_length or (match[0] + match[1]) > text_length:
            continue  # Skip if the match is out of bounds
        
        try:
            cursor.setPosition(match[0])
            cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, match[1])
            cursor.mergeCharFormat(errorCharFormat)
        except Exception as e:
            print(e)

def checkErrors(lang, text):
    print("Checkpoint 2")
    tool = getLanguage(lang)
    matches = checkWords(text, tool)
    return matches