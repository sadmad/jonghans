
from PySide2.QtGui import QRegExpValidator
from PySide2.QtCore import QRegExp

def mainValidator(input_field, regex):
        # Define the regular expression for an email
        emailRegExp = QRegExp(regex)

        # Create a QRegExpValidator using the defined regular expression
        emailValidator = QRegExpValidator(emailRegExp)

        # Apply the validator to the newEmployeeEmail QLineEdit
        input_field.setValidator(emailValidator)


