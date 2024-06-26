class Property:
    def __init__(self, id, tipo, estado, precio, fecha_registro):
        self.id = id
        self.tipo = tipo
        self.estado = estado
        self.precio = precio
        self.fecha_registro = fecha_registro

class Client:
    def __init__(self, id, nombre, email, telefono, tipo_preferencia, rango_precio_preferencia):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.tipo_preferencia = tipo_preferencia
        self.rango_precio_preferencia = rango_precio_preferencia

class Agent:
    def __init__(self, id, nombre, email, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

class Contract:
    def __init__(self, id, id_propiedad, id_cliente, id_agente, fecha_inicio, fecha_fin, tipo, monto):
        self.id = id
        self.id_propiedad = id_propiedad
        self.id_cliente = id_cliente
        self.id_agente = id_agente
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo = tipo
        self.monto = monto
