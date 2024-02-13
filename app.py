import sys
import psycopg2
from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget, QLabel
from PySide2.QtGui import QIcon, QFont
from ui_main import Ui_MainWindow
from PySide2.QtGui import QRegExpValidator
from PySide2.QtCore import QRegExp
from PySide2.QtWidgets import QLineEdit
from PySide2.QtCore import QDate  # Use PyQt5.QtCore if you're using PyQt5
from newMitarbeiterValidator import *
from PySide2.QtWidgets import QMessageBox, QMainWindow
from PySide2.QtGui import QScreen

# Validator's regex variables
emailValidatorReg = r"^\S+@\S+\.\S+$"
nameValidatorReg = r"^[a-zA-ZäöüÄÖÜß]{3,}([',. -][a-zA-ZäöüÄÖÜß ]{2,})?([a-zA-ZäöüÄÖÜß]*|[',. -][a-zA-ZäöüÄÖÜß ]{2,})*$"

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
    correct = "QLineEdit { border: 2px solid green; background-color:white}"
    # Input is invalid: Apply a style for invalid input, e.g., border color red
    incorrect = "QLineEdit { border: 2px solid red; background-color:white}"

   
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

    # Unified Field Update validation
    def updateFieldValidationFeedback(self, inputField):
        self.checkAllValidations()
        if  inputField.hasAcceptableInput():
                
                 inputField.setStyleSheet(self.correct)
        else:
                # Input is invalid: Apply a style for invalid input, e.g., border color red
                 inputField.setStyleSheet(self.incorrect)


    # New employee button activation
    def checkAllValidations(self):
        # Assume all fields have validators and use hasAcceptableInput to check validity
        isValid = (
            self.ui.newEmployeeName.hasAcceptableInput() and self.ui.newEmployeeName.text().strip() != "" and
            self.ui.newEmployeeLastname.hasAcceptableInput() and self.ui.newEmployeeLastname.text().strip() != "" and
            self.ui.newEmployeeEmail.hasAcceptableInput() and self.ui.newEmployeeEmail.text().strip() != "" and
            self.ui.newEmployeePosition.hasAcceptableInput() and self.ui.newEmployeePosition.text().strip() != ""
        )
        
        self.ui.bStoreNewEmployee.setEnabled(isValid)  # Enable/disable based on validity
    
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
        self.setWindowTitle("Junghans Shulung Datenbank")


        self.employee_id = None  # Initialize employee_id

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
        
        
        #submit new employee to store
        self.ui.bStoreNewEmployee.clicked.connect(self.StoringNewEmployee)
        
        # Populate the comboBoxEditEmployee
        self.populateComboBox()

        self.ui.bEditEmployee.clicked.connect(self.populateEmployeeFields)

    # Retrieve data from DB
    def populateComboBox(self):
        conn = connect_to_db()
        if conn is not None:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT e_id, f_name, l_name FROM employees")  # Adjust columns as needed
                for row in cursor.fetchall():
                    e_id, f_name, l_name = row
                    self.ui.comboBoxEditEmployee.addItem(f_name +" " + l_name, e_id)
            except Exception as e:
                print(f"An error occurred while fetching employees: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("Failed to connect to the database")  
        

    # Get the data of new employee from the tab       
    def StoringNewEmployee(self):
        Employeename = self.ui.newEmployeeName.text() 
        lastname = self.ui.newEmployeeLastname.text()
        email = self.ui.newEmployeeEmail.text()
        position = self.ui.newEmployeePosition.text()
        hairingDate = self.ui.dateEditNeuenMitarbeiter.date().toPython()
        
        
        self.insertDataIntoDatabase(Employeename, lastname, email, position, hairingDate)
        #self.populateComboBox()
    
    # Store new employee or edit employee in DB
    def insertDataIntoDatabase(self,  Employeename, lastname, email, position, hairingDate):
        conn = connect_to_db()
        if self.employee_id is not None:
            if conn is not None:
                try:
                    cursor = conn.cursor()
                    cursor.execute("UPDATE employees SET f_name = %s, l_name = %s, email = %s, position_title = %s, hire_date = %s WHERE e_id = %s",
                                (Employeename, lastname, email, position, hairingDate, self.employee_id))
                    conn.commit()
                     # Show a success message
                    QMessageBox.information(self, "Success", "Employee data updated successfully.")
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
                except Exception as e:
                    print(f"An error occurred: {e}")
                    conn.rollback()  # Rollback in case of error
                finally:
                    cursor.close()
                    conn.close()
            else:
                print("Failed to connect to the database")


def calculate_tab_font_size(screen_width, screen_height):
    # Example logic for calculating font size based on screen dimensions
    base_width = 1700  # Reference screen width
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



    global_font = QFont("Century Gothic", 10)
    app.setFont(global_font)
    

    mainWindow.show()
    connect_to_db()

    sys.exit(app.exec_())  # Use sys.exit() for clean exit
