# lista =[29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]
# for x in lista[:]:
#     if x %2 ==1:
#         lista.remove(x)

# print(lista)

############################# IF

a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = int(input("Para Sumar ingrese: 1\nPara restar igrese: 2\nPara multiplicar ingrese: 3\nPara finalizar ingrese: 4\n"))

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print("Programa finalizado")
else:
    print("La opcion no es correcta")

############################# WHILE

while True:
    a = int(input("Ingrese un numero: "))
    b = int(input("Ingrese otro numero: "))
    c = int(input("Para Sumar ingrese: 1\nPara restar ingrese: 2\nPara multiplicar ingrese: 3\nPara finalizar ingrese: 4\n"))

    if c == 1:
        print(f"Resultado: {a + b}")
    elif c == 2:
        print(f"Resultado: {a - b}")
    elif c == 3:
        print(f"Resultado: {a * b}")
    elif c == 4:
        print("Programa finalizado")
        break
    else:
        print("La opcion no es correcta")