
from PyQt5.QtWidgets import QTextEdit
from PyQt5 import QtCore

class Df_table_viewer(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent)
        self.init_table_viewer()
    
    def init_table_viewer(self):
        self.setFixedSize(400, 200)
        self.move(100, 100)
        self.show()
    
    def set_text(self, text):
        self.setText(text)

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])