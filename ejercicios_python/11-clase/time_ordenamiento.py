import timeit as tt
import numpy as np
import matplotlib.pyplot as plt
from random import randint

#-----------------------------------------------------------------------------
def generar_lista(num_elementos=10, rango=1000):
    '''devuelve una lista ordenada de n elementos diferentes entre 0 y m-1.
    '''
    l = [ randint(0, rango-1) for _ in range(num_elementos)]
    return l
#-----------------------------------------------------------------------------
listas = []
for N in range(1, 256):
    listas.append(generar_lista(N))
#-----------------------------------------------------------------------------
def ord_seleccion(lista):
    tam = len(lista)-1
    while tam > 0:
        pos_max = max_value_index(lista[:tam])
        lista[tam], lista[pos_max] = lista[pos_max], lista[tam]
        tam-=1

    return lista
#-----------------------------------------------------------------------------
def max_value_index(lista):
    maximo = 0
    for i in range(1, len(lista)):
        if lista[maximo] <= lista[i]:
            maximo = i
    return maximo

#-----------------------------------------------------------------------------
def experimento_timeit_seleccion(listas, num):
    """
    Realiza un experimento usando timeit para evaluar el método
    de selección para ordenamiento de listas
    con las listas pasadas como entrada
    y devuelve los tiempos de ejecución para cada lista
    en un vector.
    El parámetro 'listas' debe ser una lista de listas.
    El parámetro 'num' indica la cantidad de repeticiones a ejecutar el método para cada lista.
    """
    tiempos_seleccion = [[],[],[],[]]
    
    global lista
    
    for lista in listas:
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = num, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion[0].append(tiempo_seleccion)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion[0])
    
    return tiempos_seleccion 

def main():
    listas = []
    for N in range(1, 256):
        listas.append(generar_lista(N))
    
    tiempos_seleccion = experimento_timeit_seleccion(listas, 100)
    plt.plot(tiempos_seleccion)
if __name__ == '__main__':
    main()