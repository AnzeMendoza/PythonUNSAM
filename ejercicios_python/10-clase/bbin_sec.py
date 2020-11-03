def bbinaria_rec(lista, e):
    """Busqueda binaria recursiva.
    pre: La lista que se pase debe estar ordenada
    devuelve: True o False, el elemento esta en la lista.
    """
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = bool(lista[0] == e)
    else:
        medio = len(lista) // 2
        if lista[medio] == e:
            return True
        elif lista[medio] > e:
            res = bbinaria_rec(lista[: medio - 1], e)
        elif lista[medio] < e:
            res = bbinaria_rec(lista[medio + 1 :], e)
    return res


def main():
    print("Ejercicio 10.11: Búsqueda binaria")
    print(bbinaria_rec([1, 2, 3, 4, 5, 6, 7, 8], 5))
    print(bbinaria_rec([1, 2, 3, 4, 5, 6, 7, 8], 10))
    print(bbinaria_rec([10], 10))
    print(bbinaria_rec([], 0))


if __name__ == "__main__":
    main()
