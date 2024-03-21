from tkinter import *
import sqlite3

root = Tk()
root.geometry("1200x600")
root.config(bg="#09295c")
root.resizable(False,False)

con = sqlite3.connect("mozijegy/mozitown.db")
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
                Teremszam INT,
                Szekszam INT,
                CONSTRAINT foglal
                FOREIGN KEY (Teremszam) REFERENCES Termek (Terem_szama)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE);''')
except sqlite3.OperationalError or FileExistsError:
    pass






con.close()
root.mainloop()