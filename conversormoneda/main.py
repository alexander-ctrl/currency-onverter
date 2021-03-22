from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QComboBox, \
     QVBoxLayout, QWidget, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QDoubleValidator
from currency_converter import CurrencyConverter
import sys


stylesheetButton = """

QPushButton {
    background-color: #003d5b;
    border-style: solid;
    border-width: 2px;
    border-color: white;
    color: white;
    font-size: 15px;
    padding: 8px;
}

QPushButton::hover {
    background-color: white;
    border-style: solid;
    border-width: 2px;
    border-color: #003d5b;
    color: #003d5b;
    transition-duration: 500ms;
}

"""

class Main:
    pass

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.converterc = CurrencyConverter()
        self.width = 320
        self.height = 360
        self.title = "Conversor de moneda"
        self.left = 100
        self.top = 100
        self.currency = CurrencyConverter()

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        self.setStyleSheet("background-color: #003d5b;")
        self.setWindowIcon(QIcon("logo.png"))
        self.setFixedSize(self.width, self.height)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(10*2)
        self.widget.setLayout(self.layout)

        stylecmb = """background-color: white;
                      color: #333;
                      padding: 5px;
                      border: solid 1px #eee;
                      font-size: 18px;
                    """

        self.cmbOptionsOne = QComboBox()
        self.cmbOptionsOne.setStyleSheet(stylecmb)
        self.insertOptionsInCombobox(self.cmbOptionsOne)
        self.layout.addWidget(self.cmbOptionsOne)

        self.cmbOptionsTwo = QComboBox()
        self.cmbOptionsTwo.setStyleSheet(stylecmb)
        self.insertOptionsInCombobox(self.cmbOptionsTwo)
        self.layout.addWidget(self.cmbOptionsTwo)

        self.labelValue = """
                          color: white;
                          font-size: 18px;
                          margin: 0px;
                          """

        self.labelInfo = QLabel("Value:")
        self.labelInfo.setStyleSheet(self.labelValue)
        self.layout.addWidget(self.labelInfo)

        self.textboxValue = QLineEdit()
        self.textboxValue.setEnabled(True)
        self.textboxValue.setStyleSheet(stylecmb)

        self.doubleValidator = QDoubleValidator()
        self.textboxValue.setValidator(self.doubleValidator)
        self.layout.addWidget(self.textboxValue)

        self.labelResult = QLabel("Result:")
        self.labelResult.setStyleSheet(self.labelValue)
        self.layout.addWidget(self.labelResult)

        self.layout.addStretch(1)
        self.button = QPushButton("Converter")
        self.button.setStyleSheet(stylesheetButton)
        self.button.clicked.connect(self.converter)
        self.layout.addWidget(self.button)

        self.show()

    def insertOptionsInCombobox(self, cmbOptions):
        cmbOptions.addItems(list(self.converterc.currencies))

    def converter(self):
        self.currency = CurrencyConverter()

        currency = str(self.cmbOptionsOne.currentText())
        new_currency = str(self.cmbOptionsTwo.currentText())
        amount = float(self.textboxValue.text())

        self.labelResult.setText( "Result: " + 
                                   str(self.currency.convert(amount, currency, new_currency)))


def run():
    app = QApplication(sys.argv)
    ex = MainApplication()
    sys.exit(app.exec_())

