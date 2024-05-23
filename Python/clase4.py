# ######################### 1- colecciones 1
# texto = """gordon lanzo su curva&strawberry ha fallado por un pie!
# -grito Joe Castiglione&dos pies -le corrigio
# Troop&strawberry menea la cabeza como disgustado...
# -agrega el comentarista"""

# texto = texto.replace('curva&strawberry', 'curva... \n- Strawberry')
# texto = texto.replace("gordon", "Gordon")
# texto = texto.replace("Castiglione&dos", "Castiglione. \n- Dos")
# texto = texto.replace("Troop&strawberry", "Troop. \n- Strawberry")

# texto2 = list(texto)

# texto2[61]=' '
# texto2[98]=''
# texto2[110]=' '
# texto2[166]=''
# texto2 +='.'

# texto = ''.join(texto2)

# print(texto)

# ######################### 2- colecciones 2
# # Ejemplo 1:
# my_set_1 = set([1, 2, 3])
# my_set_2 = set([3, 4, 5])
# my_new_set = my_set_1.union(my_set_2)
# print(my_new_set)
# # Ejemplo 2:
# my_set_1 = set([1, 2, 3])
# my_set_2 = set([3, 4, 5])
# my_new_set = my_set_1.intersection(my_set_2)
# print(my_new_set)
# # Ejemplo 3:
# my_set_1 = set([1, 2, 3])
# my_set_2 = set([3, 4, 5])
# my_new_set = my_set_1.difference(my_set_2)
# print(my_new_set)

# ######################### 3- colecciones 3
# divisas = {'dolar':'$', 'euro':'€', 'libra':'£'}
# clave = input("Que moneda desea ver?")

# print(divisas.get(clave, "moneda no encontrada"))
