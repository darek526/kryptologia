#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# ~/python/04_1_listy.py

"""wiadomosc=[]
wiadomosc=input("wpisz liczbe binarną 16 bitów: \n")
for s in range(16):
    while b != 1 and b != 0:
        b = input("Podaj następną  wartosc, 0 lub 1: ")
        if b.isdigit():
            b = int(b)
            if b != 1 and b != 0:
                print("Podales bledna wartosc! Podaj 0 lub 1.")
        else:
            print("Podales bledna wartosc! Musisz podac 0 lub 1.")

klucz = input("wpisz 8 bitowy klucz: \n")"""
#liczba = input("Podaj liczby oddzielone przecinkami: \n")
def pobranie_wiadomosci():
    lista = [] # deklaracja pustej listy
    dozwolone_znaki = [0,1]
    for x in range(6):
    #lista.extend(input("Podaj bit: "))#dodajemy do listy stringi znaki
        lista.append(int(input("Podaj bit: "))) #("Podaj do listy liczb
        if int(input())==0 or int(input())== 1:
            pass
        else:
            print("Wpisujemy tylko 0 lub 1")
            break
    #if i not in dozwolone_znaki:
     #   print("Wprowadziles zlą wartość tylko 0 lub 1")
      #  break


def pobranie_klucza():
    klucz=[] #deklaracja pustej listy
    for j in range(8):
        klucz.append(int(input("Podaj bit klucza: ")))

        print("Wiadomość jawna = ",lista)
        print("klucz= ", klucz)
def szyfrowanie():
    lewa = lista [:4]
    prawa = lista [4:]

    l_szyfr = prawa
    p_szyfr = lewa #^ prawa ^ klucz
#for i range(8):


    szyfr =l_szyfr + p_szyfr
    print("Wiadomość zaszyfrowana: ", szyfr)