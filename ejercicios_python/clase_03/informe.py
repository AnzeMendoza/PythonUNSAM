#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
from pprint import pprint

def leer_camion(path):
    camion = []
    with open(path,'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            camion.append((row[0], int(row[1]), float(row[2])))
    return camion

def leer_precios(path):
    precios = {}
    with open(path, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        try:
            for row in rows:
                precios[row[0]] = float(row[1])
        except:
            return precios
    return precios

def subrayado(titulo=None):
    size = 80
    if titulo == None:
        print("#"*size)
    else:
        lenght = int((size-len(titulo))/2)
        cadena = '#'*lenght+titulo+'#'*lenght
        tit = (cadena+'#' if len(cadena)!=size else cadena)
        print(tit)

def main():
    # camion = leer_camion('Data/camion.csv')
    # costo = sum([ s[1] * s[2] for s in camion ])
    # print('costo del camion completo: ',costo)
    
    # precios = leer_precios('Data/precios.csv')
    # valor = sum([s[1]*precios[s[0]] for s in camion ])
    # print('costo del camion a precio de venta: ',valor)
    subrayado('Consulta de datos')
    
    # mas100 = [s for s in camion if s[1]>100]
    # pprint(mas100)
    # mandarinas_y_naranjas = [s for s in camion if s[0] in {'Mandarina', 'Naranja'}]
    # pprint(mandarinas_y_naranjas)
    # costo10k = [s for s in camion if s[1]*s[2]>10000]
    # print(costo10k)
    
    subrayado("Extraccion de datos")
    
    # nombre_cajon = [(s[0], s[1]) for s in camion]
    # pprint(nombre_cajon)
    
    # nombres = { s[0] for s in camion}
    # pprint(nombres)
    
    # stock = { nombre:0 for nombre in nombres}
    # print(stock)
    
    # for s in camion:
    #     stock[s[0]] += s[1]
    # print(stock)    
    
    # camion_precios = {nombre:precios[nombre] for nombre in nombres}
    # print(camion_precios)
    
    subrayado('Extranccion de datos en CSV')
    
    with open('Data/fecha_camion.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        
        select = ['nombre', 'cajones', 'precio']
        indices = [headers.index(ncolumna) for ncolumna in select]
        print(indices)
        
        row = next(rows)
        record = { ncolumna:row[index] for ncolumna, index in zip(select, indices)}
        print(record)
        camion = [ { ncolumna: row[index] for ncolumna, index in zip(select, indices) } for row in rows ]
        pprint(camion)
if __name__ == '__main__':
    main()