import matplotlib.pyplot as plt
import numpy as np
import csv

def leer_arboles(nombre_archivo):
    ''' lee el archivo que se le pasa por parametro
        Retorna: una lista de diccionarios.
    '''
    with open(nombre_archivo,encoding='utf-8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        conv = [{name: val for name, val in zip(headers,row)} for row in rows]
    return conv

def altos_de_especies(lista_arboles, especie):
    h = [ float(arbol['altura_tot']) for arbol in lista_arboles if arbol['nombre_com'] == especie ]
    return h

def alto_y_diametro_de_especies(lista_arboles, especie):
    ''' Selecciona una especie y genera una lista de tuplas que contiene (alto,diametro)
    '''
    h = [ (float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in lista_arboles if arbol['nombre_com'] == especie ]
    return h

def plotea_histograma_alto_de_especie(arboleda, especie_arbol):
    altos = np.array(altos_de_especies(arboleda,especie_arbol))
    plt.hist(altos,bins='auto')
    plt.show()

def parsea_alto_diametro(lista_tupla):
    a_y_d =  np.array(lista_tupla)
    alto, diametro = np.split(a_y_d,2, axis=1)
    return alto, diametro

def plotea_diametro_vs_alto(alto, diametro, especie=None):
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto " + (f"para {especie}s" if especie!=None else ' de varias especies'))
    plt.scatter(diametro,alto, alpha=0.3, s=90, label=especie)
    plt.legend()
    

def medidas_de_especies(especies, arboleda):
    medidas = { especie: [ (float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie ] for especie in especies}
    return medidas

def scatterplot_especie(arboleda, especie):
    alto, diametro = parsea_alto_diametro(alto_y_diametro_de_especies(arboleda, especie='Jacarandá'))
    plotea_diametro_vs_alto(alto, diametro, 'Jacarandá')
    plt.figure()
    
def scatterplot_lista_de_arboles(arboleda, especies):
    medidas = medidas_de_especies(especies, arboleda)

    for k in medidas:
        alto, diametro = parsea_alto_diametro(medidas[k])
        plotea_diametro_vs_alto(alto, diametro, k)
    plt.title("Relación diámetro-alto de varias especies")
    plt.figure()


def main():
    PATH = './Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(PATH)

    print('Ejercicio 4.30: Histograma de altos de Jacarandás')
    plotea_histograma_alto_de_especie(arboleda,'Jacarandá')

    print('Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás')
    scatterplot_especie(arboleda, 'Jacarandá')

    print('Ejercicio 4.32: Scatterplot para diferentes especies')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    scatterplot_lista_de_arboles(arboleda, especies)
    
if __name__ == "__main__":
    main()