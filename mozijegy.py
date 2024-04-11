from tkinter import *
import sqlite3

con = sqlite3.connect("mozitown.db")
cur = con.cursor()
cur.execute('PRAGMA foreign_keys=on;')

try:
    cur.execute('''CREATE TABLE Termek (
                Terem_szama INT PRIMARY KEY,
                Vetitettfilm VARCHAR(40),
                Kapacitas INT);''')
except sqlite3.OperationalError or FileExistsError:
    pass

try:
    cur.execute('''CREATE TABLE Foglalasok (
                Sorszam INT AUTO_INCREMENT PRIMARY KEY,
                Kernev TEXT,
                Veznev TEXT,
                Teremszam INT NOT NULL,
                Szekszam INT,
                FOREIGN KEY (Teremszam) REFERENCES Termek (Terem_szama));''')
except sqlite3.OperationalError or FileExistsError:
    pass
con.commit()

def insert():
    try:
        data1 = (entry1.get(), entry2.get(), entry3.get())
        data2 = (entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get())
        cur.execute('INSERT INTO Termek VALUES (?,?,?);', (data1))
        cur.execute('INSERT INTO Foglalasok VALUES (?,?,?,?,?);', (data2))
        con.commit()
    except:
        pass

def select():
    try:
        for lekeres in cur.execute('SELECT Veznev, Kernev FROM Foglalsok WHERE Teremszam = 1'):
            print(lekeres)
            con.commit()
    except:
        pass

def empty():
    try:
        cur.execute('TRUNCATE TABLE Foglalasok')
        cur.execute('TRUNCATE TABLE Termek')
        con.commit()
    except:
        pass



con.close()

root = Tk()
root.geometry("1200x600")
root.config(bg="#09295c")
root.resizable(False,False)

global entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8

frame1 = LabelFrame(root, text="Termek")
frame2 = LabelFrame(root, text="Foglalasok")

label1 = Label(frame1, text="Terem_szama")
label2 = Label(frame1, text="Vetitettfilm")
label3 = Label(frame1, text="Kapacitas")
entry1 = Entry(frame1)
entry2 = Entry(frame1)
entry3 = Entry(frame1)

label4 = Label(frame2, text="Sorszam")
label5 = Label(frame2, text="Kernev")
label6 = Label(frame2, text="Veznev")
label7 = Label(frame2, text="Teremszam")
label8 = Label(frame2, text="Szekszam")
entry4 = Entry(frame2)
entry5 = Entry(frame2)
entry6 = Entry(frame2)
entry7 = Entry(frame2)
entry8 = Entry(frame2)

gomb1 = Button(root, text="INSERT", command=lambda:insert())
gomb2 = Button(root, text="SELECT", command=lambda:select())
gomb3 = Button(root, text="EMPTY", command=lambda:empty())

frame1.grid(row=0, column=0)
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)

frame2.grid(row=0, column=1)
label4.grid(row=0, column=0)
label5.grid(row=1, column=0)
label6.grid(row=2, column=0)
label7.grid(row=3, column=0)
label8.grid(row=4, column=0)
entry4.grid(row=0, column=1)
entry5.grid(row=1, column=1)
entry6.grid(row=2, column=1)
entry7.grid(row=3, column=1)
entry8.grid(row=4, column=1)

gomb1.grid(row=1, column=0)
gomb2.grid(row=1, column=1)
gomb3.grid(row=2, column=0, columnspan=2)


root.mainloop()