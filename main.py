from main.ui import Ui_mainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import sys


def fill():
    ui.tableWidget.clear()

    labels = ['ID', 'Название сорта', 'Степень обжарки', 'Молотый/в зернах',
              'Описание вкуса',  'Цена',  'Объем упаковки']

    ui.tableWidget.setColumnCount(len(labels))
    ui.tableWidget.setHorizontalHeaderLabels(labels)
    with sqlite3.connect("Coffee.db") as connect:
        for ID, Name, stepen, Tip, Opisanie, Cena, Obem in connect.execute(
                """SELECT * FROM prise where id > 0"""):
            row = self.tableWidget.rowCount()
            ui.tableWidget.setRowCount(row + 1)
            ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(ID)))
            ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(Name))
            ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(stepen))
            ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(Tip))
            ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(Opisanie))
            ui.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(Cena)))
            ui.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Obem)))



app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)
ui.pushButton.clicked.connect(fill)
mainWindow.show()
sys.exit(app.exec_())
