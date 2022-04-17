from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPushButton, QLabel, QFrame, QProgressBar, QMainWindow, QApplication
from winreg import *

from calendarpaint import *
from darktheme import style_rc

registry = ConnectRegistry(None,HKEY_CURRENT_USER)
key = OpenKey(registry, r'SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Explorer\\Accent')
key_value = QueryValueEx(key,'AccentColorMenu')
accent_int = key_value[0]
accent = accent_int-4278190080
accent = str(hex(accent)).split('x')[1]
accent = accent[4:6]+accent[2:4]+accent[0:2]
accent = 'rgb'+str(tuple(int(accent[i:i+2], 16) for i in (0, 2, 4)))
#accentlight = 'rgb'+str(tuple(int(accent[i:i+2], 16) for i in (0, 2, 4)))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(980, 700)
        MainWindow.setMinimumSize(QtCore.QSize(980, 700))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("/*BACKGROUND*/\n"
"QWidget {\n"
"    background: transparent;\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 17px;\n"
"    font-family: \"Segoe UI Variable Small\", serif;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"/*MENU*/\n"
"QMenuBar {\n"
"    background-color: transparent;\n"
"    color: white;\n"
"    padding: 10px;\n"
"    font-size: 17px;\n"
"    font-family: \"Segoe UI Variable Small\", serif;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent;\n"
"    padding: 10px 13px;\n"
"    margin-left: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: transparent;\n"
"    padding-left: 1px;\n"
"    padding-top: 1px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent;\n"
"    padding: 5px 15px;\n"
"    border-radius: 5px;\n"
"    min-width: 60px;\n"
"    margin: 3px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"QMenu::item:pressed {\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"}\n"
"\n"
"QMenu::right-arrow {\n"
"    image: url(:/newPrefix/TreeViewClose.png);\n"
"    min-width: 40px;\n"
"    min-height: 18px;\n"
"}\n"
"\n"
"QMenuBar:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/*PUSHBUTTON*/\n"
"QPushButton {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 7px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"}\n"
"\n"
"/*RADIOBUTTON*/\n"
"QRadioButton {\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    border-radius: 13px;\n"
"    border: 2px solid #848484;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: "+accent+";\n"
"    border: 2px solid "+accent+";\n"
"    image: url(:/newPrefix/radio.png);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QRadioButton:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QRadioButton::indicator:disabled {\n"
"    border: 2px solid #646464;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"\n"
"/*CHECKBOX*/\n"
"QCheckBox {\n"
"    min-height: 30px;\n"
"    max-height: 30px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    border-radius: 5px;\n"
"    border: 2px solid #848484;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: "+accent+";\n"
"    border: 2px solid "+accent+";\n"
"    image: url(:/newPrefix/check.png);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled {\n"
"    border: 2px solid #646464;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"}\n"
"\n"
"/*GROUPBOX*/\n"
"QGroupBox {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    margin-top: 36px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    padding: 7px 15px;\n"
"    margin-left: 5px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QGroupBox::title::disabled {\n"
"    color: rgb(150, 150, 150)\n"
"}\n"
"\n"
"/*TABWIDGET*/\n"
"QTabWidget {\n"
"}\n"
"\n"
"QWidget {\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid rgb(43, 43, 43);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    padding: 7px 15px;\n"
"    margin-right: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:disabled {\n"
"    color: rgb(150, 150, 150)\n"
"}\n"
"\n"
"/*SPINBOX*/\n"
"QSpinBox {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QSpinBox::focus {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"    image: url(:/newPrefix/SpinBoxUp.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QSpinBox::down-button {\n"
"    image: url(:/newPrefix/SpinBoxDown.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QSpinBox::down-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QSpinBox::drop-down {\n"
"    background-color: transparent;\n"
"    width: 50px;\n"
"}\n"
"\n"
"QSpinBox:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QSpinBox::up-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxUpDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QSpinBox::down-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxDownDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"/*DOUBLESPINBOX*/\n"
"QDoubleSpinBox {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDoubleSpinBox::focus {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button {\n"
"    image: url(:/newPrefix/SpinBoxUp.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button {\n"
"    image: url(:/newPrefix/SpinBoxDown.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDoubleSpinBox::drop-down {\n"
"    background-color: transparent;\n"
"    width: 50px;\n"
"}\n"
"\n"
"QDoubleSpinBox:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxUpDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxDownDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"/*DATEEDIT*/\n"
"QDateEdit {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDateEdit::focus {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QDateEdit::up-button {\n"
"    image: url(:/newPrefix/SpinBoxUp.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QDateEdit::up-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QDateEdit::up-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateEdit::down-button {\n"
"    image: url(:/newPrefix/SpinBoxDown.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QDateEdit::down-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QDateEdit::down-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    background-color: transparent;\n"
"    width: 50px;\n"
"}\n"
"\n"
"QDateEdit:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateEdit::up-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxUpDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateEdit::down-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxDownDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"/*TIMEEDIT*/\n"
"QTimeEdit {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"}\n"
"\n"
"QTimeEdit:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QTimeEdit::focus {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QTimeEdit::up-button {\n"
"    image: url(:/newPrefix/SpinBoxUp.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QTimeEdit::up-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QTimeEdit::up-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QTimeEdit::down-button {\n"
"    image: url(:/newPrefix/SpinBoxDown.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QTimeEdit::down-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QTimeEdit::down-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QTimeEdit::drop-down {\n"
"    background-color: transparent;\n"
"    width: 50px;\n"
"}\n"
"\n"
"QTimeEdit:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QTimeEdit::up-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxUpDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QTimeEdit::down-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxDownDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"/*DATETIMEEDIT*/\n"
"QDateTimeEdit {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"    min-width: 190px;\n"
"    max-width: 190px;\n"
"}\n"
"\n"
"QDateTimeEdit:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QDateTimeEdit::focus {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QDateTimeEdit::up-button {\n"
"    image: url(:/newPrefix/SpinBoxUp.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QDateTimeEdit::up-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QDateTimeEdit::up-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateTimeEdit::down-button {\n"
"    image: url(:/newPrefix/SpinBoxDown.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    margin-right: 2px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QDateTimeEdit::down-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QDateTimeEdit::down-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateTimeEdit::drop-down {\n"
"    background-color: transparent;\n"
"    width: 50px;\n"
"}\n"
"\n"
"QDateTimeEdit:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateTimeEdit::up-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxUpDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QDateTimeEdit::down-button:disabled {\n"
"    image: url(:/newPrefix/SpinBoxDownDisabled.png);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"/*SLIDERVERTICAL*/\n"
"QSlider:vertical {\n"
"    min-width: 30px;\n"
"    min-height: 100px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px; \n"
"    background-color: rgb(255, 255, 255, 150);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-color: "+accent+";\n"
"    border: 6px solid #454545;\n"
"    height: 13px;\n"
"    min-width: 15px;\n"
"    margin: 0px -10px;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: "+accent+";\n"
"    border: 4px solid #454545;\n"
"    height: 17px;\n"
"    min-width: 15px;\n"
"    margin: 0px -10px;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: "+accent+";\n"
"    border: 7px solid #454545;\n"
"    height: 11px;\n"
"    min-width: 15px;\n"
"    margin: 0px -10px;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QSlider::groove:vertical:disabled {\n"
"    background-color: rgb(255, 255, 255, 75);\n"
"}\n"
"\n"
"QSlider::handle:vertical:disabled {\n"
"    background-color: #555555;\n"
"    border: 6px solid #353535;\n"
"}\n"
"\n"
"/*SLIDERHORIZONTAL*/\n"
"QSlider:horizontal {\n"
"    min-width: 100px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px; \n"
"    background-color: rgb(255, 255, 255, 150);\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: "+accent+";\n"
"    border: 6px solid #454545;\n"
"    width: 13px;\n"
"    min-height: 15px;\n"
"    margin: -10px 0;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: "+accent+";\n"
"    border: 4px solid #454545;\n"
"    width: 17px;\n"
"    min-height: 15px;\n"
"    margin: -10px 0;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: "+accent+";\n"
"    border: 7px solid #454545;\n"
"    width: 11px;\n"
"    min-height: 15px;\n"
"    margin: -10px 0;\n"
"    border-radius: 12px\n"
"}\n"
"\n"
"QSlider::groove:horizontal:disabled {\n"
"    background-color: rgb(255, 255, 255, 75);\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background-color: #555555;\n"
"    border: 6px solid #353535;\n"
"}\n"
"\n"
"/*PROGRESSBAR*/\n"
"QProgressBar {\n"
"    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.119403 rgba(255, 255, 255, 250), stop:0.273632 rgba(0, 0, 0, 0));\n"
"    border-radius: 2px;\n"
"    min-height: 4px;\n"
"    max-height: 4px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: "+accent+";\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"/*COMBOBOX*/\n"
"QComboBox {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    padding-left: 10px;\n"
"    min-height: 38px;\n"
"    max-height: 38px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"}\n"
"\n"
"QComboBox::pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/newPrefix/combobox.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background-color: transparent;\n"
"    min-width: 50px;\n"
"}\n"
"\n"
#"QComboBox QAbstractItemView {\n"
#"    color: rgb(255, 255, 255);\n"
#"    border: 1px solid rgb(0, 0, 0, 100);\n"
#"    background-color: transparent;\n"
#" }\n"
"\n"
"QComboBox:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QComboBox::down-arrow:disabled {\n"
"    image: url(:/newPrefix/ComboBoxDisabled.png);\n"
"}\n"
"\n"
"/*LINEEDIT*/\n"
"QLineEdit {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    font-size: 16px;\n"
"    font-family: \"Segoe UI\", serif;\n"
"    font-weight: 500;\n"
"    border-radius: 7px;\n"
"    border-bottom: 1px solid rgb(255, 255, 255, 200);\n"
"    padding-top: 0px;\n"
"    padding-left: 5px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"    border-bottom: 1px solid rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-bottom: 2px solid "+accent+";\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border-top: 1px solid rgb(255, 255, 255, 13);\n"
"    border-left: 1px solid rgb(255, 255, 255, 13);\n"
"    border-right: 1px solid rgb(255, 255, 255, 13);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"    border-bottom: 1px solid rgb(255, 255, 255, 100);\n"
"}\n"
"\n"
"/*SCROLLVERTICAL*/\n"
"QScrollBar:vertical {\n"
"    border: 6px solid rgb(255, 255, 255, 0);\n"
"    margin: 14px 0px 14px 0px;\n"
"    width: 16px;\n"
"}\n"
"\n"
"QScrollBar:vertical:hover {\n"
"    border: 5px solid rgb(255, 255, 255, 0);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(255, 255, 255, 130);\n"
"    border-radius: 2px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    image: url(:/newPrefix/Scrolltoptrans.png);\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    image: url(:/newPrefix/Scrolltophovertrans.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    image: url(:/newPrefix/Scrolltoppressedtrans.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    image: url(:/newPrefix/Scrollbottomtrans.png);\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:hover {\n"
"    image: url(:/newPrefix/Scrollbottomhovertrans.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    image: url(:/newPrefix/Scrollbottompressedtrans.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"/*SCROLLHORIZONTAL*/\n"
"QScrollBar:horizontal {\n"
"    border: 6px solid rgb(255, 255, 255, 0);\n"
"    margin: 0px 14px 0px 14px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QScrollBar:horizontal:hover {\n"
"    border: 5px solid rgb(255, 255, 255, 0);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(255, 255, 255, 130);\n"
"    border-radius: 2px;\n"
"    min-width: 25px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    image: url(:/newPrefix/Scrolllefttrans.png);\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:hover {\n"
"    image: url(:/newPrefix/Scrolllefthovertrans.png);\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"    image: url(:/newPrefix/Scrollleftpressedtrans.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"    image: url(:/newPrefix/Scrollrighttrans.png);\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover {\n"
"    image: url(:/newPrefix/Scrollrighthovertrans.png);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"    image: url(:/newPrefix/Scrollrightpressedtrans.png);\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"/*TEXTEDIT*/\n"
"QTextEdit {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    font-size: 16px;\n"
"    font-family: \"Segoe UI\", serif;\n"
"    font-weight: 500;\n"
"    border-radius: 7px;\n"
"    border-bottom: 1px solid rgb(255, 255, 255, 200);\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"    border: 1px solid rgb(255, 255, 255, 10);\n"
"    border-bottom: 1px solid rgb(255, 255, 255, 200);\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border-bottom: 2px solid "+accent+";\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border-top: 1px solid rgb(255, 255, 255, 13);\n"
"    border-left: 1px solid rgb(255, 255, 255, 13);\n"
"    border-right: 1px solid rgb(255, 255, 255, 13);\n"
"}\n"
"\n"
"QTextEdit:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border: 1px solid rgb(255, 255, 255, 5);\n"
"    border-bottom: 1px solid rgb(255, 255, 255, 100);\n"
"}\n"
"\n"
"/*CALENDAR*/\n"
"QCalendarWidget {\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"      height: 36px;\n"
"      font-size: 18px;\n"
"      background-color: rgb(255, 255, 255, 0);\n"
"    margin: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar { \n"
"    background-color: rgb(255, 255, 255, 0); \n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom: none;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(:/newPrefix/PrevMonth.png);\n"
"    width: 32px;\n"
"}\n"
"\n"
"#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(:/newPrefix/NextMonth.png);\n"
"    width: 32px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
"    color: white;\n"
"    margin: 5px 0px;\n"
"    padding: 0px 10px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::menu-indicator#qt_calendar_monthbutton {\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox { \n"
"    background-color: rgb(255, 255, 255, 5);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    color: rgb(255, 255, 255, 200);\n"
"    border-radius: 5px;\n"
"    font-size: 17px;\n"
"    font-family: \"Segoe UI Variable Small\", serif;\n"
"    font-weight: 400;\n"
"    padding-left: 10px;\n"
"    margin: 5px 0px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button {\n"
"    image: url(:/newPrefix/SpinBoxUp.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-right: 2px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::down-button {\n"
"    image: url(:/newPrefix/SpinBoxDown.png);\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 4px;\n"
"    margin-right: 2px;\n"
"    margin-top: 1px;\n"
"    margin-bottom: 1px;\n"
"    min-width: 30px;\n"
"    max-width: 30px;\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::down-button:hover {\n"
"    background-color: rgb(255, 255, 255, 25);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::down-button:pressed {\n"
"    background-color: rgb(255, 255, 255, 5);\n"
"}\n"
"\n"
"QCalendarWidget QWidget { \n"
"    alternate-background-color: rgb(255, 255, 255, 0); \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"     color: rgb(255, 255, 255);  \n"
"     selection-background-color: "+accent+";\n"
"     selection-color: black;\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled {\n"
"     color: rgb(150, 150, 150);  \n"
"     selection-background-color: rgb(150, 150, 150);\n"
"     selection-color: black;\n"
"    border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:disabled, #qt_calendar_monthbutton:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"/*TREEWIDGET*/\n"
"QTreeView {\n"
"    background-color: transparent;\n"
"       border: 1px solid rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
"    outline: 0;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QTreeView::item {\n"
"    padding: 7px;\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTreeView::item:selected {\n"
"    color: white;\n"
"    background-color: rgb(255, 255, 255, 13);\n"
"    border-radius: 5px;\n"
#"    border-left: 4px solid "+accent+";\n"
"    margin-bottom: 3px;\n"
"    padding-left: 0px;\n"
"}\n"
"\n"
"QTreeView::item:!selected:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    border-radius: 5px;\n"
"    margin-bottom: 3px;\n"
"    padding-left: 0px;\n"
"}\n"
"\n"
"QTreeView::branch:has-children:!has-siblings:closed,\n"
"QTreeView::branch:closed:has-children:has-siblings {\n"
"    image: url(:/newPrefix/TreeViewClose.png);\n"
"}\n"
"\n"
"QTreeView::branch:open:has-children:!has-siblings,\n"
"QTreeView::branch:open:has-children:has-siblings {\n"
"    image: url(:/newPrefix/TreeViewOpen.png);\n"
"}\n"
"\n"
"QTreeView:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"/*TOGGLESWITCH*/\n"
"#toggleSwitch {\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 17px;\n"
"    font-family: \"Segoe UI Variable Small\", serif;\n"
"    font-weight: 400;\n"
"}\n"
"\n"
"#toggleSwitch::indicator {\n"
"    width: 22px;\n"
"    height: 22px;\n"
"    border-radius: 13px;\n"
"    border: 2px solid #848484;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    image: url(:/newPrefix/ToggleSwitchOff.png);\n"
"    margin-right: 5px;\n"
"    padding-right: 25px;\n"
"    padding-left: 0px;\n"
"}\n"
"\n"
"#toggleSwitch::indicator:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"    image: url(:/newPrefix/ToggleSwitchOffHover.png);\n"
"}\n"
"\n"
"#toggleSwitch::indicator:checked {\n"
"    background-color: "+accent+";\n"
"    border: 2px solid "+accent+";\n"
"    image: url(:/newPrefix/ToggleSwitchOn.png);\n"
"    color: rgb(0, 0, 0);\n"
"    padding-left: 25px;\n"
"    padding-right: 0px;\n"
"}\n"
"\n"
"#toggleSwitch::indicator:checked:hover {\n"
"    background-color: "+accent+";\n"
"    image: url(:/newPrefix/ToggleSwitchOnHover.png);\n"
"}\n"
"\n"
"#toggleSwitch:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"#toggleSwitch::indicator:disabled {\n"
"    border: 2px solid #646464;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    image: url(:/newPrefix/ToggleSwitchDisabled.png);\n"
"}\n"
"\n"
"/*HYPERLINKBUTTON*/\n"
"#hyperlinkButton {\n"
"    color: "+accent+";\n"
"    font-size: 17px;\n"
"    font-family: \"Segoe UI Variable Small\", serif;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"    border: none;\n"
"}\n"
"\n"
"#hyperlinkButton:hover {\n"
"    background-color: rgb(255, 255, 255, 20);\n"
"}\n"
"\n"
"#hyperlinkButton::pressed {\n"
"    background-color: rgb(255, 255, 255, 15);\n"
"    color: "+accent+";\n"
"}\n"
"\n"
"#hyperlinkButton:disabled {\n"
"    color: rgb(150, 150, 150)\n"
"}"
"\n"
"QListView {\n"
"    background-color: transparent;\n"
"    font-size: 17px;\n"
"    font-family: \"Segoe UI Variable Small\", serif;\n"
"    font-weight: 400;\n"
"    padding: 7px;\n"
"    border-radius: 10px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListView::item {\n"
"    height: 35px;\n"
"}\n"
"\n"
"QListView::item:selected:active {\n"
"    background-color: rgb(255, 255, 255, 20); \n"
"    border-radius: 5px; \n"
"    padding-left: 0px; \n"
#"    border-left: 4px solid "+accent+"\n"
"}\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(10000, 10000))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.window = QtWidgets.QFrame(self.centralwidget)
        self.window.setEnabled(True)
        self.window.setGeometry(QtCore.QRect(-11, -1, 991, 701))
        self.window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window.setObjectName("window")
        self.comboBox = QtWidgets.QComboBox(self.window)
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QtCore.QRect(370, 180, 190, 40))
        self.comboBox.setToolTip("")
        self.comboBox.setStatusTip("")
        self.comboBox.setWhatsThis("")
        self.comboBox.setAccessibleName("")
        self.comboBox.setAccessibleDescription("")
        self.comboBox.setStyleSheet("")
        self.comboBox.setCurrentText("")
        self.comboBox.setMinimumContentsLength(0)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.window)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(370, 280, 190, 40))
        self.lineEdit.setMinimumSize(QtCore.QSize(181, 40))
        self.lineEdit.setStyleSheet("")
        self.lineEdit.setObjectName("lineEdit")
        self.scrollArea = QtWidgets.QScrollArea(self.window)
        self.scrollArea.setGeometry(QtCore.QRect(640, 420, 311, 200))
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 311, 200))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.textEdit.setEnabled(True)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 40))
        self.textEdit.setStyleSheet("")
        self.textEdit.setMarkdown("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.fontComboBox = QtWidgets.QFontComboBox(self.window)
        self.fontComboBox.setEnabled(True)
        self.fontComboBox.setGeometry(QtCore.QRect(370, 230, 190, 40))
        self.fontComboBox.setStyleSheet("")
        self.fontComboBox.setObjectName("fontComboBox")
        self.calendarWidget = Calendar(self.window)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setGeometry(QtCore.QRect(580, 10, 400, 400))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("")
        self.calendarWidget.setObjectName("calendarWidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.window)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QtCore.QRect(40, 340, 250, 260))
        self.treeWidget.setStyleSheet("")
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setBackground(0, QtGui.QColor(0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.treeWidget.headerItem().setForeground(0, brush)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.groupBox = QtWidgets.QGroupBox(self.window)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(360, 0, 211, 161))
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 60, 141, 40))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(20, 120, 150, 4))
        self.progressBar.setStyleSheet("")
        self.progressBar.setProperty("value", 30)
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")
        self.tabWidget = QtWidgets.QTabWidget(self.window)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(20, 0, 335, 320))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(60, 70, 141, 30))
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(60, 120, 121, 30))
        self.checkBox.setStyleSheet("")
        self.checkBox.setObjectName("checkBox")
        self.toggleSwitch = QtWidgets.QCheckBox(self.tab)
        self.toggleSwitch.setEnabled(True)
        self.toggleSwitch.setGeometry(QtCore.QRect(60, 170, 181, 30))
        self.toggleSwitch.setStyleSheet("")
        self.toggleSwitch.setObjectName("toggleSwitch")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(60, 20, 158, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Small")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.hyperlinkButton = QtWidgets.QPushButton(self.tab)
        self.hyperlinkButton.setEnabled(True)
        self.hyperlinkButton.setGeometry(QtCore.QRect(60, 220, 191, 38))
        self.hyperlinkButton.setStyleSheet("")
        self.hyperlinkButton.setObjectName("hyperlinkButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox.setEnabled(True)
        self.spinBox.setGeometry(QtCore.QRect(50, 20, 190, 40))
        self.spinBox.setStyleSheet("")
        self.spinBox.setObjectName("spinBox")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.doubleSpinBox.setEnabled(True)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 70, 190, 40))
        self.doubleSpinBox.setStyleSheet("")
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_2)
        self.dateEdit.setEnabled(True)
        self.dateEdit.setGeometry(QtCore.QRect(50, 120, 202, 40))
        self.dateEdit.setMinimumSize(QtCore.QSize(202, 40))
        self.dateEdit.setStyleSheet("")
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.tab_2)
        self.timeEdit.setGeometry(QtCore.QRect(50, 170, 202, 40))
        self.timeEdit.setMinimumSize(QtCore.QSize(202, 40))
        self.timeEdit.setStyleSheet("")
        self.timeEdit.setObjectName("timeEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab_2)
        self.dateTimeEdit.setEnabled(True)
        self.dateTimeEdit.setGeometry(QtCore.QRect(50, 220, 202, 40))
        self.dateTimeEdit.setStyleSheet("")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalSlider = QtWidgets.QSlider(self.tab_4)
        self.verticalSlider.setEnabled(True)
        self.verticalSlider.setGeometry(QtCore.QRect(80, 50, 30, 160))
        self.verticalSlider.setStyleSheet("")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.horizontalSlider = QtWidgets.QSlider(self.tab_4)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(120, 110, 160, 30))
        self.horizontalSlider.setStyleSheet("")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalScrollBar2 = QtWidgets.QScrollBar(self.tab_3)
        self.verticalScrollBar2.setGeometry(QtCore.QRect(50, 20, 16, 200))
        self.verticalScrollBar2.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalScrollBar2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.verticalScrollBar2.setStyleSheet("")
        self.verticalScrollBar2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar2.setObjectName("verticalScrollBar2")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.tab_3)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(50, 230, 201, 16))
        self.horizontalScrollBar.setStyleSheet("")
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 980, 63))
        self.menuBar.setStyleSheet("")
        self.menuBar.setObjectName("menuBar")
        self.menuMenu1 = QtWidgets.QMenu(self.menuBar)
        self.menuMenu1.setObjectName("menuMenu1")
        self.menuNew = QtWidgets.QMenu(self.menuMenu1)
        self.menuNew.setEnabled(True)
        self.menuNew.setObjectName("menuNew")
        self.menuMenu2 = QtWidgets.QMenu(self.menuBar)
        self.menuMenu2.setObjectName("menuMenu2")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionItem3 = QtWidgets.QAction(MainWindow)
        self.actionItem3.setObjectName("actionItem3")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setEnabled(True)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionPlain_Text_Document = QtWidgets.QAction(MainWindow)
        self.actionPlain_Text_Document.setObjectName("actionPlain_Text_Document")
        self.actionRich_Text_Document = QtWidgets.QAction(MainWindow)
        self.actionRich_Text_Document.setObjectName("actionRich_Text_Document")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setEnabled(True)
        self.actionAbout.setObjectName("actionAbout")
        self.menuNew.addAction(self.actionPlain_Text_Document)
        self.menuNew.addAction(self.actionRich_Text_Document)
        self.menuMenu1.addAction(self.menuNew.menuAction())
        self.menuMenu1.addAction(self.actionOpen)
        self.menuMenu1.addAction(self.actionSave)
        self.menuMenu1.addAction(self.actionExit)
        self.menuMenu2.addAction(self.actionItem3)
        self.menuMenu2.addAction(self.actionCut)
        self.menuMenu2.addAction(self.actionCopy)
        self.menuMenu2.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuMenu1.menuAction())
        self.menuBar.addAction(self.menuMenu2.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.disablebtn = QtWidgets.QPushButton(self.centralwidget)
        self.disablebtn.setObjectName('disableBtn')
        self.disablebtn.setText('Disable')
        self.disablebtn.setGeometry(QtCore.QRect(400, 500, 158, 38))
        self.enablebtn = QtWidgets.QPushButton(self.centralwidget)
        self.enablebtn.setObjectName('enableBtn')
        self.enablebtn.setText('Enable')
        self.enablebtn.setGeometry(QtCore.QRect(400, 550, 158, 38))

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mica Template"))
        self.comboBox.setPlaceholderText(_translate("MainWindow", "Pick a color"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Blue"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Gray"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Green"))
        self.comboBox.setItemText(3, _translate("MainWindow", "White"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Black"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Brown"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Violet"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Orange"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Item1"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Item2"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "Item3"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Item4"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.label.setText(_translate("MainWindow", "I am a TextBlock"))
        self.radioButton.setText(_translate("MainWindow", "RadioButton"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.toggleSwitch.setText(_translate("MainWindow", "ToggleSwitch"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.hyperlinkButton.setText(_translate("MainWindow", "HyperlinkButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Buttons"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Input"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Sliders"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Scrolls"))
        self.menuMenu1.setTitle(_translate("MainWindow", "File"))
        self.menuNew.setTitle(_translate("MainWindow", "New"))
        self.menuMenu2.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionItem3.setText(_translate("MainWindow", "Undo"))
        self.actionItem3.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionPlain_Text_Document.setText(_translate("MainWindow", "Plain Text Document"))
        self.actionRich_Text_Document.setText(_translate("MainWindow", "Rich Text Document"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setShortcut(_translate("MainWindow", "Ctrl+I"))

