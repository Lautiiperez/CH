lista =[29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]
for x in lista[:]:
    if x %2 ==1:
        lista.remove(x)

print(lista)