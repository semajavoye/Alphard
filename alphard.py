import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QLabel, QComboBox, QPushButton, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
import json
from language import get_translation, get_languages, get_settinglanguage
import check_github_version as alphard_version

# alphard_version.main()

class SettingsWindow(QMainWindow):
    def __init__(self, parent, available_languages):
        super(SettingsWindow, self).__init__(parent)
        self.parent = parent
        self.available_languages = available_languages
        self.translation = get_translation()

        self.setWindowTitle(self.translation["file_menu"]["settings"])
        self.setGeometry(100, 100, 680, 560)

        self.create_menu()

    def create_menu(self):
        settings_label = QLabel(self.translation["file_menu"]["settings"])
        self.setCentralWidget(settings_label)

        # Create a ComboBox to store the selected language
        selected_language = QComboBox(self)
        selected_language.addItems(self.available_languages)
        selected_language.setCurrentText(get_settinglanguage())

        # Button to apply language changes
        apply_button = QPushButton("Apply", self)
        apply_button.clicked.connect(lambda: self.apply_language(selected_language.currentText()))

        # Create a layout for the central widget
        layout = QVBoxLayout()
        layout.addWidget(selected_language, alignment=Qt.AlignCenter)
        layout.addWidget(apply_button, alignment=Qt.AlignCenter)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def apply_language(self, selected_language):
        # Save the selected language to settings.json
        with open("settings.json", "r") as f:
            settings = json.load(f)
            settings["languageSetting"] = selected_language.lower()

        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=2)

        # Restart the whole application
        self.parent.close()
        app = Alphard()
        app.show()


class Alphard(QMainWindow):
    def __init__(self):
        super(Alphard, self).__init__()
        self.initialize()

    def initialize(self):
        self.available_languages = get_languages()

        # Load translation for the initial language setting
        self.translation = get_translation()

        self.setWindowTitle(f"{self.translation['alphard']} {self.get_version()}")
        self.setWindowState(Qt.WindowMaximized)  # Maximize window on startup

        self.create_menu()
        self.create_table()

    def create_menu(self):
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu(self.translation["file_menu"]["file"])

        # File menu subcategories
        new_action = QAction(self.translation["file_menu"]["new"], self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction(self.translation["file_menu"]["open"], self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction(self.translation["file_menu"]["save"], self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        settings_action = QAction(self.translation["file_menu"]["settings"], self)
        settings_action.triggered.connect(self.settings)
        file_menu.addAction(settings_action)

        exit_action = QAction(self.translation["file_menu"]["exit"], self)
        exit_action.triggered.connect(self.exit_app)
        file_menu.addAction(exit_action)

        # Edit menu
        edit_menu = menu_bar.addMenu(self.translation["edit_menu"]["edit"])

        # Edit menu subcategories
        cut_action = QAction(self.translation["edit_menu"]["cut"], self)
        cut_action.triggered.connect(self.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction(self.translation["edit_menu"]["copy"], self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction(self.translation["edit_menu"]["paste"], self)
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

        # Help menu
        help_menu = menu_bar.addMenu(self.translation["help_menu"]["help"])

        about_action = QAction(self.translation["help_menu"]["about"], self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def create_table(self):
        # Create a QTableWidget
        self.table = QTableWidget(self)
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels([self.translation["tree"]["ipadr"],
                                             self.translation["tree"]["tag"],
                                             self.translation["tree"]["userpc"],
                                             self.translation["tree"]["version"],
                                             self.translation["tree"]["status"],
                                             self.translation["tree"]["userstatus"],
                                             self.translation["tree"]["country"],
                                             self.translation["tree"]["os"],
                                             self.translation["tree"]["uptime"]])

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.table)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Add some sample data
        self.add_sample_data()

    def add_sample_data(self):
        # Add sample data to the QTableWidget
        for i in range(5):
            self.table.insertRow(i)
            self.table.setItem(i, 0, QTableWidgetItem(f"192.168.0.{i + 1}"))
            self.table.setItem(i, 1, QTableWidgetItem(f"Tag {i + 1}"))
            self.table.setItem(i, 2, QTableWidgetItem(f"UserPC {i + 1}"))
            self.table.setItem(i, 3, QTableWidgetItem(f"Version {i + 1}"))
            self.table.setItem(i, 4, QTableWidgetItem(f"Status {i + 1}"))
            self.table.setItem(i, 5, QTableWidgetItem(f"User Status {i + 1}"))
            self.table.setItem(i, 6, QTableWidgetItem(f"Country {i + 1}"))
            self.table.setItem(i, 7, QTableWidgetItem(f"OS {i + 1}"))
            self.table.setItem(i, 8, QTableWidgetItem(f"Uptime {i + 1}"))

    def new_file(self):
        QMessageBox.information(self, self.translation["file_menu"]["new"], self.translation["dialogs"]["new_file"])

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, self.translation["dialogs"]["open_filelabel"],
                                                   "", "Text files (*.txt);;All files (*)")
        if file_path:
            QMessageBox.information(self, self.translation["file_menu"]["open"], f"Opening file: {file_path}")

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, self.translation["dialogs"]["save_filelabel"],
                                                   "", "Text files (*.txt);;All files (*)")
        if file_path:
            QMessageBox.information(self, self.translation["file_menu"]["save"], f"Saving file to: {file_path}")

    def settings(self):
        settings_window = SettingsWindow(self, self.available_languages)
        settings_window.show()

    def exit_app(self):
        result = QMessageBox.question(self, self.translation["file_menu"]["exit"],
                                      self.translation["dialogs"]["exit_app"],
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            self.close()

    # Additional methods for Edit menu
    def cut(self):
        QMessageBox.information(self, self.translation["edit_menu"]["edit"], self.translation["edit_menu"]["cut"])

    def copy(self):
        QMessageBox.information(self, self.translation["edit_menu"]["edit"], self.translation["edit_menu"]["copy"])

    def paste(self):
        QMessageBox.information(self, self.translation["edit_menu"]["edit"], self.translation["edit_menu"]["paste"])

    def show_about(self):
        about_text = self.translation["dialogs"]["about"]
        QMessageBox.information(self, self.translation["dialogs"]["aboutlabel"], about_text)

    def get_version(self):
        with open("settings.json", "r") as f:
            settings = json.load(f)
            version = settings["version"]
        return version


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Set the application style to a darker mode
    app.setStyle("Fusion")
    palette = app.palette()
    palette.setColor(palette.Window, Qt.darkGray)
    palette.setColor(palette.WindowText, Qt.white)
    app.setPalette(palette)

    main_window = Alphard()
    main_window.show()
    sys.exit(app.exec_())
