# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_client.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_client(object):
    def setupUi(self, Add_client):
        Add_client.setObjectName("Add_client")
        Add_client.resize(332, 286)
        self.pushButton = QtWidgets.QPushButton(Add_client)
        self.pushButton.setGeometry(QtCore.QRect(230, 200, 93, 81))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_name_client = QtWidgets.QLineEdit(Add_client)
        self.lineEdit_name_client.setEnabled(True)
        self.lineEdit_name_client.setGeometry(QtCore.QRect(32, 40, 151, 22))
        self.lineEdit_name_client.setObjectName("lineEdit_name_client")
        self.lineEdit_phone_num_client = QtWidgets.QLineEdit(Add_client)
        self.lineEdit_phone_num_client.setGeometry(QtCore.QRect(30, 230, 151, 22))
        self.lineEdit_phone_num_client.setReadOnly(False)
        self.lineEdit_phone_num_client.setObjectName("lineEdit_phone_num_client")
        self.lineEdit_age_client = QtWidgets.QLineEdit(Add_client)
        self.lineEdit_age_client.setGeometry(QtCore.QRect(30, 130, 151, 22))
        self.lineEdit_age_client.setObjectName("lineEdit_age_client")
        self.label_name_client = QtWidgets.QLabel(Add_client)
        self.label_name_client.setGeometry(QtCore.QRect(34, 10, 191, 20))
        self.label_name_client.setObjectName("label_name_client")
        self.age_client = QtWidgets.QLabel(Add_client)
        self.age_client.setGeometry(QtCore.QRect(30, 100, 141, 20))
        self.age_client.setObjectName("age_client")
        self.Phone_number_client = QtWidgets.QLabel(Add_client)
        self.Phone_number_client.setGeometry(QtCore.QRect(30, 200, 171, 20))
        self.Phone_number_client.setObjectName("Phone_number_client")
        self.label_error_name_client = QtWidgets.QLabel(Add_client)
        self.label_error_name_client.setGeometry(QtCore.QRect(34, 70, 161, 20))
        self.label_error_name_client.setText("")
        self.label_error_name_client.setObjectName("label_error_name_client")
        self.label_error_age_client = QtWidgets.QLabel(Add_client)
        self.label_error_age_client.setGeometry(QtCore.QRect(34, 160, 161, 20))
        self.label_error_age_client.setText("")
        self.label_error_age_client.setObjectName("label_error_age_client")
        self.label_error_phone_num_client = QtWidgets.QLabel(Add_client)
        self.label_error_phone_num_client.setGeometry(QtCore.QRect(34, 260, 151, 20))
        self.label_error_phone_num_client.setText("")
        self.label_error_phone_num_client.setObjectName("label_error_phone_num_client")

        self.retranslateUi(Add_client)
        QtCore.QMetaObject.connectSlotsByName(Add_client)

    def retranslateUi(self, Add_client):
        _translate = QtCore.QCoreApplication.translate
        Add_client.setWindowTitle(_translate("Add_client", "Add_client"))
        self.pushButton.setText(_translate("Add_client", "Подтвердить"))
        self.lineEdit_phone_num_client.setText(_translate("Add_client", "375"))
        self.label_name_client.setText(_translate("Add_client", "Введите имя нового клиента:"))
        self.age_client.setText(_translate("Add_client", "Укажите возраст:"))
        self.Phone_number_client.setText(_translate("Add_client", "Укажите номер телефона:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_client = QtWidgets.QDialog()
    ui = Ui_Add_client()
    ui.setupUi(Add_client)
    Add_client.show()
    sys.exit(app.exec_())
