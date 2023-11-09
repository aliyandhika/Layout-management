import tkinter as tk
from tkinter import PhotoImage
from tkinter import Label

def login():
    username = username_entry.get()
    password = password_entry.get()

    # Di sini, Anda bisa menambahkan logika autentikasi, misalnya memeriksa username dan password.
    # Contoh sederhana: jika username dan password benar, Anda bisa menambahkan kode untuk masuk,
    # jika tidak, Anda dapat menampilkan pesan kesalahan.

    if username == "dika" and password == "one comando":
        result_label.config(text="Login berhasil")
    else:
        result_label.config(text="Login gagal")

def create_account():
    # Di sini, Anda bisa menambahkan kode untuk membuat akun baru atau
    # membuka halaman pendaftaran akun.

    result_label.config(text="Buat akun baru")

# Membuat jendela utama
root = tk.Tk()
root.title("Login")

# Membuat label judul
label_title = tk.Label(root, text="Silakan Login")
label_title.pack()

img = PhotoImage(file='burung.png')
img_resize = img.subsample(25,25)
Label(root,image=img_resize,bg='white').pack(pady=6)

# Membuat label dan input untuk username
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Membuat label dan input untuk password
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")  # Untuk menyembunyikan karakter yang dimasukkan
password_entry.pack()

# Tombol untuk login
login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

# Label untuk menampilkan hasil login
result_label = tk.Label(root, text="")
result_label.pack()

# Tautan untuk membuat akun
create_account_label = tk.Label(root, text="Belum punya akun? Buat akun baru.", fg="blue", cursor="hand2")
create_account_label.pack()
create_account_label.bind("<Button-1>", lambda event: create_account())

# Menjalankan aplikasi
root.mainloop()
