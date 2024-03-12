import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import ( QApplication, QMainWindow, QPushButton,)

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Shiv Patel")
		button = QPushButton("Click Here")
		self.setCentralWidget(button)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

