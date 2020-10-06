import informe


class Lote:
    """Define la clase de un lote de fruta"""

    def __init__(self, nombre, cajones, precio):
        """Es el constructor de mi clase Lote"""
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def __repr__(self):
        return f'Lote("{self.nombre}",{self.cajones},{self.precio})'

    def costo(self):
        """Calcula el costo por lote de una producto"""
        return self.cajones * self.precio

    def vender(self, items):
        """Actualiza la cantidad del producto que se vendio."""
        self.cajones -= items
        return self.cajones


def main():
    print(f"{'Inicio del enunciado' : ^60}")
    peras = Lote("Pera", 100, 490.1)
    print(peras)
    print(f"{'Fin del enunciado' : ^60}")
    camion = informe.leer_camion("Data/camion.csv")
    print(camion)


if __name__ == "__main__":
    main()
