# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_zapis.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FUNCTION import comeback_table
from FUNCTION import record
from sucsessful_wndw import Ui_Sucsessful_windw
from error_wndw import Ui_Error_windw


class Ui_Zapis(object):
    def setupUi(self, Zapis):
        Zapis.setObjectName("Zapis")
        Zapis.resize(600, 252)
        self.comboBox_service = QtWidgets.QComboBox(Zapis)
        self.comboBox_service.setGeometry(QtCore.QRect(10, 40, 161, 22))
        self.comboBox_service.setEditable(True)
        self.comboBox_service.setObjectName("comboBox_service")
        self.label_choise_service = QtWidgets.QLabel(Zapis)
        self.label_choise_service.setGeometry(QtCore.QRect(14, 10, 151, 20))
        self.label_choise_service.setObjectName("label_choise_service")
        self.comboBox_doctors = QtWidgets.QComboBox(Zapis)
        self.comboBox_doctors.setGeometry(QtCore.QRect(190, 40, 161, 22))
        self.comboBox_doctors.setEditable(True)
        self.comboBox_doctors.setObjectName("comboBox_doctors")
        self.label_choice_doctor = QtWidgets.QLabel(Zapis)
        self.label_choice_doctor.setGeometry(QtCore.QRect(194, 10, 151, 20))
        self.label_choice_doctor.setObjectName("label_choice_doctor")
        self.comboBox_clients = QtWidgets.QComboBox(Zapis)
        self.comboBox_clients.setGeometry(QtCore.QRect(380, 40, 161, 22))
        self.comboBox_clients.setEditable(True)
        self.comboBox_clients.setObjectName("comboBox_clients")
        self.label_choice_data_time = QtWidgets.QLabel(Zapis)
        self.label_choice_data_time.setGeometry(QtCore.QRect(580, 10, 151, 20))
        self.label_choice_data_time.setObjectName("label_choice_data_time")
        self.Confirm_zapis = QtWidgets.QPushButton(Zapis)
        self.Confirm_zapis.setGeometry(QtCore.QRect(320, 170, 93, 71))
        self.Confirm_zapis.setObjectName("Confirm_zapis")
        self.label_client_name = QtWidgets.QLabel(Zapis)
        self.label_client_name.setGeometry(QtCore.QRect(384, 10, 151, 20))
        self.label_client_name.setObjectName("label_client_name")

        self.retranslateUi(Zapis)
        QtCore.QMetaObject.connectSlotsByName(Zapis)

    def retranslateUi(self, Zapis):
        _translate = QtCore.QCoreApplication.translate
        Zapis.setWindowTitle(_translate("Zapis", "Zapis"))
        self.label_choise_service.setText(_translate("Zapis", "Выберите услугу:"))
        self.label_choice_doctor.setText(_translate("Zapis", "Выберите доктора:"))
        self.Confirm_zapis.setText(_translate("Zapis", "Подтвердить"))
        self.label_client_name.setText(_translate("Zapis", "Укажите имя клиента:"))

        self.Confirm_zapis.clicked.connect(self.zapis)
        main_l = comeback_table()
        dict_servis = main_l[0]
        dict_doctors = main_l[1]
        dict_clients = main_l[2]
        for k, v in dict_servis.items():
            self.comboBox_service.addItem(v)
        for k, v in dict_doctors.items():
            self.comboBox_doctors.addItem(v)
        for k, v in dict_clients.items():
            self.comboBox_clients.addItem(v)
        print(main_l)

    def zapis(self):
        self.comboBox_clients.lineEdit().setReadOnly(True)
        self.comboBox_service.lineEdit().setReadOnly(True)
        self.comboBox_doctors.lineEdit().setReadOnly(True)

        answer = []

        main_l = comeback_table()
        dict_servis = main_l[0]
        dict_doctors = main_l[1]
        dict_clients = main_l[2]
        for k, v in dict_doctors.items():
            if v == self.comboBox_doctors.lineEdit().text():
                answer.append(k)
        for k, v in dict_servis.items():
            if v == self.comboBox_service.lineEdit().text():
                answer.append(k)
        for k, v in dict_clients.items():
            if v == self.comboBox_clients.lineEdit().text():
                answer.append(k)

        answer = tuple(answer)
        ans = record(answer)
        if ans == True:
            sucsess = QtWidgets.QDialog()
            ui2 = Ui_Sucsessful_windw()
            ui2.setupUi(sucsess)
            sucsess.show()
            sucsess.exec_()
            Zapis.close()
        else:
            error = QtWidgets.QDialog()
            ui2 = Ui_Error_windw()
            ui2.setupUi(error)
            error.show()
            error.exec_()









if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Zapis = QtWidgets.QDialog()
    ui = Ui_Zapis()
    ui.setupUi(Zapis)
    Zapis.show()
    sys.exit(app.exec_())
