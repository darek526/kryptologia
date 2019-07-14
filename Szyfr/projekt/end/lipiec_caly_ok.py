#!/usr/bin/python3
#(Shebang)sciężka do interpretera który ma zostać użyty w celu wykonania skryptu
# -*- coding: utf-8 -*-
# ustawiamy kodowanie znaków całego pliku czyli polskie litery
from datetime import timedelta #pobranie modułu time
import random#pobranie modułu random generator liczb pseudolosowych
from tkinter import *#pobranie biblioteki  tkinter umożliwia tworzenie interfejsu graficzneo
from tkinter import messagebox as msb#pobranie modułu z funkcjami do obsługi okien dialogowych
import time
from datetime import timedelta
okno=Tk()#tworzenie okna głownego programu
okno.title("Sieć Feistela")#ustawienie tytułu(nazwy) okna głownego
def losuj_tekst():# definiujemy nową funkcje
    a=[]# definiujemy pustą liste
    b=""# definiujemy pusty string
    for i in range(16):# powtarzamy blok poniżej x 16
        a.append(str(random.randint(0,1)))#dodanie do listy stringów 0 lub 1
        # funkcja randint(losowanie tylko integer z zakresu(0,1)) z modułu random
    b="".join(a)#zamiana listy na ciąg znaków bez spacji
    pobierz_tekst_jawny.delete(0,END)#czyszczenie zawartości pola
    pobierz_tekst_jawny.insert(END,(b))# wysłanie losowej wiadomości do pola
def losuj_klucz():# definiujemy nową funkcje
    c = []# definiujemy pustą liste
    d = ""# definiujemy pusty string
    for i in range(8):# powtarzamy blok poniżej x 8
        c.append(str(random.randint(0, 1)))  #dodanie do listy stringów 0 lub 1
        # funkcja randint(losowanie tylko integer z zakresu(0,1)) z modułu random
    d="".join(c)  # zamiana listy na ciąg znaków bez spacji
    pobierz_klucz.delete(0,END)#czyszczenie zawartości danego pola
    pobierz_klucz.insert(END,(d))# wysłanie losowego klucza do pola
def szyfruj():# definiujemy nową funkcje
    a = (pobierz_tekst_jawny.get())#  a i b aby skrócić poniższe zapisy
    b = (pobierz_klucz.get())
    try:#obsługa błędów
        if len(a) == 16 and int(a, 2) <= (2 ** 16):# sprawdzenie długości tekstu jawnego
            if len(b) == 8 and int(b, 2) <= (2 ** 8):# sprawdzenie długości klucza
                msb.showinfo("ok","Podano poprawny format\n wiadomość i klucza ")# okno informacyjne
                czas_start\
                    = time.monotonic()#start obliczania czasu szyfrowania
                p=int(pobierz_powtorzenia.get())
                while p > 0:
                    lewa = int(a[:8], 2)#pierwsz połowa stringu a, od początku 0 do 8 pozycji (bez 8 strażnik)
                    #2 oznacz zamiane powstałego stringu na liczbe binarną a int zamienia ją odrazu na liczbe dziesiętną
                    prawa = int(a[8:], 2)#jw
                    klucz = int(b, 2)# cały  string zamiana na liczbę binarną a później na dziesiętną
                    lewa_zaszyfr = (prawa)
                    prawa_zaszyfr = lewa ^ (prawa ^ klucz)#xor na liczbach dziesiętnych
                    lewa_zaszyfr = bin(lewa_zaszyfr)#konwersja liczby dziesiętnej na binarną wynik to znów string
                    prawa_zaszyfr = bin(prawa_zaszyfr)# jw
                    lewa_zaszyfr = lewa_zaszyfr[2:]#od 2 pozycji bo pierwsze 2 to oznaczenie 0b ze jest liczba binarna
                    if len(lewa_zaszyfr) < 8: # jeśli mniej niż 8 znaków uzupełniamy od lewej 0 aby było 8 znaków
                        lewa_zaszyfr = "0" * (8 - int(len(lewa_zaszyfr))) + (lewa_zaszyfr)
                    prawa_zaszyfr = prawa_zaszyfr[2:]# jw
                    if len(prawa_zaszyfr) < 8: #mniej niż 8 znaków
                        prawa_zaszyfr = "0" * (8 - int(len(prawa_zaszyfr))) + (prawa_zaszyfr)
                    p -= 1
                    a=(lewa_zaszyfr + prawa_zaszyfr)
                wynik = lewa_zaszyfr + prawa_zaszyfr# konkatenacja stringów
                wynik = "Wiadomość po zaszyfrowaniu \n" + wynik
                pokaz_tekst_zaszyfrowany["text"]=""# pusty ciąg znaków
                pokaz_tekst_zaszyfrowany["text"] = wynik#przekierowujemy string wynik jako text do okna
                czas_stop = time.monotonic()#koniec obliczania czasu szyfrowania
                czas = (czas_stop - czas_start)#czas szyfrowania
                czas_szyfrowania["text"] = ""  # pusty ciąg znaków
                czas_szyfrowania["text"] = "Czas szyfrowania: \n{:.6f} [s]".format(czas)
                #wyswietla czas szyfrowania w sekundach 6 miejsc po przecinku
            else:
                msb.showerror("Błąd","Nieodpowiednia ilość \nznakóœ klucza. Proszę poprawić")
                #okno z komunikatem o błędzie podanego klucza
        else:
            msb.showerror("Błąd","Nieodpowiednia ilość \nznaków wiadomości jawnej. \nProszę poprawić")
            # okno z komunikatem o błędzie podanej wiadomości
    except ValueError:
        msb.showerror("Błąd","nie używamy liter.\nProszę poprawic")

