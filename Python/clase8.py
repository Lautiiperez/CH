# ######################## 1- Welcome

# def bienvenido (ciudad):
#     return print("Hola bienvenido a {}".format(ciudad))

# bienvenido("Carhue")

# ######################## 2- Media

# numeros = [1,5,22,8,6,32,48,6]

# def media (lista):
#     suma = 0
#     for valor in lista:
#         suma += valor
#     return print(suma / len(lista))

# media(numeros)

######################## 3- Multiplo
num1 = int(input("Ingresa un numero: "))
num2 = int(input("ingresa otro un numero: "))

def es_multiplo(num1,num2):
    if (num1%num2) == 0:
        print(num2,"es multiplo de ", num1)
    else:
        print(num2,"NO es multiplo de ", num1)

es_multiplo(num1,num2)
