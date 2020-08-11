import csv
from pprint import pprint

def leer_camion(path):
    camion = []
    with open(path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            camion.append((row[0], int(row[1]), float(row[2])))
    return camion

def leer_precio(path):
    precios = {}
    with open(path) as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            return precios
    return precios

def calcula_costo_camion(lista):
    costo_camion = 0
    for camion in lista:
        costo_camion += camion[1]*camion[2]
    return costo_camion

def calcula_recaudacion_ventas(lista, diccionario):
    recaudacion = 0
    for camion in lista:
        recaudacion += diccionario[camion[0]]*camion[1]
    return recaudacion

def informe(path_camion, path_precios):
    print('############################################################')

    camiones = leer_camion(path_camion)
    precios_frutas = leer_precio(path_precios)

    costo_camion = calcula_costo_camion(camiones)
    recaudacion_total = calcula_recaudacion_ventas(camiones, precios_frutas)
    ganancia = recaudacion_total - costo_camion

    print(f'Costo del camion: $ {costo_camion}')
    print(f'Recaudacion total: $ {recaudacion_total}')
    
    if ganancia > 0:
        print(f'La ganancia genera por la venta completa del camion: $ {round(ganancia,2)}')
    else:
        print(f'La perdidas generadas por la venta completa del camion: $ {round(ganancia,2)}')

    print('############################################################')

def main():
    informe('./Data/camion.csv','./Data/precios.csv')

if __name__ == "__main__":
    main()
