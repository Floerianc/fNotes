from PyQt5.QtWidgets import(
    QPushButton,
    QLabel,
    QMenu,
    QAction,
    QComboBox,
    QSpinBox
)

language = {
    # i want to die
    'english': {
        'main': {
            'deleteCurrentNote': 'delete current Note',
            'createListGreek': 'δ',
            'createListRoman': 'IV.',
            'math': 'Σ',
            'boldButton': 'F',
            'Left': 'L',
            'Middle': 'M',
            'Right': 'R',
            'italicButton': 'K',
            'createListDec': '1.',
            'underlineButton': 'U',
            'fontSizeSpin': 'px',
            'createListDot': '•',
            'imageButton': 'Image',
            'tableButton': 'Table',
            'fontButton': 'Font',
            'fontWeightLabel': 'Font weight',
            'supButton': 'Sup',
            'subButton': 'Sub',
            'removeSupSub': 'Remove Sup/Sub',
            'searchBarRegular': 'Search...',
            'searchBarTmp': 'Search...',
            'menuFile': 'Note',
            'menuHelp': 'Help',
            'menuOther': 'Other',
            'menuExport': 'Export',
            'menuTools': 'Tools',
            'menuText_Formatting': 'Text Formatting...',
            'menuLists': 'Lists',
            'menuColors': 'Colors',
            'actionNew': 'new',
            'actionOpen': 'Open',
            'actionSave': 'Save',
            'actionSave_as': 'Save as...',
            'actionExit': 'Delete',
            'actionExit_2': 'Exit',
            'actionAbout': 'About',
            'actionSettings': 'Settings',
            'actionBold': 'Bold',
            'actionUnderline': 'Underline',
            'actionItalic': 'Italic',
            'actionLeft': 'Left',
            'actionCenter': 'Center',
            'actionRight': 'Right',
            'actionBulletpoint': 'Bulletpoint',
            'actionDecimal': 'Decimal',
            'actionAlphabet': 'Alphabet',
            'actionRoman_Numbers': 'Roman Numbers',
            'actionMath_2': 'Math',
            'actionText_Color': 'Text Color',
            'actionText_Background_Color': 'Text-Background Color',
            'actionSup': 'Sup',
            'actionSub': 'Sub',
            'actionRemove_Sup_Sub': 'Remove Sup/Sub',
            'actionChange_Font': 'Change Font',
            'actionCheck_Grammar_EXPERIMENTIAL': 'Check Grammar (EXPERIMENTIAL)',
            'actionExport_as_HTML': 'Export as HTML',
            'actionExport_as_PDF': 'Export as PDF',
        },
        'table': {
            'headerLabelTable': 'Table Designer',
            'rowsLabel': 'Rows',
            'columnsLabel': 'Columns',
            'borderStyleLabel': 'Border Style',
        },
        'settings': {
            'intervalLabel': 'Interval for auto-save feature (In seconds) (Leave at 0 to disable)',
            'decLabel': 'Decimal-points when using the basic calculator',
            'langLabel': 'Set Language of the Help-Section (Help >> About)',
            'wrapLabel': 'Enable Word-wrap in Editor',
            'spinBox': 'px',
            'settingFontSizeLabel': 'Standard Font size'
        },
        'script': {
            'runButtonScript': 'Run',
            'clearButtonScript': 'Clear',
            'scriptHandlerUnder': 'This might be slightly unstable ^^',
        }
    },
    
    'german': {
        'main': {
            'deleteCurrentNote': 'Notiz löschen',
            'createListGreek': 'δ',
            'createListRoman': 'IV.',
            'math': 'Σ',
            'boldButton': 'F',
            'Left': 'L',
            'Middle': 'M',
            'Right': 'R',
            'italicButton': 'K',
            'createListDec': '1.',
            'underlineButton': 'U',
            'fontSizeSpin': 'px',
            'createListDot': '•',
            'imageButton': 'Bild',
            'tableButton': 'Tabelle',
            'fontButton': 'Schrift',
            'fontWeightLabel': 'Schriftgewicht',
            'supButton': 'Sup',
            'subButton': 'Sub',
            'removeSupSub': 'Sup/Sub entfernen',
            'searchBarRegular': 'Suchen...',
            'searchBarTmp': 'Suchen...',
            'menuFile': 'Notiz',
            'menuHelp': 'Hilfe',
            'menuOther': 'Weiteres',
            'menuExport': 'Exportieren',
            'menuTools': 'Werkzeuge',
            'menuText_Formatting': 'Text Formattierung...',
            'menuLists': 'Listen',
            'menuColors': 'Farben',
            'actionNew': 'Neu',
            'actionOpen': 'Öffnen',
            'actionSave': 'Speichern',
            'actionSave_as': 'Speichern as...',
            'actionExit': 'Löschen',
            'actionExit_2': 'Verlassen',
            'actionAbout': 'Über',
            'actionSettings': 'Einstellungen',
            'actionBold': 'Fett',
            'actionUnderline': 'Unterstrichen',
            'actionItalic': 'Kursiv',
            'actionLeft': 'Links',
            'actionCenter': 'Mitte',
            'actionRight': 'Rechts',
            'actionBulletpoint': 'Stichpunkt',
            'actionDecimal': 'Dezimal',
            'actionAlphabet': 'Alphabet',
            'actionRoman_Numbers': 'Römische Zahlen',
            'actionMath_2': 'Mathematik',
            'actionText_Color': 'Text Farbe',
            'actionText_Background_Color': 'Hintergrundfarbe vom Text',
            'actionSup': 'Sup',
            'actionSub': 'Sub',
            'actionRemove_Sup_Sub': 'Sup/Sub entfernen',
            'actionChange_Font': 'Schriftart ändern',
            'actionCheck_Grammar_EXPERIMENTIAL': 'Grammatik überprüfen (EXPERIMENTIELL)',
            'actionExport_as_HTML': 'Als HTML exportieren',
            'actionExport_as_PDF': 'Als PDF exportieren',
        },
        'table': {
            'headerLabelTable': 'Tabellen Entwickler',
            'rowsLabel': 'Reihen',
            'columnsLabel': 'Zellen',
            'borderStyleLabel': 'Umrandung',
        },
        'settings': {
            'intervalLabel': 'Interval für das automatische Speichern (in Sekunden) (Belasse es bei 0, um die Funktion auszuschalten)',
            'decLabel': 'Nachkommastellen, wenn man den Rechner benutzt',
            'langLabel': 'Sprache in der "Über" Sektion ändern',
            'wrapLabel': 'Automatischen Zeilenbruch',
            'spinBox': 'px',
            'settingFontSizeLabel': 'Standard Schriftgröße'
        },
        'script': {
            'runButtonScript': 'Start',
            'clearButtonScript': 'Löschen',
            'scriptHandlerUnder': 'Das ist vielleicht instabil ^^',
        }
    }
}

def getCurrentLanguage(languageIndex: int):
    languages = [
        'english',
        'german'
    ]
    
    currentLanguage = language[languages[languageIndex]]
    return currentLanguage

def translateUI(ui, lang: dict, section: str):
    
    for widgetName, translation in lang[section].items():
        widget = getattr(ui, widgetName, None)
        
        if widget:
            if isinstance(widget, (QPushButton, QLabel, QAction)):
                widget.setText(translation)
            
            elif isinstance(widget, (QMenu)):
                widget.setTitle(translation)
            
            elif isinstance(widget, QComboBox):
                for index, text in enumerate(translation):
                    widget.setItemText(index, text)
            
            elif isinstance(widget, QSpinBox):
                widget.setSuffix(translation)
        

def applyLanguage(ui, languageIndex: int, section: str):
    lang = getCurrentLanguage(languageIndex)
    translateUI(ui, lang, section)