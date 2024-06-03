# ######################## 1- Welcome

# def bienvenido (ciudad):
#     return print("Hola bienvenido a {}".format(ciudad))

# bienvenido("Carhue")

######################## 2- Media

numeros = [1,5,22,8,6,32,48,6]

def media (lista):
    suma = 0
    for valor in lista:
        suma += valor
    return print(suma / len(lista))

media(numeros)