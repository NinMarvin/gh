import random, string  # Hinzufügen von randotm und strinjg1s


s=int(input('Stellen des Passworts='))  # Wie viel stellen soll das Passwort haben s(Stellen)gkm
print('')  # Eine Leere Zeile augebentgl
#ö
p=[]  # Liste5 Passwort erstellt5ll.
#undh
for i in range(s):  # Die Schleife soll so oft durchlaufen wiegg bei s(Stellen) gewählt
    r=random.choice(string.ascii_letters + string.digits)  # Es werden zufällig string.ascii_letters(groß und klein Buchstaben) und string.digits(Zahlen) erstellt
    p.append(r)  # random an Liste anhängen
        
print('Passwort:') # Passwort: ausgeben 
for i in p:  # Bei jedem Durchlauf wird eine Stelle für die Ausgabe als i nach der Reihe ausgegewählt
    print(i,end='')  # Hier wird jede Stelle der Liste in einer Reihe ausgegeben jede Stelle der Liste bis zur letzten
print()

# goo
