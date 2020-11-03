def ord_burbujeo(lista):
    """ Ordenamiento por el metodo de burbuja
    """
    tam = len(lista)
    for i in range(tam):
        for j in range(1, tam-i):
            if lista[j-1] > lista[j]:
                lista[j-1], lista[j] = lista[j], lista[j-1]
    return lista

def max_value_index(lista):
    maximo = 0
    for i in range(1, len(lista)):
        if lista[maximo] <= lista[i]:
            maximo = i
    return maximo

def ord_seleccion(lista):
    tam = len(lista)-1
    
    while tam > 0:
        pos_max = max_value_index(lista[:tam])
        lista[tam], lista[pos_max] = lista[pos_max], lista[tam]
        tam-=1

    return lista




def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista[p]

    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
    return lista


def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado

def ord_merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = ord_merge_sort(lista[:medio])
        der = ord_merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva



def main():
    lista_desordenada = [1,6,5,2, 2, 22, 2, 2, 2, 0]
    print(ord_burbujeo(lista_desordenada.copy()))
    print(ord_seleccion(lista_desordenada.copy()))
    print(ord_insercion(lista_desordenada.copy()))
    print(ord_merge_sort(lista_desordenada.copy()))
    
if __name__ == '__main__':
    main()
