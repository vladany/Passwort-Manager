import threading
import db
import secrets
import os
import time
# import pyperclip
from getpass import getpass
from time import sleep

START = """
*** Gib das Masterpasswort ein: """
# start des Programms nach Optionen abfragen
START_neu_mpw = """
*** Gib ein neues Masterpasswort ein: """

gross = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
klein = "abcdefghijklmnopqrstuvwxyz"
sonderzeichen = "!""#""$%&'()*+,-./:;<=>?@{|}~"
zahlen = "1234567890"

MENU_PROMPT = """
***************************************************************
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
Deine Eingabe: 

***************************************************************
"""

# Eintrag erfolgreich abgespeichert, frage nach nächster Aktion
MENU_1 = "**** Eintrag erfolgreich abgespeichert! ****\n\
Bitte wähle eine Option: \n\
    1. Noch ein weiteren Eintrag abspeichern. \n\
    Eingabetaste zurück zum Hauptmenü. "
MENU_1_genpw = """
    1. Passwort wird automatisch generiert.
    Eingabetaste, um eigenes Passwort einzutippen."""

# Eintrag löschen und frage nach nächster Action
MENU_3_ASK = """
    1. den Eintrag unwiderruflich löschen.
    Eingabetaste um deine Eingabe zu verbessern oder zurück zum Hauptmenü. """
MENU_3_SUCESS = """
**** Eintrag wurde erfolgreich gelöscht! ****
    3. Um noch einen Eintrag zu löschen. 
    Eingabetaste zurück zum Hauptmenü."""
MENU_3_AGAIN = """
    3. Titel zum löschen eingeben.
    Eingabetaste zurück zum Hauptmenü.
    
"""
MENU_2 = """
*** Einträge nach Titel und Benutzername sortiert. ***"""
MENU_5 = """
*** Einträge, dessen Passwörter mehrfach vorkommen. ***

"""
MENU_6 = """
*** Einträge, dessen Passwörter kürzer als 6 Zeichen sind. ***

"""
MENU_7 = """
    1. Alle Einträge unwiderruflich löschen.
    Eingabetaste züruck zum Hauptmenü. 
"""
MENU_7_SUCCESS = """
*** Alle Einträge erfolgreich gelöscht! ***"""
MENU_8 = """
    1. Zurück zum Hauptmenü.
"""
FEHLER = "Upss! Da passt wohl etwas nicht überein. Eingabetaste zurück zum Hauptmenü."

