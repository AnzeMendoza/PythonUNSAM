class Canguro:
    def __init__(self, nombre):
        """Un Canguro es un marsupial."""

        self.nombre = nombre
        self.contenido_marsupio = []

    def meter_en_marsupio(self, item):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.contenido_marsupio.append(item)

    def __repr__(self):
        return f'Canguro("{self.nombre}": {self.contenido_marsupio})'

    def __str__(self):
        return f"{self.contenido_marsupio}"


class CanguroMalo:
    """Un Canguro es un marsupial."""

    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro."""
        t = [self.nombre + " tiene en su marsupio:"]
        for obj in self.contenido_marsupio:
            s = "    " + object.__str__(obj)
            t.append(s)
        return "\n".join(t)

    def __repr__(self):
        return f'CanguroMalo("{self.nombre}": {self.contenido_marsupio})'

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)


def canguro_bueno():
    madre_canguro = Canguro("Madre")
    cangurito = Canguro("gurito")
    madre_canguro.meter_en_marsupio("billetera")
    madre_canguro.meter_en_marsupio("llaves del auto")
    cangurito.meter_en_marsupio("hola")
    cangurito.meter_en_marsupio("como")
    cangurito.meter_en_marsupio("estas?")
    madre_canguro.meter_en_marsupio(cangurito)

    print(madre_canguro)


def canguro_malo():
    # lo que no tenia es definida su metodo __repr__, por ende
    # solamente imprimia el dato que era y no lo que contenia.
    madre_canguro = CanguroMalo("Madre")
    cangurito = CanguroMalo("gurito")
    madre_canguro.meter_en_marsupio("billetera")
    madre_canguro.meter_en_marsupio("llaves del auto")
    madre_canguro.meter_en_marsupio(cangurito)

    print(madre_canguro)


def main():
    print("Ejercicio 8.11: Canguros buenos y canguros malos")
    print("########### canguros buenos ##############")
    canguro_bueno()
    print("########### canguros malos ###############")
    canguro_malo()


if __name__ == "__main__":
    main()
