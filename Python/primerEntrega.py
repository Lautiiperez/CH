# Diccionario para almacenar usuarios
usuarios = {}

# Función para validar la contraseña y el nombre de usuario
def validar_usuario_y_contrasena(usuario, contrasena):
    if len(usuario) < 4 or len(usuario) > 10:
        return False, "El nombre de usuario debe tener entre 4 y 10 caracteres."
    if len(contrasena) < 6:
        return False, "La contraseña debe ser mayor de 6 caracteres."
    if len(contrasena) > 12:
        return False, "La contraseña debe ser menor de 12 caracteres."
    if not any(char.isdigit() for char in contrasena):
        return False, "La contraseña debe contener al menos un número."
    return True, ""

# Función para registrar usuarios
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

# Función para iniciar sesión
def iniciar_sesion(usuario, contrasena=None):
    if usuario in usuarios:
        if contrasena is None:
            contrasena = input("Ingrese la contraseña: ")
        if usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso.")
        else:
            print("Contraseña incorrecta.")
    else:
        continuar = input(f"El usuario '{usuario}' no existe. ¿Desea registrarte? (s/n): ").lower()
        if continuar == 's':
            usuario_registro = input("Ingrese el nombre de usuario para el registro: ")
            contrasena_registro = input("Ingrese la contraseña para el registro: ")
            registrar_usuario(usuario_registro, contrasena_registro)
        else:
            print("No se realizó ninguna acción.")

# Función para guardar usuarios en un archivo de texto
def guardar_usuarios():
    with open('usuarios.txt', 'w') as archivo:
        for usuario, contrasena in usuarios.items():
            archivo.write(f"{usuario}:{contrasena}\n")

# Función para leer usuarios desde un archivo de texto
def leer_usuarios():
    global usuarios
    try:
        with open('usuarios.txt', 'r') as archivo:
            for linea in archivo.readlines():
                usuario, contrasena = linea.strip().split(':')
                usuarios[usuario] = contrasena
        print("Usuarios cargados desde el archivo.")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios. Creando uno nuevo...")

# Función para mostrar usuarios registrados
def mostrar_usuarios():
    print("Usuarios registrados:")
    for usuario in usuarios.keys():
        print(usuario)

# Función principal
def main():
    while True:
        try:
            print("\n1. Ver usuarios registrados\n2. Registrar usuario\n3. Iniciar sesión\n4. Salir")
            opcion = int(input("Seleccione una opción: "))  # Intentamos convertir la entrada a entero
            
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
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")
                
        except ValueError:
            print("Por favor, ingrese un número válido.")  # Capturamos el ValueError y mostramos un mensaje de error

if __name__ == "__main__":
    main()