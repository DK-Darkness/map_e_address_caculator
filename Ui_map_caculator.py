# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\map_caculator\map_caculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 717)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.I_v6p = QtWidgets.QLineEdit(self.centralwidget)
        self.I_v6p.setGeometry(QtCore.QRect(135, 70, 156, 20))
        self.I_v6p.setObjectName("I_v6p")
        self.I_v6pl = QtWidgets.QLineEdit(self.centralwidget)
        self.I_v6pl.setGeometry(QtCore.QRect(135, 100, 156, 20))
        self.I_v6pl.setObjectName("I_v6pl")
        self.I_v4p = QtWidgets.QLineEdit(self.centralwidget)
        self.I_v4p.setGeometry(QtCore.QRect(135, 130, 156, 20))
        self.I_v4p.setObjectName("I_v4p")
        self.I_v4pl = QtWidgets.QLineEdit(self.centralwidget)
        self.I_v4pl.setGeometry(QtCore.QRect(135, 160, 156, 20))
        self.I_v4pl.setObjectName("I_v4pl")
        self.I_eabitl = QtWidgets.QLineEdit(self.centralwidget)
        self.I_eabitl.setGeometry(QtCore.QRect(135, 190, 156, 20))
        self.I_eabitl.setObjectName("I_eabitl")
        self.I_psidoffset = QtWidgets.QLineEdit(self.centralwidget)
        self.I_psidoffset.setGeometry(QtCore.QRect(135, 220, 156, 20))
        self.I_psidoffset.setObjectName("I_psidoffset")
        self.L_v6p = QtWidgets.QLabel(self.centralwidget)
        self.L_v6p.setGeometry(QtCore.QRect(68, 75, 61, 12))
        self.L_v6p.setObjectName("L_v6p")
        self.L_v6pl = QtWidgets.QLabel(self.centralwidget)
        self.L_v6pl.setGeometry(QtCore.QRect(33, 105, 96, 12))
        self.L_v6pl.setObjectName("L_v6pl")
        self.L_v4p = QtWidgets.QLabel(self.centralwidget)
        self.L_v4p.setGeometry(QtCore.QRect(68, 135, 61, 12))
        self.L_v4p.setObjectName("L_v4p")
        self.L_v4pl = QtWidgets.QLabel(self.centralwidget)
        self.L_v4pl.setGeometry(QtCore.QRect(33, 165, 96, 12))
        self.L_v4pl.setObjectName("L_v4pl")
        self.L_psidoffset = QtWidgets.QLabel(self.centralwidget)
        self.L_psidoffset.setGeometry(QtCore.QRect(68, 225, 61, 12))
        self.L_psidoffset.setObjectName("L_psidoffset")
        self.L_eabitl = QtWidgets.QLabel(self.centralwidget)
        self.L_eabitl.setGeometry(QtCore.QRect(63, 195, 66, 12))
        self.L_eabitl.setObjectName("L_eabitl")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(515, 305, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.L_eup = QtWidgets.QLabel(self.centralwidget)
        self.L_eup.setGeometry(QtCore.QRect(48, 255, 81, 12))
        self.L_eup.setObjectName("L_eup")
        self.I_eup = QtWidgets.QLineEdit(self.centralwidget)
        self.I_eup.setGeometry(QtCore.QRect(135, 250, 156, 20))
        self.I_eup.setObjectName("I_eup")
        self.L_bin = QtWidgets.QLabel(self.centralwidget)
        self.L_bin.setGeometry(QtCore.QRect(745, 35, 54, 12))
        self.L_bin.setObjectName("L_bin")
        self.L_v6p_b = QtWidgets.QLabel(self.centralwidget)
        self.L_v6p_b.setGeometry(QtCore.QRect(400, 70, 716, 16))
        self.L_v6p_b.setText("")
        self.L_v6p_b.setAlignment(QtCore.Qt.AlignCenter)
        self.L_v6p_b.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v6p_b.setObjectName("L_v6p_b")
        self.L_v4p_b = QtWidgets.QLabel(self.centralwidget)
        self.L_v4p_b.setGeometry(QtCore.QRect(400, 130, 716, 16))
        self.L_v4p_b.setText("")
        self.L_v4p_b.setAlignment(QtCore.Qt.AlignCenter)
        self.L_v4p_b.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v4p_b.setObjectName("L_v4p_b")
        self.L_eup_b = QtWidgets.QLabel(self.centralwidget)
        self.L_eup_b.setGeometry(QtCore.QRect(400, 250, 716, 16))
        self.L_eup_b.setText("")
        self.L_eup_b.setAlignment(QtCore.Qt.AlignCenter)
        self.L_eup_b.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_eup_b.setObjectName("L_eup_b")
        self.L_v6a = QtWidgets.QLabel(self.centralwidget)
        self.L_v6a.setGeometry(QtCore.QRect(35, 425, 81, 16))
        self.L_v6a.setObjectName("L_v6a")
        self.L_v6a_b = QtWidgets.QLabel(self.centralwidget)
        self.L_v6a_b.setGeometry(QtCore.QRect(60, 450, 54, 12))
        self.L_v6a_b.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.L_v6a_b.setObjectName("L_v6a_b")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 345, 1121, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(352, 65, 16, 236))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.L_v4a = QtWidgets.QLabel(self.centralwidget)
        self.L_v4a.setGeometry(QtCore.QRect(300, 590, 81, 12))
        self.L_v4a.setObjectName("L_v4a")
        self.L_v6a_v = QtWidgets.QLabel(self.centralwidget)
        self.L_v6a_v.setGeometry(QtCore.QRect(125, 425, 896, 16))
        self.L_v6a_v.setText("")
        self.L_v6a_v.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v6a_v.setObjectName("L_v6a_v")
        self.L_v6a_b_v = QtWidgets.QLabel(self.centralwidget)
        self.L_v6a_b_v.setGeometry(QtCore.QRect(125, 450, 896, 16))
        self.L_v6a_b_v.setText("")
        self.L_v6a_b_v.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v6a_b_v.setObjectName("L_v6a_b_v")
        self.L_v4a_b_v = QtWidgets.QLabel(self.centralwidget)
        self.L_v4a_b_v.setGeometry(QtCore.QRect(255, 610, 436, 16))
        self.L_v4a_b_v.setText("")
        self.L_v4a_b_v.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v4a_b_v.setObjectName("L_v4a_b_v")
        self.L_v4a_h_v = QtWidgets.QLabel(self.centralwidget)
        self.L_v4a_h_v.setGeometry(QtCore.QRect(255, 640, 436, 16))
        self.L_v4a_h_v.setText("")
        self.L_v4a_h_v.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v4a_h_v.setObjectName("L_v4a_h_v")
        self.L_psid = QtWidgets.QLabel(self.centralwidget)
        self.L_psid.setGeometry(QtCore.QRect(130, 591, 36, 10))
        self.L_psid.setObjectName("L_psid")
        self.L_bin_2 = QtWidgets.QLabel(self.centralwidget)
        self.L_bin_2.setGeometry(QtCore.QRect(30, 610, 21, 16))
        self.L_bin_2.setObjectName("L_bin_2")
        self.L_hex = QtWidgets.QLabel(self.centralwidget)
        self.L_hex.setGeometry(QtCore.QRect(30, 640, 21, 16))
        self.L_hex.setObjectName("L_hex")
        self.L_dec = QtWidgets.QLabel(self.centralwidget)
        self.L_dec.setGeometry(QtCore.QRect(30, 670, 21, 16))
        self.L_dec.setObjectName("L_dec")
        self.L_psid_b = QtWidgets.QLabel(self.centralwidget)
        self.L_psid_b.setGeometry(QtCore.QRect(68, 610, 151, 16))
        self.L_psid_b.setText("")
        self.L_psid_b.setAlignment(QtCore.Qt.AlignCenter)
        self.L_psid_b.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_psid_b.setObjectName("L_psid_b")
        self.L_psid_h = QtWidgets.QLabel(self.centralwidget)
        self.L_psid_h.setGeometry(QtCore.QRect(68, 640, 151, 16))
        self.L_psid_h.setText("")
        self.L_psid_h.setAlignment(QtCore.Qt.AlignCenter)
        self.L_psid_h.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_psid_h.setObjectName("L_psid_h")
        self.L_psid_d = QtWidgets.QLabel(self.centralwidget)
        self.L_psid_d.setGeometry(QtCore.QRect(68, 670, 151, 16))
        self.L_psid_d.setText("")
        self.L_psid_d.setAlignment(QtCore.Qt.AlignCenter)
        self.L_psid_d.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_psid_d.setObjectName("L_psid_d")
        self.I_eupl = QtWidgets.QLineEdit(self.centralwidget)
        self.I_eupl.setGeometry(QtCore.QRect(137, 280, 156, 20))
        self.I_eupl.setObjectName("I_eupl")
        self.L_eupl = QtWidgets.QLabel(self.centralwidget)
        self.L_eupl.setGeometry(QtCore.QRect(15, 285, 116, 12))
        self.L_eupl.setObjectName("L_eupl")
        self.L_v4a_d_v = QtWidgets.QLabel(self.centralwidget)
        self.L_v4a_d_v.setGeometry(QtCore.QRect(255, 670, 436, 16))
        self.L_v4a_d_v.setText("")
        self.L_v4a_d_v.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.L_v4a_d_v.setObjectName("L_v4a_d_v")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MAP-E Address Caculator"))
        self.L_v6p.setText(_translate("MainWindow", "ipv6Prefix"))
        self.L_v6pl.setText(_translate("MainWindow", "ipv6PrefixLength"))
        self.L_v4p.setText(_translate("MainWindow", "ipv4Prefix"))
        self.L_v4pl.setText(_translate("MainWindow", "ipv4PrefixLength"))
        self.L_psidoffset.setText(_translate("MainWindow", "psIdOffset"))
        self.L_eabitl.setText(_translate("MainWindow", "eaBitLength"))
        self.pushButton.setText(_translate("MainWindow", "Caculate"))
        self.L_eup.setText(_translate("MainWindow", "endUserPrefix"))
        self.L_bin.setText(_translate("MainWindow", "BIN"))
        self.L_v6a.setText(_translate("MainWindow", "IPv6 Address:"))
        self.L_v6a_b.setText(_translate("MainWindow", "BIN:"))
        self.L_v4a.setText(_translate("MainWindow", "IPv4 Address"))
        self.L_psid.setText(_translate("MainWindow", "PSID"))
        self.L_bin_2.setText(_translate("MainWindow", "BIN"))
        self.L_hex.setText(_translate("MainWindow", "HEX"))
        self.L_dec.setText(_translate("MainWindow", "DEC"))
        self.L_eupl.setText(_translate("MainWindow", "endUserPrefixLength"))
