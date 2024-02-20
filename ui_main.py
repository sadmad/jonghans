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
from stylesheet import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(950, 900))
   
        MainWindow.setStyleSheet("""
                                 QWidget{background-color: rgb(34, 51, 59)}
                                 
                                 """)
        
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
        #self.pushButton.setStyleSheet()
     
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 651, 641))
        self.tabWidget.setMinimumSize(QSize(0, 641))
        font = QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        #tab start
        self.haupt = QWidget()
        self.haupt.setObjectName(u"haupt")
        self.haupt.setStyleSheet(u"")
        self.tabWidget.addTab(self.haupt, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.haupt), (u"Start"))

        # Main Frame -First From the left--------------
        self.frameMain = QFrame(self.haupt)
        self.frameMain.setObjectName(u"frameMain")
        self.frameMain.setGeometry(QRect(0, 0, 651, 601))
        self.frameMain.setStyleSheet(u"background-color:  #DFF1FA;\n""\n""")
        self.frameMain.setFrameShape(QFrame.StyledPanel)
        self.frameMain.setFrameShadow(QFrame.Raised)
        # Firma Logo in fist page
        self.label_38 = QLabel(self.frameMain)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(170, 10, 321, 131))
        self.label_38.setPixmap(QPixmap(u"qt-design/1.png"))

        # First Ftame in main page-----------------
        self.frameSearchEmp = QFrame(self.frameMain)
        self.frameSearchEmp.setObjectName(u"frameSearchEmp")
        self.frameSearchEmp.setGeometry(QRect(60, 160, 531, 141))
        self.frameSearchEmp.setFrameShape(QFrame.StyledPanel)
        self.frameSearchEmp.setFrameShadow(QFrame.Raised)

        
        # The Label 
        self.labelMainEmp = QLabel(self.frameSearchEmp)
        self.labelMainEmp.setObjectName(u"labelMainEmp")
        self.labelMainEmp.setGeometry(QRect(30, 20, 270, 20))
        self.labelMainEmp.setText("Zertifikatsübersicht für Mitarbeiter")
        self.labelMainEmp.setStyleSheet(u"color: rgb(34, 51, 59);\n""background-color: #DFF1FA")

        self.comboBoxEmployeeMain = QComboBox(self.frameSearchEmp)
        self.comboBoxEmployeeMain.setObjectName(u"comboBoxEmployeeMain")
        self.comboBoxEmployeeMain.setGeometry(QRect(30, 55, 221, 31))
        self.comboBoxEmployeeMain.setStyleSheet(combo)

        # Button search elployee's certificate
        self.bSearchEmployeeCertificate = QPushButton(self.frameSearchEmp)
        self.bSearchEmployeeCertificate.setObjectName(u"bSearchEmployeeCertificate")
        self.bSearchEmployeeCertificate.setGeometry(QRect(330, 50, 151, 41))
        self.bSearchEmployeeCertificate.setCursor(Qt.PointingHandCursor)
        self.bSearchEmployeeCertificate.setStyleSheet(stylesheets)

        self.labelMainEmp.raise_()
        self.comboBoxEmployeeMain.raise_()
        self.bSearchEmployeeCertificate.raise_()
        # First Frame-----------------

        # Second Frame---------------
        self.frameSearchExCertificate = QFrame(self.frameMain)
        self.frameSearchExCertificate.setObjectName(u"frameSearchExCertificate")
        self.frameSearchExCertificate.setGeometry(QRect(60, 320, 531, 141))
        self.frameSearchExCertificate.setFrameShape(QFrame.StyledPanel)
        self.frameSearchExCertificate.setFrameShadow(QFrame.Raised)

        # Button Search Excertificate
        self.bSearchExCertificateByDate = QPushButton(self.frameSearchExCertificate)
        self.bSearchExCertificateByDate.setObjectName(u"bSearchExCertificateByDate")
        self.bSearchExCertificateByDate.setGeometry(QRect(330, 50, 151, 41))
        self.bSearchExCertificateByDate.setCursor(Qt.PointingHandCursor)
        self.bSearchExCertificateByDate.setStyleSheet(stylesheets)
        
        self.labelSuchenExCer = QLabel(self.frameSearchExCertificate)
        self.labelSuchenExCer.setObjectName(u"labelSuchenExCer")
        self.labelSuchenExCer.setGeometry(QRect(30, 20, 441, 20))
        self.labelSuchenExCer.setText("Ablaufende Zertifikate im Zeitraum finden")
        self.labelSuchenExCer.setStyleSheet(u"color: rgb(34, 51, 59);\n""background-color: #DFF1FA")

        self.dateExpireCertificateSearch = QDateEdit(self.frameSearchExCertificate, calendarPopup=True)
        self.dateExpireCertificateSearch.setObjectName(u"dateExpireCertificateSearch")
        self.dateExpireCertificateSearch.setDate(QDate.currentDate())
        self.dateExpireCertificateSearch.setGeometry(QRect(30, 55, 231, 31))
        self.dateExpireCertificateSearch.setDisplayFormat("dd MMM yyyy") 
        self.dateExpireCertificateSearch.setStyleSheet(cal)

       
        self.add_new_certificate = QWidget()
        self.add_new_certificate.setObjectName(u"add_new_certificate")
        self.add_new_certificate.setLocale(QLocale(QLocale.German, QLocale.Germany))
        self.label = QLabel(self.add_new_certificate)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 45, 71, 21))
        self.label.setStyleSheet("color: rgb(34, 51, 59);")
        self.labelNachname = QLabel(self.add_new_certificate)
        self.labelNachname.setObjectName(u"labelNachname")
        self.labelNachname.setGeometry(QRect(360, 45, 91, 21))
        self.labelNachname.setStyleSheet("color: rgb(34, 51, 59);")
        self.labelAbteilung = QLabel(self.add_new_certificate)
        self.labelAbteilung.setObjectName(u"labelAbteilung")
        self.labelAbteilung.setGeometry(QRect(360, 135, 100, 21))
        self.labelAbteilung.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.labelEMail = QLabel(self.add_new_certificate)
        self.labelEMail.setObjectName(u"labelEMail")
        self.labelEMail.setGeometry(QRect(40, 135, 71, 21))
        self.labelEMail.setStyleSheet("color: rgb(34, 51, 59);")
        self.labelEintrittsdatum = QLabel(self.add_new_certificate)
        self.labelEintrittsdatum.setObjectName(u"labelEintrittsdatum")
        self.labelEintrittsdatum.setGeometry(QRect(40, 255, 170, 20))
        self.labelEintrittsdatum.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.labelEintrittsdatum.setText("Eintrittsdatum")
        
        # The fields of the new employee
        #-------------------------------------------------------
        self.newEmployeeName = QLineEdit(self.add_new_certificate)
        self.newEmployeeName.setObjectName(u"newEmployeeName")
        self.newEmployeeName.setGeometry(QRect(40, 70, 241, 41))
        self.newEmployeeName.setStyleSheet(u"border-style: solid;\n"
                "border-width: 1px;\n"
                "border-color: rgb(175, 221, 244);\n"
                "\n"
                "background-color: rgb(255, 255, 255);\n""")
        
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

        # Button edit Employee
        self.bEditEmployee = QPushButton(self.frame_14)
        self.bEditEmployee.setObjectName(u"bEditEmployee")
        self.bEditEmployee.setGeometry(QRect(340, 50, 151, 41))
        self.bEditEmployee.setCursor(Qt.PointingHandCursor)
        self.bEditEmployee.setStyleSheet(stylesheets)
        self.bEditEmployee.setText("Bearbeiten")

        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 20, 251, 20))
        self.label_8.setStyleSheet(u"color: rgb(34, 51, 59);\n""background-color: #DFF1FA")
        # Tab New employee edit and employee
        self.comboBoxEditEmployee = QComboBox(self.frame_14)
        self.comboBoxEditEmployee.setObjectName(u"comboBoxEditEmployee")
        self.comboBoxEditEmployee.setGeometry(QRect(10, 57, 251, 31))
        self.comboBoxEditEmployee.setStyleSheet(combo)
        
        # Meaage box after Update
        self.updateSuccessMsg = QMessageBox()
        self.updateSuccessMsg.setStyleSheet(stylesheets)
        self.updateSuccessMsg.setWindowTitle("Erfolgreich")
        self.updateSuccessMsg.setText("Die Daten wurden erfolgreich in der Datenbank gespeichert.")
        self.updateSuccessMsg.setIcon(QMessageBox.Information)
        self.updateSuccessMsg.setStandardButtons(QMessageBox.Ok)
        self.updateSuccessMsg.setWindowIcon(QIcon('qt-design\logo.png'))

        # Store data of new employee 
        self.bStoreNewEmployee = QPushButton(self.frameEmp)
        self.bStoreNewEmployee.setObjectName(u"bStoreNewEmployee")
        self.bStoreNewEmployee.setGeometry(QRect(360, 270, 241, 51))
        self.bStoreNewEmployee.setCursor(Qt.PointingHandCursor)
        self.bStoreNewEmployee.setStyleSheet(stylesheets)

        # New employee hiering date    
        self.dateEditNeuerMitarbeiter = QDateEdit(self.frameEmp, calendarPopup=True)
        self.dateEditNeuerMitarbeiter.setObjectName(u"dateEditNeuerMitarbeiter")
        self.dateEditNeuerMitarbeiter.setDate(QDate.currentDate())
        self.dateEditNeuerMitarbeiter.setGeometry(QRect(40, 278, 241, 41))
        self.dateEditNeuerMitarbeiter.setDisplayFormat("dd MMM yyyy") 
        #QLocale.setDefault(QLocale(QLocale.German, QLocale.Germany))
        self.dateEditNeuerMitarbeiter.setStyleSheet(cal)
        
        self.tabWidget.addTab(self.add_new_certificate, "")
        self.frameEmp.raise_()
        self.label.raise_()
        self.labelNachname.raise_()
        self.labelAbteilung.raise_()
        self.labelEMail.raise_()
        self.labelEintrittsdatum.raise_()
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

        # New training input -name field
        self.newTrainingName = QLineEdit(self.framNewTraining)
        self.newTrainingName.setObjectName(u"newTrainingName")
        self.newTrainingName.setGeometry(QRect(40, 70, 261, 41))
        self.newTrainingName.setStyleSheet(u"border-style: solid;\n"
                "border-width: 1px;\n"
                "border-color: rgb(175, 221, 244);\n"
                "\n"
                "background-color: rgb(255, 255, 255);\n""")
                
        # New training duration field
        self.newTrainingDuration = QLineEdit(self.framNewTraining)
        self.newTrainingDuration.setPlaceholderText("Die Tage, die das Training dauert")
        self.newTrainingDuration.setObjectName(u"newTrainingDuration")
        self.newTrainingDuration.setGeometry(QRect(350, 70, 261, 41))
        self.newTrainingDuration.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                "border-style: solid;\n"
                "border-width: 1px;\n"
                "border-color: rgb(175, 221, 244);")
        self.SchulungBezeichnung = QLabel(self.framNewTraining)
        self.SchulungBezeichnung.setObjectName(u"SchulungBezeichnung")
        self.SchulungBezeichnung.setGeometry(QRect(40, 40, 250, 21))
        self.SchulungBezeichnung.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.SchulungBezeichnung.setText("Schulung Bezeichnung")
        # Bechreibung Input
        self.BeschreibungInhalt = QLabel(self.framNewTraining)
        self.BeschreibungInhalt.setObjectName(u"BeschreibungInhalt")
        self.BeschreibungInhalt.setGeometry(QRect(40, 123, 250, 21))
        self.BeschreibungInhalt.setStyleSheet(u"color: rgb(34, 51, 59);")
        self.BeschreibungInhalt.setText("Beschreibung'/Inhalt")
        # New training Description field
        self.newTrainingDescription = QLineEdit(self.framNewTraining)
        self.newTrainingDescription.setObjectName(u"newTrainingDescription")
        self.newTrainingDescription.setGeometry(QRect(40, 150, 571, 201))
        self.newTrainingDescription.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                "border-style: solid;\n"
                "border-width: 1px;\n"
                "border-color: rgb(175, 221, 244);")
        
        # Button new training
        self.bNewTrainingStore = QPushButton(self.framNewTraining)
        self.bNewTrainingStore.setObjectName(u"bNewTrainingStore")
        self.bNewTrainingStore.setGeometry(QRect(210, 365, 221, 51))
        self.bNewTrainingStore.setCursor(Qt.PointingHandCursor)
        self.bNewTrainingStore.setStyleSheet(stylesheets)
        
        self.frameEditTraining = QFrame(self.framNewTraining)
        self.frameEditTraining.setObjectName(u"frameEditTraining")
        self.frameEditTraining.setGeometry(QRect(60, 445, 531, 141))
        self.frameEditTraining.setFrameShape(QFrame.StyledPanel)
        self.frameEditTraining.setFrameShadow(QFrame.Raised)

        # Button edit training
        self.bEditTraining = QPushButton(self.frameEditTraining)
        self.bEditTraining.setObjectName(u"bEditTraining")
        self.bEditTraining.setGeometry(QRect(320, 46, 150, 41))
        self.bEditTraining.setCursor(Qt.PointingHandCursor)
        self.bEditTraining.setStyleSheet(stylesheets)

        self.shulBearbeiten = QLabel(self.frameEditTraining)
        self.shulBearbeiten.setObjectName(u"shulBearbeiten")
        self.shulBearbeiten.setGeometry(QRect(35, 20, 251, 20))
        self.shulBearbeiten.setStyleSheet(u"color: rgb(34, 51, 59);\n""background-color: #DFF1FA")
        self.shulBearbeiten.setText("Schulung Bearbeiten")

        self.comboBoxEditTraining = QComboBox(self.frameEditTraining)
        self.comboBoxEditTraining.setObjectName(u"comboBoxEditTraining")
        self.comboBoxEditTraining.setGeometry(QRect(35, 55, 221, 31))
        self.comboBoxEditTraining.setStyleSheet(combo)

        self.tabWidget.addTab(self.add_new_person, "")

        # Tab Dokumente
        self.add_certificate = QWidget()
        self.add_certificate.setObjectName(u"add_certificate")
        self.tabWidget.addTab(self.add_certificate, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_certificate), (u"Dokumente"))
   

        self.frameCertificate = QFrame(self.add_certificate)
        self.frameCertificate.setObjectName(u"frameCertificate")
        self.frameCertificate.setGeometry(QRect(0, 0, 651, 621))
        self.frameCertificate.setStyleSheet(u"background-color:  #DFF1FA;\n""")
        self.frameCertificate.setFrameShape(QFrame.StyledPanel)
        self.frameCertificate.setFrameShadow(QFrame.Raised)

        self.comboBoxEmpCertificateTab = QComboBox(self.frameCertificate)
        self.comboBoxEmpCertificateTab.setObjectName(u"comboBoxEmpCertificateTab")
        self.comboBoxEmpCertificateTab.setGeometry(QRect(310, 80, 231, 31))
        self.comboBoxEmpCertificateTab.setStyleSheet(combo)

        self.comboBoxTrainingCertificateTab = QComboBox(self.frameCertificate)
        self.comboBoxTrainingCertificateTab.setObjectName(u"comboBoxTrainingCertificateTab")
        self.comboBoxTrainingCertificateTab.setGeometry(QRect(310, 150, 231, 31))
        self.comboBoxTrainingCertificateTab.setStyleSheet(combo)
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
        self.label_57.setGeometry(QRect(50, 345, 131, 20))
        self.label_57.setStyleSheet(u"color: rgb(34, 51, 59);\n""background-color: #DFF1FA")

        # Button upload an certificate Image
        self.bCertificateImage = QPushButton(self.frameCertificate)
        self.bCertificateImage.setObjectName(u"bCertificateImage")
        self.bCertificateImage.setGeometry(QRect(350, 330, 151, 41))
        self.bCertificateImage.setCursor(Qt.PointingHandCursor)
        self.bCertificateImage.setStyleSheet(stylesheets)

        # Button Save the certificate and connect the emplooyee and a schulung
        self.bStoreEmpCerFile = QPushButton(self.frameCertificate)
        self.bStoreEmpCerFile.setObjectName(u"bStoreEmpCerFile")
        self.bStoreEmpCerFile.setGeometry(QRect(200, 400, 250, 41))
        self.bStoreEmpCerFile.setCursor(Qt.PointingHandCursor)
        self.bStoreEmpCerFile.setStyleSheet(stylesheets)
        
        self.frame_16 = QFrame(self.frameCertificate)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(40, 448, 531, 100))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        # Button edit a liked certificate to a employee
        self.bEditCertificate = QPushButton(self.frame_16)
        self.bEditCertificate.setObjectName(u"bEditCertificate")
        self.bEditCertificate.setGeometry(QRect(380, 33, 151, 41))
        self.bEditCertificate.setCursor(Qt.PointingHandCursor)
        self.bEditCertificate.setStyleSheet(stylesheets)

        self.editDok = QLabel(self.frame_16)
        self.editDok.setObjectName(u"editDok")
        self.editDok.setGeometry(QRect(0, 10, 251, 20))
        self.editDok.setStyleSheet(u"color: rgb(34, 51, 59);\n""background-color: #DFF1FA")
        self.editDok.setText("Dokument Bearbeiten")

        self.comboBoxEditCertificate = QComboBox(self.frame_16)
        self.comboBoxEditCertificate.setObjectName(u"comboBoxEditCertificate")
        self.comboBoxEditCertificate.setGeometry(QRect(0, 40, 350, 31))
        self.comboBoxEditCertificate.setStyleSheet(combo)

        self.dateCertificateTab = QDateEdit(self.frameCertificate, calendarPopup=True)
        self.dateCertificateTab.setObjectName(u"dateCertificateTab")
        self.dateCertificateTab.setDate(QDate.currentDate())
        self.dateCertificateTab.setGeometry(QRect(310, 210, 231, 31))
        self.dateCertificateTab.setDisplayFormat("dd MMM yyyy") 
        self.dateCertificateTab.setStyleSheet(cal)

        self.expierDateCertificateTab = QDateEdit(self.frameCertificate, calendarPopup=True)
        self.expierDateCertificateTab.setObjectName(u"expierDateCertificateTab")
        self.expierDateCertificateTab.setDate(QDate.currentDate())
        self.expierDateCertificateTab.setGeometry(QRect(310, 280, 231, 31))
        self.expierDateCertificateTab.setDisplayFormat("dd MMM yyyy") 
        self.expierDateCertificateTab.setStyleSheet(cal)
        
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(150, 660, 381, 31))
        self.textEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n""border: 0\n""")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_38.setText("")
        self.bSearchEmployeeCertificate.setText(QCoreApplication.translate("MainWindow", u"Suchen", None))

        self.bSearchExCertificateByDate.setText(QCoreApplication.translate("MainWindow", u"Suchen", None))



        self.label.setText(QCoreApplication.translate("MainWindow", u"Vorname", None))
        self.labelNachname.setText(QCoreApplication.translate("MainWindow", u"Nachname", None))
        self.labelAbteilung.setText(QCoreApplication.translate("MainWindow", u"Abteilung", None))
        self.labelEMail.setText(QCoreApplication.translate("MainWindow", u"E-Mail", None))

        self.newEmployeeEmail.setText("")
        self.newEmployeeEmail.setPlaceholderText("example@domain-name.de")
        
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mitarbeiter Bearbeiten", None))
        self.bStoreNewEmployee.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_new_certificate), QCoreApplication.translate("MainWindow", u"Neuer Mitarbeiter", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Dauer", None))
        #self.label_13.setText(QCoreApplication.translate("MainWindow", u"Schulung Bezeichnung", None))
        #self.label_15.setText(QCoreApplication.translate("MainWindow", u"Beschreibung/Inhalt", None))
        self.bNewTrainingStore.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.bEditTraining.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        #self.label_9.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten Sie einen Schulung", None))


        self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_new_person), QCoreApplication.translate("MainWindow", u"Neue Schulung", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Mitarbeiter", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Schulung", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Datum", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Verfallsdatum", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Zertifikat", None))
        self.bCertificateImage.setText(QCoreApplication.translate("MainWindow", u"Bild", None))
        self.bStoreEmpCerFile.setText(QCoreApplication.translate("MainWindow", u"Speichern", None))
        self.bEditCertificate.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten", None))
        #self.label_34.setText(QCoreApplication.translate("MainWindow", u"Bearbeiten Sie eine Zertificat", None))


        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.add_certificate), QCoreApplication.translate("MainWindow", u"Dokumente", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:5.5pt; font-weight:400; font-style:normal;\">\n"
                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:6pt;\">\u00a9 Junghans Kunststoffwaren-Fabrik GmbH &amp; Co. KG</span></p></body></html>", None))
    # retranslateUi
        