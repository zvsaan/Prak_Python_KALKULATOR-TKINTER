from tkinter import *

window = Tk()
window.title("Kalkulator GUI Dengan Python")
window.geometry('330x400')

# Menambahkan label dan input
lbl = Label(window, text="Masukkan Angka Pertama:", anchor="w")
lbl.grid(column=0, row=1, padx=10, pady=10)

nilai1 = Entry(window, width=15, font=("Arial", 12))
nilai1.grid(column=1, row=1, padx=10, pady=10)

lbl2 = Label(window, text="Masukkan Angka Kedua:", anchor="w")
lbl2.grid(column=0, row=2, padx=10, pady=10)

nilai2 = Entry(window, width=15, font=("Arial", 12))
nilai2.grid(column=1, row=2, padx=10, pady=10)

lbl3 = Label(window, text="Hasil:", anchor="e")
lbl3.grid(column=0, row=4, padx=10, pady=10)

hasil = Label(window, text="0", anchor="w", bg="white", width=15)
hasil.grid(column=1, row=4, padx=10, pady=10)

def tambah():
    hasil.configure(text=(float(nilai1.get()) + float(nilai2.get())))

def kurang():
    hasil.configure(text=(float(nilai1.get()) - float(nilai2.get())))

def kali():
    hasil.configure(text=(float(nilai1.get()) * float(nilai2.get())))

def bagi():
    if float(nilai2.get()) != 0:
        hasil.configure(text=(float(nilai1.get()) / float(nilai2.get())))
    else:
        hasil.configure(text="Error: division by zero")

def pangkat():
    hasil.configure(text=(float(nilai1.get()) ** float(nilai2.get())))

def modulus():
    hasil.configure(text=(float(nilai1.get()) % float(nilai2.get())))

def akar():
    hasil.configure(text=(float(nilai1.get()) ** (1 / float(nilai2.get()))))

def akarbalik():
    hasil.configure(text=(float(nilai2.get()) ** (1 / float(nilai1.get()))))

btn = Button(window, text="Tambah", command=tambah, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=0, row=6, padx=5, pady=5)

btn = Button(window, text="Kurang", command=kurang, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=1, row=6, padx=5, pady=5)

btn = Button(window, text="Kali", command=kali, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=0, row=7, padx=5, pady=5)

btn = Button(window, text="Bagi", command=bagi, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=1, row=7, padx=5, pady=5)

btn = Button(window, text="Pangkat", command=pangkat, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=0, row=8, padx=5, pady=5)

btn = Button(window, text="Modulus", command=modulus, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=1, row=8, padx=5, pady=5)

btn = Button(window, text="Akar", command=akar, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=0, row=9, padx=5, pady=5)

btn = Button(window, text="Akar Balik", command=akarbalik, bg="blue", fg="white", font=("Arial", 12), height=2, width=10)
btn.grid(column=1, row=9, padx=5, pady=5)

window.mainloop()
