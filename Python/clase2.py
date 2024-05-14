######################### 1- Desafio de Listas
lista_1 = [1,2,3]
lista_2 = ["la", "uti", 123] 

lista_1.append(456789)
lista_1 +=("Hola mundo")

lista_2.append("Hola y adios")
lista_2 +=(5555)

lista_3 = lista_1[0:-1]
lista_4 = lista_2[1:-1]

lista_5 = lista_4 + lista_3

print (lista_1, "---", lista_2, "---", lista_3, "---", lista_4, "---", lista_5)


######################## 1- Desafio de Tuplas
tupla= (8,15,4,39,5,89,87,19,7,-755,88,123,2,11,15,9,355)

print(tupla[-1]," ,", len(tupla)," ,", tupla.index(87)," ,", list(tupla[-3:])," ,", tupla[9]," ,", tupla.count(7))

