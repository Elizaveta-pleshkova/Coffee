from PyQt5 import uic
from PyQt5.QtWidgets import *
import sqlite3
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.pushButton.clicked.connect(self.fill)


    def fill(self):
        self.del_row()

        labels = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
                  'Описание вкуса', 'Цена', 'Объем упаковки']

        self.tableWidget.setColumnCount(len(labels))
        self.tableWidget.setHorizontalHeaderLabels(labels)
        with sqlite3.connect("coffee.db") as connect:
            for ID, Name, Stepen, Tip, Opisanie, Cena, Obem in connect.execute(
                    """SELECT * FROM price where ID > 0"""):
                row = self.tableWidget.rowCount()
                self.tableWidget.setRowCount(row + 1)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(ID)))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(Name))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(Stepen))
                self.tableWidget.setItem(row, 3, QTableWidgetItem(Tip))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(Opisanie))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(Cena)))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(str(Obem)))

        self.tableWidget.resizeColumnsToContents()

    def del_row(self):
        for d in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)


app = QApplication(sys.argv)
ui = MainWindow()
ui.show()
sys.exit(app.exec_())
