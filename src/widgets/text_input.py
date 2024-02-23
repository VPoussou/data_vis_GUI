
from PyQt5.QtWidgets import QTextEdit

class Text_Input(QTextEdit):
    def __init__(self, parent, default_text):
        super().__init__(parent)
        self.default_text = default_text
        self.init_input()
    
    def init_input(self):
        self.setText(self.default_text)
        self.setFixedSize(400, 200)
        self.move(100, 100)
        self.show()
    
