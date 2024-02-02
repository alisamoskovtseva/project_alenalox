import csv

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from random import randrange
import sqlite3
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QInputDialog, QTableWidgetItem, QFileDialog

sqlite_connection = sqlite3.connect('bd7.sqlite')
cursor = sqlite_connection.cursor()
result = 0
ocenka = 2


class Ui_Welcome(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 641, 71))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 170, 211, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Привет!\n"
                                                    "Это приложение для подготовки к ЕГЭ по информатике по некоторым заданиям\n"
                                                    ""))
        self.pushButton.setText(_translate("MainWindow", "Начать"))


class Ui_task(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 439)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 110, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 210, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 110, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 310, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(100, 90, 70, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(320, 90, 70, 17))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 190, 70, 17))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(320, 190, 70, 17))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Задание 7"))
        self.pushButton_2.setText(_translate("Form", "Задание8"))
        self.pushButton_3.setText(_translate("Form", "Задание 11"))
        self.pushButton_4.setText(_translate("Form", "Задание13"))
        self.label.setText(_translate("Form", "Главная страница"))
        self.pushButton_8.setText(_translate("Form", "Таблица с результатами"))


class Ui_problem(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(671, 371)
        self.pushButton9 = QtWidgets.QPushButton(Form)
        self.pushButton9.setGeometry(QtCore.QRect(270, 320, 111, 31))
        self.pushButton9.setObjectName("pushButton9")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(100, 220, 471, 71))
        self.textEdit.setObjectName("textEdit")
        self.label9 = QtWidgets.QLabel(Form)
        self.label9.setGeometry(QtCore.QRect(10, 30, 641, 171))
        font = QtGui.QFont()
        font.setFamily("Tempus Sans ITC")
        font.setPointSize(11)
        self.label9.setFont(font)
        self.label9.setText("")
        self.label9.setAlignment(QtCore.Qt.AlignCenter)
        self.label9.setObjectName("label9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton9.setText(_translate("Form", "Ответить"))


class Ui_picteres(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 462)
        self.pushButton9 = QtWidgets.QPushButton(Form)
        self.pushButton9.setGeometry(QtCore.QRect(100, 380, 191, 31))
        self.pushButton9.setObjectName("pushButton9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 350, 251, 16))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 281, 281))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton9.setText(_translate("Form", "Вернуться на главную страницу"))


class Ui_Table(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(634, 504)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 541, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(100, 430, 151, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 430, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "результаты"))
        self.pushButton.setText(_translate("Form", "Скачать таблицу"))
        self.pushButton_2.setText(_translate("Form", "Очистить таблицу"))


class MyWidget(QMainWindow, Ui_Welcome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.qrt = Tasks()
        self.qrt.show()
        self.close()


class Tasks(QWidget, Ui_task):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run_7)
        self.pushButton_2.clicked.connect(self.run_8)
        self.pushButton_3.clicked.connect(self.run_11)
        self.pushButton_4.clicked.connect(self.run_13)
        self.pushButton_8.clicked.connect(self.run_table)

    def run_table(self):
        self.wrt = Table()
        self.wrt.show()

    def run_7(self):
        global fil
        fil, ok_pressed = QInputDialog.getText(self, "Введите ФИО", 'Введите ФИО')
        if ok_pressed and fil:
            self.wrt = Problem7()
            self.wrt.show()

    def run_8(self):
        global fil
        fil, ok_pressed = QInputDialog.getText(self, "Введите ФИО", 'Введите ФИО')
        if ok_pressed and fil:
            self.wrt = Problem8()
            self.wrt.show()

    def run_11(self):
        global fil
        fil, ok_pressed = QInputDialog.getText(self, "Введите ФИО", 'Введите ФИО')
        if ok_pressed and fil:
            self.wrt = Problem11()
            self.wrt.show()

    def run_13(self):
        global fil
        fil, ok_pressed = QInputDialog.getText(self, "Введите ФИО", 'Введите ФИО')
        if ok_pressed and fil:
            self.wrt = Problem13()
            self.wrt.show()


class Problem7(QWidget, Ui_problem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global result, ocenka
        self.count = 0
        self.otv = 0
        result = 0
        ocenka = 2
        self.clic = 0
        self.zad7()
        self.pushButton9.clicked.connect(self.ans_7)

    def zad7(self):
        self.textEdit.setText('')
        ide = randrange(1, 30)
        cursor.execute(f"""select * from zadanie7 where id = {ide}""")
        self.ans = cursor.fetchall()[-1]
        self.otv = self.ans[-1]
        self.label9.setText(self.ans[-2])
        self.label9.setWordWrap(True)

    def ans_7(self):
        global fil, result, ocenka
        self.otvet = (self.textEdit.toPlainText())
        if (self.otvet == str(self.otv)) and self.otv:
            result += 1
        if result <= 2:
            ocenka = 2
        else:
            ocenka = result
        if self.clic < 4:
            self.zad7()
            self.clic += 1
        else:
            self.count += 1
            cursor.execute(f'''INSERT INTO result(fio, number_task, ocenka) VALUES('{fil}', {7}, {ocenka})''')
            sqlite_connection.commit()
            self.close()
            self.asw = Pictr7()
            self.asw.show()


class Pictr7(QWidget, Ui_picteres):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pict_7()
        self.pushButton9.clicked.connect(self.close)

    def pict_7(self):
        pixmap = QPixmap('dinozavr.jpg')
        self.label_2.setPixmap(pixmap)
        self.label.setText(f'Вы набрали {result} баллов из 5')


class Problem8(QWidget, Ui_problem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global result, ocenka
        self.count = 0
        self.otv = 0
        result = 0
        ocenka= 2
        self.clic = 0
        self.zad8()
        self.pushButton9.clicked.connect(self.ans_8)

    def zad8(self):
        self.textEdit.setText('')
        ide = randrange(1, 30)
        cursor.execute(f"""select * from zadanie8 where id = {ide}""")
        self.ans = cursor.fetchall()[-1]
        self.otv = self.ans[-1]
        self.label9.setText(self.ans[-2])
        self.label9.setWordWrap(True)

    def ans_8(self):
        global fil, result
        self.otvet = (self.textEdit.toPlainText())
        if (self.otvet == str(self.otv)) and self.otv:
            result += 1
        if result <= 2:
            ocenka = 2
        else:
            ocenka = result
        if self.clic < 4:
            self.zad8()
            self.clic += 1
        else:
            self.count += 1
            cursor.execute(f'''INSERT INTO result(fio, number_task, ocenka) VALUES('{fil}', {8}, {ocenka})''')
            sqlite_connection.commit()
            self.close()
            self.asw = Pictr8()
            self.asw.show()


class Pictr8(QWidget, Ui_picteres):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pict_8()
        self.pushButton9.clicked.connect(self.close)

    def pict_8(self):
        pixmap = QPixmap('zayc2.jpg')
        self.label_2.setPixmap(pixmap)
        self.label.setText(f'Вы набрали {result} баллов из 5')


class Problem11(QWidget, Ui_problem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global result, ocenka
        self.count = 0
        self.otv = 0
        result = 0
        ocenka= 2
        self.clic = 0
        self.zad11()
        self.pushButton9.clicked.connect(self.ans_11)

    def zad11(self):
        self.textEdit.setText('')
        ide = randrange(1, 30)
        cursor.execute(f"""select * from zadanie11 where id = {ide}""")
        self.ans = cursor.fetchall()[-1]
        self.otv = self.ans[-1]
        self.label9.setText(self.ans[-2])
        self.label9.setWordWrap(True)

    def ans_11(self):
        global fil, result, ocenka
        self.otvet = (self.textEdit.toPlainText())
        if (self.otvet == str(self.otv)) and self.otv:
            self.result += 1
        if result <= 2:
            ocenka = 2
        else:
            ocenka = result
        if self.clic < 4:
            self.zad11()
            self.clic += 1
        else:
            self.count += 1
            cursor.execute(f'''INSERT INTO result(fio, number_task, ocenka) VALUES('{fil}', {11}, {ocenka})''')
            sqlite_connection.commit()
            self.close()
            self.asw = Pictr11()
            self.asw.show()


class Pictr11(QWidget, Ui_picteres):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pict_11()
        self.pushButton9.clicked.connect(self.close)

    def pict_11(self):
        pixmap = QPixmap('cat.jpg')
        self.label_2.setPixmap(pixmap)
        self.label.setText(f'Вы набрали {result} баллов из 5')


class Problem13(QWidget, Ui_problem):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global result
        self.count = 0
        self.otv = 0
        result = 0
        ocenka = 0
        self.clic = 0
        self.zad13()
        self.pushButton9.clicked.connect(self.ans_13)

    def zad13(self):
        self.textEdit.setText('')
        ide = randrange(1, 30)
        cursor.execute(f"""select * from zadanie13 where id = {ide}""")
        self.ans = cursor.fetchall()[-1]
        self.otv = self.ans[-1]
        self.label9.setText(self.ans[-2])
        self.label9.setWordWrap(True)

    def ans_13(self):
        global fil, result, ocenka
        self.otvet = (self.textEdit.toPlainText())
        if (self.otvet == str(self.otv)) and self.otv:
            result += 15
        if result <= 2:
            ocenka = 2
        else:
            ocenka = result
        if self.clic < 4:
            self.zad13()
            self.clic += 1
        else:  # запись в бд результат
            cursor.execute(f'''INSERT INTO result(fio, number_task, ocenka) VALUES('{fil}', {13}, {ocenka})''')
            sqlite_connection.commit()
            self.close()
            self.asw = Pictr13()
            self.asw.show()


class Pictr13(QWidget, Ui_picteres):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pict_13()
        self.pushButton9.clicked.connect(self.close)

    def pict_13(self):
        pixmap = QPixmap('zayc.jpg')
        self.label_2.setPixmap(pixmap)
        self.label.setText(f'Вы набрали {result} баллов из 5')


class Table(QWidget, Ui_Table):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global sqlite_connection
        self.table()
        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.delit)

    def table(self):
        global sqlite_connection
        cur = sqlite_connection.cursor()
        result = cur.execute("SELECT fio, number_task, ocenka FROM result").fetchall()
        if result:
            # Заполнили размеры таблицы
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(['Фио', "Номер задания", "Оценка"])
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def save(self):
        global sqlite_connection
        cur = sqlite_connection.cursor()
        res = cur.execute("SELECT fio, number_task, ocenka FROM result").fetchall()
        self.fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '')[0]
        with open(self.fname, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=';', quotechar='"',
                           quoting=csv.QUOTE_MINIMAL)
            a.writerows(res)

    def delit(self):
        global sqlite_connection
        sqlite_connection.execute("DELETE FROM result")
        sqlite_connection.commit()
        cur = sqlite_connection.cursor()
        result = cur.execute("SELECT fio, number_task, ocenka FROM result").fetchall()
        if result:
            # Заполнили размеры таблицы
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(['Фио', "Номер задания", "Оценка"])
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result))
            self.tableWidget.setHorizontalHeaderLabels(['Фио', "Номер задания", "Оценка"])
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


def except_hook(cls, excpection, traceback):
    sys.__excepthook__(cls, excpection, traceback)


# if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

# if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
# QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
