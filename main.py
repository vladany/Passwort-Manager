import os
import sys
import base64

leer = os.path.getsize("mpw.txt")
if leer == 0:
    file = open("mpw.txt", "a")
    passwort = input("Gib neues masterpw ein:")
    file.write(passwort)
    file.close()
else:
    pass

with open("mpw.txt", "r") as f:
    for row in f:
        if row.split(","):
            print(row)
            frag = input("Was ist mpw: ")
            if frag == row:
                print("success")
            else:
                print("lll")
#masterpasswort ändern
file2 = open('mpw.txt', 'w')
passwort = input("Gib neues masterpw ein:")
file2.write(passwort)
file2.close()
