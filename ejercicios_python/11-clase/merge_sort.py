###########################################################################
from random import randint

def generar_lista(num_elementos=10, rango=1000):
    '''devuelve una lista ordenada de n elementos diferentes entre 0 y m-1.
    '''
    l = [ randint(0, rango-1) for _ in range(num_elementos)]
    return l
###########################################################################
def ord_merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comparaciones = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        comparaciones, izq = ord_merge_sort(lista[:medio])
        comparaciones, der = ord_merge_sort(lista[medio:])
        comparaciones, lista_nueva = merge(izq, der, comparaciones)
    return comparaciones, lista_nueva
###########################################################################
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
def main():
    l = generar_lista()
    print(type(l))
    print(ord_merge_sort(l))
###########################################################################
if __name__ == '__main__':
    main()