import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel, QLineEdit, QTextEdit, QStackedWidget, QFormLayout)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

from core.profile.start_profiles import start_profiles
from core.profile.stop_profiles import stop_profiles
from core.profile.extension_manager import upload_extension
from core.utils.auth_service import AuthService

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rise bot + Rise Extension")
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1d1d1d;
            }
            QLabel {
                color: white;
            }
            QLineEdit, QTextEdit {
                background-color: #2d2d2d;
                color: white;
                border: 1px solid #3d3d3d;
                padding: 5px;
            }
            QPushButton {
                background-color: #1e6aa5;
                color: white;
                border: none;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #1a5482;
            }
        """)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.login_widget = LoginWidget(self)
        self.profile_manager_widget = ProfileManagerWidget(self)

        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.profile_manager_widget)

        self.auth_service = AuthService()
        self.running = False
        self.drivers = []
        self.auth_token = ""

        self.setFixedSize(400, 500)

    def login(self, username, password):
        success, message = self.auth_service.login(username, password)
        if success:
            print(message)
            self.stacked_widget.setCurrentWidget(self.profile_manager_widget)
        else:
            print(f"Error: {message}")

    def toggle_profiles(self):
        if self.running:
            stop_profiles(self.drivers, self.auth_token)
            self.profile_manager_widget.update_gui_stop()
        else:
            self.auth_token = self.profile_manager_widget.entry_auth_token.text()
            if not self.auth_token:
                print("Auth token is required.")
                return
            upload_extension(self.auth_token)
            self.drivers = start_profiles(
                int(self.profile_manager_widget.entry_num_profiles.text()),
                self.profile_manager_widget.get_proxies(),
                self.auth_token
            )
            self.profile_manager_widget.update_gui_start()
        self.running = not self.running

class LoginWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)  # Reduz o espaçamento geral

        header = QLabel("Rise bot + Rise Extension")
        header.setFont(QFont("Arial", 16))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        form_layout = QFormLayout()
        form_layout.setSpacing(5)  # Reduz o espaçamento entre os itens do formulário

        self.username_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)

        form_layout.addRow("Username:", self.username_entry)
        form_layout.addRow("Password:", self.password_entry)

        main_layout.addLayout(form_layout)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)
        login_button.setFixedHeight(35)  # Define uma altura fixa para o botão
        main_layout.addWidget(login_button)

        main_layout.setContentsMargins(20, 20, 20, 20)  # Adiciona margens ao layout principal
        self.setLayout(main_layout)

    def login(self):
        self.parent.login(self.username_entry.text(), self.password_entry.text())

class ProfileManagerWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()

        header = QLabel("Rise bot + Rise Extension")
        header.setFont(QFont("Arial", 16))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        layout.addWidget(QLabel("Number of Profiles:"))
        self.entry_num_profiles = QLineEdit()
        layout.addWidget(self.entry_num_profiles)

        layout.addWidget(QLabel("Proxies (one per line):"))
        self.text_proxies = QTextEdit()
        layout.addWidget(self.text_proxies)

        layout.addWidget(QLabel("Auth Token:"))
        self.entry_auth_token = QLineEdit()
        layout.addWidget(self.entry_auth_token)

        self.toggle_button = QPushButton("Create Profiles")
        self.toggle_button.clicked.connect(self.parent.toggle_profiles)
        layout.addWidget(self.toggle_button)

        self.setLayout(layout)

    def get_proxies(self):
        return self.text_proxies.toPlainText().strip().split("\n")

    def update_gui_start(self):
        self.toggle_button.setText("Stop Profiles")

    def update_gui_stop(self):
        self.toggle_button.setText("Create Profiles")

def setup_gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())