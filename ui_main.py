# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledWXOMnP.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 694)
        MainWindow.setStyleSheet(u"background-color: rgb(34, 51, 59);\n"
"")
       
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QTabBar::tab {\n"
"   	background-color: white;\n"
"   	border-top: 2px solid #AFDDF4;\n"
"\n"
"	border-right: 2px solid #AFDDF4;\n"
"   	border-radius: 4px;\n"
"   	padding: 5px;\n"
"   	width: 155px;     /* Adjust width as needed */\n"
"   	height: 25px;     /* Adjust height as needed */\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 10px; /* Adjust the radius as needed */\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"   background-color:#DFF1FA; /* Use your desired color */\n"
"    /* Other styling properties can also be added here if needed */\n"
"	 border-bottom:1px solid #DFF1FA;\n"
"\n"
"}\n"
"QLabel {\n"
"    background-color:  #DFF1FA; /* Replace with your desired color */\n"
"}\n"
"\n"
"")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 651, 641))
        self.tabWidget.setMinimumSize(QSize(0, 641))
        font = QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.haupt = QWidget()
        self.haupt.setObjectName(u"haupt")
        self.haupt.setStyleSheet(u"")
        self.frameMain = QFrame(self.haupt)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setGeometry(QRect(0, 0, 651, 601))
        self.frameMain.setStyleSheet(u"background-color:  #DFF1FA;\n"
"\n"
"")
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QFrame.Raised)
        self.label_38 = QLabel(self.frameMain)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(170, 10, 321, 131))
        self.label_38.setPixmap(QPixmap(u"1.png"))
        self.frameSearchEmp = QFrame(self.frameMain)
        self.frameSearchEmp.setObjectName(u"frameSearchEmp")
        self.frameSearchEmp.setGeometry(QRect(60, 160, 531, 141))
        self.frameSearchEmp.setFrameShape(QFrame.StyledPanel)
        self.frameSearchEmp.setFrameShadow(QFrame.Raised)
        self.bSearchEmployeeCertificate = QPushButton(self.frameSearchEmp)
        self.bSearchEmployeeCertificate.setObjectName(u"bSearchEmployeeCertificate")
        self.bSearchEmployeeCertificate.setGeometry(QRect(330, 50, 151, 41))
        self.bSearchEmployeeCertificate.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.label_52 = QLabel(self.frameSearchEmp)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(10, 20, 251, 20))
        self.label_52.setStyleSheet(u"color: rgb(34, 51, 59);\n"

"background-color: #DFF1FA")
        self.comboBoxEmployeeMain = QComboBox(self.frameSearchEmp)
        self.comboBoxEmployeeMain.setObjectName(u"comboBoxEmployeeMain")
        self.comboBoxEmployeeMain.setGeometry(QRect(30, 60, 221, 31))
        self.comboBoxEmployeeMain.setStyleSheet(u"background-color: rgb(224, 239, 245);")
        self.label_52.raise_()
        self.comboBoxEmployeeMain.raise_()
        self.bSearchEmployeeCertificate.raise_()
        self.frameSearchExCertificate = QFrame(self.frameMain)
        self.frameSearchExCertificate.setObjectName(u"frameSearchExCertificate")
        self.frameSearchExCertificate.setGeometry(QRect(60, 320, 531, 141))
        self.frameSearchExCertificate.setFrameShape(QFrame.StyledPanel)
        self.frameSearchExCertificate.setFrameShadow(QFrame.Raised)
        self.bSearchExCertificateByDate = QPushButton(self.frameSearchExCertificate)
        self.bSearchExCertificateByDate.setObjectName(u"bSearchExCertificateByDate")
        self.bSearchExCertificateByDate.setGeometry(QRect(330, 50, 151, 41))
        self.bSearchExCertificateByDate.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.label_58 = QLabel(self.frameSearchExCertificate)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(10, 10, 441, 20))
        self.label_58.setStyleSheet(u"color: rgb(34, 51, 59);\n"
"background-color: #DFF1FA")
        self.dateExpireCertificateSearch = QDateEdit(self.frameSearchExCertificate)
        self.dateExpireCertificateSearch.setObjectName(u"dateExpireCertificateSearch")
        self.dateExpireCertificateSearch.setGeometry(QRect(20, 60, 231, 31))
        self.dateExpireCertificateSearch.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.haupt, "")
        self.add_new_certificate = QWidget()
        self.add_new_certificate.setObjectName(u"add_new_certificate")
        self.add_new_certificate.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.label = QLabel(self.add_new_certificate)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 45, 71, 21))
        self.label.setStyleSheet(
"color: rgb(34, 51, 59);")
        self.label_2 = QLabel(self.add_new_certificate)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 45, 91, 21))
        self.label_2.setStyleSheet(
"color: rgb(34, 51, 59);")
        self.label_3 = QLabel(self.add_new_certificate)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 135, 71, 21))
        self.label_3.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.label_4 = QLabel(self.add_new_certificate)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 135, 71, 21))
        self.label_4.setStyleSheet("color: rgb(34, 51, 59);")
        self.label_5 = QLabel(self.add_new_certificate)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 255, 170, 20))
        self.label_5.setStyleSheet(u"color: rgb(34, 51, 59);")
        
        # The fields of the new employee
        #-------------------------------------------------------
        self.newEmployeeName = QLineEdit(self.add_new_certificate)
        self.newEmployeeName.setObjectName(u"newEmployeeName")
        self.newEmployeeName.setGeometry(QRect(40, 70, 241, 41))
        self.newEmployeeName.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.newEmployeeLastname = QLineEdit(self.add_new_certificate)
        self.newEmployeeLastname.setObjectName(u"newEmployeeLastname")
        self.newEmployeeLastname.setGeometry(QRect(360, 70, 241, 41))
        self.newEmployeeLastname.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);")
        self.newEmployeeEmail = QLineEdit(self.add_new_certificate)
        self.newEmployeeEmail.setObjectName(u"newEmployeeEmail")
        self.newEmployeeEmail.setGeometry(QRect(40, 160, 241, 41))
        self.newEmployeeEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);")
        self.newEmployeePosition = QLineEdit(self.add_new_certificate)
        self.newEmployeePosition.setObjectName(u"newEmployeePosition")
        self.newEmployeePosition.setGeometry(QRect(360, 160, 241, 41))
        self.newEmployeePosition.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);")
        #------------------------------------------------------------


        self.frameEmp = QFrame(self.add_new_certificate)
        self.frameEmp.setObjectName(u"frameEmp")
        self.frameEmp.setGeometry(QRect(0, 0, 651, 601))
        self.frameEmp.setStyleSheet(u"background-color: #DFF1FA")
        self.frameEmp.setFrameShape(QFrame.StyledPanel)
        self.frameEmp.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frameEmp)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(60, 360, 531, 211))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.bEditEmployee = QPushButton(self.frame_14)
        self.bEditEmployee.setObjectName(u"bEditEmployee")
        self.bEditEmployee.setGeometry(QRect(330, 50, 151, 41))
        self.bEditEmployee.setCursor(Qt.PointingHandCursor)
        self.bEditEmployee.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 20, 251, 20))
        self.label_8.setStyleSheet(u"color: rgb(34, 51, 59);\n"
"background-color: #DFF1FA")
        self.comboBoxEditEmployee = QComboBox(self.frame_14)
        self.comboBoxEditEmployee.setObjectName(u"comboBoxEditEmployee")
        self.comboBoxEditEmployee.setGeometry(QRect(40, 60, 251, 31))
        self.comboBoxEditEmployee.setStyleSheet(u"background-color: rgb(224, 239, 245);")

        # Store data of new employee 
        self.bStoreNewEmployee = QPushButton(self.frameEmp)
        self.bStoreNewEmployee.setObjectName(u"bStoreNewEmployee")
        self.bStoreNewEmployee.setGeometry(QRect(360, 270, 241, 51))
        self.bStoreNewEmployee.setCursor(Qt.PointingHandCursor)
        self.bStoreNewEmployee.setStyleSheet("""
                QPushButton {
                
                /* Styles for enabled state */
                background-color: rgb(133, 205, 242);
                color: rgb(255, 255, 255);
                }
            QPushButton:disabled {
                background-color: #B0D4E8; /* Disabled state */
                color: #A0A0A0;  /* Darker text for disabled state */
            }
""")

        # New employee hiering date    
        self.dateEditNeuenMitarbeiter = QDateEdit(self.frameEmp, calendarPopup=True)
        self.dateEditNeuenMitarbeiter.setObjectName(u"dateEditNeuenMitarbeiter")
        self.dateEditNeuenMitarbeiter.setDate(QDate.currentDate())
        self.dateEditNeuenMitarbeiter.setGeometry(QRect(40, 278, 241, 41))
        #QLocale.setDefault(QLocale(QLocale.German, QLocale.Germany))
        self.dateEditNeuenMitarbeiter.setStyleSheet("""
        QDateEdit {
                color: darkblue; /* Text color */
        
        }
        QDateEdit QAbstractItemView {
                background-color: lightblue; /* Calendar dropdown background */
                color: darkblue; /* Text color in the dropdown */
                font: 12px;
        }
        QCalendarWidget QWidget#qt_calendar_navigationbar {  
                color: red;
                                                
        }
        QCalendarWidget QWidget#qt_calendar_navigationbar QMenu, QCalendarWidget QWidget#qt_calendar_navigationbar QSpinBox {
                background-color: #152C4A;
                color: red;
        }
        QCalendarWidget { min-width: 280px; color:black} /* Set minimum width for all QCalendarWidgets */ QCalendarWidget QToolButton {
                background-color: #152C4A;
                color: black;
                font-size: 10pt;
                icon-size: 16px, 16px; /* Width, Height */
        }                
        """)
        
        self.tabWidget.addTab(self.add_new_certificate, "")
        self.frameEmp.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.newEmployeeName.raise_()
        self.newEmployeeLastname.raise_()
        self.newEmployeeEmail.raise_()
        self.newEmployeePosition.raise_()
        self.add_new_person = QWidget()
        self.add_new_person.setObjectName(u"add_new_person")
        self.add_new_person.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.pushButton_2 = QPushButton(self.add_new_person)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(320, 490, 151, 71))
        self.framNewTraining = QFrame(self.add_new_person)
        self.framNewTraining.setObjectName(u"framNewTraining")
        self.framNewTraining.setGeometry(QRect(0, 0, 651, 601))
        self.framNewTraining.setStyleSheet(u"background-color: #DFF1FA")
        self.framNewTraining.setFrameShape(QFrame.StyledPanel)
        self.framNewTraining.setFrameShadow(QFrame.Raised)
        self.label_17 = QLabel(self.framNewTraining)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(350, 40, 91, 21))
        self.label_17.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.newTrainingName = QLineEdit(self.framNewTraining)
        self.newTrainingName.setObjectName(u"newTrainingName")
        self.newTrainingName.setGeometry(QRect(40, 70, 241, 41))
        self.newTrainingName.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.newTrainingDuration = QLineEdit(self.framNewTraining)
        self.newTrainingDuration.setObjectName(u"newTrainingDuration")
        self.newTrainingDuration.setGeometry(QRect(350, 70, 261, 41))
        self.newTrainingDuration.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);")
        self.label_13 = QLabel(self.framNewTraining)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(40, 40, 71, 21))
        self.label_13.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.label_15 = QLabel(self.framNewTraining)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 120, 131, 21))
        self.label_15.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.newTrainingDescruption = QLineEdit(self.framNewTraining)
        self.newTrainingDescruption.setObjectName(u"newTrainingDescruption")
        self.newTrainingDescruption.setGeometry(QRect(40, 150, 571, 201))
        self.newTrainingDescruption.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(175, 221, 244);")
        self.bNewTrainingStore = QPushButton(self.framNewTraining)
        self.bNewTrainingStore.setObjectName(u"bNewTrainingStore")
        self.bNewTrainingStore.setGeometry(QRect(210, 360, 221, 51))
        self.bNewTrainingStore.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.frame_15 = QFrame(self.framNewTraining)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(60, 430, 531, 141))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.bEditTraining = QPushButton(self.frame_15)
        self.bEditTraining.setObjectName(u"bEditTraining")
        self.bEditTraining.setGeometry(QRect(300, 50, 151, 41))
        self.bEditTraining.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.label_9 = QLabel(self.frame_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 20, 251, 20))
        self.label_9.setStyleSheet(u"color: rgb(34, 51, 59);\n"
"background-color: #DFF1FA")
        self.comboBoxEditTraining = QComboBox(self.frame_15)
        self.comboBoxEditTraining.setObjectName(u"comboBoxEditTraining")
        self.comboBoxEditTraining.setGeometry(QRect(40, 60, 221, 31))
        self.comboBoxEditTraining.setStyleSheet(u"background-color: rgb(224, 239, 245);")
        self.tabWidget.addTab(self.add_new_person, "")
        self.add_certificate = QWidget()
        self.add_certificate.setObjectName(u"add_certificate")
        self.frameCertificate = QFrame(self.add_certificate)
        self.frameCertificate.setObjectName(u"frameCertificate")
        self.frameCertificate.setGeometry(QRect(0, 0, 651, 601))
        self.frameCertificate.setStyleSheet(u"background-color:  #DFF1FA;\n"
"")
        self.frameCertificate.setFrameShape(QFrame.StyledPanel)
        self.frameCertificate.setFrameShadow(QFrame.Raised)
        self.comboBoxEmpCertificateTab = QComboBox(self.frameCertificate)
        self.comboBoxEmpCertificateTab.setObjectName(u"comboBoxEmpCertificateTab")
        self.comboBoxEmpCertificateTab.setGeometry(QRect(310, 80, 231, 31))
        self.comboBoxEmpCertificateTab.setStyleSheet(u"background-color: rgb(224, 239, 245);")
        self.comboBoxTrainingCertificateTab = QComboBox(self.frameCertificate)
        self.comboBoxTrainingCertificateTab.setObjectName(u"comboBoxTrainingCertificateTab")
        self.comboBoxTrainingCertificateTab.setGeometry(QRect(310, 150, 231, 31))
        self.comboBoxTrainingCertificateTab.setStyleSheet(u"background-color: rgb(224, 239, 245);")
        self.label_53 = QLabel(self.frameCertificate)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(50, 90, 111, 21))
        self.label_53.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.label_54 = QLabel(self.frameCertificate)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(50, 150, 111, 21))
        self.label_54.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.label_55 = QLabel(self.frameCertificate)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(50, 210, 71, 21))
        self.label_55.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.label_56 = QLabel(self.frameCertificate)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(50, 280, 141, 21))
        self.label_56.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.label_57 = QLabel(self.frameCertificate)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setGeometry(QRect(50, 360, 131, 20))
        self.label_57.setStyleSheet(u"color: rgb(34, 51, 59);\n"
"background-color: #DFF1FA")
        self.bCertificateImage = QPushButton(self.frameCertificate)
        self.bCertificateImage.setObjectName(u"bCertificateImage")
        self.bCertificateImage.setGeometry(QRect(350, 350, 151, 41))
        self.bCertificateImage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.frame_16 = QFrame(self.frameCertificate)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(50, 420, 531, 141))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.bEditCertificate = QPushButton(self.frame_16)
        self.bEditCertificate.setObjectName(u"bEditCertificate")
        self.bEditCertificate.setGeometry(QRect(300, 50, 151, 41))
        self.bEditCertificate.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(133, 205, 242);")
        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(40, 20, 251, 20))
        self.label_34.setStyleSheet(u"color: rgb(34, 51, 59);\n"
"background-color: #DFF1FA")
        self.comboBoxEditCertificate = QComboBox(self.frame_16)
        self.comboBoxEditCertificate.setObjectName(u"comboBoxEditCertificate")
        self.comboBoxEditCertificate.setGeometry(QRect(40, 60, 221, 31))
        self.comboBoxEditCertificate.setStyleSheet(u"background-color: rgb(224, 239, 245);")
        self.dateCertificateTab = QDateEdit(self.frameCertificate)
        self.dateCertificateTab.setObjectName(u"dateCertificateTab")
        self.dateCertificateTab.setGeometry(QRect(310, 210, 231, 31))
        self.dateCertificateTab.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.expierDateCertificateTab = QDateEdit(self.frameCertificate)
        self.expierDateCertificateTab.setObjectName(u"expierDateCertificateTab")
        self.expierDateCertificateTab.setGeometry(QRect(310, 280, 231, 31))
        self.expierDateCertificateTab.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabWidget.addTab(self.add_certificate, "")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 660, 381, 31))
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_38.setText("")
        self.bSearchEmployeeCertificate.setText(QCoreApplication.translate("MainWindow", u"Suchen", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Suche nach einem Mitarbeiter", None))
        self.bSearchExCertificateByDate.setText(QCoreApplication.translate("MainWindow", u"Suchen", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Suchen Sie nach ablaufenden Zertifikaten", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.haupt), QCoreApplication.translate("MainWindow", u"Hauptfenster", None))


        self.label.setText(QCoreApplication.translate("MainWindow", u"Vorname", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nachname", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stelle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Anstellungsdatum", None))
        self.newEmployeeEmail.setText("")
        self.newEmployeeEmail.setPlaceholderText("example@domain-name.de")
        
        self.bEditEmployee.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten Sie einen Mitarbeiter", None))
        self.bStoreNewEmployee.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_new_certificate), QCoreApplication.translate("MainWindow", u"Neuen Mitarbeiter", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Dauer", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Beschreibung", None))
        self.bNewTrainingStore.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.bEditTraining.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten Sie einen Schulung", None))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_new_person), QCoreApplication.translate("MainWindow", u"Neue Schulung", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Mitarbeiter", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Schulung", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Datum", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Verfallsdatum", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Zertifikat", None))
        self.bCertificateImage.setText(QCoreApplication.translate("MainWindow", u"Bild", None))
        self.bEditCertificate.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten Sie eine Zertificat", None))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_certificate), QCoreApplication.translate("MainWindow", u"Zertifikat registrieren", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:5.5pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">\u00a9 Junghans Kunststoffwaren-Fabrik GmbH &amp; Co. KG</span></p></body></html>", None))
    # retranslateUi
        