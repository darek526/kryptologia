"""
# https://pl.python.org/forum/index.php?topic=5243.0;wap2
#def wprowadzenie_licby_binarnej():
    liczba = input("Wpisz liczbe binarną:\n ")
    #liczba = liczba.upper()
    dozwolone_znaki = ['0', '1']
    for i in range(16):
        if i not in dozwolone_znaki:
            print("Wprowadziles zlą wartość tylko 0 lub 1")
            wprowadzanie_liczby()
    wybor_typu(liczba)
    print(liczba)
    #return (16 * "=" + "Koniec programu" + 16 * "=")
"""
#!/usr/bin/env/usr/bin/python3

def main():
    liczba = "1110001110001110"
    klucz ="10101010"
    print("Wiadomość", liczba)
    print("Zaszyfrowana wiadomosć",szyfruj(liczba))
def wprowadzenie_liczby_binarnej():
    #liczba=input("wpisz liczbe 16 bitową: ")
    liczba = liczba.upper()
    dozwolone_znaki = ['0', '1']
    for i in range(16):
        if i not in dozwolone_znaki:
            print("Wprowadziles zlą wartość tylko 0 lub 1")
            wprowadzanie_liczby()
    print(liczba)
    print(szyfruj(liczba))

def szyfruj(s):#s przekazuje wpisany napis
    """Dzielimy ciąg na strone lewą i prawą"""
    liczba = "1110001110001110"
    klucz ="10101010"
    lewa = liczba[:8]
    prawa = liczba[8:]
    lewa_szyfr = prawa
    prawa_szyfr = lewa #^ prawa ^ klucz
    t=""#zaczynamy od pustego napisu
    for c in s:#przechodz pokoleji łancuch s
        t=c + t#
    return lewa_szyfr + prawa_szyfr#zwraca zaszyfrowaną wiadomść
main()