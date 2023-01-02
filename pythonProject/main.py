from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from design import Ui_MainWindow
from fuctions.getContent import content
import requests


class interface_1(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.searchBookBt.clicked.connect(self.PrintScreen)
        self.ui.listSeachedBooks.clicked.connect(self.PrintScreen2)
        self.books = []

    def PrintScreen(self):
        self.books = []
        self.books = content(self.ui.searchBar.text())
        for item in self.books:
            self.ui.listSeachedBooks.addItem(item[0])

    def PrintScreen2(self):
        self.ui.listWidget_2.clear()
        row = self.ui.listSeachedBooks.currentRow()
        self.ui.listWidget_2.addItem("Book Name = " + self.books[row][0])
        self.ui.listWidget_2.addItem("Price = " + self.books[row][1])
        self.ui.listWidget_2.addItem("Author = " + self.books[row][2])
        self.ui.listWidget_2.addItem("Summary = " + self.books[row][3])
        #img = QImage()
        #img.loadFromData(requests.get(self.books[row][3]).content)
        #self.ui.bookPictures.setPixmap(QPixmap(img))
        #self.ui.bookPictures.setScaledContents(True)


app = QApplication([])
window = interface_1()
window.show()
app.exec()