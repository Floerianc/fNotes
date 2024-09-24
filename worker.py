import time
from grammar import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QTextEdit

class WorkerThread(QThread):
    updateNote = pyqtSignal()
    
    def __init__(self, wait):
        self.waitTime = wait
        super().__init__()
    
    def run(self):
        while True:
            self.updateNote.emit()
            time.sleep(self.waitTime)

class WorkerThreadStats(QThread):
    updateStats = pyqtSignal()
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        while True:
            self.updateStats.emit()
            time.sleep(1)

class GrammarCheck(QThread):
    markErrors = pyqtSignal(QTextEdit, list)
    
    def __init__(self, txt: str, lang: int, tE: QTextEdit) -> None:
        super().__init__()
        
        self.txt = txt
        self.language = lang
        self.tE = tE
    
    def run(self):
        print("Checkpoint 1")
        matches = checkErrors(self.language, self.txt)
        
        if matches:
            print("Checkpoint 4")
            self.markErrors.emit(self.tE, matches)
        
        self.quit()