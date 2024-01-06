from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QTabWidget, QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtWidgets import QApplication, QTextEdit, QToolBar, QWidget
from PySide6.QtGui import QAction, QIcon
import pyperclip
import sys
import os


base_dir = os.path.dirname(__file__)

class TextEditor(QTextEdit):
    def __init__(self):
        super().__init__()
        
        # self.resize(1200, 720)
        
class ToolBar(QToolBar):
    def __init__(self, methods):
        super().__init__()
        
        self.setIconSize(QSize(32, 32))
        
        button_exit = QAction(QIcon(os.path.join(base_dir, "images/quitIcon.png")), "", self)
        button_exit.triggered.connect(methods[0])
        
        button_copy = QAction(QIcon(os.path.join(base_dir, "images/copyIcon.png")), "", self)
        button_copy.triggered.connect(methods[1])
        
        button_cut = QAction(QIcon(os.path.join(base_dir, "images/cutIcon.png")), "", self)
        button_cut.triggered.connect(methods[2])
        
        button_paste = QAction(QIcon(os.path.join(base_dir, "images/pasteIcon.png")), "", self)
        button_paste.triggered.connect(methods[3])
        
        button_undo = QAction(QIcon(os.path.join(base_dir, "images/undoIcon.png")), "", self)
        button_undo.triggered.connect(methods[4])
        
        button_redo = QAction(QIcon(os.path.join(base_dir, "images/redoIcon.png")), "", self)
        button_redo.triggered.connect(methods[5])
        
        self.addActions([button_exit, button_copy, button_cut, button_paste, button_undo, button_redo])
        
    def talk(self):
        print("You would like to close the application.")
        
        


class MainWindow(QMainWindow):
    
    editor = None
    editor_selected_text = ""
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Text Editor")
        self.setMinimumSize(QSize(1200, 720))
        
        toolBar = ToolBar(methods=[self.close, self.copy, self.cut, self.paste, self.undo, self.redo])
        self.addToolBar(toolBar)
        
        self.editor = TextEditor()
        self.setCentralWidget(self.editor)
        
    
        
    def close(self):
        print("close has been initiated")
        QApplication.instance().quit()
        
    def copy(self):
        text = self.editor.textCursor().selectedText()
        
        self.editor.copy()
        
    def cut(self):
        self.copy()
        
        self.editor.textCursor().removeSelectedText()
                
    def paste(self):
        
        self.editor.paste()
        
    def undo(self):
        self.editor.undo()
        
    def redo(self):
        self.editor.redo()
        
        
        
app = QApplication(sys.argv)
  
window = MainWindow()

window.show()

app.exec()
