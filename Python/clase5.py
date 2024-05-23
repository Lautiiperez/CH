######################### Expresioens Anidadas
nombre = input("Nombre:")
edad = int(input("Edad:"))

validacion = nombre != "****" and 8 > len(nombre) >= 4 and 20 > edad > 5 and edad*3 > 35

print(validacion)