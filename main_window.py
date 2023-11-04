import sys
from PySide6 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.button = QtWidgets.QPushButton('Open Folder Dialog')
        self.button.clicked.connect(self.open_folder_dialog)
        self.label = QtWidgets.QLabel()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def open_folder_dialog(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath:
            self.label.setText(f'Selected Folder: {folderpath}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())