def menu():

    connection = db.connect()
    db.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "9":
        while user_input == "1":
            titel = input("Gebe den Titel ein: ")
            benutzername = input("Gebe den Benutzernamen ein: ")
            genpw = input(MENU_1_genpw)
            if genpw == "1":
                pw = ""
                # Den Nutzer die verschieden Funktionen zur verfügung stellen!
                laenge = int(input("Bitte gib die Passwortlänge ein: "))
                frage = input(
                    "1. Großbuchstaben,Kleinbuchstaben,Zahlen und Sonderzeichen"
                    "\n2. Kleinbuchstaben, Zahlen und Sonderzeichen willst"
                    "\n3. Zahlen und Sonderzeichen"
                    "\n4. nur Sonderzeichen"
                    "\n5. nur Großbuchstaben"
                    "\n6. nur Kleinbuchstaben"
                    "\n7. nur Zahlen"
                    "\n8. Sonderzeichen und Großbuchstaben"
                    "\n9. Sonderzeichen und Kleinbuchstaben"
                    "\n10. Sonderzeichen und Zahlen"
                    "\n11. Großbuchstaben und Kleinbuchstaben"
                    "\n12. Großbuchstaben und Zahlen"
                    "\n13. Kleinbuchstaben und Zahlen"
                    "\n"
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

        if user_input == "2":
            print(MENU_2) # ausgabe alle einträge mit titel und dem benutzernamen
            passworter = db.get_all_pw(connection)
            for k in passworter:
                print(k)

        while user_input == "3":
            titel = input("Gebe den Titel ein, den du löschen möchtest: ")
            benutzername = input("Gebe den Benutzernamen ein, den du löschen möchtest: ")
            user_bestatigung = input(MENU_3_ASK) # bei 1. löschen bestätigen bei beliebige taste weiter
            if user_bestatigung == "1":
                db.delete(connection, titel, benutzername)
                user_input = input(MENU_3_SUCESS) #nochmal löschen 3. oder weiter
            else:
                user_input = input(MENU_3_AGAIN) #nochmal titel zum löschen eigeben oder weiter

        if user_input =="4":
            i = 3
            with open("mpw.txt", "r") as f:
                for row in f:
                    if row.split(","):
                        frag = getpass("Um das Masterpasswort zu ändern, gib bitte das alte Masterpasswort nochmal ein: ")
                        if frag == row:
                            file2 = open('mpw.txt', 'w')
                            passwort = getpass("Gib dein neues Masterpasswort ein:")
                            file2.write(passwort)
                            file2.close()
                            print("*** Passwort erfolgreich geändert! ***")
                            break
                        else:
                            while frag != row and i != 0:
                                print("Flasches Passwort! Noch ", i, "Versuche übrig.")
                                frag = getpass("Gib das Masterpasswort ein: ")
                                i = i - 1
                            if frag == row:
                                file2 = open('mpw.txt', 'w')
                                passwort = getpass("Gib dein neues Masterpasswort ein:")
                                file2.write(passwort)
                                file2.close()
                                print("*** Passwort erfolgreich geändert! ***")
                            else:
                                print("Du hast es zu oft falsch eingegeben. Der Passwort-Manager wird beendet in ...")
                                sec = 3
                                while sec != 0:
                                    sec = sec - 1
                                    sleep(1)
                                    print(sec)
                                exit()
        elif user_input == "5":
            alle_doppelte = db.pruefe_doppelte(connection)
            print(MENU_5)
            print(alle_doppelte)

        elif user_input == "6":
            min_len = db.min_leange(connection)
            print(MENU_6)
            print(min_len)

        elif user_input == "7":
            frag_nochmal = input(MENU_7)
            if frag_nochmal == "1":
                db.loesch_db(connection)
                print(MENU_7_SUCCESS)

        elif user_input =="8":
            titel = input("Welchen Titel möchtest du aufrufen: ")
            benutzername = input("Welches Benutzerkonto möchtest du aufrufen: ")
            konto = db.get_benutzerkonto(connection, titel, benutzername)[0]
            print(konto)
            frage_timer = ""
            sec = 30
            while frage_timer != "1" and sec != 0:
                sec = 5
                frage_timer = input(MENU_8)
                sec = sec - 1
                sleep(1)
                # pyperclip.copy("")

    print("Das Programm wird beendet in...")
    sec = 4
    while sec != 0:
        sec = sec - 1
        sleep(1)
        print(sec)
    exit()

def mpw():
    leer = os.path.getsize("mpw.txt")
    if leer == 0:
        file = open("mpw.txt", "a")
        passwort = getpass(START_neu_mpw)
        file.write(passwort)
        file.close()
        menu()
    else:
        i=3
        with open("mpw.txt", "r") as f:
            for row in f:
                if row.split(","):
                    frag = getpass(START)
                    if frag == row:
                        menu()
                    else:
                        while frag != row and i != 0:
                            print("Flasches Passwort! Noch ", i, "Versuche übrig.")
                            frag = getpass(START)
                            i = i-1
                    if frag == row:
                        menu()
                    else:
                        print("Wende dich bitte an den Support!")
                        sec = 5
                        while sec != 0:
                            sec = sec - 1
                            sleep(1)
                            print(sec)
                        exit()

def timer():
    global time
    time = 50000

    for i in range(50000):
        time = time - 1
        sleep(1)
    print("*** Schließe den Passwort-Manager! ***")
    quit(mpw())

timer_thread = threading.Thread(target=timer)
timer_thread.start()
mpw()
# pyperclip.copy(konto)

