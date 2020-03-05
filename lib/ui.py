from PyQt5.QtGui import  *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.createFormGroupBox()


        toolbar = QToolBar("Main")
        self.addToolBar(toolbar)
        self.setWindowTitle("Crypto Performance")
        self.show()

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Crypto Performance calculator")
        form = QFormLayout()
        form.addRow(QLabel("Daily Amount"), QLineEdit())
        form.addRow(QLabel("Crypto coin"), QComboBox())
        form.addRow(QLabel("Year"), QComboBox())
        form.addRow(QLabel("ROI"), QLabel())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Window = MainWindow()
    Window.show()
    sys.exit(app.exec_())      
