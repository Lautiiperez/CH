# Diccionario para simular base de datos
usuarios = {}

# Función que valida la contraseña y usuario
def validar_usuario_y_contrasena(usuario, contrasena):
    if len(usuario) < 4 or len(usuario) > 12:
        return False, "El nombre de usuario debe tener entre 4 y 12 caracteres."
    if len(contrasena) < 6:
        return False, "La contraseña debe ser mayor de 6 caracteres."
    if len(contrasena) > 12:
        return False, "La contraseña debe ser menor de 12 caracteres."
    if not any(char.isdigit() for char in contrasena):
        return False, "La contraseña debe contener al menos un número."
    return True, ""

# Función que registra los usuarios
def registrar_usuario(usuario, contrasena):
    valido, mensaje_error = validar_usuario_y_contrasena(usuario, contrasena)
    if not valido:
        print(mensaje_error)
        return
    if usuario in usuarios:
        print("El usuario ya existe. Por favor, elige otro nombre.")
    else:
        usuarios[usuario] = contrasena
        print(f"Usuario {usuario} registrado exitosamente.")
        guardar_usuarios()

# Función que inicia sesión
def iniciar_sesion(usuario, contrasena=None):
    if usuario in usuarios:
        if contrasena is None:
            contrasena = input("Ingrese la contraseña: ")
        if usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        print("El usuario no existe.")
        continuar = input("¿Desea registrarte? (s/n): ").lower()
        if continuar == 's':
            usuario_registro = input("Ingrese el nombre de usuario para el registro: ")
            contrasena_registro = input("Ingrese la contraseña para el registro: ")
            registrar_usuario(usuario_registro, contrasena_registro)
        else:
            print("No se realizó ninguna acción.")

# Función que guarda los usuarios en un archivo de texto
def guardar_usuarios():
    with open('usuarios.txt', 'w') as archivo:
        for usuario, contrasena in usuarios.items():
            archivo.write(f"{usuario}:{contrasena}\n")

# Función que lee los usuarios del archivo de texto
def leer_usuarios():
    global usuarios
    try:
        with open('usuarios.txt', 'r') as archivo:
            for linea in archivo.readlines():
                usuario, contrasena = linea.strip().split(':')
                usuarios[usuario] = contrasena
        print("Cargando usuarios del archivo...")
        
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.\nCreando un registro nuevo...")

# Función que muestra los usuarios ya registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios.keys():
        print(usuario)

def cambiar_contrasena():
    usuario = input("Ingrese el nombre de usuario: ")
    if usuario not in usuarios:
        continuar = input(f"El usuario '{usuario}' no existe. ¿Desea registrarte? (s/n): ").lower()
        if continuar == 's':
            usuario_registro = input("Ingrese el nombre de usuario para el registro: ")
            contrasena_registro = input("Ingrese la contraseña para el registro: ")
            valido, mensaje_error = validar_usuario_y_contrasena(usuario_registro, contrasena_registro)
            if not valido:
                print(mensaje_error)
                return
            
            usuarios[usuario_registro] = contrasena_registro
            print("Usuario registrado exitosamente.")
        else:
            print("No se realizó ninguna acción.")
            return
    
    # Verificar si el usuario ya tiene una contraseña establecida
    if usuarios[usuario] is None:
        print("El usuario no ha establecido una contraseña aún. Por favor, establezca una contraseña primero.")
        return
    
    contrasena_actual = input("Ingrese la contraseña actual: ")
    if usuarios[usuario]!= contrasena_actual:
        print("La contraseña actual es incorrecta.")
        return
    
    nueva_contrasena = input("Ingrese la nueva contraseña: ")
    valido, mensaje_error = validar_usuario_y_contrasena(usuario, nueva_contrasena)
    if not valido:
        print(mensaje_error)
        return
    
    usuarios[usuario] = nueva_contrasena
    print(f"La contraseña de {usuario} ha sido cambiada exitosamente.")
    guardar_usuarios()

# Función principal (Menu)
def main():
    while True:
        try:
            print("\n1. Ver usuarios registrados\n2. Registrar usuario\n3. Iniciar sesión\n4. Cambiar contraseña\n5. Salir")
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                leer_usuarios()
                mostrar_usuarios()
            elif opcion == 2:
                usuario = input("Ingrese el nombre de usuario: ")
                contrasena = input("Ingrese la contraseña: ")
                registrar_usuario(usuario, contrasena)
            elif opcion == 3:
                usuario = input("Ingrese el nombre de usuario: ")
                iniciar_sesion(usuario)
            elif opcion == 4:
                cambiar_contrasena()
            elif opcion == 5:
                print("Saliendo...")
                break
            else:
                print("Opción inválida. Ingrese una opción del 1 al 5.")
                
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()