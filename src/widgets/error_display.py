
from PyQt5.QtWidgets import QLabel

class Error_Display(QLabel):
    def __init__(self, parent, default_text):
        super().__init__(parent)
        self.default_text = default_text
        self.init_error_display()
    
    def init_error_display(self):
        self.setText(self.default_text)
        self.setFixedSize(400, 200)
        self.move(100, 100)
        self.show()