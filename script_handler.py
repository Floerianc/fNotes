import sys
from io import StringIO
from code import InteractiveInterpreter

def executeScript(code: str):
    output = StringIO()
    sys.stdout = output
    sys.stderr = output
    
    try:
        InteractiveInterpreter().runcode(code)
    except Exception as e:
        output.write(e)
    finally:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__
    
    return output.getvalue()

def clearTextEdits(ui):
    ui.scriptEditor.clear()
    ui.scriptOutput.clear()

def getAndSetOutput(ui, code: str):
    output = executeScript(code)
    ui.scriptOutput.setText(output)