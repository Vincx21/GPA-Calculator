from PyQt5.QtWidgets import (
    QApplication, QWidget, QTableWidget, QTableWidgetItem, QFormLayout, QPushButton, QLabel, QMessageBox
)
from PyQt5 import QtCore

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Subject', 'Grade'])

        self.button_addline = QPushButton('Add Line')
        self.button_calculate = QPushButton('Calculate GPA')
        self.label = QLabel('Result =')
        self.label_a = QLabel('')
        self.label_a_minus = QLabel('')
        self.label_b_plus = QLabel('')
        self.label_b = QLabel('')
        self.label_b_minus = QLabel('')
        self.label_c_plus = QLabel('')
        self.label_c = QLabel('')
        self.label_d = QLabel('')
        self.label_e = QLabel('')
        self.label_total_index = QLabel('')
        self.label_total_credit = QLabel('')
        self.label_gpa = QLabel('')

        self.layout.addRow(self.button_addline)
        self.layout.addRow(self.button_calculate)
        self.layout.addRow(self.table)
        self.layout.addRow(self.label)
        self.layout.addRow(self.label_a)
        self.layout.addRow(self.label_a_minus)
        self.layout.addRow(self.label_b_plus)
        self.layout.addRow(self.label_b)
        self.layout.addRow(self.label_b_minus)
        self.layout.addRow(self.label_c_plus)
        self.layout.addRow(self.label_c)
        self.layout.addRow(self.label_d)
        self.layout.addRow(self.label_e)
        self.layout.addRow(self.label_total_index)
        self.layout.addRow(self.label_total_credit)
        self.layout.addRow(self.label_gpa)

        self.button_addline.clicked.connect(self.add_line)
        self.table.itemChanged.connect(self.change)
        self.button_calculate.clicked.connect(self.calculate)
        
    def change(self, item):
        row = item.row()
        col = item.column()
        if col == 1 and not item.text().isnumeric():
            item.setText('')
        if col == 1 and item.text().isnumeric():
            if float(item.text()) > 100.0:
                item.setText('')
            elif float(item.text()) < 0.0:
                item.setText('')

    def add_line(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        
    def calculate(self):
        total = 0.0
        index = 0.0
        credit = 3.0
        a = 0
        a_minus = 0
        b_plus = 0
        b = 0
        b_minus = 0
        c_plus = 0
        c = 0
        d = 0
        e = 0
        total_credit = self.table.rowCount() * credit
        for row in range(0, self.table.rowCount()):
            score = self.table.item(row,1)
            if float(score.text()) >= 85.0:
                index = 4.0 * credit
                total += index
                a += 1
            elif float(score.text()) >= 80.0:
                index = 3.67 * credit
                total += index
                a_minus += 1
            elif float(score.text()) >= 75.0:
                index = 3.33 * credit
                total += index
                b_plus += 1
            elif float(score.text()) >= 70.0:
                index = 3.0 * credit
                total += index
                b += 1
            elif float(score.text()) >= 67.0:
                index = 2.67 * credit
                total += index
                b_minus += 1
            elif float(score.text()) >= 64.0:
                index = 2.33 * credit
                total += index
                c_plus += 1
            elif float(score.text()) >= 60.0:
                index = 2.0 * credit
                total += index
                c += 1
            elif float(score.text()) >= 55.0:
                index = 1.0 * credit
                total += index
                d += 1
            elif float(score.text()) < 55.0:
                index = 0.0 * credit
                total += index
                e += 1
        gpa = total / total_credit
        self.label_a.setText('A   = ' + str(a))
        self.label_a_minus.setText('A-  = ' + str(a_minus))
        self.label_b_plus.setText('B+ = ' + str(b_plus))
        self.label_b.setText('B   = ' + str(b))
        self.label_b_minus.setText('B-  = ' + str(b_minus))
        self.label_c_plus.setText('C+ = ' + str(c_plus))
        self.label_c.setText('C   = ' + str(c))
        self.label_d.setText('D   = ' + str(d))
        self.label_e.setText('E   = ' + str(e))
        self.label_total_index.setText('Total Index = ' + str(total))
        self.label_total_credit.setText('Total Credit = ' + str(total_credit))
        self.label_gpa.setText('GPA = ' + str(gpa))

app = QApplication([])
window = Window()
window.show()
app.exec_()
