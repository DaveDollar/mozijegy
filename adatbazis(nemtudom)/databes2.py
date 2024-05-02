from tkinter import *
import sqlite3

def init():
    # adatbázis kapcsolat indítása
    global db_kapcsolat, db_kurzor
    print("Csatlakozás az adatbázishoz...")
    db_kapcsolat = sqlite3.connect("filmek.db")
    db_kurzor = db_kapcsolat.cursor()
    res = db_kurzor.execute("SELECT * FROM vetitesek")
    if res.fetchone() is None:
        print("Nincs adatbázis!\nÚj létrehozása és feltöltése...")
        feltolt()

def olvas(mit : tuple, honnan : str, _filter="", kereses="1"):
    # ha csak 2 paramétert adunk meg, akkor az sql kérelem:
    # SELECT [1. paraméter](adat1, adat2, ...) FROM [2. paraméter]tábla;
    # ha megadjuk mind a 4 paramétert, akkor az sql kérelem ez lesz:
    # SELECT [1. paraméter](adat1, adat2, ...) FROM [2. paraméter]tábla WHERE [3. paraméter]adat4=[4. paraméter]valami
    db_kurzor.execute("SELECT {0} FROM {1} WHERE {2}{3}{4}".format(",".join(mit), honnan, _filter, "=" if _filter != "" else " ", kereses))
    oszlopok = db_kurzor.fetchall()
  
    return oszlopok

# bármilyen sql kérelem futtatása
futtat = lambda x: db_kurzor.execute(x)

def hozzaad(tabla : str, oszlopok : tuple, ertekek : tuple):
    # INSERT INTO [1. paraméter] ([2. paraméter]) VALUES ([3. paraméter])
    # az adattípusokat kiírja a program csaxólok
    query = "INSERT INTO '{0}' ({1}) VALUES({2})".format(tabla, ",".join(oszlopok))
    db_kurzor.execute(query, ertekek)
    db_kapcsolat.commit()

def torol(tabla : str, _id="", ertek="1"):
    # 1 paraméter esetén
    # mindent töröl az adott táblából
    # 3 paraméter esetén
    # DELETE FROM [1. paraméter] WHERE [2. paraméter]=[3. paraméter]
    query = "DELETE FROM '{0}' WHERE {1}{2}{3}".format(tabla, _id, "=" if _id != "" else " ", ertek)
    db_kurzor.execute(query)
    db_kapcsolat.commit()

def terem_get(n : int):
    # megszerez nekünk egy adott számú termet az adatbázisból
    return olvas("*", "termek", "terem_id", str(n))

def zar():
    # lezárja az adatbázisos kapcsolatot
    if db_kapcsolat and db_kurzor:
        print("db close")
        db_kurzor.close()
        db_kapcsolat.close()

def feltolt():
    # az adatbázis feltöltése
    db_kurzor.execute(""" CREATE TABLE IF NOT EXISTS 'vetitesek' (
        'vetites_id' integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        'terem' integer NOT NULL,
        'cim' varchar(50) COLLATE BINARY NOT NULL,
        'ido' datetime NOT NULL,
        'mufaj' varchar(10) COLLATE BINARY NOT NULL,
        'jatekido' integer NOT NULL
    );""")

    db_kurzor.execute("""
    CREATE TABLE IF NOT EXISTS 'foglalasok' (
        'foglalas_id' integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        'vezeteknev' varchar(50) COLLATE BINARY NOT NULL,
        'keresztnev' varchar(50) COLLATE BINARY NOT NULL,
        'szekszam' integer NOT NULL,
        'vetites' integer NOT NULL,
        FOREIGN KEY (vetites) REFERENCES 'vetitesek' ('vetites_id') ON DELETE CASCADE ON UPDATE CASCADE
    );""")

    db_kurzor.execute("""
    CREATE TABLE IF NOT EXISTS termek (
        terem_id integer NOT NULL PRIMARY KEY,
        szekek integer NOT NULL
    );
    """)

    db_kurzor.execute("""
    INSERT INTO termek ('terem_id', 'szekek') VALUES
        (1, 50),
        (2, 80),
        (3, 45),
        (4, 42),
        (5, 75)
    """)

    db_kurzor.execute("""INSERT INTO 'vetitesek' ('terem', 'cim', 'ido', 'mufaj', 'jatekido') VALUES
        (1, '13 ÖRDÖGŰZÉS', '2023-03-14 21:30:30', 'HORROR', 104),
        (2, '65', '2023-03-15 00:00:00', 'HORROR', 93),
        (3, 'JOHN WICK: 4. FELVONÁS', '2023-03-16 14:40:00', 'AKCIÓ', 170),
        (4, 'AVATAR: A VÍZ ÚTJA', '2023-03-16 15:00:00', 'KALANDFILM', 193),
        (5, 'CSIZMÁS, A KANDÚR: AZ UTOLSÓ KÍVÁNSÁG', '2023-03-18 15:00:00', 'ANIMÁCIÓ', 102);
    """
    )
    db_kapcsolat.commit()