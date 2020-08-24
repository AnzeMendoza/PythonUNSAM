import csv
from pprint import pprint

def leer_arboles(nombre_archivo):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        conv = [{name: val for name, val in zip(headers,row)} for row in rows]
    return conv

def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
        headers = next(rows)
        # types = [str, int, float]
        conv = [ {name:val for name, val in zip(headers, row) } for row in rows if row[7]==parque]
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
    
    arboleda = leer_arboles(path)
    altos = altos_de_especies(arboleda,'Jacarandá')
    altos_y_diametros = altos_y_diametro_de_especies(arboleda, 'Jacarandá')
    medidas = medidas_de_especies(especies, arboleda)

if __name__ == "__main__":
    main()