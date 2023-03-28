# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_doctor.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FUNCTION import return_table
from sucsessful_wndw import Ui_Sucsessful_windw
from error_wndw import Ui_Error_windw


class Ui_Add_doctor(object):

    def setupUi(self, Add_doctor):
        Add_doctor.setObjectName("Add_doctor")
        Add_doctor.resize(487, 177)
        self.Confirm_add_doctor = QtWidgets.QPushButton(Add_doctor)
        self.Confirm_add_doctor.setGeometry(QtCore.QRect(380, 70, 93, 71))
        self.Confirm_add_doctor.setObjectName("Confirm_add_doctor")
        self.lineEdit = QtWidgets.QLineEdit(Add_doctor)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 141, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_phone_num_doctor = QtWidgets.QLineEdit(Add_doctor)
        self.lineEdit_phone_num_doctor.setGeometry(QtCore.QRect(210, 40, 141, 22))
        self.lineEdit_phone_num_doctor.setObjectName("lineEdit_phone_num_doctor")
        self.label_doctor_name = QtWidgets.QLabel(Add_doctor)
        self.label_doctor_name.setGeometry(QtCore.QRect(24, 10, 141, 20))
        self.label_doctor_name.setObjectName("label_doctor_name")
        self.label_doctor_age = QtWidgets.QLabel(Add_doctor)
        self.label_doctor_age.setGeometry(QtCore.QRect(20, 90, 161, 20))
        self.label_doctor_age.setObjectName("label_doctor_age")
        self.label_position_doctor = QtWidgets.QLabel(Add_doctor)
        self.label_position_doctor.setGeometry(QtCore.QRect(214, 90, 151, 20))
        self.label_position_doctor.setObjectName("label_position_doctor")
        self.label_doct_phone_number = QtWidgets.QLabel(Add_doctor)
        self.label_doct_phone_number.setGeometry(QtCore.QRect(214, 10, 191, 20))
        self.label_doct_phone_number.setObjectName("label_doct_phone_number")
        self.label_error_name_doctor = QtWidgets.QLabel(Add_doctor)
        self.label_error_name_doctor.setGeometry(QtCore.QRect(20, 70, 141, 20))
        self.label_error_name_doctor.setText("")
        self.label_error_name_doctor.setObjectName("label_error_name_doctor")
        self.label_error_phone_number_doctor = QtWidgets.QLabel(Add_doctor)
        self.label_error_phone_number_doctor.setGeometry(QtCore.QRect(210, 70, 141, 20))
        self.label_error_phone_number_doctor.setText("")
        self.label_error_phone_number_doctor.setObjectName("label_error_phone_number_doctor")
        self.comboBox = QtWidgets.QComboBox(Add_doctor)
        self.comboBox.setGeometry(QtCore.QRect(210, 120, 141, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.dateEdit = QtWidgets.QDateEdit(Add_doctor)
        self.dateEdit.setGeometry(QtCore.QRect(20, 120, 151, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(Add_doctor)
        QtCore.QMetaObject.connectSlotsByName(Add_doctor)

    def retranslateUi(self, Add_doctor):
        _translate = QtCore.QCoreApplication.translate
        Add_doctor.setWindowTitle(_translate("Add_doctor", "Add_doctor"))
        self.Confirm_add_doctor.setText(_translate("Add_doctor", "Подтвердить"))
        self.lineEdit_phone_num_doctor.setText(_translate("Add_doctor", "375"))
        self.label_doctor_name.setText(_translate("Add_doctor", "Введите имя доктора:"))
        self.label_doctor_age.setText(_translate("Add_doctor", "Дата рождения доктора:"))
        self.label_position_doctor.setText(_translate("Add_doctor", "Укажите профобласть:"))
        self.label_doct_phone_number.setText(_translate("Add_doctor", "Укажите телефонный номер:"))

        self.Confirm_add_doctor.clicked.connect(self.add_doctor)
        poz_dict = {}
        poz = return_table('POSITION')
        print(poz.fetchall())
        for x in poz.fetchall():
            poz_dict.update({x[0]:x[1]})
        print(poz_dict)
        for k,v in poz_dict.items():
            self.comboBox.addItem(v)


    def check_phone_num(self):
        if self.lineEdit_phone_num_doctor.text() != '':
            self.label_error_phone_number_doctor.setText('')
            if self.lineEdit_phone_num_doctor.text() != '375':
                self.label_error_phone_number_doctor.setText('')
                if self.lineEdit_phone_num_doctor.text().isdigit():
                    self.label_error_phone_number_doctor.setText('')
                    if len(self.lineEdit_phone_num_doctor.text()) == 12:
                        self.label_error_phone_number_doctor.setText('')
                        return True
                    else:
                        self.label_error_phone_number_doctor.setText('Мало цифр для номера!')
                        return False
                else:
                    self.label_error_phone_number_doctor.setText('Только цифры!!!')
                    return False
            else:
                self.label_error_phone_number_doctor.setText('Вы ничего не ввели!')
                return False
        else:
            self.label_error_phone_number_doctor.setText('Поле пустое!!!')
            return False

    def add_doctor(self):
        name = any(x.isdigit() for x in self.lineEdit.text())
        if name == False:
            self.label_error_name_doctor.setText('')
            if self.check_phone_num() == True:
                if self.dateEdit.text() != '01.01.2000':
                    if self.comboBox.lineEdit().text() != '':
                        self.lineEdit.setReadOnly(True)
                        self.lineEdit_phone_num_doctor.setReadOnly(True)
                        self.dateEdit.setReadOnly(True)
                        self.comboBox.lineEdit().setReadOnly(True)
                        poz_dict = {}
                        poz = return_table('POSITION')
                        for x in poz.fetchall():
                            poz_dict.update({x[0]: x[1]})
                        # result = (self.lineEdit.text(), self.dateEdit.text(), self.lineEdit_phone_num_doctor.text(),
                        #           self.comboBox.lineEdit().text())
                        answ = []
                        for k,v in poz_dict.items():
                            if v == self.comboBox.lineEdit().text():
                                answ.append(k)
                        answ.append(self.lineEdit_phone_num_doctor.text())
                        answ.append(self.dateEdit.text())
                        answ.append(self.lineEdit.text())
                        print(answ)


                        # answer = True
                        # if answer == True:
                        #     sucsess = QtWidgets.QDialog()
                        #     ui2 = Ui_Sucsessful_windw()
                        #     ui2.setupUi(sucsess)
                        #     sucsess.show()
                        #     sucsess.exec_()
                        #     Add_doctor.close()
                        # else:
                        #     error = QtWidgets.QDialog()
                        #     ui2 = Ui_Error_windw()
                        #     ui2.setupUi(error)
                        #     error.show()
                        #     error.exec_()
        else:
            self.label_error_name_doctor.setText('В имени не бывает цифр!')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Add_doctor = QtWidgets.QDialog()
    ui = Ui_Add_doctor()
    ui.setupUi(Add_doctor)
    Add_doctor.show()
    sys.exit(app.exec_())
