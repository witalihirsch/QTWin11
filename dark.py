from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QPushButton, QLabel, QFrame, QProgressBar, QMainWindow, QApplication
from winreg import *

from calendarpaint import *
from icons import styledark_rc

registry = ConnectRegistry(None,HKEY_CURRENT_USER)
key = OpenKey(registry, r'SOFTWARE\\Microsoft\Windows\\CurrentVersion\\Explorer\\Accent')
key_value = QueryValueEx(key,'AccentColorMenu')
accent_int = key_value[0]
accent = accent_int-4278190080
accent = str(hex(accent)).split('x')[1]
accent = accent[4:6]+accent[2:4]+accent[0:2]
accent = 'rgb'+str(tuple(int(accent[i:i+2], 16) for i in (0, 2, 4)))

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
        MainWindow.setStyleSheet('''/*BACKGROUND*/
QWidget {
    background: transparent;
    color: rgb(255, 255, 255);
    font-size: 17px;
    font-family: "Segoe UI Variable Small", serif;
    font-weight: 400;
}

/*MENU*/
QMenuBar {
    background-color: transparent;
    color: white;
    padding: 10px;
    font-size: 17px;
    font-family: "Segoe UI Variable Small", serif;
    font-weight: 400;
}

QMenuBar::item {
    background-color: transparent;
    padding: 10px 13px;
    margin-left: 5px;
    border-radius: 5px;
}

QMenuBar::item:selected {
    background-color: rgb(255, 255, 255, 20);
}

QMenuBar::item:pressed {
    background-color: rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
}

QMenu {
    background-color: transparent;
    padding-left: 1px;
    padding-top: 1px;
    border-radius: 5px;
    border: 1px solid rgb(255, 255, 255, 13);
}

QMenu::item {
    background-color: transparent;
    padding: 5px 15px;
    border-radius: 5px;
    min-width: 60px;
    margin: 3px;
}

QMenu::item:selected {
    background-color: rgb(255, 255, 255, 16);
}

QMenu::item:pressed {
    background-color: rgb(255, 255, 255, 10);
}

QMenu::right-arrow {
    image: url(:/TreeView/img dark/TreeViewClose.png);
    min-width: 40px;
    min-height: 18px;
}

QMenuBar:disabled {
    color: rgb(150, 150, 150);
}

QMenu::item:disabled {
    color: rgb(150, 150, 150);
    background-color: transparent;
}

/*PUSHBUTTON*/
QPushButton {
    background-color: rgb(255, 255, 255, 18);
    border: 1px solid rgb(255, 255, 255, 13);
    border-radius: 7px;
    min-height: 38px;
    max-height: 38px;
}

QPushButton:hover {
    background-color: rgb(255, 255, 255, 25);
    border: 1px solid rgb(255, 255, 255, 10);
}

QPushButton::pressed {
    background-color: rgb(255, 255, 255, 7);
    border: 1px solid rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
}

QPushButton::disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
}

/*RADIOBUTTON*/
QRadioButton {
    min-height: 30px;
    max-height: 30px;
}

QRadioButton::indicator {
    width: 22px;
    height: 22px;
    border-radius: 13px;
    border: 2px solid #848484;
    background-color: rgb(255, 255, 255, 0);
    margin-right: 5px;
}

QRadioButton::indicator:hover {
    background-color: rgb(255, 255, 255, 16);
}

QRadioButton::indicator:pressed {
    background-color: rgb(255, 255, 255, 20);
    border: 2px solid #434343;
    image: url(:/RadioButton/img dark/RadioButton.png);
}

QRadioButton::indicator:checked {
    background-color: '''+accent+''';
    border: 2px solid '''+accent+''';
    image: url(:/RadioButton/img dark/RadioButton.png);
}

QRadioButton::indicator:checked:hover {
    image: url(:/RadioButton/img dark/RadioButtonHover.png);
}

QRadioButton::indicator:checked:pressed {
    image: url(:/RadioButton/img dark/RadioButtonPressed.png);
}

QRadioButton:disabled {
    color: rgb(150, 150, 150);
}

QRadioButton::indicator:disabled {
    border: 2px solid #646464;
    background-color: rgb(255, 255, 255, 0);
}

/*CHECKBOX*/
QCheckBox {
    min-height: 30px;
    max-height: 30px;
}

QCheckBox::indicator {
    width: 22px;
    height: 22px;
    border-radius: 5px;
    border: 2px solid #848484;
    background-color: rgb(255, 255, 255, 0);
    margin-right: 5px;
}

QCheckBox::indicator:hover {
    background-color: rgb(255, 255, 255, 16);
}

QCheckBox::indicator:pressed {
    background-color: rgb(255, 255, 255, 20);
    border: 2px solid #434343;
}

QCheckBox::indicator:checked {
    background-color: '''+accent+''';
    border: 2px solid '''+accent+''';
    image: url(:/CheckBox/img dark/CheckBox.png);
}

QCheckBox::indicator:checked:pressed {
    image: url(:/CheckBox/img dark/CheckBoxPressed.png);
}

QCheckBox:disabled {
    color: rgb(150, 150, 150);
}

QCheckBox::indicator:disabled {
    border: 2px solid #646464;
    background-color: rgb(255, 255, 255, 0);
}

/*GROUPBOX*/
QGroupBox {
    border-radius: 5px;
    border: 1px solid rgb(255, 255, 255, 13);
    margin-top: 36px;
}

QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    background-color: rgb(255, 255, 255, 16);
    padding: 7px 15px;
    margin-left: 5px;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QGroupBox::title::disabled {
    color: rgb(150, 150, 150)
}

/*TABWIDGET*/
QTabWidget {
}

QWidget {
    border-radius: 5px;
}

QTabWidget::pane {
    border: 1px solid rgb(43, 43, 43);
    border-radius: 5px;
}

QTabWidget::tab-bar {
    left: 5px;
}

QTabBar::tab {
    background-color: rgb(255, 255, 255, 0);
    padding: 7px 15px;
    margin-right: 2px;
}

QTabBar::tab:hover {
    background-color: rgb(255, 255, 255, 13);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:selected {
    background-color: rgb(255, 255, 255, 16);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
}

QTabBar::tab:disabled {
    color: rgb(150, 150, 150)
}

/*SPINBOX*/
QSpinBox {
    background-color: rgb(255, 255, 255, 10);
    border: 1px solid rgb(255, 255, 255, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
    min-width: 100px;
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QSpinBox:hover {
    background-color: rgb(255, 255, 255, 16);
    border: 1px solid rgb(255, 255, 255, 13);
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QSpinBox::focus {
    background-color: rgb(255, 255, 255, 5);
    border: 1px solid rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
    border-bottom: 2px solid '''+accent+''';
}

QSpinBox::up-button {
    image: url(:/SpinBox/img dark/SpinBoxUp.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QSpinBox::up-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QSpinBox::up-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QSpinBox::down-button {
    image: url(:/SpinBox/img dark/SpinBoxDown.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QSpinBox::down-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QSpinBox::down-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QSpinBox::drop-down {
    background-color: transparent;
    width: 50px;
}

QSpinBox:disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
    border: 1px solid rgb(255, 255, 255, 5);
}

QSpinBox::up-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxUpDisabled.png);
}

QSpinBox::down-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxDownDisabled.png);
}

/*DOUBLESPINBOX*/
QDoubleSpinBox {
    background-color: rgb(255, 255, 255, 10);
    border: 1px solid rgb(255, 255, 255, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
    min-width: 100px;
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QDoubleSpinBox:hover {
    background-color: rgb(255, 255, 255, 16);
    border: 1px solid rgb(255, 255, 255, 13);
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QDoubleSpinBox::focus {
    background-color: rgb(255, 255, 255, 5);
    border: 1px solid rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
    border-bottom: 2px solid '''+accent+''';
}

QDoubleSpinBox::up-button {
    image: url(:/SpinBox/img dark/SpinBoxUp.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDoubleSpinBox::up-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QDoubleSpinBox::up-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QDoubleSpinBox::down-button {
    image: url(:/SpinBox/img dark/SpinBoxDown.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDoubleSpinBox::down-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QDoubleSpinBox::down-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QDoubleSpinBox::drop-down {
    background-color: transparent;
    width: 50px;
}

QDoubleSpinBox:disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
    border: 1px solid rgb(255, 255, 255, 5);
}

QDoubleSpinBox::up-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxUpDisabled.png);
}

QDoubleSpinBox::down-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxDownDisabled.png);
}

/*DATETIMEEDIT*/
QDateTimeEdit {
    background-color: rgb(255, 255, 255, 10);
    border: 1px solid rgb(255, 255, 255, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
    min-width: 100px;
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QDateTimeEdit:hover {
    background-color: rgb(255, 255, 255, 16);
    border: 1px solid rgb(255, 255, 255, 13);
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QDateTimeEdit::focus {
    background-color: rgb(255, 255, 255, 5);
    border: 1px solid rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
    border-bottom: 2px solid '''+accent+''';
}

QDateTimeEdit::up-button {
    image: url(:/SpinBox/img dark/SpinBoxUp.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDateTimeEdit::up-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QDateTimeEdit::up-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QDateTimeEdit::down-button {
    image: url(:/SpinBox/img dark/SpinBoxDown.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QDateTimeEdit::down-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QDateTimeEdit::down-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QDateTimeEdit::drop-down {
    background-color: transparent;
    width: 50px;
}

QDateTimeEdit:disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
    border: 1px solid rgb(255, 255, 255, 5);
}

QDateTimeEdit::up-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxUpDisabled.png);
}

QDateTimeEdit::down-button:disabled {
    image: url(:/SpinBox/img dark/SpinBoxDownDisabled.png);
}

/*SLIDERVERTICAL*/
QSlider:vertical {
    min-width: 30px;
    min-height: 100px;
}

QSlider::groove:vertical {
    width: 5px; 
    background-color: rgb(255, 255, 255, 150);
    border-radius: 2px;
}

QSlider::handle:vertical {
    background-color: '''+accent+''';
    border: 6px solid #454545;
    height: 13px;
    min-width: 15px;
    margin: 0px -10px;
    border-radius: 12px
}

QSlider::handle:vertical:hover {
    background-color: '''+accent+''';
    border: 4px solid #454545;
    height: 17px;
    min-width: 15px;
    margin: 0px -10px;
    border-radius: 12px
}

QSlider::handle:vertical:pressed {
    background-color: '''+accent+''';
    border: 7px solid #454545;
    height: 11px;
    min-width: 15px;
    margin: 0px -10px;
    border-radius: 12px
}

QSlider::groove:vertical:disabled {
    background-color: rgb(255, 255, 255, 75);
}

QSlider::handle:vertical:disabled {
    background-color: #555555;
    border: 6px solid #353535;
}

/*SLIDERHORIZONTAL*/
QSlider:horizontal {
    min-width: 100px;
    min-height: 30px;
}

QSlider::groove:horizontal {
    height: 5px; 
    background-color: rgb(255, 255, 255, 150);
    border-radius: 2px;
}

QSlider::handle:horizontal {
    background-color: '''+accent+''';
    border: 6px solid #454545;
    width: 13px;
    min-height: 15px;
    margin: -10px 0;
    border-radius: 12px
}

QSlider::handle:horizontal:hover {
    background-color: '''+accent+''';
    border: 4px solid #454545;
    width: 17px;
    min-height: 15px;
    margin: -10px 0;
    border-radius: 12px
}

QSlider::handle:horizontal:pressed {
    background-color: '''+accent+''';
    border: 7px solid #454545;
    width: 11px;
    min-height: 15px;
    margin: -10px 0;
    border-radius: 12px
}

QSlider::groove:horizontal:disabled {
    background-color: rgb(255, 255, 255, 75);
}

QSlider::handle:horizontal:disabled {
    background-color: #555555;
    border: 6px solid #353535;
}

/*PROGRESSBAR*/
QProgressBar {
    background-color: qlineargradient(spread:reflect, x1:0.5, y1:0.5, x2:0.5, y2:1, stop:0.119403 rgba(255, 255, 255, 250), stop:0.273632 rgba(0, 0, 0, 0));
    border-radius: 2px;
    min-height: 4px;
    max-height: 4px;
}

QProgressBar::chunk {
    background-color: '''+accent+''';
    border-radius: 2px;
}

/*COMBOBOX*/
QComboBox {
    background-color: rgb(255, 255, 255, 16);
    border: 1px solid rgb(255, 255, 255, 13);
    border-radius: 5px;
    padding-left: 10px;
    min-height: 38px;
    max-height: 38px;
}

QComboBox:hover {
    background-color: rgb(255, 255, 255, 20);
    border: 1px solid rgb(255, 255, 255, 10);
}

QComboBox::pressed {
    background-color: rgb(255, 255, 255, 20);
    border: 1px solid rgb(255, 255, 255, 13);
    color: rgb(255, 255, 255, 200);
}

QComboBox::down-arrow {
    image: url(:/ComboBox/img dark/ComboBox.png);
}

QComboBox::drop-down {
    background-color: transparent;
    min-width: 50px;
}

QComboBox:disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
    border: 1px solid rgb(255, 255, 255, 5);
}

QComboBox::down-arrow:disabled {
    image: url(:/ComboBox/img dark/ComboBoxDisabled.png);
}

/*LINEEDIT*/
QLineEdit {
    background-color: rgb(255, 255, 255, 16);
    border: 1px solid rgb(255, 255, 255, 13);
    font-size: 16px;
    font-family: "Segoe UI", serif;
    font-weight: 500;
    border-radius: 7px;
    border-bottom: 1px solid rgb(255, 255, 255, 150);
    padding-top: 0px;
    padding-left: 5px;
}

QLineEdit:hover {
    background-color: rgb(255, 255, 255, 20);
    border: 1px solid rgb(255, 255, 255, 10);
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QLineEdit:focus {
    border-bottom: 2px solid '''+accent+''';
    background-color: rgb(255, 255, 255, 5);
    border-top: 1px solid rgb(255, 255, 255, 13);
    border-left: 1px solid rgb(255, 255, 255, 13);
    border-right: 1px solid rgb(255, 255, 255, 13);
}

QLineEdit:disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
    border: 1px solid rgb(255, 255, 255, 5);
}

/*SCROLLVERTICAL*/
QScrollBar:vertical {
    border: 6px solid rgb(255, 255, 255, 0);
    margin: 14px 0px 14px 0px;
    width: 16px;
}

QScrollBar:vertical:hover {
    border: 5px solid rgb(255, 255, 255, 0);
}

QScrollBar::handle:vertical {
    background-color: rgb(255, 255, 255, 130);
    border-radius: 2px;
    min-height: 25px;
}

QScrollBar::sub-line:vertical {
    image: url(:/ScrollVertical/img dark/ScrollTop.png);
    subcontrol-position: top;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:vertical:hover {
    image: url(:/ScrollVertical/img dark/ScrollTopHover.png);
}

QScrollBar::sub-line:vertical:pressed {
    image: url(:/ScrollVertical/img dark/ScrollTopPressed.png);
}

QScrollBar::add-line:vertical {
    image: url(:/ScrollVertical/img dark/ScrollBottom.png);
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical:hover {
    image: url(:/ScrollVertical/img dark/ScrollBottomHover.png);
}

QScrollBar::add-line:vertical:pressed {
    image: url(:/ScrollVertical/img dark/ScrollBottomPressed.png);
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

/*SCROLLHORIZONTAL*/
QScrollBar:horizontal {
    border: 6px solid rgb(255, 255, 255, 0);
    margin: 0px 14px 0px 14px;
    height: 16px;
}

QScrollBar:horizontal:hover {
    border: 5px solid rgb(255, 255, 255, 0);
}

QScrollBar::handle:horizontal {
    background-color: rgb(255, 255, 255, 130);
    border-radius: 2px;
    min-width: 25px;
}

QScrollBar::sub-line:horizontal {
    image: url(:/ScrollHorizontal/img dark/ScrollLeft.png);
    subcontrol-position: left;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal:hover {
    image: url(:/ScrollHorizontal/img dark/ScrollLeftHover.png);
}

QScrollBar::sub-line:horizontal:pressed {
    image: url(:/ScrollHorizontal/img dark/ScrollLeftPressed.png);
}

QScrollBar::add-line:horizontal {
    image: url(:/ScrollHorizontal/img dark/ScrollRight.png);
    subcontrol-position: right;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal:hover {
    image: url(:/ScrollHorizontal/img dark/ScrollRightHover.png);
}

QScrollBar::add-line:horizontal:pressed {
    image: url(:/ScrollHorizontal/img dark/ScrollRightPressed.png);
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}

/*TEXTEDIT*/
QTextEdit {
    background-color: rgb(255, 255, 255, 16);
    border: 1px solid rgb(255, 255, 255, 13);
    font-size: 16px;
    font-family: "Segoe UI", serif;
    font-weight: 500;
    border-radius: 7px;
    border-bottom: 1px solid rgb(255, 255, 255, 150);
    padding: 5px;
}

QTextEdit:hover {
    background-color: rgb(255, 255, 255, 20);
    border: 1px solid rgb(255, 255, 255, 10);
    border-bottom: 1px solid rgb(255, 255, 255, 150);
}

QTextEdit:focus {
    border-bottom: 2px solid '''+accent+''';
    background-color: rgb(255, 255, 255, 5);
    border-top: 1px solid rgb(255, 255, 255, 13);
    border-left: 1px solid rgb(255, 255, 255, 13);
    border-right: 1px solid rgb(255, 255, 255, 13);
}

QTextEdit:disabled {
    color: rgb(150, 150, 150);
    background-color: rgb(255, 255, 255, 13);
    border: 1px solid rgb(255, 255, 255, 5);
}

/*CALENDAR*/
QCalendarWidget {
}

QCalendarWidget QToolButton {
    height: 36px;
    font-size: 18px;
    background-color: rgb(255, 255, 255, 0);
    margin: 5px;
}

QCalendarWidget QWidget#qt_calendar_navigationbar { 
    background-color: rgb(255, 255, 255, 0); 
    border: 1px solid rgb(255, 255, 255, 13);
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
    border-bottom: none;
}

#qt_calendar_prevmonth {
    qproperty-icon: url(:/PrevNext/img dark/PrevMonth.png);
    width: 32px;
}

#qt_calendar_nextmonth {
    qproperty-icon: url(:/PrevNext/img dark/NextMonth.png);
    width: 32px;
}

#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgb(255, 255, 255, 16);
    border-radius: 5px;
}

#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgb(255, 255, 255, 10);
    border-radius: 5px;
}

#qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: white;
    margin: 5px 0px;
    padding: 0px 10px;
}

#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgb(255, 255, 255, 16);
    border-radius: 5px;
}

#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgb(255, 255, 255, 10);
    border-radius: 5px;
}

QCalendarWidget QToolButton::menu-indicator#qt_calendar_monthbutton {
    background-color: transparent;
}

QCalendarWidget QMenu {
    background-color : #202020;
}

QCalendarWidget QSpinBox {
    margin: 5px 0px;
}

QCalendarWidget QSpinBox::focus {
    background-color: rgb(255, 255, 255, 5);
    border: 1px solid rgb(255, 255, 255, 13);
    color: rgb(0, 0, 0, 200);
    border-bottom: 2px solid '''+accent+''';
}

QCalendarWidget QSpinBox::up-button {
    image: url(:/SpinBox/img dark/SpinBoxUp.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QCalendarWidget QSpinBox::up-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QCalendarWidget QSpinBox::up-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QCalendarWidget QSpinBox::down-button {
    image: url(:/SpinBox/img dark/SpinBoxDown.png);
    background-color: rgb(0, 0, 0, 0);
    border: 1px solid rgb(0, 0, 0, 0);
    border-radius: 4px;
    margin-top: 1px;
    margin-bottom: 1px;
    margin-right: 2px;
    min-width: 30px;
    max-width: 30px;
    min-height: 20px;
}

QCalendarWidget QSpinBox::down-button:hover {
    background-color: rgb(255, 255, 255, 13);
}

QCalendarWidget QSpinBox::down-button:pressed {
    background-color: rgb(255, 255, 255, 5);
}

QCalendarWidget QWidget { 
    alternate-background-color: rgb(255, 255, 255, 0); 
}

QCalendarWidget QAbstractItemView:enabled {
    color: rgb(255, 255, 255);  
    selection-background-color: '''+accent+''';
    selection-color: black;
    border: 1px solid rgb(255, 255, 255, 13);
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
    outline: 0;
}

QCalendarWidget QAbstractItemView:disabled {
    color: rgb(150, 150, 150);  
    selection-background-color: rgb(150, 150, 150);
    selection-color: black;
    border: 1px solid rgb(255, 255, 255, 13);
    border-top-left-radius: 0px;
    border-top-right-radius: 0px;
    border-bottom-left-radius: 5px;
    border-bottom-right-radius: 5px;
}

#qt_calendar_yearbutton:disabled, #qt_calendar_monthbutton:disabled {
    color: rgb(150, 150, 150);
}

#qt_calendar_prevmonth:disabled {
    qproperty-icon: url(:/PrevNext/img dark/PrevMonthDisabled.png);
}

#qt_calendar_nextmonth:disabled {
    qproperty-icon: url(:/PrevNext/img dark/NextMonthDisabled.png);
}

/*TREEWIDGET*/
QTreeView {
    background-color: transparent;
    border: 1px solid rgb(255, 255, 255, 13);
    border-radius: 5px;
    outline: 0;
    padding-right: 5px;
}

QTreeView::item {
    padding: 7px;
    margin-top: 3px;
}

QTreeView::item:selected {
    color: white;
    background-color: rgb(255, 255, 255, 13);
    border-radius: 5px;
    margin-bottom: 3px;
    padding-left: 0px;
}

QTreeView::item:!selected:hover {
    background-color: rgb(255, 255, 255, 16);
    border-radius: 5px;
    margin-bottom: 3px;
    padding-left: 0px;
}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {
    image: url(:/TreeView/img dark/TreeViewClose.png);
}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings {
    image: url(:/TreeView/img dark/TreeViewOpen.png);
}

QTreeView:disabled {
    color: rgb(150, 150, 150);
}

/*TOGGLESWITCH*/
#toggleSwitch {
    color: rgb(255, 255, 255);
    font-size: 17px;
    font-family: "Segoe UI Variable Small", serif;
    font-weight: 400;
}

#toggleSwitch::indicator {
    width: 22px;
    height: 22px;
    border-radius: 13px;
    border: 2px solid #848484;
    background-color: rgb(255, 255, 255, 0);
    image: url(:/ToggleSwitch/img dark/ToggleSwitchOff.png);
    margin-right: 5px;
    padding-right: 25px;
    padding-left: 0px;
}

#toggleSwitch::indicator:hover {
    background-color: rgb(255, 255, 255, 13);
    image: url(:/ToggleSwitch/img dark/ToggleSwitchOffHover.png);
}

#toggleSwitch::indicator:pressed {
    background-color: rgb(255, 255, 255, 20);
    width: 26px;
    padding-right: 21px;
    image: url(:/ToggleSwitch/img dark/ToggleSwitchOffPressed.png);
}

#toggleSwitch::indicator:checked {
    background-color: '''+accent+''';
    border: 2px solid '''+accent+''';
    image: url(:/ToggleSwitch/img dark/ToggleSwitchOn.png);
    padding-left: 25px;
    padding-right: 0px;
}

#toggleSwitch::indicator:checked:hover {
    background-color: '''+accent+''';
    image: url(:/ToggleSwitch/img dark/ToggleSwitchOnHover.png);
}

#toggleSwitch::indicator:checked:pressed {
    background-color: '''+accent+''';
    width: 26px;
    padding-left: 21px;
    image: url(:/ToggleSwitch/img dark/ToggleSwitchOnPressed.png);
}

#toggleSwitch:disabled {
    color: rgb(150, 150, 150);
}

#toggleSwitch::indicator:disabled {
    border: 2px solid #646464;
    background-color: rgb(255, 255, 255, 0);
    image: url(:/ToggleSwitch/img dark/ToggleSwitchDisabled.png);
}

/*HYPERLINKBUTTON*/
#hyperlinkButton {
    color: '''+accent+''';
    font-size: 17px;
    font-family: "Segoe UI Variable Small", serif;
    border-radius: 5px;
    background-color: rgb(255, 255, 255, 0);
    border: none;
}

#hyperlinkButton:hover {
    background-color: rgb(255, 255, 255, 20);
}

#hyperlinkButton::pressed {
    background-color: rgb(255, 255, 255, 15);
    color: '''+accent+''';
}

#hyperlinkButton:disabled {
    color: rgb(150, 150, 150)
}

/*LISTVIEW*/
QListView {
    background-color: transparent;
    font-size: 17px;
    font-family: "Segoe UI Variable Small", serif;
    font-weight: 400;
    padding: 7px;
    border-radius: 10px;
    outline: 0;
}

QListView::item {
    height: 35px;
}

QListView::item:selected {
    background-color: rgb(255, 255, 255, 13);
    color: white;
    border-radius: 5px;
    padding-left: 0px;
}''')
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
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setEnabled(True)
        self.menuFile.setObjectName("menuFile")
        self.actionNew = QtWidgets.QMenu(self.menuFile)
        self.actionNew.setEnabled(True)
        self.actionNew.setStyleSheet("")
        self.actionNew.setObjectName("actionNew")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menuBar)
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
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
        self.actionNew.addAction(self.actionPlain_Text_Document)
        self.actionNew.addAction(self.actionRich_Text_Document)
        self.menuFile.addAction(self.actionNew.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
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
        self.comboBox.setItemText(7, _translate("MainWindow", "Cyan"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Orange"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Red"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Yellow"))
        self.textEdit.setHtml(_translate("MainWindow", ""))
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
        self.enablebtn.setText(_translate("MainWindow", "Enabled"))
        self.disablebtn.setText(_translate("MainWindow", "Disabled"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setTitle(_translate("MainWindow", "New"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionPlain_Text_Document.setText(_translate("MainWindow", "Project"))
        self.actionRich_Text_Document.setText(_translate("MainWindow", "Project File"))
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