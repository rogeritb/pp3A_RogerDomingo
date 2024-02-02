"""
Roger Domingo Meléndez
Prova pràctica 3
e1.py "MATRIU H"

Implementar
"""
try:
    files = int(input("Digues un nombre senar: "))
    files = files + 1

    columnes = int(input("Digues un nombre senar: "))
    columnes = columnes + 1

    matriu = files and columnes

    if files and columnes % 2 != 0 or files != columnes:
        print("Valors invalids")
    else:
        contador = 0
        print ("1 ", end="")
        for n in range (matriu - 2):
            print("1 ", end= "")
        print("1 ", end= "")
        print("\n", end= "")
        for n in range (matriu - 2):
            print("1", end= "")
            contador = contador + 1
            if contador == (matriu - 1) / 2:
                for n in range (matriu - 2):
                    print(" 1", end= "")
            else:
                for n in range (matriu - 2):
                    print(" 0", end= "")
            print(" 1")
        print("1 ", end= "")
        for n in range (files - 2):
            print("1 ", end= "")
        print("1 ", end= "")
except:
    print("Valors incorrectes")