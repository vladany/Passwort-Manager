import db
import secrets
import os
import time
import pyperclip
from threading import Thread
from getpass import getpass
from time import sleep

# start des Programms nach Optionen abfragen

gross = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klein = "abcdefghijklmnopqrstuvwxyz"
sonderzeichen = "!""#""$%&'()*+,-./:;<=>?@{|}~"
zahlen = "1234567890"

MENU_PROMPT = """
----------PASSWORTMANAGER---------- \n\
Bitte wähle eine Option: \n\
    1. Füge ein neuen Eintrag hinzu \n\
    2. Siehe alle Einträge ein \n\
    3. Lösche einen alten Eintrag \n\
    4. Ändere Masterpasswort \n\
    5. Prüfe Passwörter nach Duplizität \n\
    6. Prüfe Passwörter, die kürzer als 6 Zeichen sind \n\
    7. Lösche alle Einträge\n\
    8. Suche nach einem Eintrag, um das Passwort zu kopieren
    9. Beenden
Deine Eingabe: """

# Eintrag erfolgreich abgespeichert, frage nach nächster Aktion
MENU_1 = "****Eintrag erfolgreich abgespeichert!****\n\
Bitte wähle eine Option: \n\
    1. Noch ein weiteren Eintrag abspeichern. \n\
    2. Zurück zum Hauptmenü. "

# Eintrag löschen und frage nach nächster Action
MENU_3_ASK = "Wenn du den Eintrag unwiderruflich löschen möchtest, drücke die 1. \n\
Möchtest du zum Hauptmenü oder deine Eingabe verbessern bestätige mit Eingabetaste."
MENU_3_SUCESS = "Eintrag wurde erfolgreich gelöscht! noch einen löschen 3. oder weiter dann eingabe?"
MENU_3_AGAIN = "Noch mal Titel zum löschen eingeben 3. Andernfalls Eingabetaste zum Hauptmenü."
FEHLER = "Upss! Da passt wohl etwas nicht überein. Kehre zum Hauptmenü zurück."

