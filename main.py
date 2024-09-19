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
from worker import *
from calc import calculate
import conditions as c
import settings
import table
import translation

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
        self.wrap = QtWidgets.QTextEdit.LineWrapMode.WidgetWidth
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
        self.listWidget.clicked.connect(lambda: self.openNoteFromListWidget(self.listWidget))
        self.tmpListWidget.clicked.connect(lambda: self.openNoteFromListWidget(self.tmpListWidget))
        self.deleteCurrentNote.clicked.connect(self.setHyperLink)
        self.colorPickerButton.clicked.connect(self.setColor)
        self.markerPickerButton.clicked.connect(self.setMarker)
        self.math.clicked.connect(self.calc)
        self.pdfButton.clicked.connect(self.saveAsPDF)
        self.fontButton.clicked.connect(self.changeFont)
        self.fontWeightSpin.valueChanged.connect(self.setFontWeight)
        
        self.actionSave.triggered.connect(self.saveNote)
        self.actionExit.triggered.connect(self.deleteNote)
        self.actionNew.triggered.connect(self.newNote)
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionOpen.triggered.connect(self.openNoteFromMenu)
        self.actionSettings.triggered.connect(self.showSettings)
        
        self.createListDot.clicked.connect(lambda: self.createList('LD'))
        self.createListDec.clicked.connect(lambda: self.createList('LDec'))
        self.createListGreek.clicked.connect(lambda: self.createList('LUA'))
        self.createListRoman.clicked.connect(lambda: self.createList('LUR'))
        
        self.boldButton.clicked.connect(self.setBold)
        self.italicButton.clicked.connect(self.setItalic)
        self.underlineButton.clicked.connect(self.setUnderlined)
        self.fontSizeSpin.valueChanged.connect(self.setFontSizeSpin)
        self.imageButton.clicked.connect(self.insertPicture)
        self.tableButton.clicked.connect(self.table)
        
        self.Left.clicked.connect(lambda: self.setAlignment('L'))
        self.Middle.clicked.connect(lambda: self.setAlignment('M'))
        self.Right.clicked.connect(lambda: self.setAlignment('R'))
    
    def connectWorker(self):
        '''Connects the WorkerThread to a function and starts it'''
        self.Worker = WorkerThread(self.autoSave)
        self.Worker.updateNote.connect(self.saveTmp)
        self.Worker.start()
    
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
        self.fontSizeSpin.setValue(int(self.fontsize)) # WHY DOES IT FORCE ME TO USE INT
        
        self.lang = translation.getCurrentLanguage(self.language)
        translation.translateMainUi(self, self.lang)
    
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
        
        with open(path, "r", encoding="UTF-8") as f:
            content = f.read()
        
        self.editor.setText(content)
        self.namelabel.setText(itemText)
    
    def openNoteFromMenu(self):
        notePath = QFileDialog.getOpenFileName(Form)
        noteName = notePath[0].split("/")[-1]
        
        with open(notePath[0], "r") as note:
            content = note.read()
            self.editor.setText(content)
            self.namelabel.setText(noteName)
    
    
    def saveNote(self):
        '''Saves note to the ./user_content/note folder
        
        It replaces the spaces in self.namelabels text with underscores.
        In that way we won't have any problems with redirecting to that path
        later on. 
        '''
        noteName = f"{self.namelabel.toPlainText().replace(' ', '_')}"
        
        with open(f"./user_content/note/{noteName}", "w", encoding="UTF-8") as note:
            note.write(self.editor.toHtml())
        self.listNotes()
    
    def saveTmp(self):
        '''Does the same as saveNote() but with a few more conditions (c.tmpFileCondition())
        '''
        if not c.tmpFileCondition(self.namelabel.toPlainText()):
            return
        else:
            noteName = c.tmpFileCondition(self.namelabel.toPlainText())
        
        try:
            with open(f"./user_content/tmp/{noteName}", "w", encoding="UTF-8") as tmp:
                tmp.write(self.editor.toHtml())
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
        
        translation.translateSettings(self.settingsUI, self.lang)
        
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
            'fontsize': self.settingsUI.doubleSpinBox.value()
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
        
        translation.translateTable(self.TableUI, self.lang)
        
        self.windowTable.show()
    
    def changeFont(self):
        '''Opens QFontDialog and applies the 
        selected Font to the editor'''
        font = QFontDialog.getFont()
        self.editor.setCurrentFont(font[0])
    
    def setFontWeight(self):
        self.editor.setFontWeight(self.fontWeightSpin.value())
        print(self.fontWeightSpin.value())
    
    def setHyperLink(self):
        cursor = self.editor.textCursor()
        selectedText = cursor.selectedText()
        
        hyperlink = f'<a href="{selectedText}">HyperLink</a>'
        self.editor.insertHtml(hyperlink)


if __name__ == "__main__":
    app = QtWidgets.QApplication(argv)
    Form = QtWidgets.QMainWindow()
    
    ui = Application(Form)
    Form.show()
    app.exec()