import csv


def parse_csv(lines, select=None, types=None, has_headers=True):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    """
    filas = csv.reader(lines)
    # Lee los encabezados del archivo
    if has_headers:
        encabezados = next(filas)
    registros = []

    # Si se indicó un selector de columnas,
    #    buscar los índices de las columnas especificadas.
    # Y en ese caso achicar el conjunto de encabezados para diccionarios

    if select and has_headers:
        indices = [encabezados.index(nombre_columna) for nombre_columna in select]
        encabezados = select
    else:
        indices = []

    for fila in filas:
        if not fila:  # Saltear filas vacías
            continue
        if types:
            fila = [func(val) for func, val in zip(types, fila)]
        # Filtrar la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]
        # Armar el diccionario
        registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
        # print(registros)
        registros.append(registro)

    return registros
