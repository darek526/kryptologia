"""a=int(input("Podaj liczbe binarną"))
b=int(input("Podaj liczbe binarną"))
#a=bin(a)
#b=bin(b)
c=a^b
print(bin(c))"""
klucz = 0b00001111#input("wpisz 8 bitowy klucz: \n")
wiadomosc= 0b0100111011001100#input("wpisz liczbe binarną 16 bitów: \n")
"""print(klucz)
print(bin(klucz))
print(wiadomosc)
print(bin(wiadomosc))"""
#lewa = wiadomosc[:8]
#prawa = wiadomosc[8:]
#print("Lewa  = ",lewa,"\nPrawa = ",prawa)
#lewy_szyfr= prawa

#prawy_szyfr=bin(lewa) ^ bin(prawa) ^ bin(klucz)
#print(bin(prawy_szyfr))
#szyfr = lewy_szyfr + prawy_szyfr
#print("Wiadomosc zaszyfrowana: ", szyfr)
"""
while a != 1 and a != 0:
    a = input("Podaj pierwsza wartosc, 0 lub 1: ")
    if a.isdigit():
        a = int(a)
        if a != 1 and a != 0:
            print("Podales bledna wartosc! Podaj 0 lub 1.")
    else:
        print("Podales litere lub znak! Musisz podac cyfre 0 lub 1.")
while b != 1 and b != 0:
    b = input("Podaj druga wartosc, 0 lub 1: ")
    if b.isdigit():
        b = int(b)
        if b != 1 and b != 0:
            print("Podales bledna wartosc! Podaj 0 lub 1.")
    else:
        print("Podales bledna wartosc! Musisz podac 0 lub 1.")
while dzialanie != 1 and dzialanie != 2 and dzialanie != 3:
    dzialanie = input(
        "\nWybierz, ktora operacje chcesz wykonac: \n 1 - AND\n 2 - OR\n 3 - XOR\n 4 - Wyjscie\n\nTwoj wybor to: \n")
    if dzialanie == "1":
        print("\nWynik dzialania AND wynosi: ")
        print(a and b)
        break
    elif dzialanie == "2":
        print("\nWynik dzialania OR wynosi: ")
        print(a or b)
        break
    elif dzialanie == "3":
        print("\nWynik dzialania XOR wynosi: ")
        print(a ^ b)
        break
    elif dzialanie == "4":
        break
    else:
        print("\nZly wybor!\n")

"""
#input("Aby zakonczyc dzialanie programu naciśnij enter")
