######################## 1- Mi primer programa
nombre = input("Escribe tu Nombre:")
apellido = input("Escribe tu Apellido:")
edad = int(input("Escribe tu Edad:"))

print(nombre ," ", apellido , " tiene " , edad , " años.")


######################## 2- Desafio String
cadena_1 = "versatil"
cadena_2 = "Python"
cadena_3 = "es un lenguaje"
cadena_4 = "de programacion"

frase = cadena_2 + " "+ cadena_3 + " " + cadena_4 +" "+ cadena_1

print(frase)


######################## 3- Desafio Numeros
partidos_ganados = int(input("Cuantos partidos gano?"))
partidos_empatados = int(input("Cuantos partidos empato?"))
partidos_perdidos = int(input("Cuantos partidos perdio?"))

total_partidos = partidos_ganados+partidos_empatados+partidos_perdidos

resultado = ((partidos_ganados * 3) + partidos_empatados + (partidos_perdidos * 0))/(total_partidos)

if (total_partidos) > 20:
    print("La cantidad maxima de partidos debe ser 20")
else: 
    print("El promedio es: " + str(resultado))


######################## 4- Desafio Slicing
cadena = "acitametaM ,5.8 ,otipeP ordeP"
cadena_volteada = cadena[::-1]

nombre_alumno = cadena_volteada[0:12]
nota = cadena_volteada[14:17]
materia = cadena_volteada[19:29]

print(nombre_alumno,"a sacado un",nota,"en",materia)


######################## 5- Mi primer programa en Python
nota_1 = int(input("Nota N°1:"))
nota_2 = int(input("Nota N°2:"))
nota_3 = int(input("Nota N°3:"))

nota_final = (nota_1 * 0.2) + (nota_2 * 0.3) + (nota_3 * 0.5)
print("la nota final es: ", nota_final)