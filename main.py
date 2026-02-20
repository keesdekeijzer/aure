import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QDialog, QMessageBox, QStatusBar, QLabel
from PyQt6.QtWidgets import QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog
# from mainwindow import Ui_MainWindow
from PyQt6.uic import loadUi
import datetime
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog
from PyQt6.QtGui import QTextCursor
import sqlite3

from config import configuratie

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content 


class Venster(QMainWindow):
    def __init__(self):
        super().__init__()

        # Hoofdvenster
        loadUi("aure_mainwindow.ui",self)

        self.current_path = None
        self.current_fontsize = 12
        self.is_vet = False
        self.unsaved_changes = False
        self.docs = configuratie["opslaglocatie"]


        self.actionOpen.triggered.connect(self.open)
        self.actionOpslaan.triggered.connect(self.opslaan)

        self.actionSluiten.triggered.connect(self.sluiten)

    def open(self):
        bestandsnaam, _ = QFileDialog.getOpenFileName(self, "Open bestand", self.docs, "Tekstbestanden (*.txt);;Alle bestanden (*.*)")
        if bestandsnaam:
            try:
                inhoud = read_file(bestandsnaam)
                self.textEdit.setPlainText(inhoud)
                self.current_path = bestandsnaam
                self.statusbar.showMessage(f"Bestand geopend: {bestandsnaam}", 5000)
            except Exception as e:
                QMessageBox.critical(self, "Fout", str(e))

    def opslaan(self):
        if self.current_path is None:
            bestandsnaam, _ = QFileDialog.getSaveFileName(self, "Opslaan als", self.docs, "Tekstbestanden (*.txt);;Alle bestanden (*.*)")
            if bestandsnaam:
                self.current_path = bestandsnaam
            else:
                return  # Gebruiker heeft opslaan geannuleerd

        try:
            with open(self.current_path, 'w') as file:
                file.write(self.textEdit.toPlainText())
            self.statusbar.showMessage(f"Bestand opgeslagen: {self.current_path}", 5000)
        except Exception as e:
            QMessageBox.critical(self, "Fout", str(e))

    def sluiten(self):
        self.close()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Venster()
    ui.show()
    app.exec()