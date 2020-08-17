import csv
from pprint import pprint
from collections import Counter

def leer_parque(path, parque):
    lista_parque = []
    with open(path, 'r') as f:
        headers = next(f).split(',')
        rows = csv.reader(f)
        for row in rows:
            aux_dic = dict(zip(headers, row))
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

def obtener_alturas(lista_arboles, especie):
    lista_altura = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            lista_altura.append(float(arbol['altura_tot']))
    return(lista_altura)

def maximo(lista):
    try:
        maximo_lista = float(lista[0])
        for i in range(1,len(lista)):
            if maximo_lista < float(lista[i]):
                maximo_lista = float(lista[i])
        return maximo_lista
    except:
        print("error al calcular el maximo de una lista, esta vacia o no se paso parametro")

def promedio(lista):
    try:
        acumulador = 0
        for altura in lista:
            acumulador += float(altura)
        return round(acumulador/len(lista), 2)
    except:
        print("error al calcular el maximo de una lista, esta vacia o no se paso parametro")

def obtener_inclinaciones(lista_arboles, especie):
    inclinacion = []
    for arbol in lista_arboles:
        if arbol['nombre_com'] == especie:
            inclinacion.append(arbol['inclinacio'])
    return inclinacion

def especimen_mas_inclinado(lista_arboles):
    especies_arboles_parque = list(especies(lista_arboles))
    inclinacion_maxima = maximo(obtener_inclinaciones(lista_arboles,especies_arboles_parque[0]))
    especie_maxima = especies_arboles_parque[0]

    for especie in especies_arboles_parque:
        if inclinacion_maxima < maximo(obtener_inclinaciones(lista_arboles,especie)):
            especie_maxima = especie
            inclinacion_maxima = maximo(obtener_inclinaciones(lista_arboles,especie))

    print(f'especie: {especie_maxima}\t maxima inclinacion: {inclinacion_maxima}')

def especie_promedio_mas_inclinado(lista_arboles):
    especies_arboles_parque = list(especies(lista_arboles))
    inclinacion_promedio_maxima = promedio(obtener_inclinaciones(lista_arboles,especies_arboles_parque[0]))
    especie_maxima = especies_arboles_parque[0]

    for especie in especies_arboles_parque:
        if inclinacion_promedio_maxima < promedio(obtener_inclinaciones(lista_arboles,especie)):
            especie_maxima = especie
            inclinacion_promedio_maxima = promedio(obtener_inclinaciones(lista_arboles,especie))
    print(f'especie: {especie_maxima}\t maxima inclinacion: {inclinacion_promedio_maxima}')


def main():
    pprint(contar_ejemplares(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ')))
    pprint(contar_ejemplares(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS')))
    pprint(contar_ejemplares(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO')))

    lista_arboles = obtener_alturas(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'), 'Jacarandá')
    print('maximo: ',maximo(lista_arboles))
    print( 'promedio: ',promedio(lista_arboles))
    print(obtener_inclinaciones(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'GENERAL PAZ'), 'Jacarandá'))
    especimen_mas_inclinado(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'CENTENARIO'))
    especie_promedio_mas_inclinado(leer_parque('./Data/arbolado-en-espacios-verdes.csv', 'ANDES, LOS'))
    
if __name__ == "__main__":
    main()
