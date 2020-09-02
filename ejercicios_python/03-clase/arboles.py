import csv
from pprint import pprint

def leer_arboles(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        conv = [{name: val for name, val in zip(headers,row)} for row in rows]
    return conv

def altos_de_especies(lista_arboles, especie):
    h = [ float(arbol['altura_tot']) for arbol in lista_arboles if arbol['nombre_com'] == especie ]
    return h

def altos_y_diametro_de_especies(lista_arboles, especie):
    h = [ (float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in lista_arboles if arbol['nombre_com'] == especie ]
    return h

def medidas_de_especies(especies, arboleda):
    medidas = { especie: [ (float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie ] for especie in especies}
    return medidas

def main():
    path = './Data/arbolado-en-espacios-verdes.csv'
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    
    print('ejercicio 3.18')
    arboleda = leer_arboles(path)

    print('ejercicio 3.19')
    altos = altos_de_especies(arboleda,'Jacarandá')

    print('ejercicio 3.20')
    altos_y_diametros = altos_y_diametro_de_especies(arboleda, 'Jacarandá')

if __name__ == "__main__":
    main()