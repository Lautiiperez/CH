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

# 


def mayor_de_edad():
    resultado = ""
    respuesta = input("Ingrese su edad: ")
    edad = None
    
    if '.' in respuesta or ',' in respuesta:
        resultado = "Ingrese una edad válida"
    else:
        edad = int(respuesta)  
    
    if edad is not None:  
        if edad <= 0:
            resultado = "Ingrese una edad válida"
        elif edad >= 18:
            resultado = "Es mayor de edad"
        else:
            resultado = "No es mayor de edad"
    
    return resultado

print(mayor_de_edad())