from random import randint
import matplotlib.pyplot as plt 
import numpy as np

###########################################################################
def generar_lista(num_elementos=10, rango=1000):
    '''devuelve una lista ordenada de n elementos diferentes entre 0 y m-1.
    '''
    l = [ randint(0, rango-1) for _ in range(num_elementos)]
    return l
###########################################################################
def ord_burbujeo(lista):
    """ Ordenamiento por el metodo de burbuja
    """
    contador_burbujeo = 0
    tam = len(lista)
    for i in range(tam):
        for j in range(1, tam-i):
            if lista[j-1] > lista[j]:
                lista[j-1], lista[j] = lista[j], lista[j-1]
            contador_burbujeo+=1
    
    # print('###',contador_burbujeo)
    return contador_burbujeo, lista
###########################################################################
def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    contador_reubicaciones = 0

    v = lista[p]
    
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        contador_reubicaciones+=1

    lista[j] = v
    # print('ppp: ',contador_reubicaciones)

    return contador_reubicaciones

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    contador_insercion = 0
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            contador_insercion+=reubicar(lista, i + 1)

    return contador_insercion, lista
###########################################################################
def max_value_index(lista):
    maximo = 0
    contador_max = 0
    for i in range(1, len(lista)):
        if lista[maximo] <= lista[i]:
            maximo = i
        contador_max+=1
    return contador_max, maximo

def ord_seleccion(lista):
    tam = len(lista)-1
    contador_seleccion = 0
    while tam > 0:
        contador, pos_max = max_value_index(lista[:tam])
        contador_seleccion+=contador
        lista[tam], lista[pos_max] = lista[pos_max], lista[tam]
        tam-=1

    return contador_seleccion, lista
###########################################################################
def ord_merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comp = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        comp, izq = ord_merge_sort(lista[:medio])
        comp, der = ord_merge_sort(lista[medio:])
        comp, lista_nueva = merge(izq, der, comp)
    return comp, lista_nueva

def merge(lista1, lista2, comp):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        comp += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return comp, resultado
###########################################################################
def grafica_complejidad():
    N = 256
    largos = np.arange(N)+1 #estos son los largos de listas que voy a usar
    comps_promedio_burbujeo = np.zeros(N)
    comps_promedio_insercion = np.zeros(N)
    comps_promedio_seleccion = np.zeros(N)
    comps_promedio_merge = np.zeros(N)
    
    for i, n in enumerate(largos):
        lista = generar_lista(num_elementos=i) # genero lista de largo n

        comps_promedio_burbujeo[i], lb = ord_burbujeo(lista.copy())
        comps_promedio_insercion[i], li = ord_insercion(lista.copy())
        comps_promedio_seleccion[i], ls = ord_seleccion(lista.copy())
        comps_promedio_merge[i], lm = ord_merge_sort(lista.copy())
    
    plt.plot(largos,comps_promedio_burbujeo,label='burbujeo')    
    plt.plot(largos,comps_promedio_insercion,label='insercion')
    plt.plot(largos,comps_promedio_seleccion,label='seleccion')
    plt.plot(largos,comps_promedio_merge,label='merge-sort')

    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")

    plt.legend()
###########################################################################
def main():
    grafica_complejidad()

if __name__ == '__main__':
    main()
