
# Imports for the base PyQt5 submodules and required native libraries
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
import sys
# Imports for the Widgets
from widgets.error_display import Error_Display
from widgets.push_button import Push_Button
from widgets.text_input import Text_Input
from widgets.df_table_viewer import Df_table_viewer
# Imports for the Models
from models.browse_files import browse_files
from models.df_sampler import df_sampler
from models.read_csv import read_csv

class Vasco(QWidget):
    def __init__(self):
        super().__init__()
        self.df = None

        self.init_GUI()

    def init_GUI(self):
        self.layout = QGridLayout()

        self.error_display = Error_Display(self, "Nothing wrong, yet.")
        self.layout.addWidget(self.error_display, 0, 0)

        self.open_file_button = Push_Button("Open File", self)
        self.open_file_button.clicked.connect(self.open_file)
        self.layout.addWidget(self.open_file_button, 1, 0)

        self.head_button = Push_Button("Head", self)
        self.tail_button = Push_Button("Tail", self)
        self.sample_button = Push_Button("Sample", self)
        self.sample_size_input = Text_Input(self, "5")

        self.head_button.clicked.connect(lambda: self.sampler_buttons_handler("head"))
        self.tail_button.clicked.connect(lambda: self.sampler_buttons_handler("tail"))
        self.sample_button.clicked.connect(lambda: self.sampler_buttons_handler("sample"))

        self.layout.addWidget(self.head_button, 1, 1)
        self.layout.addWidget(self.tail_button, 1, 2)
        self.layout.addWidget(self.sample_button, 1, 3)
        self.layout.addWidget(self.sample_size_input, 1, 4)

        self.df_table_viewer = Df_table_viewer(self)
        self.layout.addWidget(self.df_table_viewer, 2, 0)

        self.setLayout(self.layout)

    def open_file(self):
        file_path = browse_files()
        if file_path:
            self.error_display.setText("File path: " + file_path)
            self.df = read_csv(file_path)
    
    def sampler_buttons_handler(self, sample_type):
        sample_size = int(self.sample_size_input.toPlainText())
        self.df_table_viewer.set_text(df_sampler(self.df, sample_type, sample_size))
        


def main():
    app = QApplication([])

    view = Vasco()
    view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()