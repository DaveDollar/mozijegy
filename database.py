import sqlite3

class DatabaseManager:

    def __init__(self, path: str) -> None:
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()

        def create_database(self):
            try:
                self.cursor.execute("SELECT * FROM Termek")
                return
            except Exception:
                termek = """CREATE TABLE Termek (
                    Terem_szama INT PRIMARY KEY,
                    Vetitettfilm VARCHAR(40) NOT NULL,
                    Kapacitas INT NOT NULL );"""
                self.cursor.execute(termek)
                foglalasok = """CREATE TABLE Foglalasok (
                Sorszam INT AUTO_INCREMENT PRIMARY KEY,
                Kernev TEXT NOT NULL,
                Veznev TEXT NOT NULL,
                Teremszam INT NOT NULL,
                Szekszam INT NOT NULL,
                FOREIGN KEY (Teremszam) REFERENCES Termek(Terem_szama) );"""
                self.cursor.execute(foglalasok)

        def add_terem(self, tszam: int, nev: str, kap: int):
            command = f"""INSERT INTO film VALUES ('{tszam}','{nev}','{kap})"""
            self.cursor.execute(command)
            self.connection.commit()

        def add_foglalas(self, ker: str, vez: str, tszam: int, szek: int):
            command = f"""INSERT INTO rendezo VALUES (NULL,'{ker}','{vez}','{tszam}','{szek}')"""
            self.cursor.execute(command)
            self.connection.commit()

        def search(self, attributes: str, table: str, extra: str):
            command = f"""SELECT {attributes} FROM {table} {extra}"""
            try:
                self.cursor.execute(command)
                return self.cursor.fetchall()
            except sqlite3.OperationalError:
                print(command)

#path = "J:\IKT-1\Mozijegy\mozijegy\mozitown.db"