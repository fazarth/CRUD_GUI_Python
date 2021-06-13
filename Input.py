import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title("Data Dosen dan Mahasiswa - Tezza Fazar - 1610631170215")
window.geometry("500x320")
window.iconbitmap('icon.ico')

# ==============================================================================

tabControl = ttk.Notebook(window)

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Input Dosen')

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Input Mahasiswa')

tabControl.pack(expand=1, fill="both")

# ==============================================================================

def bersih():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
# ------------------------------------------------------------------------------
def bersihd():
    e1d.delete(0,END)
    e2d.delete(0,END)
    e3d.delete(0,END)
    e4d.delete(0,END)

# ==============================================================================

def keluar():
    window.destroy()

# ==============================================================================

def cek():

    db = pymysql.connect("localhost", "root", "", "dbpy")
    cursor = db.cursor()

    npm = e1.get()
    sql = "SELECT * FROM mhs WHERE npm = '"+str(npm)+"'"
    notif = cursor.execute(sql)
    data = cursor.fetchall()

    if (notif):
        messagebox.showinfo("Notifikasi !", "Data ditemukan")
        bersih()
    else:
        messagebox.showwarning("Notifikasi !", "Data tidak ditemukan")

    for tp in data:
        e1.insert(END, tp[0])
        e2.insert(END, tp[1])
        e3.insert(END, tp[2])
        e4.insert(END, tp[3])
# ------------------------------------------------------------------------------
def cekd():

    db = pymysql.connect("localhost", "root", "", "dbpy")
    cursor = db.cursor()

    nid = e1d.get()
    sql = "SELECT * FROM dsn WHERE nid = '"+str(nid)+"'"
    notif = cursor.execute(sql)
    data = cursor.fetchall()

    if (notif):
        messagebox.showinfo("Notifikasi !", "Data ditemukan")
        bersihd()
    else:
        messagebox.showwarning("Notifikasi !", "Data tidak ditemukan")

    for tp in data:
        e1d.insert(END, tp[0])
        e2d.insert(END, tp[1])
        e3d.insert(END, tp[2])
        e4d.insert(END, tp[3])

# =============================================================================

def ubah() :
    db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
    cursor = db.cursor()

    npm = e1.get()
    nama = e2.get()
    fakultas = e3.get()
    jurusan = e4.get()

    update=(nama,fakultas,jurusan)
    sql = "UPDATE mhs SET nama=%s, fakultas=%s, jurusan=%s WHERE npm ='"+str(npm)+"'"
    notif = cursor.execute(sql, (update))

    if (notif):
        messagebox.showinfo("Notifikasi !", "Data berhasil diubah")
        bersih()
    else:
        messagebox.showwarning("Notifikasi !", "Data gagal diubah")
# ------------------------------------------------------------------------------
def ubahd() :
    db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
    cursor = db.cursor()

    nid = e1d.get()
    nama = e2d.get()
    alamat = e3d.get()
    matakuliah = e4d.get()

    updated=(nama,alamat,matakuliah)
    sql = "UPDATE dsn SET nama=%s, alamat=%s, matakuliah=%s WHERE nid ='"+str(nid)+"'"
    notif = cursor.execute(sql, (updated))

    if (notif):
        messagebox.showinfo("Notifikasi !", "Data berhasil diubah")
        bersihd()
    else:
        messagebox.showwarning("Notifikasi !", "Data gagal diubah")

# ==============================================================================

def hapus() :
    db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
    cursor = db.cursor()

    npm = e1.get()

    sql = "DELETE FROM mhs WHERE npm ='" + str(npm) + "'"
    notif = cursor.execute(sql)

    if (notif):
        messagebox.showinfo("Notifikasi !", "Data berhasil dihapus")
        bersih()
    else:
        messagebox.showwarning("Notifikasi !", "Data gagal dihapus")
# ------------------------------------------------------------------------------
def hapusd() :
    db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
    cursor = db.cursor()

    nid = e1d.get()

    sql = "DELETE FROM dsn WHERE nid ='" + str(nid) + "'"
    notif = cursor.execute(sql)

    if (notif):
        messagebox.showinfo("Notifikasi !", "Data berhasil dihapus")
        bersihd()
    else:
        messagebox.showwarning("Notifikasi !", "Data gagal dihapus")

# ==============================================================================

def simpan():
    if  e1.get() == "" or e2.get() == "" or e3.get() == "" or e4.get() == "":
        messagebox.showinfo("Notifikasi !", "Data tidak boleh kosong!")

    else :
        db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
        cursor = db.cursor()

        npm = e1.get()
        nama = e2.get()
        fakultas = e3.get()
        jurusan = e4.get()

        msk = (npm, nama, fakultas, jurusan)
        sql = "INSERT INTO mhs(npm, nama, fakultas, jurusan) VALUES" + str(msk)
        notif = cursor.execute(sql)


        if (notif):
            messagebox.showinfo("Notifikasi !", "Data berhasil disimpan")
            bersih()
        else:
            messagebox.showwarning("Notifikasi !", "Data gagal disimpan")
