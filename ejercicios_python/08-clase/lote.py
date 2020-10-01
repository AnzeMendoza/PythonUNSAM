class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def costo(self):
        return self.cajones*self.precio
    
    def vender(self, items):
        self.cajones -= items
        return self.cajones

