# !/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as msb

okno=Tk()
okno.title("Sieć Feistela")#napis na ramce

def szyfruj():
    a = int(pobierz_tekst_jawny.get())
    b = int(pobierz_klucz.get())
    dodawanie = a + b
    wynik = "wiadomość po zaszyfrowaniu \n{}".format(dodawanie)
    pokaz_tekst_zaszyfrowany = Label(okno, bg="silver")
    pokaz_tekst_zaszyfrowany["text"] = wynik
    pokaz_tekst_zaszyfrowany.grid(row=2, column=1)
def deszyfruj():
    a = int(pobierz_szyfr.get())
    b = int(pobierz_klucz2.get())
    dodawanie = a + b
    wynik = "wiadomość po odszyfrowaniu \n{}".format(dodawanie)
    pokaz_tekst_zaszyfrowany = Label(okno, bg="silver")
    pokaz_tekst_zaszyfrowany["text"] = wynik
    pokaz_tekst_zaszyfrowany.grid(row=6, column=1)
def koniec():
    if msb.askokcancel("Pytanie", "Czy na pewno kończymy pracę"):
        # okno dialogowe z przyciskami ok i cancel - zwraca prawdę, gdy ok jest wciśnięte
        msb.showinfo("Info","Koniec, żegnam")
        okno.destroy()#zamyka nasze okno
    else:
        msb.showinfo("Info","Ok, popracujmy dalej")#powrót do okna

#definiowanie etykiet
tekst_jawny = Label(okno, text ="Wpisz wiadomość, 16 bitów", bg = "silver")
klucz = Label(okno, text = "Wpisz klucz,8 bitów", bg = "silver")
tekst_zaszyfrowany = Label(okno,text = "Wiadomość zaszyfrowana", bg = "silver")
szyfr = Label(okno, text ="Wpisz wiadomość zaszyfrowaną", bg = "silver")
klucz2 = Label(okno, text = "Wpisz klucz,8 bitów", bg = "silver")
#definiowanie pola do wpisywania
pobierz_tekst_jawny = Entry(okno,width=16, bg ="yellow")
pobierz_klucz = Entry(okno,width=8, bg = "yellow")
pobierz_szyfr = Entry(okno,width=16, bg ="yellow")
pobierz_klucz2 = Entry(okno,width=8, bg = "yellow")
#aktywacja położenia etkiet i pól wpisywania tekstu
tekst_jawny.grid(row = 0)
klucz.grid(row = 1)
pobierz_tekst_jawny.grid(row = 0, column = 1)
pobierz_klucz.grid(row = 1,column = 1)
szyfr.grid(row = 4)
klucz2.grid(row = 5)
pobierz_szyfr.grid(row = 4, column = 1)
pobierz_klucz2.grid(row = 5, column = 1)
#definiowanie przycisków nazwy,kolory, położenie
przycisk1 = Button(okno,text = "Szyfruj wiadomość", bg = "green", command = szyfruj)
przycisk1.grid(row = 2, column = 0)
przycisk2 = Button(okno, text = "Deszyfruj widomość", bg = "green", command = deszyfruj)
przycisk2.grid(row = 6, column = 0)
przycisk3 = Button(okno,text = "Zamknij program",bg = "red", command = koniec)
przycisk3.grid(row = 8, column = 1)

okno.mainloop()#włączamy pętle