# ------------------------------------------------------------------------------
def simpand():
    if  e1d.get() == "" or e2d.get() == "" or e3d.get() == "" or e4d.get() == "":
        messagebox.showinfo("Notifikasi !", "Data tidak boleh kosong!")
    else :
        db = pymysql.connect("localhost", "root", "", "dbpy", autocommit=True)
        cursor = db.cursor()

        nid = e1d.get()
        nama = e2d.get()
        alamat = e3d.get()
        matakuliah = e4d.get()

        mskd = (nid, nama, alamat, matakuliah)
        sql = "INSERT INTO dsn (nid, nama, alamat, matakuliah) VALUES" + str(mskd)
        notif = cursor.execute(sql)

        if (notif):
            messagebox.showinfo("Notifikasi !", "Data berhasil disimpan")
            bersihd()
        else:
            messagebox.showwarning("Notifikasi !", "Data gagal disimpan")

# ==============================================================================
def laporan():  # 7
    window.destroy()
    import LaporanMhs
# ==============================================================================
def laporand():  # 7
    window.destroy()
    import LaporanDsn
# ==============================================================================
#                  INPUT DATA MAHASISWA

label_0 = Label(tab1, text="Input Data Mahasiswa",width=20,font=("bold", 18))
label_0.place(x=105,y=20)

# ------------------------------------------------------------------------------
l1=Label(tab1, text="NPM")
l1.place(x=50,y=120)

npm_text=StringVar()
e1=Entry(tab1,textvariable=npm_text)
e1.place(x=145,y=120, width=150)

# ------------------------------------------------------------------------------

l2=Label(tab1, text="Nama")
l2.place(x=50,y=160)

nama_text=StringVar()
e2=Entry(tab1,textvariable=nama_text)
e2.place(x=145,y=160, width=150)

# ------------------------------------------------------------------------------

l3=Label(tab1, text="Fakultas")
l3.place(x=50,y=200)

fakultas_text=StringVar()
e3=Entry(tab1,textvariable=fakultas_text)
e3.place(x=145,y=200, width=150)

# ------------------------------------------------------------------------------

l4=Label(tab1, text="Jurusan")
l4.place(x=50,y=240)

jurusan_text=StringVar()
e4=Entry(tab1,textvariable=jurusan_text)
e4.place(x=145,y=240, width=150)

# ------------------------------------------------------------------------------
b1=Button(tab1, text="Simpan", width=14, command=simpan, bg="whitesmoke", fg="green")
b1.place(x=52,y=70)

b2=Button(tab1, text="Cek", width=14, command=cek, bg="whitesmoke", fg="blue")
b2.place(x=180,y=70)

b3=Button(tab1, text="Hapus", width=6, command=hapus, bg="whitesmoke", fg="red")
b3.place(x=360,y=117, height=23, width=60)

b4=Button(tab1, text="Ubah", width=6, command=ubah, bg="whitesmoke", fg="brown")
b4.place(x=360,y=157, height=23, width=60)

b5=Button(tab1, text="Bersih", width=6, command=bersih, bg="whitesmoke", fg="violet")
b5.place(x=360,y=197, height=23, width=60)

b6=Button(tab1, text="Keluar", width=6, command=keluar, bg="whitesmoke", fg="orange")
b6.place(x=360,y=237, height=23, width=60)

b7=Button(tab1, text="Laporan", width=14, command=laporan, bg="whitesmoke")
b7.place(x=313,y=70)

# ------------------------------------------------------------------------------
# ==============================================================================
#                 INPUT DATA DOSEN

label_1 = Label(tab2, text="Input Data Dosen",width=20,font=("bold", 18))
label_1.place(x=105,y=20)

# ------------------------------------------------------------------------------
l1d=Label(tab2, text="NID")
l1d.place(x=50,y=120)

nid_text=StringVar()
e1d=Entry(tab2,textvariable=nid_text)
e1d.place(x=145,y=120, width=150)

# ------------------------------------------------------------------------------

l2d=Label(tab2, text="Nama")
l2d.place(x=50,y=160)

nama_text=StringVar()
e2d=Entry(tab2,textvariable=nama_text)
e2d.place(x=145,y=160, width=150)

# ------------------------------------------------------------------------------

l3d=Label(tab2, text="Alamat")
l3d.place(x=50,y=200)

alamat_text=StringVar()
e3d=Entry(tab2,textvariable=alamat_text)
e3d.place(x=145,y=200, width=150)

# ------------------------------------------------------------------------------

l4d=Label(tab2, text="Matakuliah")
l4d.place(x=50,y=240)

matakuliah_text=StringVar()
e4d=Entry(tab2,textvariable=matakuliah_text)
e4d.place(x=145,y=240, width=150)

# ------------------------------------------------------------------------------

b1d=Button(tab2, text="Simpan", width=14, command=simpand, bg="whitesmoke", fg="green")
b1d.place(x=52,y=70)

b2d=Button(tab2, text="Cek", width=14, command=cekd, bg="whitesmoke", fg="blue")
b2d.place(x=180,y=70)

b3d=Button(tab2, text="Hapus", width=6, command=hapusd, bg="whitesmoke", fg="red")
b3d.place(x=360,y=117, height=23, width=60)

b4d=Button(tab2, text="Ubah", width=6, command=ubahd, bg="whitesmoke", fg="brown")
b4d.place(x=360,y=157, height=23, width=60)

b5d=Button(tab2, text="Bersih", width=6, command=bersihd, bg="whitesmoke", fg="violet")
b5d.place(x=360,y=197, height=23, width=60)

b6d=Button(tab2, text="Keluar", width=6, command=keluar, bg="whitesmoke", fg="orange")
b6d.place(x=360,y=237, height=23, width=60)

b7d=Button(tab2, text="Laporan", width=14, command=laporand, bg="whitesmoke")
b7d.place(x=313,y=70)

# ------------------------------------------------------------------------------



window.mainloop()