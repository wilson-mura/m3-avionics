# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/toad_gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 426)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 723, 337))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_2 = toad_frame_1(self.scrollAreaWidgetContents)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame_5 = toad_frame_3(self.scrollAreaWidgetContents)
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)
        self.frame = toad_frame_master(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 2, 1)
        self.frame_6 = toad_frame_4(self.scrollAreaWidgetContents)
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout.addWidget(self.frame_6, 1, 2, 1, 1)
        self.frame_4 = toad_frame_5(self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout.addWidget(self.frame_4, 1, 3, 1, 1)
        self.frame_3 = toad_frame_2(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.gridLayout.addWidget(self.frame_3, 0, 2, 1, 1)
        self.frame_dart_location = QtGui.QFrame(self.scrollAreaWidgetContents)
        self.frame_dart_location.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_dart_location.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_dart_location.setObjectName(_fromUtf8("frame_dart_location"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_dart_location)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_dart_position = QtGui.QLabel(self.frame_dart_location)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_dart_position.setFont(font)
        self.label_dart_position.setObjectName(_fromUtf8("label_dart_position"))
        self.verticalLayout_3.addWidget(self.label_dart_position)
        self.formWidget_2 = QtGui.QWidget(self.frame_dart_location)
        self.formWidget_2.setObjectName(_fromUtf8("formWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.formWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.formWidget_2)
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.formWidget_2)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.lcdNumber = QtGui.QLCDNumber(self.formWidget_2)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.gridLayout_2.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.altitudeLabel = QtGui.QLabel(self.formWidget_2)
        self.altitudeLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.altitudeLabel.setObjectName(_fromUtf8("altitudeLabel"))
        self.gridLayout_2.addWidget(self.altitudeLabel, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.formWidget_2)
        self.label_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.formWidget_2)
        self.label_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.formWidget_2)
        self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 2, 1, 1)
        self.lcdNumber_2 = QtGui.QLCDNumber(self.formWidget_2)
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.gridLayout_2.addWidget(self.lcdNumber_2, 1, 1, 1, 1)
        self.lcdNumber_3 = QtGui.QLCDNumber(self.formWidget_2)
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))
        self.gridLayout_2.addWidget(self.lcdNumber_3, 2, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.formWidget_2)
        self.scrollArea_2 = QtGui.QScrollArea(self.frame_dart_location)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 619, 310))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.latitudeLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.latitudeLabel.setObjectName(_fromUtf8("latitudeLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.latitudeLabel)
        self.latitudeLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.latitudeLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.latitudeLineEdit.setReadOnly(True)
        self.latitudeLineEdit.setObjectName(_fromUtf8("latitudeLineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.latitudeLineEdit)
        self.longitudeLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.longitudeLabel.setObjectName(_fromUtf8("longitudeLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.longitudeLabel)
        self.longitudeLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.longitudeLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.longitudeLineEdit.setReadOnly(True)
        self.longitudeLineEdit.setObjectName(_fromUtf8("longitudeLineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.longitudeLineEdit)
        self.line = QtGui.QFrame(self.scrollAreaWidgetContents_2)
        self.line.setMaximumSize(QtCore.QSize(500, 16777215))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.line)
        self.label_displacement = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_displacement.setFont(font)
        self.label_displacement.setObjectName(_fromUtf8("label_displacement"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.label_displacement)
        self.dxLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.dxLabel.setObjectName(_fromUtf8("dxLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.dxLabel)
        self.dxLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.dxLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dxLineEdit.setReadOnly(True)
        self.dxLineEdit.setObjectName(_fromUtf8("dxLineEdit"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.dxLineEdit)
        self.dyLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.dyLabel.setObjectName(_fromUtf8("dyLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.dyLabel)
        self.dyLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.dyLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dyLineEdit.setReadOnly(True)
        self.dyLineEdit.setObjectName(_fromUtf8("dyLineEdit"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dyLineEdit)
        self.dzLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.dzLabel.setObjectName(_fromUtf8("dzLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.dzLabel)
        self.dzLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.dzLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dzLineEdit.setReadOnly(True)
        self.dzLineEdit.setObjectName(_fromUtf8("dzLineEdit"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.dzLineEdit)
        self.dxDtLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.dxDtLabel.setObjectName(_fromUtf8("dxDtLabel"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.dxDtLabel)
        self.dxDtLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.dxDtLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dxDtLineEdit.setReadOnly(True)
        self.dxDtLineEdit.setObjectName(_fromUtf8("dxDtLineEdit"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.dxDtLineEdit)
        self.dyDtLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.dyDtLabel.setObjectName(_fromUtf8("dyDtLabel"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.dyDtLabel)
        self.dyDtLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.dyDtLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dyDtLineEdit.setReadOnly(True)
        self.dyDtLineEdit.setObjectName(_fromUtf8("dyDtLineEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.dyDtLineEdit)
        self.dzDtLabel = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.dzDtLabel.setObjectName(_fromUtf8("dzDtLabel"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.dzDtLabel)
        self.dzDtLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        self.dzDtLineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        self.dzDtLineEdit.setReadOnly(True)
        self.dzDtLineEdit.setObjectName(_fromUtf8("dzDtLineEdit"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.dzDtLineEdit)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.gridLayout.addWidget(self.frame_dart_location, 0, 3, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_menu_bar = QtGui.QMenu(self.menubar)
        self.menu_menu_bar.setObjectName(_fromUtf8("menu_menu_bar"))
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu_menu_bar.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "TOAD GCS", None))
        self.label_dart_position.setText(_translate("MainWindow", "Dart Position", None))
        self.label_2.setText(_translate("MainWindow", "Speed", None))
        self.label.setText(_translate("MainWindow", "Max alt", None))
        self.altitudeLabel.setText(_translate("MainWindow", "Altitude", None))
        self.label_3.setText(_translate("MainWindow", "m", None))
        self.label_4.setText(_translate("MainWindow", "m", None))
        self.label_5.setText(_translate("MainWindow", "m/s", None))
        self.latitudeLabel.setText(_translate("MainWindow", "Latitude", None))
        self.longitudeLabel.setText(_translate("MainWindow", "Longitude", None))
        self.label_displacement.setText(_translate("MainWindow", "Displacement from pad", None))
        self.dxLabel.setText(_translate("MainWindow", "dx", None))
        self.dyLabel.setText(_translate("MainWindow", "dy", None))
        self.dzLabel.setText(_translate("MainWindow", "dz", None))
        self.dxDtLabel.setText(_translate("MainWindow", "dx/dt", None))
        self.dyDtLabel.setText(_translate("MainWindow", "dy/dt", None))
        self.dzDtLabel.setText(_translate("MainWindow", "dz/dt", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Main", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Map", None))
        self.menu_menu_bar.setTitle(_translate("MainWindow", "(menu bar)", None))

from toad_frame_1 import toad_frame_1
from toad_frame_2 import toad_frame_2
from toad_frame_3 import toad_frame_3
from toad_frame_4 import toad_frame_4
from toad_frame_5 import toad_frame_5
from toad_frame_master import toad_frame_master

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

