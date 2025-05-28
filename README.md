# 📘 Manajemen Buku – PyQt5 Desktop App

Aplikasi desktop sederhana berbasis **Python + PyQt5 + SQLite** untuk melakukan manajemen data buku. Aplikasi ini mendukung fitur **CRUD (Create, Read, Update, Delete)**, **pencarian real-time**, serta **ekspor data ke CSV** menggunakan custom dialog berbasis PyQt.

---

## 👤 Pembuat

- **Nama**: Rizki Rahman Maulana  
- **NIM**: F1D022093
  
---

## 🎯 Fitur Utama
- ✅ Input data buku (judul, pengarang, tahun)
- ✅ Tabel dinamis QTableWidget dengan scroll area aktif
- ✅ Real-time search berdasarkan judul
- ✅ Edit data via double click
- ✅ Hapus data via menu atau tombol
- ✅ Ekspor data ke CSV via custom dialog ekspor
- ✅ Auto-resize kolom tabel
- ✅ Clipboard integration: tombol "Paste Judul dari Clipboard"
- ✅ Dockable search panel (bisa geser/detach)
- ✅ Status bar berisi nama dan NIM
- ✅ Form input dibungkus QScrollArea agar tetap bisa diakses saat window kecil

---

## 🖼 Tampilan UI

Terdiri dari dua file hasil desain Qt Designer:
- `manajemen_Buku.ui` → tampilan utama (form + tabel + menu)
- `ekspor_CSV.ui` → dialog ekspor data

Sudah dikompilasi jadi:
- `manajemen_Buku.py`
- `ekspor_CSV.py`

---

## 🧠 Struktur Proyek

```
📁 manajemen-buku-app/
├── main.py                 # Main logic aplikasi
├── manajemen_Buku.ui        #file qt designer ui utama
├── manajemen_Buku.py       # Hasil pyuic5 dari .ui utama
├── ekspor_CSV.ui            #file qt designer dialog ekspor
├── ekspor_CSV.py           # Hasil pyuic5 dari dialog ekspor
├── dataku.csv              # hasil ekspor csv
├── buku.db                # Database SQLite (otomatis dibuat)
└── README.md              
```

---
## 📋 Penambahan Fitur Week 11–13

**🔖 QClipboard**

Tombol baru: Paste Judul dari Clipboard

Bisa paste dari aplikasi luar (Notepad, Word, dll)

**🧩 QDockWidget**

Komponen pencarian sekarang berada di panel yang bisa dipindah dan dilepas

Lebih fleksibel dalam layout tampilan

**📢 QStatusBar**

Nama dan NIM pembuat ditampilkan di bagian bawah aplikasi secara permanen

**🖱 QScrollArea**

Form input dibungkus QScrollArea agar tidak overflow saat tampilan kecil

Tabel juga mendukung scroll vertikal & horizontal secara otomatis

---

## 🛠 Cara Menjalankan

1. **Install dependensi:**
```bash
pip install PyQt5
```

2. **Jalankan aplikasi:**
```bash
python main.py
```

---

## 📤 Ekspor CSV

- Pilih menu `File > Ekspor ke CSV` atau tombol `Ekspor`
- Masukkan nama file dan tag (opsional) di dialog
- Pilih lokasi simpan file
- File CSV akan menyimpan seluruh isi tabel buku, lengkap dengan header: `ID, Judul, Pengarang, Tahun`

---

## Hasil Screenshot
1. Buat desain di qt desainer
![Screenshot (862)](https://github.com/user-attachments/assets/5cb74cdd-efb0-4cb7-86cb-78d1e5471bf0)
![Screenshot (863)](https://github.com/user-attachments/assets/6ed2bcb4-9d53-4a79-be7e-92b5fb406779)

2. Convert .ui ke .py
![Screenshot (864)](https://github.com/user-attachments/assets/1eaed455-7816-4677-8f5e-4f5155d39a3f)


3. Tambahkan Logic ke .py yang di convert
![Screenshot (871)](https://github.com/user-attachments/assets/cf10c42f-5454-481b-b3cf-2936f55667d7)


4. Tampilan hasil Run
![Screenshot (865)](https://github.com/user-attachments/assets/f4ccc7a2-91c7-4218-8cab-f540c3d134b7)
![Screenshot (866)](https://github.com/user-attachments/assets/b40d976c-5354-4e1d-80d1-344ce08ec7c6)
![Screenshot (867)](https://github.com/user-attachments/assets/c524ec91-1277-49b3-8ae8-89c86bb2bb9b)
![Screenshot (868)](https://github.com/user-attachments/assets/4e671cc3-8c9c-4426-b716-57491af95a59)
![Screenshot (869)](https://github.com/user-attachments/assets/a3ee79d1-9440-4338-b497-82e7a20d597e)
![Screenshot (879)](https://github.com/user-attachments/assets/23812810-6d20-4269-b6a0-f7ad717ec251)
![Screenshot (880)](https://github.com/user-attachments/assets/fbd65212-6fec-49d0-aa11-68270ea1e64e)
![Screenshot (881)](https://github.com/user-attachments/assets/968b8882-878d-47a4-9398-ecbd1348cd1b)


6. Tampilan csv
![Screenshot (870)](https://github.com/user-attachments/assets/ab5c641b-9658-47ba-919d-26e0814abd31)






