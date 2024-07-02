from Cliente import Cliente
from Pedido import Pedido

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")
    return Cliente(nombre, email, direccion, telefono)

def crear_pedido(cliente):
    id_pedido = Pedido.contador_pedidos + 1  
    fecha_creacion = input("Ingrese la fecha de creación del pedido (dd/mm/yyyy): ")
    productos = input("Ingrese los productos del pedido separados por coma: ").split(',')
    return Pedido(id_pedido, fecha_creacion, cliente, productos)  

def listar_clientes(clientes):
    for cliente in clientes.values():
        print(cliente.nombre, cliente.email, cliente.direccion, cliente.telefono)

def listar_pedidos(clientes):
    for cliente_id, cliente in clientes.items():
        print(f"\nPedidos de {cliente.nombre}:")
        for pedido in cliente.pedidos:
            print(pedido)

def main():
    clientes = {}
    while True:
        print("\n1. Crear nuevo cliente\n2. Crear nuevo pedido\n3. Listar clientes\n4. Listar pedidos\n5. Salir")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            cliente = crear_cliente()
            clientes[cliente.nombre] = cliente
            print("Cliente creado exitosamente.")
        elif opcion == 2:
            if not clientes:
                print("No hay clientes creados. Por favor, cree un cliente primero.")
            else:
                cliente_nombre = input("Ingrese el nombre del cliente al que pertenece el pedido: ")
                if cliente_nombre in clientes:
                    cliente = clientes[cliente_nombre]
                    pedido = crear_pedido(cliente)
                    cliente.agregar_pedido(pedido)
                    print("Pedido creado exitosamente.")
                else:
                    print("Cliente no encontrado.")
        elif opcion == 3:
            if not clientes:
                print("No hay clientes creados aun.")
            else:
                listar_clientes(clientes)
        elif opcion == 4:
            listar_pedidos(clientes)
        elif opcion == 5:
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
