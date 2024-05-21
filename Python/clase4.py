texto = """gordon lanzo su curva&strawberry ha fallado por un pie!
-grito Joe Castiglione&dos pies -le corrigio
Troop&strawberry menea la cabeza como disgustado...
-agrega el comentarista"""

texto = texto.replace('curva&strawberry', 'curva... \n- Strawberry')
texto = texto.replace("gordon", "Gordon")
texto = texto.replace("Castiglione&dos", "Castiglione. \n- Dos")
texto = texto.replace("Troop&strawberry", "Troop. \n- Strawberry")

texto2 = list(texto)

texto2[61]=' '
texto2[98]=''
texto2[110]=' '
texto2[166]=''
texto2[-1]='a.'

texto = ''.join(texto2)


print(texto)