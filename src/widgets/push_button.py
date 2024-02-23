
from PyQt5.QtWidgets import QPushButton

class Push_Button(QPushButton):
    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.init_button()

    def init_button(self):
        self.setFixedSize(100, 50)
        self.move(100, 100)
        self.show()
    
    def set_text(self, text):
        self.setText(text)