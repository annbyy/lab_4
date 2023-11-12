import sys
from PySide6 import QtWidgets
from PySide6.QtCore import QFile, QTextStream
from lab_3_4 import data_returner

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

        #добавляем поле ввода даты и кнопку "Get Data"
        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setDisplayFormat("dd.MM.yyyy")
        self.button_get_data = QtWidgets.QPushButton('Get Data')
        self.button_get_data.clicked.connect(self.get_data_for_date)

        layout.addWidget(self.button_open_folder)
        layout.addWidget(self.button_create_annotation)
        layout.addWidget(self.label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.button_get_data)

        self.setLayout(layout)

    def open_folder_dialog(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folderpath:
            self.label.setText(f'Selected Folder: {folderpath}')
            self.selected_folder = folderpath

    def create_annotation_file(self):
        if hasattr(self, 'selected_folder'):
            file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Annotation File', self.selected_folder)
            print(f'File Path: {file_path}')
        if file_path:
            self.label.setText(f'Annotation File Created: {file_path}')

            # Теперь создайте файл и напишите в него что-то
            file = QFile(file_path)
            if file.open(QFile.WriteOnly | QFile.Text):
                stream = QTextStream(file)
                stream << "This is your annotation content."
                file.close()
            else:
                self.label.setText(f'Failed to create annotation file at: {file_path}')
        else:
            self.label.setText('Please select a folder first')

    def get_data_for_date(self):
        selected_date = self.date_input.date().toString("dd.MM.yyyy")
        collected_data = data_returner(selected_date)
        self.label.setText(f'Data for Date {selected_date}: {collected_data}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())