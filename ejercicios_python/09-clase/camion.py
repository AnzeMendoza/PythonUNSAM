class Camion:
    """Clase Camion del ejercicio 9.2"""

    def __init__(self, lotes):
        """Constructor de la clase Camion"""
        self._lotes = lotes

    def __iter__(self):
        """Sobrecarga del metodo iterador"""
        return self._lotes.__iter__()

    def __len__(self):
        """Sobrecarga del metodo len()"""
        return len(self._lotes)

    def __getitem__(self, index):
        """Sobrecarga del metodo index"""
        return self._lotes[index]

    def __contains__(self, nombre):
        """Para el uso del metodo in"""
        return any([lote.nombre == nombre for lote in self._lotes])

    def precio_total(self):
        """Calculo del precio total de productos pertenecientes al camion."""
        return sum([l.costo() for l in self._lotes])

    def contar_cajones(self):
        """Cuenta las especies que hay en el camion."""
        from collections import Counter

        cantidad_total = Counter()
        for l in self._lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
