lista=[]
for i in range(4):
    while 1:
        try:
            lista.append(int(input("Podaj bit: \t")))
            break
        except ValueError:
            print ("Pomyliłeś się. Tylko 0 lub 1. Spróbuj jeszcze raz...")
print(lista)