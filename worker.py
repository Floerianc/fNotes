import time
from PyQt5.QtCore import QThread, pyqtSignal

class WorkerThread(QThread):
    updateNote = pyqtSignal()
    
    def __init__(self, wait):
        self.waitTime = wait
        super().__init__()
    
    def run(self):
        while True:
            self.updateNote.emit()
            time.sleep(self.waitTime)