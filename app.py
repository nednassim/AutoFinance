import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QGridLayout, QGroupBox
)
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtCore import Qt

class MortgageCalculator(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mortgage Calculator")
        self.setStyleSheet("background-color: #f6f4f0;")
        self.init_ui()

    def calculate(self):
        print("Calculate button clicked")

    def init_ui(self):
        main_layout = QHBoxLayout()

        # --- Left Panel ---
        left_layout = QVBoxLayout()

        # Category buttons
        category_layout = QHBoxLayout()
        for text in ["Home", "Vehicle", "Vacations"]:
            btn = QPushButton(text)
            btn.setFixedSize(100, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #5a6ff0, stop:1 #3f51b5);
                    color: white;
                    font-weight: bold;
                    border-radius: 10px;
                }
            """)
            category_layout.addWidget(btn)
        left_layout.addLayout(category_layout)

        # Input container with gradient
        input_frame = QGroupBox()
        input_frame.setStyleSheet("""
            QGroupBox {
                border: 2px solid #ccc;
                border-radius: 12px;
                padding: 12px;
                background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #ffffff, stop:1 #e3e6f3);
            }
        """)
        input_layout = QGridLayout()

        labels = [
            "Property Value", "Loan Amount", "Down Payment", "Interest Rate",
            "Loan Term", "Property Taxes", "Homeowners Insurance", "Private Mortgage Insurance (PMI)"
        ]
        self.inputs = {}
        default_values = [
            "86740", "32740", "80040", "7.77",
            "30", "2.58", "72000", "0.5"
        ]

        for i, (label, default) in enumerate(zip(labels, default_values)):
            row, col = divmod(i, 2)
            label_widget = QLabel(label)
            label_widget.setFont(QFont("", 10))

            edit = QLineEdit()
            edit.setText(default)
            edit.setStyleSheet("padding: 5px; border: 1px solid #aaa; border-radius: 6px;")
            self.inputs[label] = edit

            input_layout.addWidget(label_widget, row * 2, col)
            input_layout.addWidget(edit, row * 2 + 1, col)

        input_frame.setLayout(input_layout)
        left_layout.addWidget(input_frame)

        # Calculate button
        calc_btn = QPushButton("Calculate")
        calc_btn.setStyleSheet("background-color: #3f51b5; color: white; font-weight: bold; height: 40px;")
        calc_btn.clicked.connect(self.calculate)
        left_layout.addWidget(calc_btn)

        # --- Right Panel ---
        right_layout = QVBoxLayout()

        self.chart = QChart()
        self.chart.setTitle("Mortgage Breakdown")
        self.series = QPieSeries()
        self.series.append("Principal", 54558.32)
        self.series.append("Tax", 8934.01)
        self.series.append("Insurance", 498.00)
        self.chart.addSeries(self.series)
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(self.chart_view.renderHints())
        right_layout.addWidget(self.chart_view, 2)

        self.summary_label = QLabel("""
    <b>Mortgage Repayment Summary</b><br>
    Mortgage Amount: $979,899.62<br>
    Loan pay-off date: Apr, 2054<br>
    Monthly Tax Paid: $225.00<br>
    Monthly Insurance: $200.00<br>
    Annual Payment: $32,653.32<br>
    Total Monthly Payment: $9,721.94
            """)
        self.summary_label.setTextFormat(Qt.TextFormat.RichText)
        self.summary_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        right_layout.addWidget(self.summary_label, 1)

        choose_bank = QPushButton("Choose Bank")
        choose_bank.setFixedWidth(120)
        choose_bank.setStyleSheet("background-color: #3f51b5; color: white; font-weight: bold;")
        right_layout.addWidget(choose_bank)
        print("Choose Bank button clicked")
        # Add panels to main layout
        main_layout.addLayout(left_layout, 3)
        main_layout.addLayout(right_layout, 2)
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load custom font
    font_path = "./fonts/AlBayan.ttf"  # Replace with your actual .ttf file path
    font_id = QFontDatabase.addApplicationFont(font_path)
    if font_id != -1:
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        app.setStyleSheet("QWidget { font-family: font_family; font-size: 10pt; }")
        print(f"Loaded font: {font_family}")

    else:
        print("Failed to load font. Falling back to default.")
        app.setFont(QFont("Helvetica Neue", 10))

   # app.setStyleSheet("QWidget { font-family: 'Helvetica Neue'; font-size: 10pt; }")

    window = MortgageCalculator()
    window.resize(500, 100)
    window.show()
    sys.exit(app.exec())
