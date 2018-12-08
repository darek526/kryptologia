lista=[]
for i in range(4):
    while 1:# pętla nie skończona można wpisac True ten sam efekt każda wartość różna od zera to też prawda
        try:
            a=lista.append(int(input("Wpisz 0 lub 1: \t")))
            break#jeśli jest błąd wyśietla komunikat i wraca do petli while info
            # wpisaniu 0 lub 1  jesli niema błędu break zamyka petle while i wraca do petli for
        except ValueError:
            print ("Pomyliłeś się. Tylko 0 lub 1. Spróbuj jeszcze raz...")
        except UnicodeError:
            print ("Pomyliłeś się. Tylko 0 lub 1. Spróbuj jeszcze raz...")
print(lista)