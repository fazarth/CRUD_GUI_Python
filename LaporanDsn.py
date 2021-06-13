from tkinter import *
from tkinter.ttk import Treeview
import pymysql

window = Tk()
window.title('Data Dosen')
window.geometry("500x320")
window.iconbitmap('icon.ico')

def keluar():
    window.destroy()
def pindah():
    window.destroy()
    import Input

# ==============================================================================
#             TABEL DATA DOSEN

judul_kolom = ("NID","Nama","Alamat","Matakuliah")
class Tabel(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.ShowTable()
        self.place(x=20,y=70)
        btnpindah = Button(window, text="Kembali", command=pindah, bg="whitesmoke", fg="green")
        btnpindah.place(x=20, y=30, width=100)
        btnkeluar = Button(window, text="Keluar", command=keluar, bg="whitesmoke", fg="red")
        btnkeluar.place(x=150, y=30, width=100)
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def ShowTable(self):

        tv = Treeview(self, columns=judul_kolom, show='headings')
        tv.grid(sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM dsn")
        data_table = cursor.fetchall()

        for kolom in judul_kolom:
            tv.heading(kolom, text=kolom)

        tv.column("NID", width=50, anchor="w")
        tv.column("Nama", width=130, anchor="w")
        tv.column("Alamat", width=130, anchor="w")
        tv.column("Matakuliah", width=140, anchor="w")

        for data in data_table:
            tv.insert('', 'end', values=data)

        cursor.close()
        db.close()

Tabel(window)
window.mainloop()

