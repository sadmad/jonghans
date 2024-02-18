stylesheets = """
QMessageBox { background-color: rgb(224, 239, 245); font: 8pt;}
QPushButton {
    /* Styles for enabled state */
    background-color: rgb(133, 205, 242);
    color: rgb(255, 255, 255);
    border: 1px solid #5DADE2; /* Slightly darker border for depth */
    padding: 5px;
    border-radius: 4px; /* Rounded corners */
    min-width: 6em;
}

QPushButton:hover {
    background-color: rgb(143, 215, 250);
}

QPushButton:pressed {
    /* Simulate push by darkening the color and changing padding */
    background-color: rgb(123, 195, 232); /* Darker shade for pressed state */
    padding: 4px; /* Adjust padding to simulate movement */
    border: 1px solid #3498DB;
}

QPushButton:disabled {
    background-color: #B0D4E8; /* Disabled state */
    color: #A0A0A0;  /* Darker text for disabled state */
}"""

cal = """
        QDateEdit {
                color: darkblue; /* Text color */
                height: 40px; 
        
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
                background-color: lightblue;
                color: darkblue;
        }
        QCalendarWidget { min-width: 280px; color:black} /* Set minimum width for all QCalendarWidgets */ 
        QCalendarWidget QToolButton {
                background-color: lightblue;
                color: white;
                font-size: 10pt;
                icon-size: 15px, 15px; /* Width, Height */
               
        }
        /* For the previous month button */
        QCalendarWidget QToolButton#qt_calendar_prevmonth {
            qproperty-icon: url('pre.png'); /* Not standard CSS */
        }

        /* For the next month button */
        QCalendarWidget QToolButton#qt_calendar_nextmonth {
            qproperty-icon: url('next.png'); /* Not standard CSS */
        }
        """
combo = """
QComboBox {
    border: 1px solid #5DADE2; /* Matching QPushButton border */
    padding: 1px 18px 1px 3px; /* Left padding less to compensate for arrow button */
    min-width: 5em;
    background-color: rgb(133, 205, 242); /* Matching QPushButton background */
    color: rgb(255, 255, 255); /* Matching QPushButton text color */
    border-radius: 4px; /* Matching QPushButton rounded corners */
    font: 14px bold;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px; /* Width of the drop-down button */
    border-left-color: #5DADE2; /* Slightly darker border for depth, matching QPushButton */
    border-left-style: solid;
    border-left-width: 1px; /* Matching QPushButton style */
    border-top-right-radius: 2px; /* Rounded corners for the right side */
    border-bottom-right-radius: 2px;
    background-color: rgb(133, 205, 242); /* Background to match QPushButton */

}
QComboBox:hover::drop-down {
    background-color: rgb(143, 215, 250); /* Hover effect matching QPushButton */
}
QComboBox::down-arrow:on { /* Arrow when combo box is open */
    top: 1px; /* Slight shift to simulate pressing */
}
QComboBox::down-arrow {
    image: url("icons8-expand-arrow-100.png"); /* Use a custom arrow icon that matches your design */
    width: 12px;
    height: 12px;
}

QComboBox QAbstractItemView {
    border: 2px solid #5DADE2;; /* Border for the dropdown */
    background-color:#E1F0FF; /* Matching the QDateEdit dropdown background */
    color: darkblue; /* Text color in the dropdown */
    selection-background-color: #a0d4f7; /* Highlight color when an item is selected */
    selection-color: darkblue; /* Text color for a selected item */  
}
QComboBox QAbstractScrollArea QScrollBar {
    width: 1em; /* Adjust the width of the scrollbar */
}

QComboBox QAbstractScrollArea QScrollBar:vertical {
    background: #F2F2F2; /* Background color of the scrollbar track */
}

QComboBox QAbstractScrollArea QScrollBar::handle:vertical {
    background: rgb(133, 205, 242); /* Background color of the scrollbar handle */
    min-height: 7px; /* Minimum height of the scrollbar handle */
}

QComboBox QAbstractScrollArea QScrollBar::add-line:vertical, 
QComboBox QAbstractScrollArea QScrollBar::sub-line:vertical {
    border: none;
    background: none;
    height: 0;
}

QComboBox QAbstractScrollArea QScrollBar::up-arrow:vertical, 
QComboBox QAbstractScrollArea QScrollBar::down-arrow:vertical {
    background: none;
}

QComboBox QAbstractScrollArea QScrollBar::add-page:vertical, 
QComboBox QAbstractScrollArea QScrollBar::sub-page:vertical {
    background: none;
}



"""