def menu():

    connection = db.connect()
    db.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "9":
        while user_input == "1":
            titel = input("Gebe den Titel ein: ")
            benutzername = input("Gebe den Benutzernamen ein: ")
            genpw = input("Möchtest du, dass dein Passwort automatisch generiert wird dann drücke die 1."
                  "\nWenn du das Passwort selbst eingeben möchtest, dann drücke beliebige Taste.")
            if genpw == "1":
                pw = ""
                # Den Nutzer die verschieden Funktionen zur verfügung stellen!
                laenge = int(input("Bitte gebe die Passwortlänge ein!: "))
                frage = input(
                    "Möchtest du Großbuchstaben,Kleinbuchstaben,Zahlen und Sonderzeichen ,dann drücke die 1.,"
                    "\nwenn du Kleinbuchstaben, Zahlen und Sonderzeichen willst, dann drücke die 2.,"
                    "\nwenn du Zahlen und Sonderzeichen willst, dann drücke die 3.,"
                    "\nwenn du nur Sonderzeichen willst, dann drücke die 4.,"
                    "\nwenn du nur Großbuchstaben willst, dann drücke die 5.,"
                    "\nwenn du nur Kleinbuchstaben willst, dann drücke die 6. ,"
                    "\nwenn du nur Zahlen willst, dann drücke die 7. ,"
                    "\nwenn du Sonderzeichen und Großbuchstaben willst, dann drücke die 8.!"
                    "\nwenn du Sonderzeichen und Kleinbuchstaben willst, dann drücke die 9.!"
                    "\nwenn du Sonderzeichen und Zahlen willst, dann drücke die 10.!"
                    "\nwenn du nur Großbuchstaben und Kleinbuchstaben willst, dann drücke die 11.,"
                    "\nwenn du nur Großbuchstaben und Zahlen willst, dann drücke die 12.,"
                    "\nwenn du nur Kleinbuchstaben und Zahlen willst, dann drücke die 13. ,"
                )
                if frage == "1":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(gross + klein + sonderzeichen + zahlen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "2":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(klein + sonderzeichen + zahlen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "3":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(sonderzeichen + zahlen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "4":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(sonderzeichen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "5":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(gross)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "6":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(klein)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "7":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(zahlen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "8":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(gross + sonderzeichen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "9":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(sonderzeichen + klein)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "10":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(zahlen + sonderzeichen)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "11":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(gross + klein)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "12":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(zahlen + gross)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                elif frage == "13":
                    for _ in range(laenge):
                        pw = pw + secrets.choice(zahlen + klein)
                    db.add_pw(connection, titel, benutzername, pw)
                    user_input = input(MENU_1)
                else:
                    user_input = input(FEHLER)
            else:
                pw = getpass("Gib dein Passwort ein: ")
                db.add_pw(connection, titel, benutzername, pw)
                user_input = input(MENU_1)

        while user_input == "3":
            titel = input("Gebe den Titel ein, den du löschen möchtest: ")
            user_bestatigung = input(MENU_3_ASK) # bei 1. löschen bestätigen bei beliebige taste weiter
            if user_bestatigung == "1":
                db.delete(connection, titel)
                user_input = input(MENU_3_SUCESS) #nochmal löschen 3. oder weiter
            else:
                user_input = input(MENU_3_AGAIN) #nochmal titel zum löschen eigeben oder weiter

        if user_input == "2":
            print("Einträge nach Titel, Benutzername und Passwort sortiert.")
            passworter = db.get_all_pw(connection)
            for k in passworter:
                print(k)

        elif user_input =="4":
            i = 3
            with open("mpw.txt", "r") as f:
                for row in f:
                    if row.split(","):
                        frag = input("Um das Masterpasswort zu ändern, gib bitte das alte Masterpasswort nochmal ein: ")
                        if frag == row:
                            file2 = open('mpw.txt', 'w')
                            passwort = input("Gib dein neues Masterpasswort ein:")
                            file2.write(passwort)
                            file2.close()
                            print("Passwort erfolgreich geändert!")
                        else:
                            while frag != row and i != 0:
                                print("Flasches Passwort! Noch ", i, "Versuche übrig.")
                                frag = input("Gib das Masterpasswort ein: ")
                                i = i - 1
                        if frag == row:
                            file2 = open('mpw.txt', 'w')
                            passwort = input("Gib dein neues Masterpasswort ein:")
                            file2.write(passwort)
                            file2.close()
                            print("Passwort erfolgreich geändert!")
                        else:
                            print("Du hast es zu oft falsch eingegeben. Der Passwort-Manager wird beendet.")
                            sec = 5
                            while sec != 0:
                                sec = sec - 1
                                time.sleep(1)
                                print(sec)
                            exit()
        elif user_input == "5":
            alle_doppelte = db.pruefe_doppelte(connection)
            print(alle_doppelte)
        elif user_input == "6":
            min_len = db.min_leange(connection)
            print(min_len)
        elif user_input == "7":
            frag_nochmal = input("Möchtest du sicher die ganzen Einträge löschen? Dann drücke 1. anderfalls beliebige Taste.")
            if frag_nochmal == "1":
                db.loesch_db(connection)
        elif user_input =="8":
            titel = input("Welchen Titel möchtest du aufrufen? ")
            benutzername = input("Welches Benutzerkonto möchtest du aufrufen? ")
            konto = db.get_benutzerkonto(connection, titel, benutzername)[0]
            pyperclip.copy(konto)
            sec = 30
            frage_timer = input("Möchtest du zum Hauptmenü? Dann Drücke die 1. ")
            while sec != 0 and frage_timer != "1":
                sec = sec - 1
                time.sleep(1)
            pyperclip.copy("")

    print("Das Programm wird beendet in...")
    sec = 4
    while sec != 0:
        sec = sec - 1
        time.sleep(1)
        print(sec)
    exit()

def mpw():
    leer = os.path.getsize("mpw.txt")
    if leer == 0:
        file = open("mpw.txt", "a")
        passwort = input("Gib dein neues Masterpasswort ein:")
        file.write(passwort)
        file.close()
    else:
        i=3
        with open("mpw.txt", "r") as f:
            for row in f:
                if row.split(","):
                    frag = input("Was ist mpw: ")
                    if frag == row:
                        menu()
                    else:
                        while frag != row and i != 0:
                            print("Flasches Passwort! Noch ", i, "Versuche übrig.")
                            frag = input("Was ist mpw: ")
                            i = i-1
                    if frag == row:
                        menu()
                    else:
                        print("Wende dich bitte an den Support!")
                        sec = 5
                        while sec != 0:
                            sec = sec - 1
                            time.sleep(1)
                            print(sec)
                        exit()
def timer():
    k=0
    for i in range(5):
        sleep(1)
    exit()

# t1 = Thread(target=timer)
t2 = Thread(target=mpw)
# t1.start()
t2.start()
