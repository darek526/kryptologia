"""lista=[]
for i in range(4):
    while True:
        try:
            a=lista.append(int(input("Wpisz 0 lub 1: \t")))
            break
            try:
                if 0 <= a <= 1:
                    print("Dziękuję.")
            except:
                print("Spróbuj jeszcze raz tylko  0 lub 1")
        except ValueError:
            print("To musi być cyfra!")
print(lista)
"""
wiadomosc=[]
for i in range(4):
    while True:
        wiadomosc =wiadomosc.append(input("Podaj 1 lub 0").strip())
        if "." in wiadomosc or wiadomosc.isnumeric():
            wiadomosc = int(wiadomosc)
            if 0 <= wiadomosc <= 1:
                print("Dziękuję")
                break
            else:
                print("Spróbuj jeszcze raz, tylko 0 lub 1")
        else:
            # Nie wpisano cyfry
            print("wpisz cyfre!")
print(wiadomosc)
"""
Zamiana liter na kod ascii:
[ord(x) for x in "abc"]#system 10-tny
[hex(ord(x))[2:] for x in "abc"]#system 16-owy
[bin(ord(x))[2:] for x in "abc"]#sytem binarny

"""

