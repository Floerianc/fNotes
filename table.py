from asset.ui.py.table import *

def getBorderStyle(tableStyle, key):
    styles = {
        'Solid': tableStyle.BorderStyle.BorderStyle_Solid,
        'Dashed': tableStyle.BorderStyle.BorderStyle_Dashed,
        'DotDash': tableStyle.BorderStyle.BorderStyle_DotDash,
        'DotDotDash': tableStyle.BorderStyle.BorderStyle_DotDotDash,
        'Dotted': tableStyle.BorderStyle.BorderStyle_Dotted,
        'Double': tableStyle.BorderStyle.BorderStyle_Double,
        'Groove': tableStyle.BorderStyle.BorderStyle_Groove,
        'Inset': tableStyle.BorderStyle.BorderStyle_Inset,
        'None': tableStyle.BorderStyle.BorderStyle_None,
        'Outset': tableStyle.BorderStyle.BorderStyle_Outset,
        'Ridge': tableStyle.BorderStyle.BorderStyle_Ridge,
    }
    return styles[key]

def tableWindow(self):
    self.windowTable = QtWidgets.QDialog()
    
    self.TableUI = UI_Dialog_Table()
    self.TableUI.setupUi(self.windowTable)
    
    self.TableUI.buttonBox.accepted.connect(lambda: insertTable(self))
    self.TableUI.buttonBox.rejected.connect(lambda: self.closeWindow(self.windowTable))
    
    self.windowTable.show()

def insertTable(self):
    rows = self.TableUI.Rows.value()
    columns = self.TableUI.Columns.value()
    key = self.TableUI.borderStyle.currentText()
    
    cursor = self.editor.textCursor()
    
    tableStyle = QtGui.QTextTableFormat()
    borderStyle = getBorderStyle(tableStyle, key)
    tableStyle.setCellPadding(5)
    tableStyle.setBorderStyle(borderStyle)
    
    cursor.insertTable(rows, columns, tableStyle)