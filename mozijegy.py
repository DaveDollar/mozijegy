from tkinter import *
import sqlite3

root = Tk()
root.geometry("1200x600")
root.config(bg="#09295c")
root.resizable(False,False)

con = sqlite3.connect("mozitown.db")
cur = con.cursor()

try:
    cur.execute('''CREATE TABLE Mozijegy (
                Sorszam integer PRIMARY KEY,
                Erv_datum DATE NOT NULL,
                Film VARCHAR(40) NOT NULL,
                Sor integer NOT NULL,
                Szek integer NOT NULL);''')
except sqlite3.OperationalError or FileExistsError:
    pass
try:
    cur.execute('''CREATE TABLE Szemely (
                Szem_szam integer PRIMARY KEY,
                Eletkor integer NOT NULL,
                Daik/Nyugdij BOOLEAN);''')
except sqlite3.OperationalError or FileExistsError:
    pass
try:
    cur.execute('''CREATE TABLE Vesz (
                VAZON integer PRIMARY KEY,
                SZID integer NOT NULL,
                MID integer NOT NULL,
                AR VARCHAR(6) NOT NULL,
                V_datum DATE NOT NULL,
                FOREIGN KEY (SZID) REFERENCES Szemely (Szem_szam)
                    ON UPDATE CASCADE
                    ON UPDATE CASCADE
                FOREIGN KEY (MID) REFERENCES Mozijegy (Sorszam)
                    ON UPDATE CASCADE
                    ON UPDATE CASCADE);''')
except sqlite3.OperationalError or FileExistsError:
    pass






con.close()
root.mainloop()