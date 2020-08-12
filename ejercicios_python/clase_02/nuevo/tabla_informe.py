import csv
# from pprint import pprint
def leer_camion(path):
    camion = []
    with open(path,'r') as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            camion.append((row[0], int(row[1]), float(row[2])))
    return camion

def leer_precio(path):
    precios = {}
    with open(path, 'r') as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            return precios
    return precios

def hacer_informe(lista_camion, diccionario_precios):
    informe = []
    for camion in lista_camion:
        tupla2list = list(camion)
        tupla2list.append(diccionario_precios[tupla2list[0]]-tupla2list[2])
        informe.append(tuple(tupla2list))
    return informe

def imprime_headers(headers):
    subrayado = []
    for _ in range(len(headers)):
        subrayado.append('----------')
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % tuple(subrayado))

def imprime_tabla(lista):
    for nombre, cajones, precio, cambio in lista:
        precio_billete = '$'+str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio_billete:>10s} {cambio:>10.2f}')

def imprime_informe():
    camiones = leer_camion('./Data/camion.csv')
    precios_frutas = leer_precio('./Data/precios.csv')
    informe = hacer_informe(camiones, precios_frutas)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

    imprime_headers(headers)
    imprime_tabla(informe)

def main():
    imprime_informe()

if __name__ == "__main__":
    main()