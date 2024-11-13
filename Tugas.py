import tkinter as tk  # Mengimpor library tkinter untuk membuat GUI
from tkinter import messagebox  # Mengimpor messagebox untuk menampilkan pesan kesalahan

# Fungsi untuk menghitung dan menampilkan prediksi program studi (prodi)
def hasil_prediksi():
    try:
        total_nilai = 0  # Inisialisasi total Nilai
        for entry in entries:  # Loop melalui setiap input Nilai
            Nilai = int(entry.get())  # Mengambil Nilai dari input sebagai integer
            if not (0 <= Nilai <= 100):  # Memeriksa apakah Nilai antara 0 dan 100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Memunculkan error jika Nilai tidak valid
            total_nilai += Nilai  # Menambahkan Nilai ke total

        # Menghitung rata-rata Nilai
        rata_rata = total_nilai / len(entries)
        
        # Menentukan prodi berdasarkan rata-rata Nilai
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Manajemen"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        # Mengupdate label dengan prediksi prodi dan rata-rata Nilai
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError as ve:  # Jika terjadi ValueError, tampilkan pesan kesalahan
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Inisialisasi window utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Mengatur judul window
root.geometry("500x600")  # Mengatur ukuran window
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang

# Label judul aplikasi
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Times New Roman", 18, "bold"), bg="#f0f0f0")
judul_label.pack(pady=20)  # Menambahkan jarak vertikal

# Frame untuk menampung field input
frame_input = tk.Frame(root, bg="#f0f0f0")
frame_input.pack(pady=10)

# List untuk menampung field input Nilai
entries = []
for i in range(10):  # Loop untuk membuat 10 field input untuk 10 mata pelajaran
    # Label untuk setiap field input
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Times New Roman", 12), bg="#f0f0f0")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Posisi label di sebelah kiri
    # Field input untuk Nilai setiap mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Times New Roman", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Posisi field input di sebelah label
    entries.append(entry)  # Menambahkan field input ke list untuk akses nanti

# Tombol untuk menjalankan prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Times New Roman", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Menambahkan jarak vertikal

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Times New Roman", 14, "italic", "bold"), fg="blue", bg="#f0f0f0")
hasil_label.pack(pady=20)  # Menambahkan jarak vertikal

# Menjalankan main loop untuk menjaga window tetap terbuka
root.mainloop()
