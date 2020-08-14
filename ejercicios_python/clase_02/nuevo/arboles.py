import csv
from pprint import pprint
from collections import Counter

def leer_parque(path, parque):
    lista_parque = []
    with open(path,'r') as f:
        headers = next(f).split(',')
        rows = csv.reader(f)
        for row in rows:
            aux_dic = dict(zip(headers,row))
            if aux_dic['espacio_ve'] == parque:
                lista_parque.append(aux_dic)
    return lista_parque

def especies(lista_arboles):
    conjunto = []
    for arbol in lista_arboles:
        conjunto.append(arbol['nombre_com'])
    return set(conjunto)

def contar_ejemplares(lista_arboles):
    tenencia = Counter()

    for arbol in lista_arboles:
        tenencia[arbol['nombre_com']] += 1
    
    return tenencia.most_common(5)

def obtener_alturas (lista_arboles, especie):
    tenencia = Counter()

    for altura in lista_arboles:
        tenencia[especie] += float(altura['altura_tot'])
    print(tenencia)

def main():
    # pprint(contar_ejemplares(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')))
    # pprint(contar_ejemplares(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'EJERCITO DE LOS ANDES')))
    # pprint(contar_ejemplares(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')))

    print(obtener_alturas(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'), 'Jacarandás'))

if __name__ == "__main__":
    main()