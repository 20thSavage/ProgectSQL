# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from add_service import Ui_Add_servis
from add_client import Ui_Add_client
from add_doctor import Ui_Add_doctor
from add_zapis import Ui_Zapis

names_servis = ['id', 'name', 'price', 'time']
names_doctors = ['id', 'name', 'year', 'phone', 'position']
names_clients = ['id', 'name', 'age', 'phone']
names_zapis = ['id', 'client', 'servis', 'doctor', 'time']


class Ui_list(object):
    def setupUi(self, list):
        list.setObjectName("list")
        list.resize(596, 368)
        self.tableWidget = QtWidgets.QTableWidget(list)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 561, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.Add_btn = QtWidgets.QPushButton(list)
        self.Add_btn.setGeometry(QtCore.QRect(20, 260, 121, 91))
        self.Add_btn.setObjectName("Add_btn")
        self.change_btn = QtWidgets.QPushButton(list)
        self.change_btn.setGeometry(QtCore.QRect(160, 260, 171, 91))
        self.change_btn.setAutoFillBackground(False)
        self.change_btn.setAutoRepeat(False)
        self.change_btn.setDefault(False)
        self.change_btn.setFlat(False)
        self.change_btn.setObjectName("change_btn")
        self.del_btn = QtWidgets.QPushButton(list)
        self.del_btn.setGeometry(QtCore.QRect(472, 260, 111, 91))
        self.del_btn.setObjectName("del_btn")

        self.retranslateUi(list)
        QtCore.QMetaObject.connectSlotsByName(list)

    def retranslateUi(self, list):
        _translate = QtCore.QCoreApplication.translate
        list.setWindowTitle(_translate("list", "list"))
        self.Add_btn.setText(_translate("list", "Добавить новое"))
        self.change_btn.setText(_translate("list", "Изменить существующее"))
        self.del_btn.setText(_translate("list", "Удалить запись"))

        self.Add_btn.clicked.connect(self.add_new)
        self.del_btn.clicked.connect(self.check)

    def check(self, listt):
        if listt == names_servis:
            return 'Servis'
        if listt == names_zapis:
            return 'Zapis'
        if listt == names_doctors:
            return 'Doctors'
        if listt == names_clients:
            return 'Clients'

    def add_new(self):
        names_col = []

        for x in range(0, self.tableWidget.columnCount()):
            add = self.tableWidget.horizontalHeaderItem(x)
            names_col.append(add.text())
        answ = self.check(names_col)
        if answ == 'Servis':
            app2 = QtWidgets.QDialog()
            ui2 = Ui_Add_servis()
            ui2.setupUi(app2)
            app2.show()
            app2.exec_()
        elif answ == 'Clients':
            app2 = QtWidgets.QDialog()
            ui2 = Ui_Add_client()
            ui2.setupUi(app2)
            app2.show()
            app2.exec_()
        elif answ == 'Doctors':
            app2 = QtWidgets.QDialog()
            ui2 = Ui_Add_doctor()
            ui2.setupUi(app2)
            app2.show()
            app2.exec_()
        elif answ == 'Zapis':
            app2 = QtWidgets.QDialog()
            ui2 = Ui_Zapis()
            ui2.setupUi(app2)
            app2.show()
            app2.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    list = QtWidgets.QDialog()
    ui = Ui_list()
    ui.setupUi(list)
    list.show()
    sys.exit(app.exec_())
