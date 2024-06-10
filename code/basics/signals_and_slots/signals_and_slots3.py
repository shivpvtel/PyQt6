from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton)

import sys
from random import choice


window_titles = [
    "My App", "My App", "Still my app", "Stop, still my app", "what on earth","okay","stop", "please",
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.setWindowTitle("My App")
        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)
    def the_button_was_clicked(self):
        print("clicked")
        new_window_title = choice(window_titles)
        print("setting title: %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self,window_title):
        print("Window title changed: %s" % window_title)

        if window_titles == "something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
