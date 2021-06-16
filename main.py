import db
import stdiomask
import getpass

#start des Programms nach Optionen abfragen

MENU_PROMPT ="""
----------PASSWORTMANAGER---------- \n\
Bitte wähle eine Option: \n\
    1. Füge ein neuen Eintrag hinzu \n\
    2. Siehe alle Einträge ein \n\
    3. Lösche einen alten Eintrag \n\
    4. Ändere Masterpasswort \n\
    5. Prüfe Passwörter nach Duplizität \n\
    6. Prüfe Passwörter, die kürzer als 6 Zeichen sind \n\
    7. Lösche alle Einträge\n\
    8. Beende
Deine Eingabe: """

#Eintrag erfolgreich abgespeichert, frage nach nächster Aktion
MENU_1 ="****Eintrag erfolgreich abgespeichert!****\n\
Bitte wähle eine Option: \n\
    1. Noch ein weiteren Eintrag abspeichern. \n\
    2. Zurück zum Hauptmenü. "

#Eintrag löschen und frage nach nächster Action
MENU_3_ASK = "Wenn du den Eintrag unwiderruflich löschen möchtest, drücke die 1. \n\
Möchtest du zum Hauptmenü oder deine Eingabe verbessern bestätige mit Eingabetaste."
MENU_3_SUCESS = "Eintrag wurde erfolgreich gelöscht! noch einen löschen 3. oder weiter dann eingabe?"
MENU_3_AGAIN = "Noch mal Titel zum löschen eingeben 3. Andernfalls Eingabetaste zum Hauptmenü."

def menu():
    connection = db.connect()
    db.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "9":
        while user_input == "1":
            titel = input("Gebe den Titel ein: ")
            benutzername = input("Gebe den Benutzernamen ein: ")
            pw = input("Gebe das Passwort ein: ")
            db.add_pw(connection, titel, benutzername, pw)
            user_input = input(MENU_1)

        while user_input == "3":
            titel = input("Gebe den Titel ein, den du löschen möchtest: ")
            user_bestatigung = input(MENU_3_ASK) #bei 1. löschen bestätigen bei beliebige taste weiter
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
        elif user_input == "8":

            a = (getpass_ak.getpass('password: '))
        else:
            pass

menu()