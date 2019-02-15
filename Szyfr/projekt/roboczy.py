# !/usr/bin/python3
# -*- coding: utf-8 -*-
import random
from tkinter import *
from tkinter import messagebox as msb

okno=Tk()
okno.title("Sieć Feistela")#napis na ramce
def losuj_tekst():
    a=[]
    b=""
    for i in range(16):
        a.append(str(random.randint(0,1)))#utworzenie listy stringów
    b="".join(a)#zamiana listy na ciąg znaków bez spacji
    #text_Input.set(operator)
    pobierz_tekst_jawny.delete(0,END)
    pobierz_tekst_jawny.insert(END,(b))
def losuj_klucz():
    c = []
    d = ""
    for i in range(8):
        c.append(str(random.randint(0, 1)))  # utworzenie listy stringów
    d="".join(c)  # zamiana listy na ciąg znaków bez spacji
    pobierz_klucz.delete(0,END)
    pobierz_klucz.insert(END,(d))
def szyfruj():
    a = (pobierz_tekst_jawny.get())
    b = (pobierz_klucz.get())
    while len(a)!=16 or len(b)!=6:
        try:
            if len(pobierz_tekst_jawny) == 16 and int(pobierz_tekst_jawny, 2) <= (2 ** 16):
                if len(pobierz_klucz) == 8 and int(pobierz_klucz, 2) <= (2 ** 8):
                    pass
                    #szyfrogram = prog_szyfr.szyfrowanie(tekst_jawny, klucz, szyfrogram)
                else:
                    msb.showinfo("Nieodpowiednia ilość cyfr klucza. Proszę poprawić")
                    break
            else:
                msb.showinfo("Nieodpowiednia ilość cyfr widomości jawnej. Proszę poprawić")
                break
        except TypeError:
            pass
    else:
        msb.showinfo("Podano odpowiednie wartości")
        #msb.showinfo("Nie używamy liter, tylko 0 lub 1.Proszę poprawić")
    lewa=int(a[:8],2)
    prawa=int(a[8:],2)
    klucz=int(b,2)
    lewa_zaszyfr=(prawa)
    prawa_zaszyfr=lewa^(prawa^klucz)
    lewa_zaszyfr =bin(lewa_zaszyfr)
    prawa_zaszyfr=bin(prawa_zaszyfr)
    wynik = lewa_zaszyfr[2:] + prawa_zaszyfr[2:]
    wynik="wiadomość po zaszyfrowaniu \n" +wynik
    pokaz_tekst_zaszyfrowany["text"] = wynik
def deszyfruj():
    a = (pobierz_szyfr.get())
    b = (pobierz_klucz2.get())
    lewa = int(a[:8], 2)
    prawa = int(a[8:], 2)
    klucz = int(b, 2)
    prawa_odszyfr= (lewa)
    lewa_odszyfr = prawa ^ (lewa ^ klucz)
    lewa_odszyfr = bin(lewa_odszyfr)
    prawa_odszyfr = bin(prawa_odszyfr)
    lewa_odszyfr = lewa_odszyfr[2:]
    if len(lewa_odszyfr) < 8:#mniej niż 8 znaków
        lewa_odszyfr="0" *(8 - len(lewa_odszyfr) + int(lewa_odszyfr))
    prawa_odszyfr = prawa_odszyfr[2:]
    if len(prawa_odszyfr) < 8:
        prawa_odszyfr="0"* (8-len(prawa_odszyfr) + int(prawa_odszyfr))
    wynik = lewa_odszyfr + prawa_odszyfr
    wynik = "wiadomość po odszyfrowaniu \n" + wynik
    pokaz_tekst_zaszyfrowany = Label(okno, bg="silver")
    pokaz_tekst_zaszyfrowany["text"] = wynik
    pokaz_tekst_zaszyfrowany.grid(row=8, column=1)
def koniec():
    if msb.askokcancel("Pytanie", "Czy na pewno kończymy pracę"):
        # okno dialogowe z przyciskami ok i cancel - zwraca prawdę, gdy ok jest wciśnięte
        msb.showinfo("Info","Koniec, żegnam")
        okno.destroy()#zamyka nasze okno
    else:
        msb.showinfo("Info","Ok, popracujmy dalej")#powrót do okna
#definiowanie etykiet
tekst_jawny = Label(okno, text ="Wpisz wiadomość, 16 bitów")
klucz = Label(okno, text = "Wpisz klucz,8 bitów")
pokaz_tekst_zaszyfrowany = Label(okno, bg="silver")
tekst_zaszyfrowany = Label(okno,text = "Wiadomość zaszyfrowana")
szyfr = Label(okno, text ="Wpisz wiadomość zaszyfrowaną")
klucz2 = Label(okno, text = "Wpisz klucz,8 bitów")
#definiowanie pola do wpisywania
pobierz_tekst_jawny = Entry(okno,width=16)
pobierz_klucz = Entry(okno,width=8)
pobierz_szyfr = Entry(okno,width=16)
pobierz_klucz2 = Entry(okno,width=8)
#aktywacja położenia etkiet i pól wpisywania tekstu
tekst_jawny.grid(row = 0)
klucz.grid(row = 1)
pobierz_tekst_jawny.grid(row = 0, column = 1)
pobierz_klucz.grid(row = 1,column = 1)
pokaz_tekst_zaszyfrowany.grid(row=4, column=1)
szyfr.grid(row = 6)
klucz2.grid(row = 7)
pobierz_szyfr.grid(row = 6, column = 1)
pobierz_klucz2.grid(row = 7, column = 1)
#definiowanie przycisków nazwy,kolory, położenie
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
okno.mainloop()#włączamy pętle
