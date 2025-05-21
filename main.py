# Versi upgrade: menu bar logic aktif (File, Edit), dan ekspor data lewat dialog ekspor_CSV.py

import sqlite3
import csv
import sys
from PyQt5 import QtWidgets, QtCore
from manajemen_Buku import Ui_ManajemenBuku
from ekspor_CSV import Ui_SimpanCSV

class ExportDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SimpanCSV()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("Pilih Lokasi...")
        self.ui.comboBox.addItem("Local Disk (Manual Path)")

    def get_values(self):
        return {
            "filename": self.ui.lineEdit_3.text().strip(),
            "tag": self.ui.lineEdit_4.text().strip(),
            "location": self.ui.comboBox.currentText()
        }

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ManajemenBuku()
        self.ui.setupUi(self)
        self.db_conn = sqlite3.connect("buku.db")
        self.cursor = self.db_conn.cursor()
        self.selected_id = None

        self.init_db()
        self.setup_ui_logic()
        self.load_data()

    def init_db(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS buku (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                judul TEXT NOT NULL,
                pengarang TEXT NOT NULL,
                tahun TEXT NOT NULL
            )
        """)
        self.db_conn.commit()

    def setup_ui_logic(self):
        self.ui.pushButton_3.clicked.connect(self.save_data)
        self.ui.pushButton_2.clicked.connect(self.export_via_dialog)
        self.ui.tableWidget.itemDoubleClicked.connect(self.load_row_to_form)
        self.ui.lineEdit_4.textChanged.connect(self.search_data)

        # Menu bar actions
        self.ui.actionSimpan.triggered.connect(self.save_data)
        self.ui.actionEkspor_ke_CSV.triggered.connect(self.export_via_dialog)
        self.ui.actionKeluar.triggered.connect(self.close)
        self.ui.actionCari_Judul.triggered.connect(lambda: self.ui.lineEdit_4.setFocus())
        self.ui.actionHapus_Data.triggered.connect(self.delete_selected_row)
        self.ui.actionAuto_Fill.triggered.connect(self.demo_fill)
        self.ui.actionStart_Dictation.triggered.connect(lambda: QtWidgets.QMessageBox.information(self, "Info", "Fitur dictation belum tersedia."))

        header = self.ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def load_data(self, filter_text=""):
        self.ui.tableWidget.setRowCount(0)
        query = "SELECT * FROM buku WHERE judul LIKE ?" if filter_text else "SELECT * FROM buku"
        self.cursor.execute(query, ('%' + filter_text + '%',) if filter_text else ())
        for row_data in self.cursor.fetchall():
            row_number = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def save_data(self):
        judul = self.ui.lineEdit.text().strip()
        pengarang = self.ui.lineEdit_2.text().strip()
        tahun = self.ui.lineEdit_3.text().strip()

        if not (judul and pengarang and tahun):
            QtWidgets.QMessageBox.warning(self, "Warning", "Semua field harus diisi!")
            return

        if self.selected_id:
            self.cursor.execute("UPDATE buku SET judul=?, pengarang=?, tahun=? WHERE id=?",
                                (judul, pengarang, tahun, self.selected_id))
            self.selected_id = None
        else:
            self.cursor.execute("INSERT INTO buku (judul, pengarang, tahun) VALUES (?, ?, ?)",
                                (judul, pengarang, tahun))

        self.db_conn.commit()
        self.clear_form()
        self.load_data()

    def load_row_to_form(self, item):
        row = item.row()
        self.selected_id = int(self.ui.tableWidget.item(row, 0).text())
        self.ui.lineEdit.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.lineEdit_2.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.lineEdit_3.setText(self.ui.tableWidget.item(row, 3).text())

    def clear_form(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()

    def search_data(self, text):
        self.load_data(filter_text=text)

    def delete_selected_row(self):
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            QtWidgets.QMessageBox.warning(self, "Hapus Data", "Pilih data terlebih dahulu.")
            return
        item_id = self.ui.tableWidget.item(current_row, 0).text()
        self.cursor.execute("DELETE FROM buku WHERE id=?", (item_id,))
        self.db_conn.commit()
        self.load_data()

    def demo_fill(self):
        self.ui.lineEdit.setText("Contoh Judul")
        self.ui.lineEdit_2.setText("Anonim")
        self.ui.lineEdit_3.setText("2025")

    def export_via_dialog(self):
        dialog = ExportDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            values = dialog.get_values()
            filename = values["filename"] or "data_buku"
            path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save CSV", f"{filename}.csv", "CSV Files (*.csv)")
            if path:
                self.cursor.execute("SELECT * FROM buku")
                rows = self.cursor.fetchall()
                with open(path, "w", newline="", encoding="utf-8") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["ID", "Judul", "Pengarang", "Tahun"])
                    writer.writerows(rows)
                QtWidgets.QMessageBox.information(self, "Export Sukses", f"Data berhasil diekspor ke {path}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())

