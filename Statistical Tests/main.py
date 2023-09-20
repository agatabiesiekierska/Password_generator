from PyQt5.QtWidgets import * 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import *
import sys
from test_Q_Dixona import *
from test_t_studenta import *


class WindowApplication(QMainWindow):
    def __init__(self):
        super().__init__()

# Set the title and the size of the window
        self.setWindowTitle('STATISTICAL TESTS'.upper())
        self.setGeometry(0,0,650,400)
        self.setStyleSheet('background-color: lightgray')

# Set the Label the title to the programm  
        self.label_1 = QLabel('='*5 + 'STATISTICAL TESTS' + '='*5, self)
        self.label_1.move(15, 2)
        self.label_1.resize(600,100)
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setFont(QFont('Arial',25))

# Set the Label telling what user should do 
        self.label_2 = QLabel('Provide the file path and select the statistical test', self)
        self.label_2.move(15,80)
        self.label_2.resize(600,25)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setFont(QFont('Arial',16))

# Set the Label telling user what to type (path to file) 
        self.label_3 = QLabel('Path to file \nwith data:', self)
        self.label_3.move(15,115)
        self.label_3.resize(200,100)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setFont(QFont('Arial',12))

# Set the Label telling user what to type (significance) 
        self.label_4 = QLabel('Significance: ', self)
        self.label_4.move(15,200)
        self.label_4.resize(200,30)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setFont(QFont('Arial',12))

# Set the Label telling user what to type (real value - only in t-Student test)  
        self.label_5 = QLabel('Real value:\n(only in Student\'s t-test)', self)
        self.label_5.move(275,200)
        self.label_5.resize(170,50)
        self.label_5.setAlignment(Qt.AlignRight)
        self.label_5.setFont(QFont('Arial',12))

# Set the Label telling user what to type (path to export) 
        self.label_6 = QLabel('Path to \nexport results:', self)
        self.label_6.move(15,225)
        self.label_6.resize(200,90)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setFont(QFont('Arial',12))

        self.UiComponents()
        self.show()

    # method for widgets
    def UiComponents(self):
 
# Create a button for Q-Dixon
        self.button_1 = QPushButton('Dixon\'s Q test', self)
        self.button_1.setGeometry(300, 200, 150, 60)
        self.button_1.move(100, 325)
        self.button_1.clicked.connect(self.on_click_1)
        self.button_1.setStyleSheet('background-color : white')

# Create a button for t-Student        
        self.button_2 = QPushButton('Student\'s t-test', self)
        self.button_2.setGeometry(300, 200, 150, 60)
        self.button_2.move(400, 325)
        self.button_2.clicked.connect(self.on_click_2)
        self.button_2.setStyleSheet('background-color : white')

# Create textbox for path to import data
        self.textbox_1 = QLineEdit(self)
        self.textbox_1.move(175,150)
        self.textbox_1.resize(280,40)
        self.textbox_1.setStyleSheet('background-color : white')

# Create textbox for path to export data
        self.textbox_4 = QLineEdit(self)
        self.textbox_4.move(175,250)
        self.textbox_4.resize(280,40)
        self.textbox_4.setStyleSheet('background-color : white')

# Create textbox for significance level
        self.textbox_2 = QLineEdit(self)
        self.textbox_2.move(175,200)
        self.textbox_2.resize(100,40)
        self.textbox_2.setStyleSheet('background-color : white')
# Create textbox for real value (for t-Student)
        self.textbox_3 = QLineEdit(self)
        self.textbox_3.move(450,200)
        self.textbox_3.resize(100,40)
        self.textbox_3.setStyleSheet('background-color : white')
# action method for Dixon
    def on_click_1(self):
        try:
                path_to_imp = self.textbox_1.text()
                path_to_exp = self.textbox_4.text()
                path_to_exp+=r'\results_Q-Dixon.txt'
                significance = float(self.textbox_2.text())
                series = DixonTest(path_to_imp,significance)
                series.Export_to_file(path_to_exp)
                QMessageBox.question(self, 'Results', 'Results Exported Correctly!')
                self.textbox_1.setText('')
                self.textbox_2.setText('')
                self.textbox_3.setText('')
                self.textbox_4.setText('')
        except: QMessageBox.question(self, 'Results', 'ERROR')
       

# action method for t-Student 
    def on_click_2(self):
        try:
                path_to_imp = self.textbox_1.text()
                path_to_exp = self.textbox_4.text()
                path_to_exp+=r'\results_t-Student.txt'
                significance = float(self.textbox_2.text())
                real_val = float(self.textbox_3.text())
                series = tStudent(path_to_imp,significance, real_val)
                series.Export_to_file(path_to_exp)
                QMessageBox.question(self, 'Results', 'Results Exported Correctly!')
                self.textbox_1.setText('')
                self.textbox_2.setText('')
                self.textbox_3.setText('')
                self.textbox_4.setText('')
        except: QMessageBox.question(self, 'Results', 'ERROR')



# Create layout and add all elements
        self.layout = QGridLayout()
        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.button_1)
        self.layout.addWidget(self.button_2)


        self.setLayout(self.layout)
         
# Show the GUI
        self.show()

# create pyqt5 app
App = QApplication(sys.argv)
 
# create the instance of our Window
window = WindowApplication()
 
# start the app
sys.exit(App.exec())
    
