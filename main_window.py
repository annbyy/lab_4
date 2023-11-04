import sys
from PySide6 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        self.button_open_folder = QtWidgets.QPushButton('Open Folder Dialog')
        self.button_open_folder.clicked.connect(self.open_folder_dialog)

        self.button_create_annotation = QtWidgets.QPushButton('Create Annotation File')
        self.button_create_annotation.clicked.connect(self.create_annotation_file)

        self.label = QtWidgets.QLabel()
        layout.addWidget(self.button_open_folder)
        layout.addWidget(self.button_create_annotation)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def open_folder_dialog(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath:
            self.label.setText(f'Selected Folder: {folderpath}')
            self.selected_folder = folderpath

    def create_annotation_file(self):
        if hasattr(self, 'selected_folder'):
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Annotation File', self.selected_folder)
            if file_path:
                self.label.setText(f'Annotation File Created: {file_path}')
        else:
            self.label.setText('Please select a folder first.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())