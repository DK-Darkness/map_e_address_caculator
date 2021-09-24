import sys
from IPy import IP
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_map_caculator import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.caculateAll)

    def caculateAll(self):
        v6prefix = self.I_v6p.text()
        v6prefixLen = self.I_v6pl.text()
        v4prefix = self.I_v4p.text()
        v4prefixLen = self.I_v4pl.text()
        eaBitLen = self.I_eabitl.text()
        psidOffset = self.I_psidoffset.text()
        endUserPrefix = self.I_eup.text()
        endUserPrefixLen = self.I_eupl.text()

        v6prefixBin = IP(v6prefix).strBin()[:int(v6prefixLen)]
        v4prefixBin = IP(v4prefix).strBin()[:int(v4prefixLen)]
        endUserPrefixBin = IP(endUserPrefix).strBin()[:int(endUserPrefixLen)]

        self.L_v6p_b.setText(v6prefixBin)
        self.L_v4p_b.setText(v4prefixBin)
        self.L_eup_b.setText(endUserPrefixBin)


        psidLen = int(v4prefixLen) + int(eaBitLen) - 32


        psidBin = endUserPrefixBin[-psidLen:]
        psidHex = hex(int(psidBin,2))
        psidDec = int(psidBin,2)

        self.L_psid_b.setText(psidBin)
        self.L_psid_h.setText(psidHex)
        self.L_psid_d.setText(str(psidDec))

        ipv4SuffixBin = endUserPrefixBin[-int(eaBitLen):-psidLen]
        ipv4AddrBin = v4prefixBin+ipv4SuffixBin
        ipv4AddrHex = hex(int(ipv4AddrBin,2))
        ipv4AddrDec = str(IP(ipv4AddrHex))

        self.L_v4a_b_v.setText(ipv4AddrBin)
        self.L_v4a_h_v.setText(ipv4AddrHex)
        self.L_v4a_d_v.setText(ipv4AddrDec)

        ipv6AddrBin = v6prefixBin+ipv4SuffixBin+psidBin+'00000000'+'00000000'+ipv4AddrBin+'00000000'+'00'+psidBin+'00000000'
        ipv6Addr = str(IP(hex(int(ipv6AddrBin,2))))

        self.L_v6a_b_v.setText(ipv6AddrBin)
        self.L_v6a_v.setText(ipv6Addr)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())