def deszyfruj():# definiujemy nową funkcje
    a = (pobierz_szyfr.get())# a i b aby skrócić poniższe zapisy
    b = (pobierz_klucz2.get())
    try:#obsługa błędów
        if len(a) == 16 and int(a, 2) <= (2 ** 16):#sprawdzenie długości szyfru
            if len(b) == 8 and int(b, 2) <= (2 ** 8):# sprawdzenie długości klucza
                msb.showinfo("ok","Podano poprawny format\n wiadomość i klucza ")# okno informacyjne
                czas_start = time.monotonic()#początek liczenia czasu
                p = int(pobierz_powtorzenia.get())#zamiana stringu na int
                while p > 0:#pętla licząca ilość szyfrowań
                    lewa = int(a[:8], 2)#pierwsz połowa stringu a, od początku 0 do 8 pozycji (bez 8 strażnik)
                    #2 oznacz zamiane powstałego stringu na liczbe binarną a int zamienia ją odrazu na liczbe dziesiętną
                    prawa = int(a[8:], 2)# jw
                    klucz = int(b, 2)# cały klucz string zamiana na liczbę binarną a później na dziesiętną
                    prawa_odszyfr = (lewa)
                    lewa_odszyfr = prawa ^ (lewa ^ klucz)#xor na liczbach dziesiętnych
                    lewa_odszyfr = bin(lewa_odszyfr)#konwersja liczby dziesiętnej na binarną wynik to znów string
                    prawa_odszyfr = bin(prawa_odszyfr)# jw
                    lewa_odszyfr = lewa_odszyfr[2:]#od 2 pozycji bo pierwsze 2 to oznaczenie 0b ze jest liczba binarna
                    if len(lewa_odszyfr) < 8:  # mniej niż 8 znaków dodajemy tyle 0 ile znaków brakuje
                        lewa_odszyfr = "0" * (8 - int(len(lewa_odszyfr))) + (lewa_odszyfr)
                    prawa_odszyfr = prawa_odszyfr[2:]
                    if len(prawa_odszyfr) < 8:# mniej niż 8 znaków dodajemy tyle 0 ile znaków brakuje
                        prawa_odszyfr = "0" * (8 - int(len(prawa_odszyfr))) + (prawa_odszyfr)
                    p -= 1
                    a = (lewa_odszyfr + prawa_odszyfr)
                wynik = lewa_odszyfr + prawa_odszyfr# konkatenacja stringów
                wynik = "Wiadomość po odszyfrowaniu \n" + wynik
                pokaz_tekst_odszyfrowany["text"]=""# pusty ciąg znaków
                pokaz_tekst_odszyfrowany["text"] = wynik#przekierowujemy string wynik jako text do okna
                czas_stop = time.monotonic()# koniec liczenia czasu
                czas = (czas_stop - czas_start)#czas szyfrowanai
                czas_deszyfrowania["text"] = ""  # pusty ciąg znaków
                czas_deszyfrowania["text"] = "Czas deszyfrowania: \n{:.6f} [s]".format(czas)
                # wyswietla czas deszyfrowania w sekundach 6 miejsc po przecinku
            else:
                msb.showerror("Błąd","Nieodpowiednia ilość \nznaków klucza. Proszę poprawić")
                #okno z komunikatem o błędzie podanego klucza
        else:
            msb.showerror("Błąd","Nieodpowiednia ilość \nznaków wiadomości zaszyfrowanej. \nProszę poprawić")
            # okno z komunikatem o błędzie podanej ilości znaków
    except ValueError:# okno z komunikatem o wpisanym błędnym typie
        msb.showerror("Błąd","Nie używamy liter.\nProszę poprawic")
