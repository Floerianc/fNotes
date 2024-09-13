language = {
    'english': {
        'deleteCurrentNote': 'delete current Note',
        'createListGreek': 'δ',
        'createListRoman': 'IV.',
        'math': 'Σ',
        'pushButton': 'F',
        'Left': 'L',
        'Middle': 'M',
        'Right': 'R',
        'pushButton_2': 'K',
        'createListDec': '1.',
        'pushButton_3': 'U',
        'spinBox': 'px',
        'createListDot': '•',
        'imageButton': 'Image',
        'tableButton': 'Table',
        'tabWidget1': 'Basic',
        'tabWidget2': 'Advanced',
        'fontButton': 'Font',
        'label': 'Font weight',
        'menuFile': 'Note',
        'menuHelp': 'Help',
        'menuOther': 'Other',
        'actionNew': 'new',
        'actionOpen': 'Open',
        'actionSave': 'Save',
        'actionSave_as': 'Save as...',
        'actionExit': 'Delete',
        'actionExit_2': 'Exit',
        'actionAbout': 'About',
        'actionSettings': 'Settings',
    },
    
    'german': {
        'deleteCurrentNote': 'Notiz löschen',
        'createListGreek': 'δ',
        'createListRoman': 'IV.',
        'math': 'Σ',
        'pushButton': 'F',
        'Left': 'L',
        'Middle': 'M',
        'Right': 'R',
        'pushButton_2': 'K',
        'createListDec': '1.',
        'pushButton_3': 'U',
        'spinBox': 'px',
        'createListDot': '•',
        'imageButton': 'Bild',
        'tableButton': 'Tabelle',
        'tabWidget1': 'Einfach',
        'tabWidget2': 'Erweitert',
        'fontButton': 'Schrift',
        'label': 'Gewicht der Schriftart',
        'menuFile': 'Notiz',
        'menuHelp': 'Hilfe',
        'menuOther': 'Weitere',
        'actionNew': 'Neu',
        'actionOpen': 'Öffnen',
        'actionSave': 'Speichern',
        'actionSave_as': 'Speichern als...',
        'actionExit': 'Löschen',
        'actionExit_2': 'Verlassen',
        'actionAbout': 'Über',
        'actionSettings': 'Einstellungen'
    }
}

def translate(self):
    languages = [
        'english',
        'german'
    ]
    
    currentLanguage = language[languages[self.language]]
    
    self.deleteCurrentNote.setText(currentLanguage['deleteCurrentNote'])
    self.createListGreek.setText(currentLanguage['createListGreek'])
    self.createListRoman.setText(currentLanguage['createListRoman'])
    self.math.setText(currentLanguage['math'])
    self.pushButton.setText(currentLanguage['pushButton'])
    self.Left.setText(currentLanguage['Left'])
    self.Right.setText(currentLanguage['Right'])
    self.pushButton_2.setText(currentLanguage['pushButton_2'])
    self.createListDec.setText(currentLanguage['createListDec'])
    self.Middle.setText(currentLanguage['Middle'])
    self.pushButton_3.setText(currentLanguage['pushButton_3'])
    self.spinBox.setSuffix(currentLanguage['spinBox'])
    self.createListDot.setText(currentLanguage['createListDot'])
    self.imageButton.setText(currentLanguage['imageButton'])
    self.tableButton.setText(currentLanguage['tableButton'])
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), currentLanguage['tabWidget1'])
    self.fontButton.setText(currentLanguage['fontButton'])
    self.label.setText(currentLanguage['label'])
    self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), currentLanguage['tabWidget2'])
    self.menuFile.setTitle(currentLanguage['menuFile'])
    self.menuHelp.setTitle(currentLanguage['menuHelp'])
    self.menuOther.setTitle(currentLanguage['menuOther'])
    self.actionNew.setText(currentLanguage['actionNew'])
    self.actionOpen.setText(currentLanguage['actionOpen'])
    self.actionSave.setText(currentLanguage['actionSave'])
    self.actionSave_as.setText(currentLanguage['actionSave_as'])
    self.actionExit.setText(currentLanguage['actionExit'])
    self.actionAbout.setText(currentLanguage['actionAbout'])
    self.actionExit_2.setText(currentLanguage['actionExit_2'])
    self.actionSettings.setText(currentLanguage['actionSettings'])