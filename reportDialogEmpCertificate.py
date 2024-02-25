from functools import partial
from PySide2.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QTextEdit)
from PySide2.QtPrintSupport import QPrinter, QPrintDialog
from PySide2.QtGui import QPainter, QRegion
from PySide2.QtCore import Qt, QPoint   # Add this line to import Qt
import webbrowser
import os
import subprocess
import pyfiglet
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Preformatted, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime
from reportlab.lib.units import inch, mm, cm

class ReportDialog(QDialog):
    data = None
    def __init__(self, certificatesData, parent=None):
        self.data = certificatesData
        super(ReportDialog, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        print(certificatesData)
        employee = certificatesData[0][0] + " " + certificatesData[0][1]
        # Create and set the employee name label
        self.employeeNameLabel = QLabel(f"Certificates for {employee}")
        self.employeeNameLabel.setAlignment(Qt.AlignCenter)  # Optional: Center-align the text
        self.layout.addWidget(self.employeeNameLabel)

        # Initialize table with columns
        self.table = QTableWidget(len(certificatesData), 4)  # Adjust number of columns as needed
        self.table.setHorizontalHeaderLabels(["Certificate Name", "Issue Date", "Expiration Date", "View"])
        
        # Populate table rows with certificate data
        for row, cert in enumerate(certificatesData):
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
    
    def header(canvas, doc):
        logo_path = "qt-design/1.png"
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.black)  # Set text color
        canvas.drawImage(logo_path, 40, 740, width=120, height=25, mask='auto')  # Adjust as needed
        #empName = f"Report of certificates {self.data[0][0]} {self.datap[0][1]}"
        # Make sure there's enough space between the logo and the text
        canvas.drawString(470, 755, "Schulung")  # Adjust Y coordinate so it's below the logo
        canvas.drawString(470, 742, "Berichtsdatum: " + datetime.now().strftime("%Y-%m-%d"))
        canvas.restoreState()

        
    def printReport(self):
        # Current date for the report
        current_date = datetime.now().strftime("%Y-%m-%d")
        styles = getSampleStyleSheet()
        date_paragraph = Paragraph(current_date, styles['Normal'])
        # Create PDF
        pdf_file = "report.pdf"
        title_style = styles['Heading3']
        title_style.alignment = 1       
        name_paragraph = Paragraph(f"{self.data[0][0]} {self.data[0][1]}", title_style)
        elements = [name_paragraph]

        my_spacer = Spacer(1, 10*mm)  # Width is set to 1 since it's not relevant

        # Assuming you have a list 'elements' to which you add your document's content
        elements.append(my_spacer)    
        # Prepare report data
        reportData = [['Zertifikat', 'Ausstellungsdatum', 'Ablaufdatum']] + [[row[2], row[3].strftime("%Y-%m-%d"), row[4].strftime("%Y-%m-%d")] for row in self.data]

        # Create a SimpleDocTemplate object
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)


        # Define the table style
        table_style = TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.grey),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),
            ('GRID', (0,0), (-1,-1), 1, colors.black),
        ])
        # Create the table
        table = Table(reportData, style=table_style)    
        # Elements to add to the document
        elements.append(table)
        

        doc.build(elements, onFirstPage=ReportDialog.header, onLaterPages=ReportDialog.header)
        print(f"Report saved as {pdf_file}")

        # Define potential Adobe Reader paths
        adobe_reader_paths = [
            
            "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe",

            # Add any other paths where Adobe Reader might be installed
        ]

        # Find the first existing path to Adobe Reader
        reader_path = next((path for path in adobe_reader_paths if os.path.exists(path)), None)

        if reader_path:
            try:
                # Attempt to print the PDF file using Adobe Reader
                subprocess.run([reader_path, "/p", pdf_file], check=True)
            except subprocess.SubprocessError as e:
                print(f"Error opening Adobe Reader: {e}")
        else:
            print("Adobe Reader executable not found. Please check the installation.")