def koniec():# definiujemy nową funkcje
    if msb.askokcancel("Pytanie", "Czy na pewno kończymy pracę"):
        # okno dialogowe z przyciskami ok i cancel - zwraca prawdę, gdy ok jest wciśnięte
        msb.showinfo("Info","Koniec, żegnam")
        okno.destroy()#zamyka nasze okno i cały program
    else:
        msb.showinfo("Info","Ok, popracujmy dalej")#powrót do okna programu
def kasowanie():# czyszczenie zawartości poszczególnych pól i okien
    pobierz_tekst_jawny.delete(0, END)
    pobierz_klucz.delete(0,END)
    pobierz_powtorzenia.delete(0, END)
    pobierz_szyfr.delete(0,END)
    pobierz_klucz2.delete(0,END)
    czas_szyfrowania["text"] = ""
    czas_deszyfrowania["text"] = ""
    pokaz_tekst_zaszyfrowany["text"]=""
    pokaz_tekst_odszyfrowany["text"] = ""
#definiowanie etykiet tresc
tekst_jawny = Label(okno, text ="Wpisz wiadomość 16 bitów")
klucz = Label(okno, text = "Wpisz klucz,8 bitów")
powtorzenia = Label(okno, text = "Wpisz ilość powtórzeń szyfrowań")
pokaz_tekst_zaszyfrowany = Label(okno)
tekst_zaszyfrowany = Label(okno,text = "Wiadomość zaszyfrowana")
czas_szyfrowania = Label(okno)
szyfr = Label(okno, text ="Wpisz wiadomość zaszyfrowaną")
klucz2 = Label(okno, text = "Wpisz klucz,8 bitów")
pokaz_tekst_odszyfrowany = Label(okno)
czas_deszyfrowania = Label(okno)
#definiowanie pola do wpisywania długość
pobierz_tekst_jawny = Entry(okno,width=16)
pobierz_klucz = Entry(okno,width=8)
pobierz_powtorzenia = Entry(okno, width=8)
pobierz_szyfr = Entry(okno,width=16)
pobierz_klucz2 = Entry(okno,width=8)
#aktywacja położenia etkiet i pól wpisywania tekstu wiersze i kolumny
tekst_jawny.grid(row = 0)
klucz.grid(row = 1)
pobierz_tekst_jawny.grid(row = 0, column = 1)
pobierz_klucz.grid(row = 1,column = 1)
powtorzenia.grid(row = 0, column = 2)
pobierz_powtorzenia.grid(row = 1,column = 2)
pokaz_tekst_zaszyfrowany.grid(row = 4, column = 1)
czas_szyfrowania.grid(row = 4, column = 2)
szyfr.grid(row = 6)
klucz2.grid(row = 7)
pobierz_szyfr.grid(row = 6, column = 1)
pobierz_klucz2.grid(row = 7, column = 1)
pokaz_tekst_odszyfrowany.grid(row=8, column=1)
czas_deszyfrowania.grid(row = 8, column = 2)
#definiowanie przycisków nazwy, położenie, uruchamiane funkcje
przycisk1 = Button(okno,text = "Szyfruj wiadomość", command = szyfruj)
przycisk1.grid(row = 4, column = 0)
przycisk2 = Button(okno, text = "Deszyfruj widomość", command = deszyfruj)
przycisk2.grid(row = 8, column = 0)
przycisk3 = Button(okno, text = "Losowanie wiadomości", command = losuj_tekst)
przycisk3.grid(row = 2, column = 0)
przycisk4 = Button(okno, text = "Losowanie klucza", command = losuj_klucz)
przycisk4.grid(row = 2, column = 1)
przycisk5 = Button(okno,text = "Zamknij program", command = koniec)
przycisk5.grid(row = 9, column = 1)
przycisk6 = Button(okno,text = "Wyczyść wszystkie pola",command = kasowanie)#
przycisk6.grid(row = 9)
okno.mainloop()#włączamy pętle okna głownego"
