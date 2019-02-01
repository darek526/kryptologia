# !/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox as msb

okno=Tk()
okno.title("Szyfr Feistla")#napis na ramce

def szyfruj():
    pass
def deszyfruj():
    pass
def koniec():
    if msb.askokcancel("Pytanie", "Czy na pewno kończymy pracę"):
        # okno dialogowe z przyciskami ok i cancel - zwraca prawdę, gdy ok jest wciśnięte
        msb.showinfo("Info","Koniec, żegnam")
        okno.destroy()#zamyka nasze okno
    else:
        msb.showinfo("Info","Ok, popracujmy dalej")

#definiowanie etykiet
tekst_jawny = Label(okno, text ="Wpisz wiadomość, 16 bitów", bg = "silver")
klucz = Label(okno, text = "Wpisz klucz,8 bitów", bg = "silver")
tekst_zaszyfrowany = Label(okno,text = "Wiadomość zaszyfrowana", bg = "silver")
szyfr = Label(okno, text ="Wpisz wiadomość zaszyfrowaną", bg = "silver")
klucz2 = Label(okno, text = "Wpisz klucz,8 bitów", bg = "silver")
tekst_odszyfrowany =Label(okno, text = "Wiadomość odszyfrowana", bg = "silver")

#definiowanie pola do wpisywania
pobierz_tekst_jawny = Entry(okno,width=16, bg ="yellow")
pobierz_klucz = Entry(okno,width=8, bg = "yellow")
pokaz_tekst_zaszyfrowany= Entry(okno,width=16, bg = "silver")
pobierz_szyfr = Entry(okno,width=16, bg ="yellow")
pobierz_klucz2 = Entry(okno,width=8, bg = "yellow")
pokaz_tekst_odszyfrowany = Entry(okno,width=16, bg = "silver")

#aktywacja położenia etkiet i pól wpisywania tekstu
tekst_jawny.grid(row = 0)
klucz.grid(row = 1)
pobierz_tekst_jawny.grid(row = 0, column = 1)
pobierz_klucz.grid(row = 1,column = 1)
tekst_zaszyfrowany.grid(row =3 )
pokaz_tekst_zaszyfrowany.grid(row = 3, column = 1 )
szyfr.grid(row = 4)
klucz2.grid(row = 5)
pobierz_szyfr.grid(row = 4, column = 1)
pobierz_klucz2.grid(row = 5, column = 1)
tekst_odszyfrowany.grid(row = 7)
pokaz_tekst_odszyfrowany.grid(row = 7, column = 1)

#definiowanie przycisków nazwy,kolory, położenie
przycisk1 = Button(okno,text = "Szyfruj wiadomość", bg = "green", command = szyfruj)
przycisk1.grid(row = 2, column = 1)
przycisk2 = Button(okno, text = "Deszyfruj widomość", bg = "green", command = deszyfruj)
przycisk2.grid(row = 6, column = 1)
przycisk3 = Button(okno,text = "Zamknij program",bg = "red", command = koniec)
przycisk3.grid(row = 8, column = 1)

okno.mainloop()#włączamy pętle
