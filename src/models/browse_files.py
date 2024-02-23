from PyQt5.QtWidgets import QFileDialog

def browse_files():
    file = QFileDialog.getOpenFileName()
    return file[0]