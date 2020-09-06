import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo,'rt', encoding="utf8") as f:
        filas = csv.reader(f)
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
            if not fila:    # Saltear filas vacías
                continue
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [ fila[index] for index in indices]
            # Armar el diccionario
            registro = dict(zip(encabezados, fila)) if has_headers else tuple(fila)
            # print(registros)
            registros.append(registro)

    return registros

def main():
    print('Ejercicio 5.5: Conversión de tipo')
    camion = parse_csv('Data/camion.csv',types=[str, int, float])
    cajones_lote = parse_csv('Data/camion.csv', select=['nombre', 'cajones'], types=[str, int])
    print(camion)
    print('-'*30)
    print(cajones_lote)
    
    print('-'*30)
    print('Ejercicio 5.6: Trabajando sin encabezado')
    precios = parse_csv('Data/precios.csv', types=[str,float], has_headers=False)
    print(precios)

if __name__ == '__main__':
    main()