######################## 1- conversaciones tipos de datos
def conversion(*args):
    if len(args) == 1:
        metros = args[0] / 1000
        centimetros = args[0] / 100
        milimetros = args[0]
        return (metros , centimetros , milimetros)
    elif len(args) == 3:
        metros = args[0] / 1000
        centimetros = args[1] / 100
        milimetros = args[2]
        return (metros + centimetros + milimetros)
    else:
        return "Valores incorrectos"

print(conversion(200, 40, 1))

def cuenta(num):
    num -=1
    if num >0:
        print (num)
        cuenta(num)
    else:
        print("boom")
    print("fin funcion", num)

cuenta(5)