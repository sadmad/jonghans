import sys
import os
import shutil
import psycopg2
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QFont, QScreen, QRegExpValidator
from ui_main import Ui_MainWindow
from PySide2.QtCore import QRegExp, QDate  # Use PyQt5.QtCore if you're using PyQt5
from newMitarbeiterValidator import *




# Validator's regex variables
emailValidatorReg = r"^\S+@\S+\.\S+$"
nameValidatorReg = r"^[a-zA-ZäöüÄÖÜß]{3}(?:[a-zA-ZäöüÄÖÜß]*)(?:[,.-]?[a-zA-ZäöüÄÖÜß ]{2,})?$"
trainingNameValidReg = r"^[a-zA-ZäöüÄÖÜß0-9]{3}(?:[a-zA-ZäöüÄÖÜß0-9]*)(?:[,.-]?[a-zA-ZäöüÄÖÜß0-9 ]{2,})?$"
onlyNumValidation = r"^[0-9]{1,2}$"

# DB Connection
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname="shulung", 
            user="postgres", 
            password="123123", 
            host="localhost"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

class MainWindow(QMainWindow):
    
    # Input is valid: Apply a style for valid input, e.g., border color green
    correct = "QLineEdit { border: 2px solid rgb(34, 139, 34); background-color: rgb(220, 245, 220);}"
    # Input is invalid: Apply a style for invalid input, e.g., border color red
    incorrect = "QLineEdit { border: 2px solid rgb(205, 92, 92); background-color:  rgb(250, 220, 220)}"

 
    # Populate the new employee tab'd fields 
    def populateEmployeeFields(self):
        self.employee_id = self.ui.comboBoxEditEmployee.currentData()  # Retrieve the stored employee ID
        conn = connect_to_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                # Fetch the data for the selected employee
                cursor.execute("SELECT f_name, l_name, email, hire_date, position_title FROM employees WHERE e_id = %s", (self.employee_id,))
                employee_data = cursor.fetchone()
                if employee_data:
                    f_name, l_name, email, hire_date, position_title = employee_data
                    # Populate the input fields with the employee's data
                    self.ui.newEmployeeName.setText(f_name)
                    self.ui.newEmployeeLastname.setText(l_name)
                    self.ui.newEmployeeEmail.setText(email)
                    self.ui.newEmployeePosition.setText(position_title)
                    # You may also want to handle the hire_date field if necessary
                    self.ui.dateEditNeuenMitarbeiter.setDate(QDate(hire_date.year, hire_date.month, hire_date.day))
            except Exception as e:
                print(f"Error fetching employee details: {e}")
            finally:
                cursor.close()
                conn.close()
            
        else:
            print("Failed to connect to the database")

    # Populate fields of tab dokumente
    def populateCerEmpfields(self):
        id = self.ui.comboBoxEditCertificate.currentData() # Rrtrive the stored list of ids cer_id
        conn = connect_to_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                query = """
                        SELECT certificate.*, employees.e_id, employees.f_name, employees.l_name, schulung.s_id, schulung.s_name
                        FROM certificate
                        JOIN employees ON certificate.e_id = employees.e_id
                        JOIN schulung ON certificate.s_id = schulung.s_id
                        WHERE certificate.c_id = %s;
                        """
                cursor.execute(query, (id,))
                certifucateData = cursor.fetchall()

                if certifucateData:
                    # Assuming certificateData[0] contains the data tuple
                    data = certifucateData[0]
                    print(data)
                    # Example of setting data to UI elements
                    # Set employee name combining first name and last name
                    self.ui.comboBoxEmpCertificateTab.setCurrentText(f"{data[7]} {data[8]}") # Adjust the index based on your data
                    # Set training name
                    self.ui.comboBoxTrainingCertificateTab.setCurrentText(data[10]) # Adjust the index based on your data
                    # Set dates (assuming your UI has a method to set date from a QDate)
                    self.ui.dateCertificateTab.setDate(data[3]) # Adjust method to set QDate
                    self.ui.expierDateCertificateTab.setDate(data[4]) # Adjust method to set QDate
                    # For setting the file name, you'll need to handle it based on how you manage file selection
                    self.certificateAddress = data[5]
           

            except Exception as e:
                print(f"Error fetching certificate details: {e}")
            finally:
                cursor.close()
                conn.close()
            self.document = id
        else:
            print("Failed to connect to the database")    


    # Populate the new Training tab's fields
    def populateTrainingFields(self):
        self.schul_id = self.ui.comboBoxEditTraining.currentData()  # Retrieve the stored employee ID
        conn = connect_to_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                # Fetch the data for the selected employee
                cursor.execute("SELECT s_name, duration, description  FROM schulung WHERE s_id = %s", (self.schul_id,))
                training_data = cursor.fetchone()
                if training_data:
                    s_name, duration, description = training_data
                    # Populate the input fields with the employee's data
                    self.ui.newTrainingName.setText(s_name)
                    self.ui.newTrainingDuration.setText(str(duration))
                    self.ui.newTrainingDescription.setText(description)

            except Exception as e:
                print(f"Error fetching employee details: {e}")
            finally:
                cursor.close()
                conn.close()
            
        else:
            print("Failed to connect to the database")
    # New employee button activation---------------------
    def checkAllValidations(self):
        # Assume all fields have validators and use hasAcceptableInput to check validity
        isValid = (
            self.ui.newEmployeeName.hasAcceptableInput() and self.ui.newEmployeeName.text().strip() != "" and
            self.ui.newEmployeeLastname.hasAcceptableInput() and self.ui.newEmployeeLastname.text().strip() != "" and
            self.ui.newEmployeeEmail.hasAcceptableInput() and self.ui.newEmployeeEmail.text().strip() != "" and
            self.ui.newEmployeePosition.hasAcceptableInput() and self.ui.newEmployeePosition.text().strip() != ""
        )
        
        self.ui.bStoreNewEmployee.setEnabled(isValid)  # Enable/disable based on validity

    # Unified Field Update validation new employee
    def updateFieldValidationFeedback(self, inputField):
        self.checkAllValidations()
        if  inputField.hasAcceptableInput():
            inputField.setStyleSheet(self.correct)
        else:
            # Input is invalid: Apply a style for invalid input, e.g., border color red
            inputField.setStyleSheet(self.incorrect)



    # New training button activation---------------------
    def checkAllValidationsT(self):
        # Assume all fields have validators and use hasAcceptableInput to check validity
        isValid = (
            self.ui.newTrainingName.hasAcceptableInput() and self.ui.newTrainingName.text().strip() != "" and
            self.ui.newTrainingDuration.hasAcceptableInput() and self.ui.newTrainingDuration.text().strip() != ""
        )

        self.ui.bNewTrainingStore.setEnabled(isValid)  # Enable/disable based on validity


    # Unified Feild Update Validation Training
    def updateFieldValidationFeedbackT(self, inputField):
        self.checkAllValidationsT()
        if  inputField.hasAcceptableInput():
            inputField.setStyleSheet(self.correct)
        else:
            # Input is invalid: Apply a style for invalid input, e.g., border color red
            inputField.setStyleSheet(self.incorrect)


    # File Address certifilates tab
    def getTheFileAddress(self):
        try:
            options = QFileDialog.Options()
            # Correct usage of QFileDialog to open a file dialog
            self.fileName, _ = QFileDialog.getOpenFileName(self, "Zertifikatsdatei auswählen", "",
                                                  "PDF Files (*.pdf);;Image Files (*.jpg *.jpeg *.png)", options=options)
            
        except Exception as e:
            print(self.fileName)
    
    # Link the emp and certifikate and store the certificate file in the folder
    def storeEmpCertificate(self):
        eId = self.ui.comboBoxEmpCertificateTab.currentData() 
        sId = self.ui.comboBoxTrainingCertificateTab.currentData()
        dateOfIssue = self.ui.dateCertificateTab.date().toPython()
        expiration = self.ui.expierDateCertificateTab.date().toPython()
        # Extract employee name from the form
        employee_name = self.ui.comboBoxEmpCertificateTab.currentText()
       
        if self.fileName is not None:
            # Check if the file is updated we need to delete the old file
            if self.certificateAddress is not None:
                # Check if the file exists before attempting to delete
                if os.path.exists(self.certificateAddress):
                    try:
                        os.remove(self.certificateAddress)
                        print("Old certificate file deleted successfully.")
                    except Exception as e:
                        print(f"Error deleting the old certificate file: {e}")
                else:
                    print("Old certificate file does not exist.")

            # Define the directory path based on the employee's name
            directory_path = os.path.join('Dokumente', employee_name)
            # Create the directory if it does not exist
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
            # Copy the file to the new directory
            shutil.copy(self.fileName, directory_path)
            # Generate the full path of the new file
            new_file_path = os.path.join(directory_path, os.path.basename(self.fileName))
        else:
            new_file_path = self.certificateAddress
        conn = connect_to_db()
        if conn is not None:
            cursor = conn.cursor()
            if self.document is None:
                try:
                    
                    query = """
                            INSERT INTO certificate (e_id, s_id, date_of_issue, date_of_expiration, certificate_image_path)VALUES(%s, %s, %s, %s, %s)
                            """
                    cursor.execute(query, (eId, sId, dateOfIssue, expiration, new_file_path ))
                    conn.commit()
        
                    # Display  a success message in the message box
                    self.ui.updateSuccessMsg.exec_()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
                except Exception as e:
                    print(f"Error storing the certificate for the employee data: {e}")
                    conn.rollback()
                finally:
                    cursor.close()
                    conn.close()
            else:
                try:
                   
                    cursor.execute("UPDATE certificate SET e_id = %s, s_id = %s, date_of_issue = %s, date_of_expiration = %s, certificate_image_path=%s WHERE c_id = %s", (eId, sId, dateOfIssue, expiration, new_file_path, self.document))
                    conn.commit()
                    # Display  a success message in the message box
                    self.ui.updateSuccessMsg.exec_() 
                except Exception as e:
                    print(f"Error updating the certificate for the employee data: {e}")
                    conn.rollback()
                finally:
                    cursor.close()
                    conn.close()

        else:
            print("Failed to connect to the database")

    # # Update employee in DB
    # def updateEmployeeData(self):
    #     employee_id = self.ui.comboBoxEditEmployee.currentData()
    #     f_name = self.ui.newEmployeeName.text()
    #     l_name = self.ui.newEmployeeLastname.text()
    #     email = self.ui.newEmployeeEmail.text()
    #     position = self.ui.newEmployeePosition.text()
    #     # Assume you have a dateEdit widget for the hire_date
    #     # hire_date = self.ui.dateEditNeuenMitarbeiter.date().toPython()
        
    #     conn = connect_to_db()
    #     if conn is not None:
    #         try:
    #             cursor = conn.cursor()
    #             cursor.execute("UPDATE employees SET f_name = %s, l_name = %s, email = %s, position_title = %s WHERE e_id = %s",
    #                         (f_name, l_name, email, position, employee_id))
    #             conn.commit()
    #             print("Employee data updated successfully")
    #         except Exception as e:
    #             print(f"Error updating employee data: {e}")
    #             conn.rollback()
    #         finally:
    #             cursor.close()
    #             conn.close()
    #     else:
    #         print("Failed to connect to the database")



    def __init__(self):
        super(MainWindow, self).__init__()  # Use super() for initialization
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.centralwidget)  # Set the central widget
        self.setWindowIcon(QIcon("qt-design\logo.png"))
        self.setWindowTitle("Junghans")
        
        self.employee_id = None  # Initialize employee_id
        self.schul_id = None # Initialize t_id
        self.fileName = None 
        self.document = None
        self.certificateAddress = None
        # Initial check to set the correct state of the button when the app starts
        self.checkAllValidations()

        #---------------------------------
        #call the email validation new employee
        self.ui.newEmployeeEmail.textChanged.connect(lambda: self.updateFieldValidationFeedback(self.ui.newEmployeeEmail))
        mainValidator(self.ui.newEmployeeEmail, emailValidatorReg)

        #name
        self.ui.newEmployeeName.textChanged.connect(lambda: self.updateFieldValidationFeedback(self.ui.newEmployeeName))
        mainValidator(self.ui.newEmployeeName, nameValidatorReg)

        #lastname
        self.ui.newEmployeeLastname.textChanged.connect(lambda: self.updateFieldValidationFeedback(self.ui.newEmployeeLastname))
        mainValidator(self.ui.newEmployeeLastname, nameValidatorReg)

        #Stelle
        self.ui.newEmployeePosition.textChanged.connect(lambda: self.updateFieldValidationFeedback(self.ui.newEmployeePosition))
        mainValidator(self.ui.newEmployeePosition, nameValidatorReg)
        #---------------------------------
        



        # New training tab validation
        #=---------------------------
        self.checkAllValidationsT()
        # Name
        self.ui.newTrainingName.textChanged.connect(lambda: self.updateFieldValidationFeedbackT(self.ui.newTrainingName))
        mainValidator(self.ui.newTrainingName, trainingNameValidReg)
        self.ui.newTrainingDuration.textChanged.connect(lambda: self.updateFieldValidationFeedbackT(self.ui.newTrainingDuration))
        mainValidator(self.ui.newTrainingDuration, onlyNumValidation)
        #----------------------------
        
        #submit new employee to store
        self.ui.bStoreNewEmployee.clicked.connect(self.StoringNewEmployee)
        
        # Populate the comboBoxEditEmployee
        self.populateComboBoxEmp()
        self.ui.bEditEmployee.clicked.connect(self.populateEmployeeFields)

        # Populate the comboboxTraining
        self.populateComboBoxTraining()
        self.ui.bEditTraining.clicked.connect(self.populateTrainingFields)

        # Submit New Training 
        self.ui.bNewTrainingStore.clicked.connect(self.StoringNewTraining)

        # Get the file address
        self.ui.bCertificateImage.clicked.connect(self.getTheFileAddress)
        # Store the employee's training
        self.ui.bStoreEmpCerFile.clicked.connect(self.storeEmpCertificate)

        # bearbeiten on registered certificate for a employee
        self.ui.bEditCertificate.clicked.connect(self.populateCerEmpfields)


        self.populateComboBoxCertifictes()
    # End Of INIT-------------------------

        
    # New Employee Database Connecetions--------------        
    # Retrieve data from DB EMPLOYEE TABLE
    def populateComboBoxEmp(self):
        conn = connect_to_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT e_id, f_name, l_name FROM employees")  # Adjust columns as needed
                for row in cursor.fetchall():
                    e_id, f_name, l_name = row
                    self.ui.comboBoxEditEmployee.addItem(f_name +" " + l_name, e_id)
                    self.ui.comboBoxEmpCertificateTab.addItem(f_name +" " + l_name, e_id)
                    self.ui.comboBoxEmployeeMain.addItem(f_name +" " + l_name, e_id)
            except Exception as e:
                print(f"An error occurred while fetching employees: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Failed to connect to the database")  

    # Populate combobox of the frame in the the certificate(Dokumente) tab    
    def populateComboBoxCertifictes(self):
        conn=connect_to_db()

        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT c_id, e_id, s_id FROM certificate")
                for row in cursor.fetchall():
                    cer_id, emp_id, schul_id = row
                    cursor.execute("SELECT f_name, l_name From employees WHERE e_id = %s", (emp_id,))
                    emp_row = cursor.fetchone()
                    empName = f"{emp_row[0]} {emp_row[1]}"  # Assuming f_name is emp_row[0] and l_name is emp_row[1]
                    cursor.execute("SELECT s_name From schulung WHERE s_id = %s", (schul_id,))
                    schul_row = cursor.fetchone()
                    schulName = schul_row[0]  # Assuming s_name is schul_row[0]
                    self.ui.comboBoxEditCertificate.addItem(empName + " -> " + schulName, cer_id)
                    
            except Exception as e:
                print(f"An error occurred while fetching certificates: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Failed to connect to the database")

    # Get the data of employee from the fields and store or update the employee data       
    def StoringNewEmployee(self):
        Employeename = self.ui.newEmployeeName.text() 
        lastname = self.ui.newEmployeeLastname.text()
        email = self.ui.newEmployeeEmail.text()
        position = self.ui.newEmployeePosition.text()
        hairingDate = self.ui.dateEditNeuenMitarbeiter.date().toPython()
        
        conn = connect_to_db()
        if self.employee_id is not None:
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE employees SET f_name = %s, l_name = %s, email = %s, position_title = %s, hire_date = %s WHERE e_id = %s",
                                (Employeename, lastname, email, position, hairingDate, self.employee_id))
                    conn.commit()
                    
    
                    # Display  a success message in the message box
                    self.ui.updateSuccessMsg.exec_()
                    print("Employee data updated successfully")
                except Exception as e:
                    print(f"Error updating employee data: {e}")
                    conn.rollback()
                finally:
                    cursor.close()
                    conn.close()
            else:
                 ("Failed to connect to the database")
        else:
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    query = """
                    INSERT INTO employees (f_name, l_name, email, hire_date, position_title)
                    VALUES (%s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (Employeename, lastname, email, hairingDate, position))
                    conn.commit()  # Commit the transaction
                    # Display  a success message in the message box
                    self.ui.updateSuccessMsg.exec_()
                except Exception as e:
                    print(f"An error occurred: {e}")
                    conn.rollback()  # Rollback in case of error
                finally:
                    cursor.close()
                    conn.close()
            else:
                print("Failed to connect to the database")
        
        #self.insertNewEmployeeDataIntoDatabase(Employeename, lastname, email, position, hairingDate)
        #self.populateComboBox()
    

    #------------------------
                
    # Retrieve data from DB table training
    def populateComboBoxTraining(self):
        conn = connect_to_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT s_id, s_name FROM schulung")  # Adjust columns as needed
                for row in cursor.fetchall():
                    s_id, s_name = row
                    self.ui.comboBoxEditTraining.addItem(s_name, s_id)
                    self.ui.comboBoxTrainingCertificateTab.addItem(s_name, s_id)
            except Exception as e:
                print(f"An error occurred while fetching employees: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Failed to connect to the database")  
        
    # Get The Data From the training Tab
    def StoringNewTraining(self):
        training = self.ui.newTrainingName.text()
        duration = self.ui.newTrainingDuration.text()
        description = self.ui.newTrainingDescription.text()

        conn = connect_to_db()
        if self.schul_id is None:
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    query = """
                            INSERT INTO schulung (s_name, duration, description)VALUES(%s, %s, %s)
                            """
                    cursor.execute(query, ( training, duration, description))
                    conn.commit()
                    # Display  a success message in the message box
                    self.ui.updateSuccessMsg.exec_()
                except Exception as e:
                    print(f"An error occurred: {e}")
                    conn.rollback()  # Rollback in case of error
                finally:
                    cursor.close()
                    conn.close()
            else:
                print("Failed to connect to the database")
        else:
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    query = "UPDATE schulung SET s_name=%s, duration=%s, description=%s WHERE s_id =%s"
                    cursor.execute(query, (training, duration, description, self.schul_id))
                    conn.commit()
                    # Display  a success message in the message box
                    self.ui.updateSuccessMsg.exec_()
                except Exception as e:
                    print(f"An error occurred: {e}")
                    conn.rollback()  # Rollback in case of error
                finally:
                    cursor.close()
                    conn.close()
            else:
                print("Failed to connect to the database")
        # Display  a success message in the message box


    # New Training Database Connections
    def insertNewTraininDataIntoDatabase(self, training, duration, description):
        pass

    #----------------------------------



# Change the font size---------------------
def calculate_tab_font_size(screen_width, screen_height):
    # Example logic for calculating font size based on screen dimensions
    base_width = 1750  # Reference screen width
    base_font_size = 8  # Base font size for tabs at the reference resolution
    scaling_factor = screen_width / base_width
    print(screen_width,scaling_factor)
    return int(base_font_size * scaling_factor)
    
def adjust_tab_font_size(tab_widget, font_size):
    font = QFont()
    font.setPointSize(font_size)
    tab_widget.setFont(font)

def adjust_label_font_size(widget, font_size):
    font = QFont()
    font.setPointSize(font_size)
    if isinstance(widget, QLabel):
        widget.setFont(font)
    for child in widget.findChildren(QLabel):
        child.setFont(font)
#--------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Pass sys.argv

    screen = app.primaryScreen()
    size = screen.size()
    print("this is the screen size: ",size)
    new_font_size = calculate_tab_font_size(size.width(), size.height())  # Define this function based on previous examples
    # Assuming mainWindow is your main window instance, adjust its labels and tabs
    
    mainWindow = MainWindow()  # This is where you initialize your main window
    adjust_label_font_size(mainWindow, new_font_size)  # Adjust labels
    adjust_tab_font_size(mainWindow.ui.tabWidget, new_font_size)


    global_font = QFont("Century Gothic", 9)
    app.setFont(global_font)
    mainWindow.show()
    

    sys.exit(app.exec_())  # Use sys.exit() for clean exit
