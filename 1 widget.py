import sys
import csv
import sqlite3

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QCheckBox, QPushButton, QFileDialog


# ТАБЛИЦА


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('MainWindow.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.con = sqlite3.connect('data.db')  # подключение бд
        self.create.clicked.connect(self.update_data)
        self.aaaaa.clicked.connect(self.csv_write)
        self.update_result()
        self.go_out.clicked.connect(self.close)
        self.update.clicked.connect(self.update_)

    def csv_write(self):
        cur = self.con.cursor()
        res = cur.execute("SELECT name, importance, closed, description FROM tasks").fetchall()
        self.fname = QFileDialog.getSaveFileName(self, 'Выбрать файл', '')[0]
        with open(self.fname, 'w', newline='') as fp:
            a = csv.writer(fp, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            a.writerow([self.tableWidget.horizontalHeaderItem(i).text()
                        for i in range(self.tableWidget.columnCount())])
            a.writerows(res)

    def update_data(self):
        name_task = self.name_task.text()
        description = self.description.text()
        dedline = self.dedline.dateTime().toString()
        importance = self.importance_box.currentText()
        cursor = self.con.cursor()
        str = f'''INSERT INTO tasks
                          (name, dedline, description, importance)
                          VALUES
                          ('{name_task}', '{dedline}', '{description}', {importance});'''
        cursor.execute(str)
        self.con.commit()
        self.update_result()

    def update_(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT id, name, importance, closed FROM tasks ORDER BY -importance").fetchall()
        if result:
            # Заполнили размеры таблицы
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(['Название', "Важность", "Выполнено", 'Инфо'])
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                elem = list(elem)
                b = elem[-1]
                elem[-1] = QCheckBox()
                elem[-1].setChecked(b)
                elem[-1].stateChanged.connect(lambda checked, x=elem[0]: self.update_checkBox(x))
                btn = QPushButton(f'Подробнее', self)
                btn.clicked.connect(lambda checked, x=elem[0]: self.about(x))
                elem.append(btn)

                for j, val in enumerate(elem[1:]):
                    if type(val) == QCheckBox or type(val) == QPushButton:
                        self.tableWidget.setCellWidget(i, j, val)
                    else:
                        item = QTableWidgetItem(str(val))
                        self.tableWidget.setItem(i, j, item)

    def update_result(self):
        cur = self.con.cursor()
        # Получили результат запроса, который ввели в текстовое поле
        result = cur.execute("SELECT id, name, importance, closed FROM tasks ORDER BY -importance").fetchall()
        if result:
            # Заполнили размеры таблицы
            self.tableWidget.setRowCount(len(result))
            # Если запись не нашлась, то не будем ничего делать
            self.tableWidget.setColumnCount(len(result[0]))
            self.tableWidget.setHorizontalHeaderLabels(['Название', "Важность", "Выполнено", 'Инфо'])
            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                elem = list(elem)
                b = elem[-1]
                elem[-1] = QCheckBox()
                elem[-1].setChecked(b)
                elem[-1].stateChanged.connect(lambda checked, x=elem[0]: self.update_checkBox(x))
                btn = QPushButton(f'Подробнее', self)
                btn.clicked.connect(lambda checked, x=elem[0]: self.about(x))
                elem.append(btn)

                for j, val in enumerate(elem[1:]):
                    if type(val) == QCheckBox or type(val) == QPushButton:
                        self.tableWidget.setCellWidget(i, j, val)
                    else:
                        item = QTableWidgetItem(str(val))
                        self.tableWidget.setItem(i, j, item)

    def update_checkBox(self, _id):
        cursor = self.con.cursor()
        aaa = f''' UPDATE tasks SET closed = {int(self.sender().isChecked())} WHERE id = {_id}'''
        cursor.execute(aaa)
        self.con.commit()

    def about(self, _id):
        self.qrt = MyWidget2(_id)
        self.qrt.show()
        # нужны ид и по ним получать всю инфу о задаче. ид не выводить(срез)

        # Имя элемента совпадает с objectName в QTDesigner


class MyWidget2(QMainWindow):
    def __init__(self, _id):
        super().__init__()
        self.id = _id
        self.con = sqlite3.connect('data.db')
        uic.loadUi('Widget.ui', self)
        self.output()
        self.ok.clicked.connect(self.close)
        self.delete_2.clicked.connect(self.delette)
        self.delete_2.clicked.connect(self.close)

    def output(self):
        cur = self.con.cursor()
        name = cur.execute(f'''SELECT name FROM tasks WHERE id = {self.id}''').fetchone()
        description = cur.execute(f'''SELECT description FROM tasks WHERE id = {self.id}''').fetchone()
        dedline = cur.execute(f'''SELECT dedline FROM tasks WHERE id = {self.id}''').fetchone()
        importance = cur.execute(f'''SELECT importance FROM tasks WHERE id = {self.id}''').fetchone()
        self.name1.setText(*name)
        self.name1.setWordWrap(True)
        self.description.setText(*description)
        self.description.setWordWrap(True)
        self.dedline.setText(*dedline)
        self.importance.setText(str(*importance))

    def delette(self):
        cur = self.con.cursor()
        sql_delete = f'''DELETE from tasks where id = {self.id}'''
        cur.execute(sql_delete)
        self.con.commit()



def except_hook(cls, excpection, traceback):
    sys.__excepthook__(cls, excpection, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(
        "QMainWindow{background-color:#F0F8FF} QWidget{background-color:#F0F8FF} QLabel{font-size: 13pt;} QPushButton{font-size: 12pt;} QPushButton{background-color:#ADD8E6} "
        "QPushButton{border-radius: 10px}")
    form = MainWindow()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
