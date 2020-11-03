from vigilante import vigilar
import csv


def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]


def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def filtrar_datos(filas, nombres):
    for fila in filas:
        if fila["nombre"] in nombres:
            yield fila


def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, float])
    rows = hace_dicts(rows, ["nombre", "precio", "volumen"])
    return rows


def ticker(path_camion, path_log, fmt):
    """Imprime en tiempo real los indicadores de un camión.
    pre: La ejecución no termina hasta que mato el proceso.
    """
    camion = informe.leer_camion(path_camion)
    filas = parsear_datos(vigilar(path_log))
    filas = filtrar_datos(filas, camion)
    formato = formato_tabla.crear_formateador(fmt)
    formato.encabezado(["nombre", "precio", "volumen"])
    for fila in filas:
        f = [str(fila["nombre"]), str(fila["precio"]), str(fila["volumen"])]
        formato.fila(f)


if __name__ == "__main__":
    import formato_tabla
    import informe

    PATH_CAMION = "Data/camion.csv"
    PATH_LOG = "Data/mercadolog.csv"
    ticker(PATH_CAMION, PATH_LOG, "txt")
