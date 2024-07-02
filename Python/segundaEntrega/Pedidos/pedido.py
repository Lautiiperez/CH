from Cliente import Cliente

class Pedido:
    contador_pedidos = 0

    def __init__(self, id_pedido, fecha_creacion, cliente, productos):
        self.id_pedido = id_pedido
        self.fecha_creacion = fecha_creacion
        self.cliente = cliente
        self.productos = productos
        Pedido.contador_pedidos += 1

    def __str__(self):
        return f"ID Pedido: {self.id_pedido}, Fecha: {self.fecha_creacion}, Cliente: {self.cliente.nombre}, Productos: {', '.join(self.productos)}"
