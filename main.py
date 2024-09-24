from sys import argv
from os import(
    listdir, 
    remove
)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import(
    QColorDialog, 
    QFileDialog, 
    QFontDialog
)
from xhtml2pdf import pisa
from asset.ui.py.ui import *
from asset.ui.py.about import *
from asset.ui.py.settingsUI import *
from asset.ui.py.table import *
from asset.ui.py.script import *
from worker import *
from calc import calculate
import conditions as c
import settings
import table
import translation
import crypto
import grammar
import script_handler

'''
i hate creating comments
'''

class Application(Ui_MainWindow):
    def __init__(self, form) -> None:
        super().__init__()
        
        self.language = 0
        self.lang = dict
        self.dec = 9
        self.autoSave = 5
        self.wrap = QtGui.QTextOption.WrapMode.WordWrap
        self.fontsize = 8
        
        self.setupUi(form)
        self.listNotes()
        self.connectButtons()
        self.connectWorker()
        self.applyConfig()
    
    def connectButtons(self):
        '''This function connects every button to a certain function
        Note that I use lambda on a few buttons so I can use the parameter(s)
        on the given function.
        '''
        
        button_mappings = {
            self.deleteCurrentNote:     self.deleteNote,
            self.colorPickerButton:     self.setColor,
            self.markerPickerButton:    self.setMarker,
            self.math:                  self.calc,
            self.fontButton:            self.changeFont,
            self.boldButton:            self.setBold,
            self.italicButton:          self.setItalic,
            self.underlineButton:       self.setUnderlined,
            self.imageButton:           self.insertPicture,
            self.tableButton:           self.table,
            self.createListDot:         lambda: self.createList('LD'),
            self.createListDec:         lambda: self.createList('LDec'),
            self.createListGreek:       lambda: self.createList('LUA'),
            self.createListRoman:       lambda: self.createList('LUR'),
            self.supButton:             lambda: self.setSupOrSub('sup'),
            self.subButton:             lambda: self.setSupOrSub('sub'),
            self.removeSupSub:          lambda: self.setSupOrSub('rm'),
            self.Left:                  lambda: self.setAlignment('L'),
            self.Middle:                lambda: self.setAlignment('M'),
            self.Right:                 lambda: self.setAlignment('R'),
        }
        
        for button, func in button_mappings.items():
            button.clicked.connect(func)
        
        action_mappings = {
            self.actionSave:                        self.saveNote,
            self.actionExit:                        self.deleteNote,
            self.actionNew:                         self.newNote,
            self.actionAbout:                       self.showAbout,
            self.actionOpen:                        self.openNoteFromMenu,
            self.actionSettings:                    self.showSettings,
            self.actionBold:                        self.setBold,
            self.actionUnderline:                   self.setUnderlined,
            self.actionItalic:                      self.setItalic,
            self.actionText_Color:                  self.setColor,
            self.actionText_Background_Color:       self.setMarker,
            self.actionMath_2:                      self.calc,
            self.actionChange_Font:                 self.changeFont,
            self.actionCheck_Grammar_EXPERIMENTIAL: self.grammarInit,
            self.actionExport_as_PDF:               self.saveAsPDF,
            self.actionExport_as_HTML:              self.saveAsHTML,
            self.actionPython_Script:               self.script,
            self.actionExit_2:                      lambda: self.closeWindow(self), # instead of closing it just let it crash lol
            self.actionLeft:                        lambda: self.setAlignment('L'),
            self.actionCenter:                      lambda: self.setAlignment('M'),
            self.actionRight:                       lambda: self.setAlignment('R'),
            self.actionSup:                         lambda: self.setSupOrSub('sup'),
            self.actionSub:                         lambda: self.setSupOrSub('sub'),
            self.actionRemove_Sup_Sub:              lambda: self.setSupOrSub('rm'),
            self.actionBulletpoint:                 lambda: self.createList('LD'),
            self.actionDecimal:                     lambda: self.createList('LDec'),
            self.actionAlphabet:                    lambda: self.createList('LUA'),
            self.actionRoman_Numbers:               lambda: self.createList('LUR'),
        }
        
        for button, func in action_mappings.items():
            button.triggered.connect(func)
        
        self.fontWeightSpin.valueChanged.connect(self.setFontWeight)
        self.fontSizeSpin.valueChanged.connect(self.setFontSizeSpin)
        
        self.listWidget.clicked.connect(lambda: self.openNoteFromListWidget(self.listWidget))
        self.tmpListWidget.clicked.connect(lambda: self.openNoteFromListWidget(self.tmpListWidget))
        
        self.searchBarRegular.textChanged.connect(lambda: self.searchItems(self.listWidget, self.searchBarRegular))
        self.searchBarTmp.textChanged.connect(lambda: self.searchItems(self.tmpListWidget, self.searchBarTmp))
    
    def connectWorker(self):
        '''Connects the WorkerThread to a function and starts it'''
        self.Worker = WorkerThread(self.autoSave)
        self.Worker.updateNote.connect(self.saveTmp)
        self.Worker.start()
        
        self.WorkerStats = WorkerThreadStats()
        self.WorkerStats.updateStats.connect(self.updateStatsEditor)
        self.WorkerStats.start()
    
    def applyConfig(self):
        '''Applies the config of the user
        
        First it saves their value in variables.
        a few functions will change immediately 
        when changing the variables value.
        
        However, a few functions/elements,
        such as the editor, need a specific
        function.
        '''
        finishedConfig = settings.readConfig()
        
        self.language = finishedConfig['language']
        self.dec = finishedConfig['decimalNumbers']
        self.autoSave = c.autoSaveTime(finishedConfig['autoSave'])
        self.wrap = c.getwordWrapStatus(finishedConfig['wrap'])
        self.fontsize = finishedConfig['fontsize']
        
        self.editor.setWordWrapMode(self.wrap)
        self.editor.setFontPointSize(self.fontsize)
        self.fontSizeSpin.setValue(int(self.fontsize))
        
        self.lang = translation.getCurrentLanguage(self.language)
        translation.applyLanguage(self, self.language, 'main')
    
    def getNotes(self):
        '''Returns a list of each note and its relative path
        
        For each directory it goes through every note in that folder
        
        and adds it along with its path to a list in a tuple.
        '''
        dirs = [
            "./user_content/note",
            "./user_content/tmp"
        ]
        notes = []
        
        for directory in dirs:
            for note in listdir(directory):
                notes.append((directory, note))
        return notes
    
    def listNotes(self):
        '''Adds all notes to their listWidget
        
        1. It gets all notes from getNotes()
        2. Clears both lists to prevent notes from duplicating in lists
        3. Adds each note to it's list
            If the files path has "tmp" in its name it will be moved over to the tmpListWidget
        '''
        notes = self.getNotes()
        
        self.listWidget.clear()
        self.tmpListWidget.clear()
        
        for note in notes:
            if "tmp" in note[0]:
                self.tmpListWidget.addItem(note[1])
            else:
                self.listWidget.addItem(note[1])
    
    def openNoteFromListWidget(self, listWidget):
        '''Gets the path of the note selected and reads from it
        
        After getting a list of each note from getNotes() the
        program gets the text of the Item that has been selected.
        
        So if you press on "Example" it will also return you the text
        "Example".
        
        After that it tries to find the path to that note.
        So if you clicked on "Example" it will look for the file "Example"
        in the ./user_content/note and in the ./user_content/tmp directory.
        
        If it finds the fitting file it returns the path, reads from that file
        and sets the editors text to the content from that file.
        It will also set the namelabels text to the name of that file.
        '''
        notes = self.getNotes()
        itemText = listWidget.currentItem().text()
        path = c.returnPathIfNoteExists(notes, itemText)
        content = crypto.decrypt(path)
        
        self.editor.setText(content)
        self.namelabel.setText(itemText)
    
    def openNoteFromMenu(self):
        notePath = QFileDialog.getOpenFileName(Form)
        noteName = notePath[0].split("/")[-1]
        
        try:
            content = crypto.decrypt(notePath[0])
            self.editor.setHtml(content)
            self.namelabel.setText(noteName)
        except Exception as e:
            raise BaseException(f"The program failed to open a Note from the Menu\nperhaps it was because of the decrypt function.\n{e}")
    
    def saveNote(self):
        '''Saves note to the ./user_content/note folder
        
        It replaces the spaces in self.namelabels text with underscores.
        In that way we won't have any problems with redirecting to that path
        later on. 
        '''
        noteName = f"{self.namelabel.toPlainText().replace(' ', '_')}"
        
        with open(f"./user_content/note/{noteName}", "w+", encoding="utf-8") as note:
            e = self.editor.toHtml()
            eNote = crypto.encrypt(e)
            note.write(eNote)
        
        self.listNotes()
    
    def saveTmp(self):
        '''Does the same as saveNote() but with a few more conditions (c.tmpFileCondition())
        '''
        if not c.tmpFileCondition(self.namelabel.toPlainText()):
            return
        else:
            noteName = c.tmpFileCondition(self.namelabel.toPlainText())
        
        try:
            with open(f"./user_content/tmp/{noteName}", "w+", encoding="UTF-8") as tmp:
                e = self.editor.toHtml()
                eNote = crypto.encrypt(e)
                tmp.write(eNote)
        except:
            pass
        
    
    def deleteNote(self):
        '''Deletes the selected note from the listWidget and deletes it from the Computer
        
        1. Gets all notes from getNotes()
        2. Gets name of current note (e.g. "Example")
        3. Uses c.IndexOfNoteInList(listWidgets, note) to 
        find the Index of that note in the given list.
        4. As it returns the index it will be removed from the list
        5. For each note in notes it will look for the note
        where note[1] fits with the current notes name.
        6. It takes the directory of the fitting file (e.g. "user_content\\note")
        and combines it with the name of the file (e.g. "Example")
        7. It removes the file from the system
        (Example path: "user_content\\note\\Example") 
        
            Quick Reminder:
        
        The tuple in notes consists of:
            - the directory of the file (e.g. "user_content\\note") [note[0]]
            - the name of the file (e.g. "Example") [note[1]]
        '''
        notes = self.getNotes()
        currentNote = f"{self.namelabel.toPlainText()}"
        
        listWidget, item = c.IndexOfNoteInList([self.listWidget, self.tmpListWidget], currentNote)
        listWidget.takeItem(item)
        
        path = c.returnPathIfNoteExists(notes, currentNote)
        remove(path)
        
        self.editor.clear()
        self.namelabel.clear()
    
    def newNote(self):
        '''Creates a new note
        clear the editors text and changes 
        the namelabel text to "New Note".
        '''
        self.editor.clear()
        self.namelabel.setText("New Note")
    
    def searchItems(self, listWidget: QtWidgets.QListWidget, searchBar: QtWidgets.QTextEdit):
        d = {
            self.listWidget: 'user_content\\note',
            self.tmpListWidget: 'user_content\\tmp'
        }
        
        query = searchBar.toPlainText().lower()
        path = d[listWidget]
        notes = listdir(path)
        listWidget.clear()
        
        for note in notes:
            if query in note.lower():
                listWidget.addItem(note)
    
    
    def setBold(self):
        '''Makes the font bold if it isn't and vice versa'''
        if self.editor.fontWeight() != QFont.Weight.Bold:
            self.editor.setFontWeight(QFont.Weight.Bold)
        
        else:
            self.editor.setFontWeight(QFont.Weight.Normal)
    
    def setItalic(self):
        '''Turns the font italic if it isn't and vice versa'''
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not state)
    
    def setUnderlined(self):
        '''Underlines the font if it isn't and... you know already'''
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not state)
    
    def setFontSizeSpin(self):
        '''Sets the Font point size to the value in the spinBox'''
        self.editor.setFontPointSize(self.fontSizeSpin.value())
    
    def setAlignment(self, direction):
        '''Sets Alignment of the text
        
        When the function is called, we give the parameter a value.
        
        For example, we can use "L" as the direction (parameter).
        
        Then we cycle through each alignment in the alignments list
        and if our direction ("L") is in one of the elements within
        the tuple then we will get the Alignment in that tuple
        and apply it to the text in that line.
        '''
        alignments = {
            'L': QtCore.Qt.AlignmentFlag.AlignLeft,
            'M': QtCore.Qt.AlignmentFlag.AlignCenter,
            'R': QtCore.Qt.AlignmentFlag.AlignRight
        }
        self.editor.setAlignment(alignments[direction])
    
    def setColor(self):
        '''Changes the color of the text
        
        First it opens the QColorDialog so you can choose a color.
        Then we change the text color to the color you chose.
        
        After thats done, we change the stylesheet of the button you pressed
        so the color fits with the color you selected.'''
        color = QColorDialog.getColor()
        self.editor.setTextColor(color)
        self.colorPickerButton.setStyleSheet(
            f"background-color:{color.name()};\n "
            "border-style: solid;\n "
            "border-color: rgb(255, 255, 255);\n "
            "border-width: 2px"
        )
    
    def setMarker(self):
        '''Changes the background of the text
        
        Same as setColor() but with the Background Color
        instead of the text color'''
        color = QColorDialog.getColor()
        self.editor.setTextBackgroundColor(color)
        self.markerPickerButton.setStyleSheet(
            f"background-color:{color.name()};\n"
            "border-style: solid;\n "
            "border-color: rgb(255, 255, 255);\n "
            "border-width: 2px"
        )
    
    def createList(self, listStyleName):
        '''Creates a list in the editor
        
        When the function is called, we give the parameter
        (in this case it's listStyleName) a value
        
        The values can be:
        - LD
        - LDec
        - LUA
        - LUR
        
        Each of these values are connected to a specific
        List Design.
        
        The program checks where the cursor in your editor is
        and creates a list in that line with a style from this list.'''
        lists = {
            'LD': QtGui.QTextListFormat.Style.ListDisc,
            'LDec': QtGui.QTextListFormat.Style.ListDecimal,
            'LUA': QtGui.QTextListFormat.Style.ListUpperAlpha,
            'LUR': QtGui.QTextListFormat.Style.ListUpperRoman
        }
        
        cursor = self.editor.textCursor()
        cursor.createList(lists[listStyleName])
    
    def calc(self):
        '''Tries to solve a given mathematical problem in the selected Text
        
        The expression is the selected text (e.g. "9+9" or sqrt2)
        The result is returned from the calculate function in calc.py
        
        After we get the result we insert that result in the editor.
        '''
        expression = self.editor.textCursor().selectedText()
        result = calculate(expression, self.dec)
        
        self.editor.insertPlainText(f"{result}")
    
    def showAbout(self):
        '''Displays the "About" Window.'''
        self.aboutWindow = QtWidgets.QDialog()
        self.aboutUI = Ui_Form()
        self.aboutUI.setupUi(self.aboutWindow)
        
        content = c.getLanguage(self.language)
        
        self.aboutUI.textEdit.setMarkdown(content)
        self.aboutWindow.show()
    
    def saveAsPDF(self):
        '''Saves the users note as a PDF
        
        First we get the path where we have
        to save the PDF to via a QFileDialog.
        
        After thats done we convert the editors
        content into a .HTML script.
        
        Then we check the name of the PDF and if
        it's valid.
        
        If the name is valid we create a PDF
        using xhtml2pdf and the CreatePDF function.
        We give it the content of the editor as HTML
        and the file object (BufferedRandom) as params.
        '''
        pdfPath = QFileDialog.getSaveFileName(Form)
        content = self.editor.toHtml()
        
        if c.PDFNameCondition(pdfPath, self.editor.toPlainText()):
            with open(f"{pdfPath[0]}.pdf", "w+b") as pdf:
                pisa.CreatePDF(content, pdf)
        else:
            return
    
    def showSettings(self):
        '''Displays the Settings Window
        '''
        self.settingsWindow = QtWidgets.QDialog()
        
        self.settingsUI = UI_Form_Settings()
        self.settingsUI.setupUi(self.settingsWindow)
        
        self.settingsUI.buttonBox.accepted.connect(self.updateSettings)
        self.settingsUI.buttonBox.rejected.connect(lambda: self.closeWindow(self.settingsWindow))
        
        translation.applyLanguage(self.settingsUI, self.language, 'settings')
        
        self.settingsWindow.show()
    
    def closeWindow(self, window):
        '''Closes a given window'''
        window.close()
    
    def updateSettings(self):
        '''Updates the settings and applies them
        
        First we create a dict that features all the values
        within the settings like the language, autoSave interval
        and the standard font-size.
        
        Then we call the function writeConfig(), 
        for more information go to the definition.
        
        After we have re-written the config file
        and applied the config, we close the window
        '''
        appliedSettings = {
            'lang': self.settingsUI.langComboBox.currentIndex(),
            'dec': self.settingsUI.decSpinBox.value(),
            'auto': self.settingsUI.intervalSpinBox.value(),
            'wrap': self.settingsUI.wordWrap.checkState(),
            'fontsize': self.settingsUI.spinBox.value()
        }
        
        settings.writeConfig(appliedSettings)
        self.applyConfig()
        self.closeWindow(self.settingsWindow)
    
    def insertPicture(self):
        '''Inserts an Image into the editor
        
        - We get the file source
        - We find the textCursor()
        - We insert the image
        
        kthxbai
        '''
        imgPath = QFileDialog.getOpenFileName(Form)[0]
        
        cursor = self.editor.textCursor()
        cursor.insertImage(imgPath)
    
    def table(self):
        '''Generates and inserts a Table'''
        
        self.windowTable = QtWidgets.QDialog()
        
        self.TableUI = UI_Dialog_Table()
        self.TableUI.setupUi(self.windowTable)
        
        self.TableUI.buttonBox.accepted.connect(lambda: table.insertTable(self))
        self.TableUI.buttonBox.rejected.connect(lambda: self.closeWindow(self.windowTable))
        
        translation.applyLanguage(self.TableUI, self.language, 'table')
        
        self.windowTable.show()
    
    def script(self):
        self.windowScript = QtWidgets.QDialog()
        
        self.UIScript = Ui_Form_Script()
        self.UIScript.setupUi(self.windowScript)
        
        self.UIScript.runButtonScript.clicked.connect(
            lambda: script_handler.getAndSetOutput(self.UIScript, self.UIScript.scriptEditor.toPlainText())
        )
        self.UIScript.clearButtonScript.clicked.connect(
            lambda: script_handler.clearTextEdits(self.UIScript)
        )
        
        self.windowScript.show()
    
    def changeFont(self):
        '''Opens QFontDialog and applies the 
        selected Font to the editor'''
        font = QFontDialog.getFont()
        self.editor.setCurrentFont(font[0])
    
    def setFontWeight(self):
        self.editor.setFontWeight(self.fontWeightSpin.value())
        print(self.fontWeightSpin.value())
    
    def setSupOrSub(self, o):
        
        # this code is ridiculous
        cursor = self.editor.textCursor()
        Text = cursor.selectedText()
        
        if o == "sub" or o == "sup":
            Text = f"<{o}>{Text}</{o}>"
        
        else:
            Text = f"<p style='vertical-align: middle; font-size: {self.fontsize};'>{Text}</p>"
        self.editor.insertHtml(Text)
    
    def grammarInit(self):
        txt = self.editor.toPlainText()
        
        self.grammarWorker = GrammarCheck(txt, self.language, self.editor)
        self.grammarWorker.markErrors.connect(grammar.markError)
        self.grammarWorker.start()
    
    def updateStatsEditor(self):
        chars = len(self.editor.toPlainText())
        t = self.editor.toPlainText().replace(" ", "")
        charsWithoutSpace = len(t)
        words = len(self.editor.toPlainText().split())
        
        readingSpeedLoud = round((words / 183) * 60, 1)
        readingSpeedSilent = round((words / 238) * 60, 1)
        
        statsText = (
            f"Characters: {chars}\tCharacters without Spaces: {charsWithoutSpace}\tWords: {words}\tReading Time (aloud): {readingSpeedLoud}s\tReading Time (silent): {readingSpeedSilent}s"
        )
        self.statsLabel.setText(statsText)
    
    def saveAsHTML(self):
        notes = self.getNotes()
        htmlPath = QFileDialog.getSaveFileName(Form) # htmlPath[0]
        path = c.returnPathIfNoteExists(notes, self.namelabel.toPlainText())
        
        d = crypto.decrypt(path)
        
        with open(f"{htmlPath[0]}.html", "w", encoding="UTF-8") as h:
            h.write(d)


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    Form = QtWidgets.QMainWindow()
    
    ui = Application(Form)
    Form.show()
    app.exec()


""" 
Weitere Ideen:
- ~~Echtzeit Grammatikkorektur (Deutsch)~~
- Hotkeys
- ~~Stats while Typing~~
- ~~Script Editor~~
- ~~Save as HTML~~
- ~~Toolbar~~
- ~~Encryption~~
- ~~Search browser für die Notes~~
"""