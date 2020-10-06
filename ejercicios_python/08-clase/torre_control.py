class TorreDeControl:
    """Representa a una cola, con operaciones de encolar y desencolar.
    Aplicado a una torre de control de un aeropuerto.
    """

    def __init__(self):
        """Crea dos colas vacias."""
        self.arrivos = []
        self.partidas = []

    def nuevo_arribo(self, nro_vuelo):
        """Encola el elemento nro_vuelo."""
        self.arrivos.append(nro_vuelo)

    def nueva_partida(self, nro_vuelo):
        """Encola el elemento nro_vuelo."""
        self.partidas.append(nro_vuelo)

    def ver_estado(self):
        """Retorna el estado de las listas: arrivos, partidas."""
        print(f'Vuelos esperando aterrizar: {", ".join(self.arrivos)}')
        print(f'Vuelos esperando depegar: {", ".join(self.partidas)}')

    def asignar_pista(self):
        """Es una cola con prioridad, la cual es arrivos, una vez vacia
        sigue con partidas
        """
        if self.esta_vacia():
            print("No hay vuelos en espera.")
        elif len(self.arrivos) > 0:
            print(f"El vuelo {self.arrivos.pop(0)} aterrizó con éxito.")
        elif len(self.partidas) > 0:
            print(f"El vuelo {self.partidas.pop(0)} despego con éxito.")

    def esta_vacia(self):
        """Devuelve
        True si las colas esta vacia,
        """
        return (len(self.partidas) + len(self.arrivos)) == 0


def main():
    print("##### Ejercicio 8.12: Torre de Control #####")
    torre = TorreDeControl()
    torre.nuevo_arribo("AR156")
    torre.nueva_partida("KLM1267")
    torre.nuevo_arribo("AR32")
    torre.ver_estado()

    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()


if __name__ == "__main__":
    main()
