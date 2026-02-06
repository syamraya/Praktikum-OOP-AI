# 🧠 Modul OOP Python – Battle System  
**Koding dan Kecerdasan Artifisial | Fase F – Kelas XI RPL**

Repository ini berisi **praktikum dan jawaban lengkap Latihan 1–6**
tentang **Pemrograman Berorientasi Objek (OOP)** menggunakan Python.

---

## 📌 Tujuan Pembelajaran
- Memahami konsep dasar OOP
- Menerapkan 4 Pilar OOP
- Membuat program Python yang terstruktur, aman, dan scalable

---

# ✅ JAWABAN LATIHAN 1–6

---

## 🔹 Latihan 1 – Atribut & Object

📸 **Screenshot Hasil Program**  
![Latihan 1](screenshots/latihan1.png)

**Pertanyaan:**  
Apa yang terjadi jika `hero1.hp` diubah menjadi 500 setelah objek dibuat?

**Jawaban:**  
Nilai HP `hero1` akan berubah menjadi 500 tanpa error karena atribut `hp`
bersifat **public** dan dapat diakses langsung dari luar class.

**Kesimpulan:**  
Atribut public fleksibel, tetapi tidak aman jika tidak dikontrol.

---

## 🔹 Latihan 2 – Interaksi Antar Objek

📸 **Screenshot Hasil Program**  
![Latihan 2](screenshots/latihan2.png)

**Pertanyaan:**  
Mengapa parameter `lawan` menerima objek, bukan string?

**Jawaban:**  
Karena objek menyimpan **atribut dan method**, sehingga dapat:
- Mengubah HP lawan
- Memanggil method `diserang()`
- Menjalankan logika game secara nyata

**Kesimpulan:**  
Dalam OOP, **objek berinteraksi dengan objek**, bukan sekadar data.

---

## 🔹 Latihan 3 – Inheritance & `super()`

📸 **Screenshot Error & Output**  
![Latihan 3](screenshots/latihan3.png)

**Error yang muncul:**
AttributeError: 'Mage' object has no attribute 'name'


**Jawaban:**  
Error terjadi karena constructor class induk (`Hero`) tidak dijalankan,
sehingga atribut `name`, `hp`, dan `attack_power` tidak dibuat.

**Peran `super()`:**
- Menjalankan constructor parent
- Menghubungkan data class anak dan induk
- Menjamin pewarisan berjalan dengan benar

---

## 🔹 Latihan 4 – Encapsulation

📸 **Screenshot Uji Encapsulation**  
![Latihan 4](screenshots/latihan4.png)

### 1️⃣ Akses `hero1._Hero__hp`
Nilai HP tetap bisa diakses karena **Name Mangling**, bukan keamanan mutlak.

### 2️⃣ Setter tanpa validasi
HP bisa menjadi negatif dan merusak logika game.

**Kesimpulan:**  
Setter penting untuk menjaga **integritas data**.

---

## 🔹 Latihan 5 – Abstraction & Interface

📸 **Screenshot Error Abstract Class**  
![Latihan 5](screenshots/latihan5.png)

**Error:**
TypeError: Can't instantiate abstract class Hero


**Jawaban:**  
Class `Hero` melanggar kontrak karena tidak mengimplementasikan method
abstract yang diwajibkan oleh `GameUnit`.

**mencetak cetakan:**  
Apa gunanya? Gunanya adalah sebagai Standar atau Blueprint Utama (Contract Provider). GameUnit memastikan bahwa semua unit di dalam game (Hero, Monster, Boss) memiliki struktur yang seragam.
Standarisasi: Menjamin siapa pun yang membuat unit baru pasti menyediakan method serang dan info.
Polimorfisme: Memudahkan kita mengelola banyak objek berbeda dalam satu daftar (list) karena kita sudah yakin semuanya bisa dipanggil dengan perintah yang sama.

---

## 🔹 Latihan 6 – Polymorphism

📸 **Screenshot Polymorphism Loop**  
![Latihan 6](screenshots/latihan6.png)

**Pertanyaan: Apakah program berjalan lancar?**

**Jawaban:**
Ya, program berjalan sangat lancar. Meskipun kita menambah class Healer dan memasukkannya ke dalam list pasukan, baris kode for pahlawan in pasukan: pahlawan.serang() tidak perlu diubah sama sekali. Python secara otomatis mengenali bahwa Healer adalah bagian dari pasukan dan menjalankan method serang miliknya sendiri.

**Kesimpulan:**
Keuntungan utama Polimorfisme adalah fleksibilitas dan skalabilitas. Programmer bisa menambah ratusan karakter baru (seperti Tank, Assassin, atau Support) di masa depan tanpa harus mengutak-atik kode sistem inti (seperti sistem pertarungan atau sistem info). Cukup buat class baru, maka karakter tersebut akan langsung "nyambung" dengan sistem yang sudah ada.

**Konsistensi Penamaan**
**Pertanyaan:**
Apa yang terjadi?

**Jawaban:**
Akan terjadi Error (AttributeError) atau hasil tidak sesuai harapan. Saat loop mencoba memanggil unit.serang(), Python tidak akan menemukan method tersebut pada objek Archer karena namanya sudah diubah menjadi tembak_panah. Jika Archer masih mewarisi Hero, ia mungkin akan menjalankan method serang milik Hero (induk) bukannya tembak_panah.

Mengapa nama harus persis sama? Dalam konsep Polimorfisme, nama method adalah "tombol" yang seragam.

Antarmuka Tunggal: Programmer sistem inti hanya perlu tahu satu nama "tombol" (misal: .serang()) untuk menggerakkan semua jenis karakter.

Kontrak: Nama yang sama memastikan bahwa berbagai objek yang berbeda jenis dapat diperlakukan sebagai satu tipe yang sama dalam sebuah daftar (list). Jika namanya berbeda-beda, kita terpaksa menggunakan banyak if/else untuk mengecek tipe karakter satu per satu, yang mana akan membuat kode menjadi berantakan dan sulit dikelola.
