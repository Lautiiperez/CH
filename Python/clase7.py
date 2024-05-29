######################### 1- Solicitud de Nros al usuario
num1 = 0
num2 = 0
total = 0

while True:
    parcial = 0
    total += total
    num1 = input("Ingresa un numero: ")
    if num1 == "exit":
        print(total, " y ", parcial )
        break
    num2 = input("Ingresa un numero: ")
    elif num1 == "exit":
        print(total, " y ", parcial )
        break
    elif type(num2) == int:
        total = num1 + num2
        parcial = num1 + num2
    elif num2 == "exit":
        print(total, " y ", parcial )
        break
    else:
        print("Dato ingresado no valido")

