import sqlite3


connection = sqlite3.connect('database1.py')
cursor = connection.cursor()

def create_database():
    try:
        cursor.execute("SELECT * FROM Termek")
        return
    except Exception:
        termek = """CREATE TABLE Termek (
            Terem_szama INT PRIMARY KEY,
            Vetitettfilm VARCHAR(40) NOT NULL,
            Kapacitas INT NOT NULL );"""
        cursor.execute(termek)
        foglalasok = """CREATE TABLE Foglalasok (
        Sorszam INT AUTO_INCREMENT PRIMARY KEY,
        Kernev TEXT NOT NULL,
        Veznev TEXT NOT NULL,
        Teremszam INT NOT NULL,
        Szekszam INT NOT NULL,
        FOREIGN KEY (Teremszam) REFERENCES Termek(Terem_szama) );"""
        cursor.execute(foglalasok)

def add_terem(tszam: int, nev: str, kap: int):
    command = f"""INSERT INTO film VALUES ('{tszam}','{nev}','{kap})"""
    cursor.execute(command)
    connection.commit()

def add_foglalas(ker: str, vez: str, tszam: int, szek: int):
    command = f"""INSERT INTO rendezo VALUES (NULL,'{ker}','{vez}','{tszam}','{szek}')"""
    cursor.execute(command)
    connection.commit()

def search(attributes: str, table: str, extra: str):
    command = f"""SELECT {attributes} FROM {table} {extra}"""
    try:
        cursor.execute(command)
        return cursor.fetchall()
    except sqlite3.OperationalError:
        print(command)

#path = "J:\IKT-1\Mozijegy\mozijegy\mozitown.db"