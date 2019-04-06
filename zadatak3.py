lista = [1,6,54,20,32,44,12]

for i in range(2, len(lista),3):
    print(i)
    lista[i]=None
print (lista)