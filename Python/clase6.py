# ######################## 1-Generaciones Digitales
# anio = int(input("Ingresa el anio en el que nacises"))

# if 2001 <= anio <= 2010:
#     print("Generación Z")

# elif 1980 <= anio <= 2000:
#     print("Generación Y")

# elif 1965 <= anio <= 1979:
#     print("Generacion X")

# elif 1946 <= anio <= 1964:
#     print("Baby Boomer")
    
# elif 1920 <= anio <= 1940:
#     print("Generación Silenciosa")
# else:
#     print("No existe generacion asociada")

# ######################## 2-Credito Bancario

# edad = int(input("Ingrese su edad: "))
# antiguedad = int(input("Ingrese su Antiguedad en años: "))
# ingreso = int(input("Ingrese su salario en USD: "))

# if edad >=18 and antiguedad >= 3 and ingreso > 2500:
#     print("Credito Aprobado")
# elif edad >= 18 and ingreso >= 4000:
#     print("Credito Aprobado por salario")
# else: 
#     print("Credito no Aprobado")

######################## 3-Marvel Vs. CapCom
nombre = input("Ingrese su nombre: ").title()
preferencia = input("Para Marvel ingresa: M\nPara CapCom ingresa: C\nCual prefieres?: ").upper()

if (preferencia == "M" and nombre[0] <= "M") or (preferencia == "C" and  nombre[0] > "M"):
    print(f"{nombre} Pertenece al grupo A")
else:
    print(f"{nombre} Pertenece al grupo B")

# ######################### Ejercicio en clase
# # Chequeamos si el usuario existe e imprimimos el resultado.

# lista_usuario = ["Jose", "Joel", "Julia", "Itatí", "Lucía", "Luz", "Franco", "Gaspar", "Gabriel", "Germán"]

# usuario = input("Ingrese nombre de usuario: ").title()

# if usuario in lista_usuario:
#     print(f"{usuario} esta dentro de la lista")
# else:
#     print(f"{usuario} no esta dentro de la lista")

