from functools import partial
from PySide2.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QTextEdit)
from PySide2.QtPrintSupport import QPrinter, QPrintDialog
from PySide2.QtGui import QPainter, QRegion
from PySide2.QtCore import Qt, QPoint   # Add this line to import Qt
import webbrowser
import os
import subprocess

class ReportDialog(QDialog):
    def __init__(self, certificateData, parent=None):
        super(ReportDialog, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        employee = certificateData[0][0] + " " + certificateData[0][1]
        # Create and set the employee name label
        self.employeeNameLabel = QLabel(f"Certificates for {employee}")
        self.employeeNameLabel.setAlignment(Qt.AlignCenter)  # Optional: Center-align the text
        self.layout.addWidget(self.employeeNameLabel)

        # Initialize table with columns
        self.table = QTableWidget(len(certificateData), 4)  # Adjust number of columns as needed
        self.table.setHorizontalHeaderLabels(["Certificate Name", "Issue Date", "Expiration Date", "View"])
        
        # Populate table rows with certificate data
        for row, cert in enumerate(certificateData):
            self.table.setItem(row, 0, QTableWidgetItem(cert[2]))  # Assuming cert[1] is the certificate name
            self.table.setItem(row, 1, QTableWidgetItem(cert[3].strftime("%Y-%m-%d")))  # Assuming cert[3] is the issue date
            self.table.setItem(row, 2, QTableWidgetItem(cert[4].strftime("%Y-%m-%d")))  # Assuming cert[4] is the expiration date
            view_btn = QPushButton('View')
            # Using partial to handle the file path
            view_btn.clicked.connect(partial(self.view_certificate, cert[5]))  # Assuming cert[5] is the file path

            self.table.setCellWidget(row, 3, view_btn)

        self.layout.addWidget(self.table)

        # Add Print Button
        self.printButton = QPushButton("Print Table")
        self.layout.addWidget(self.printButton)
        self.printButton.clicked.connect(self.printReport)
        

    
    def view_certificate(self, file_path):
        if os.path.exists(file_path):
            # For Windows
            os.startfile(file_path)
            # For macOS: subprocess.call(('open', file_path))
            # For Linux: subprocess.call(('xdg-open', file_path))
        else:
            print("File does not exist:", file_path)

    def printReport(self):

        printer = QPrinter(QPrinter.HighResolution)
        printer.setPageSize(QPrinter.A4)
        printer.setOrientation(QPrinter.Portrait)
        
        printDialog = QPrintDialog(printer, self)
        
        if printDialog.exec_() == QPrintDialog.Accepted:
            painter = QPainter(printer)
            offset = 200  # Start offset for printing
            line_height = 120  # Adjust based on your needs
          
            # Print title
            painter.drawText(QPoint(100, offset), "Certificates for Employee")
            offset += line_height
           
            # Print column headers
            painter.drawText(QPoint(100, offset), "Certificate Name")
            painter.drawText(QPoint(300, offset), "Issue Date")
            painter.drawText(QPoint(500, offset), "Expiration Date")
            offset += line_height

            # Iterate through table rows and print each cell
            for row in range(self.table.rowCount()):
                painter.drawText(QPoint(100, offset), self.table.item(row, 0).text())
                painter.drawText(QPoint(300, offset), self.table.item(row, 1).text())
                painter.drawText(QPoint(500, offset), self.table.item(row, 2).text())
                offset += line_height

            painter.end()
    # def printSecondaryWindow(self):
    #     # Step 1: Setup the Printer
        
    #     printer = QPrinter(QPrinter.HighResolution)
    #     printer.setPageSize(QPrinter.A4)  # Example: set to A4 size
    #     printer.setOrientation(QPrinter.Portrait)  # Set orientation
       
    #     # Step 2: Show Print Dialog
    #     printDialog = QPrintDialog(printer)

    #     if printDialog.exec_() == QPrintDialog.Accepted:
    #         # Step 3: Render the Window to the Printer
    #         painter = QPainter(printer)
    #         self.render(painter, QPoint(), QRegion(self.rect()), QWidget.DrawChildren)
    #         painter.end()
        # if printDialog.exec_() == QPrintDialog.Accepted:
        #     painter = QPainter(printer)
        #     painter.drawText(100, 100, "Hello, world!")
        #     painter.end()
        # def printTable(self):
        #     printer = QPrinter(QPrinter.HighResolution)
        #     dialog = QPrintDialog(printer, self)

        #     if dialog.exec_() == QPrintDialog.Accepted:
        #         painter = QPainter(printer)
        #         # Start the painter
        #         painter.begin(printer)
        #         # Render the table specifically
        #         self.table.render(painter)
        #         # End the painter
        #         painter.end()