import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from main_1 import Ui_MainWindow


class HeadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.initUI()

    def initUI(self):
        self.connection = sqlite3.connect('coffee.sqlite')
        self.cursor = self.connection.cursor()
        self.print_info_coffee()

    def print_info_coffee(self):
        result = self.cursor.execute("""SELECT * FROM table_of_coffee""").fetchall()
        if not result:
            self.tableWidget.clear()
            return
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'сорт', 'степень обжарки', 'молотый/в зёрнах',
                                                    'описание вкуса', 'цена', 'объём'])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = HeadWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
