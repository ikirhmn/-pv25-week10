# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manajemen_Buku.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManajemenBuku(object):
    def setupUi(self, ManajemenBuku):
        ManajemenBuku.setObjectName("ManajemenBuku")
        ManajemenBuku.resize(537, 547)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        ManajemenBuku.setPalette(palette)
        ManajemenBuku.setAutoFillBackground(False)
        ManajemenBuku.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(ManajemenBuku)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 10, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(200, 50, 75, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(227, 227, 227))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.pushButton.setPalette(palette)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: #e3e3e3;   /* Warna biru */\n"
"    color: black;                /* Warna teks */\n"
"    border-radius: 5px;          /* Sudut tombol */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;   /* Warna pas di-hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c6690;   /* Warna pas ditekan */\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 50, 75, 23))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #e3e3e3;   /* Warna biru */\n"
"    color: black;                /* Warna teks */\n"
"    border-radius: 5px;          /* Sudut tombol */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;   /* Warna pas di-hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c6690;   /* Warna pas ditekan */\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 100, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 100, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 140, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 180, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 260, 511, 20))
        self.lineEdit_4.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_4.setDragEnabled(False)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 290, 511, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 220, 75, 23))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #e3e3e3;   /* Warna biru */\n"
"    color: black;                /* Warna teks */\n"
"    border-radius: 5px;          /* Sudut tombol */\n"
"    padding: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #00aa00;   /* Warna pas di-hover */\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #1c6690;   /* Warna pas ditekan */\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 490, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        ManajemenBuku.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ManajemenBuku)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuCari_Judul = QtWidgets.QMenu(self.menubar)
        self.menuCari_Judul.setObjectName("menuCari_Judul")
        ManajemenBuku.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ManajemenBuku)
        self.statusbar.setObjectName("statusbar")
        ManajemenBuku.setStatusBar(self.statusbar)
        self.actionSimpan = QtWidgets.QAction(ManajemenBuku)
        self.actionSimpan.setObjectName("actionSimpan")
        self.actionEkspor_ke_CSV = QtWidgets.QAction(ManajemenBuku)
        self.actionEkspor_ke_CSV.setObjectName("actionEkspor_ke_CSV")
        self.actionKeluar = QtWidgets.QAction(ManajemenBuku)
        self.actionKeluar.setObjectName("actionKeluar")
        self.actionCari_Judul = QtWidgets.QAction(ManajemenBuku)
        self.actionCari_Judul.setObjectName("actionCari_Judul")
        self.actionHapus_Data = QtWidgets.QAction(ManajemenBuku)
        self.actionHapus_Data.setObjectName("actionHapus_Data")
        self.actionAuto_Fill = QtWidgets.QAction(ManajemenBuku)
        self.actionAuto_Fill.setObjectName("actionAuto_Fill")
        self.actionStart_Dictation = QtWidgets.QAction(ManajemenBuku)
        self.actionStart_Dictation.setObjectName("actionStart_Dictation")
        self.menuFile.addAction(self.actionSimpan)
        self.menuFile.addAction(self.actionEkspor_ke_CSV)
        self.menuFile.addAction(self.actionKeluar)
        self.menuCari_Judul.addAction(self.actionCari_Judul)
        self.menuCari_Judul.addAction(self.actionHapus_Data)
        self.menuCari_Judul.addSeparator()
        self.menuCari_Judul.addAction(self.actionAuto_Fill)
        self.menuCari_Judul.addAction(self.actionStart_Dictation)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCari_Judul.menuAction())

        self.retranslateUi(ManajemenBuku)
        QtCore.QMetaObject.connectSlotsByName(ManajemenBuku)

    def retranslateUi(self, ManajemenBuku):
        _translate = QtCore.QCoreApplication.translate
        ManajemenBuku.setWindowTitle(_translate("ManajemenBuku", "MainWindow"))
        self.label.setText(_translate("ManajemenBuku", "Manajemen Buku"))
        self.pushButton.setText(_translate("ManajemenBuku", "Data Buku"))
        self.pushButton_2.setText(_translate("ManajemenBuku", "Ekspor"))
        self.label_2.setText(_translate("ManajemenBuku", "Judul :"))
        self.label_3.setText(_translate("ManajemenBuku", "Pengarang :"))
        self.label_4.setText(_translate("ManajemenBuku", "Tahun :"))
        self.lineEdit_4.setText(_translate("ManajemenBuku", "Cari Judul..."))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("ManajemenBuku", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("ManajemenBuku", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("ManajemenBuku", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("ManajemenBuku", "4"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ManajemenBuku", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ManajemenBuku", "Judul"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ManajemenBuku", "Pengarang"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ManajemenBuku", "Tahun"))
        self.pushButton_3.setText(_translate("ManajemenBuku", "Simpan"))
        self.label_5.setText(_translate("ManajemenBuku", "-Rizki Rahman Maulana/F1D022093-"))
        self.menuFile.setTitle(_translate("ManajemenBuku", "File"))
        self.menuCari_Judul.setTitle(_translate("ManajemenBuku", "Edit"))
        self.actionSimpan.setText(_translate("ManajemenBuku", "Simpan"))
        self.actionEkspor_ke_CSV.setText(_translate("ManajemenBuku", "Ekspor ke CSV"))
        self.actionKeluar.setText(_translate("ManajemenBuku", "Keluar"))
        self.actionCari_Judul.setText(_translate("ManajemenBuku", "Cari Judul"))
        self.actionHapus_Data.setText(_translate("ManajemenBuku", "Hapus Data"))
        self.actionAuto_Fill.setText(_translate("ManajemenBuku", "Auto Fill"))
        self.actionStart_Dictation.setText(_translate("ManajemenBuku", "Start Dictation"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ManajemenBuku()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())