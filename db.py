import sqlite3

CREATE_TABLE_PWS = "CREATE TABLE IF NOT EXISTS pws (titel TEXT, benutzername TEXT PRIMARY KEY, pw TEXT);"
INSERT_PW = "INSERT INTO pws (titel, benutzername, pw) VALUES (?, ?, ?);"
GET_ALL_PW = "SELECT * FROM pws;"
DELETE_PW = "DELETE FROM pws WHERE titel = ?;"
GET_BENUTZERKONTO = """
SELECT pw FROM pws 
WHERE titel = ? AND benutzername =?;"""
PRUEFE_DOPPELTE_PW = """
SELECT pw
FROM pws
GROUP BY pw
HAVING COUNT (*) >1 ;"""
MIN_LEANGE = """
SELECT *
FROM pws
WHERE length(pw) < 6;"""
LOESCH_DB = "DROP TABLE pws"

def connect():
    return sqlite3.connect("eintrag.db")

def loesch_db(connection):
    with connection:
        connection.execute(LOESCH_DB)

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TABLE_PWS)

def add_pw(connection, titel, benutzername, pw,):
    with connection:
        connection.execute(INSERT_PW, (titel, benutzername, pw))

def get_all_pw(connection):
    with connection:
        return connection.execute(GET_ALL_PW).fetchall()

def min_leange(connection):
    with connection:
        return connection.execute(MIN_LEANGE).fetchall()

def pruefe_doppelte(connection):
    with connection:
        return connection.execute(PRUEFE_DOPPELTE_PW).fetchall()

def delete(connection, titel):
    with connection:
        return connection.execute(DELETE_PW, (titel,)).fetchall()

def get_benutzerkonto(connection, titel, benutzername):
    with connection:
        return connection.execute(GET_BENUTZERKONTO, (titel, benutzername,)).fetchone()
