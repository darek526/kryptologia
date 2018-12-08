lista = []  # deklaracja pustej listy
try:
    for x in range(6):
          # lista.extend(input("Podaj bit: "))#dodajemy do listy stringi znaki
        lista.append(int(input("Podaj bit: ")))  # ("Podaj do listy liczb
        if int(input()) != 0 or int(input()) != 1:
             pass
except ValueError:
        print("Pomyliłeś się. tylko 1 lub 0! Spróbuj jeszcze raz")
