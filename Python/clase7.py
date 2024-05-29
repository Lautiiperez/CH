######################### 1- Solicitud de Nros al usuario
num1 = 0
num2 = 0
total = 0

while True:
    parcial = int(num1) + int(num2)
    total += int(num1) + int(num2)

    num1 = input("Ingresa un numero o exit para terminar: ")
    if num1.lower() == "exit":
        print(total, " y ", parcial )
        break
    num2 = input("Ingresa otro numero para sumarlo: ")
    if num2.lower() == "exit":
        print(total, " y ", parcial )
        break
    
    
    

