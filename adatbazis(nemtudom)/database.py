import sqlite3

connection = sqlite3.connect('database1.db')
cursor = connection.cursor()

def create_database():
    try:
        cursor.execute("SELECT * FROM Foglalasok")
        return
    except Exception:
        foglalasok = """CREATE TABLE Foglalasok (
        Sorszam INT AUTO_INCREMENT PRIMARY KEY,
        Film CHAR NOT NULL,
        Szekszam INT NOT NULL,
        Nap DATE NOT NULL,
        Ora TIME NOT NULL);"""
        cursor.execute(foglalasok)

def add_foglalas(Film, Szekszam, Nap, Ora):
    command = f"""INSERT INTO termek VALUES ('{Film}','{Szekszam}','{Nap}','{Ora})"""
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