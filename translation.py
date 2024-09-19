language = {
    # i want to die
    'english': {
        'main': {
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
        'table': {
            'headerLabelTable': 'Table Designer',
            'rowsLabel': 'Rows',
            'columnsLabel': 'Columns',
            'borderStyle_0': 'Solid',
            'borderStyle_1': 'Dashed',
            'borderStyle_2': 'DotDash',
            'borderStyle_3': 'DotDotDash',
            'borderStyle_4': 'Dotted',
            'borderStyle_5': 'Double',
            'borderStyle_6': 'Groove',
            'borderStyle_7': 'Inset',
            'borderStyle_8': 'None',
            'borderStyle_9': 'Outset',
            'borderStyle_10': 'Ridge',
            'borderStyleLabel': 'Border Style',
        },
        'settings': {
            'intervalLabel': 'Interval for auto-save feature (In seconds) (Leave at 0 to disable)',
            'decLabel': 'Decimal-points when using the basic calculator',
            'langComboBox_0': 'English',
            'langComboBox_1': 'Deutsch',
            'langLabel': 'Set Language of the Help-Section (Help >> About)',
            'wrapLabel': 'Enable Word-wrap in Editor',
            'doubleSpinBox': 'px',
            'settingFontSizeLabel': 'Standard Font size'
        }
    },
    
    'german': {
        'main': {
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
            'label': 'Gewicht der Schrift',
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
        },
        'table': {
            'headerLabelTable': 'Tabellen Entwickler',
            'rowsLabel': 'Reihen',
            'columnsLabel': 'Zellen',
            'borderStyle_0': 'Solid',
            'borderStyle_1': 'Dashed',
            'borderStyle_2': 'DotDash',
            'borderStyle_3': 'DotDotDash',
            'borderStyle_4': 'Dotted',
            'borderStyle_5': 'Double',
            'borderStyle_6': 'Groove',
            'borderStyle_7': 'Inset',
            'borderStyle_8': 'None',
            'borderStyle_9': 'Outset',
            'borderStyle_10': 'Ridge',
            'borderStyleLabel': 'Umrandung',
        },
        'settings': {
            'intervalLabel': 'Interval für das automatische Speichern (in Sekunden) (Belasse es bei 0, um die Funktion auszuschalten)',
            'decLabel': 'Nachkommastellen, wenn man den Rechner benutzt',
            'langComboBox_0': 'English',
            'langComboBox_1': 'Deutsch',
            'langLabel': 'Sprache in der "Über" Sektion ändern',
            'wrapLabel': 'Automatischen Zeilenbruch',
            'doubleSpinBox': 'px',
            'settingFontSizeLabel': 'Standard Schriftgröße'
        }
    }
}

def translateMainUi(ui, currentLanguage):
    languageSection = currentLanguage['main']
    
    ui.deleteCurrentNote.setText(languageSection['deleteCurrentNote'])
    ui.createListGreek.setText(languageSection['createListGreek'])
    ui.createListRoman.setText(languageSection['createListRoman'])
    ui.math.setText(languageSection['math'])
    ui.boldButton.setText(languageSection['pushButton'])
    ui.Left.setText(languageSection['Left'])
    ui.Right.setText(languageSection['Right'])
    ui.italicButton.setText(languageSection['pushButton_2'])
    ui.Middle.setText(languageSection['Middle'])
    ui.underlineButton.setText(languageSection['pushButton_3'])
    ui.fontSizeSpin.setSuffix(languageSection['spinBox'])
    ui.createListDec.setText(languageSection['createListDec'])
    ui.createListDot.setText(languageSection['createListDot'])
    ui.imageButton.setText(languageSection['imageButton'])
    ui.tableButton.setText(languageSection['tableButton'])
    ui.toolBox.setTabText(ui.toolBox.indexOf(ui.tab), languageSection['tabWidget1'])
    ui.fontButton.setText(languageSection['fontButton'])
    ui.fontWeightLabel.setText(languageSection['label'])
    ui.toolBox.setTabText(ui.toolBox.indexOf(ui.tab_2), languageSection['tabWidget2'])
    ui.menuFile.setTitle(languageSection['menuFile'])
    ui.menuHelp.setTitle(languageSection['menuHelp'])
    ui.menuOther.setTitle(languageSection['menuOther'])
    ui.actionNew.setText(languageSection['actionNew'])
    ui.actionOpen.setText(languageSection['actionOpen'])
    ui.actionSave.setText(languageSection['actionSave'])
    ui.actionSave_as.setText(languageSection['actionSave_as'])
    ui.actionExit.setText(languageSection['actionExit'])
    ui.actionAbout.setText(languageSection['actionAbout'])
    ui.actionExit_2.setText(languageSection['actionExit_2'])
    ui.actionSettings.setText(languageSection['actionSettings'])

def translateTable(ui, currentLanguage):
    languageSection = currentLanguage['table']
    
    ui.headerLabelTable.setText(languageSection['headerLabelTable'])
    ui.rowsLabel.setText(languageSection['rowsLabel'])
    ui.columnsLabel.setText(languageSection['columnsLabel'])
    ui.borderStyle.setItemText(0, languageSection['borderStyle_0'])
    ui.borderStyle.setItemText(1, languageSection['borderStyle_1'])
    ui.borderStyle.setItemText(2, languageSection['borderStyle_2'])
    ui.borderStyle.setItemText(3, languageSection['borderStyle_3'])
    ui.borderStyle.setItemText(4, languageSection['borderStyle_4'])
    ui.borderStyle.setItemText(5, languageSection['borderStyle_5'])
    ui.borderStyle.setItemText(6, languageSection['borderStyle_6'])
    ui.borderStyle.setItemText(7, languageSection['borderStyle_7'])
    ui.borderStyle.setItemText(8, languageSection['borderStyle_8'])
    ui.borderStyle.setItemText(9, languageSection['borderStyle_9'])
    ui.borderStyle.setItemText(10, languageSection['borderStyle_10'])
    ui.borderStyleLabel.setText(languageSection['borderStyleLabel'])

def translateSettings(ui, currentLanguage):
    languageSection = currentLanguage['settings']
    
    ui.intervalLabel.setText(languageSection['intervalLabel'])
    ui.decLabel.setText(languageSection['decLabel'])
    ui.langComboBox.setItemText(0, languageSection['langComboBox_0'])
    ui.langComboBox.setItemText(1, languageSection['langComboBox_1'])
    ui.langLabel.setText(languageSection['langLabel'])
    ui.wrapLabel.setText(languageSection['wrapLabel'])
    ui.doubleSpinBox.setSuffix(languageSection['doubleSpinBox'])
    ui.settingFontSizeLabel.setText(languageSection['settingFontSizeLabel'])

def getCurrentLanguage(languageIndex: int):
    languages = [
        'english',
        'german'
    ]
    
    currentLanguage = language[languages[languageIndex]]
    return currentLanguage