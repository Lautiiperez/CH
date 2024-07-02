class Cliente:
    def __init__(self, nombre, email, direccion, telefono):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)