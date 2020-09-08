from google.cloud import vision
from google.cloud.vision import types
import os
import io

execution_path = os.getcwd()
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'XXXXXXXXXXXXXXXXXXXXXXXXXXXX.json' ## Use your Google .json credenticals here 

dest = ''

def OCR():
    client = vision.ImageAnnotatorClient()
    path = dest
    image_file = io.open(path,'rb').read()
    image1 = vision.types.Image(content = image_file)
    response = client.text_detection(image = image1)
    global doc_text
    doc_text = response.full_text_annotation.text
    print(doc_text)
 


from PyQt5 import uic
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class Ui(QtWidgets.QMainWindow):

    ##Importing GUI file

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)
        self.show()
        self.openb.clicked.connect(self.openFileNameDialog)
        self.readb.clicked.connect(self.reading)
            
        
    ## Dialog window for image file opening
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        global dest
        dest = fileName
        print(dest)
        if fileName:
            self.pic.setPixmap(QtGui.QPixmap(fileName))
            
        
    ## Result text output  
    def reading(self):
        OCR()
        self.result.setText(doc_text)
        
app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()