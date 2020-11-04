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
    return contador_burbujeo, lista


def main():
    lista = [
        [1, 2, -3, 8, 1, 5],
        [1, 2, 3, 4, 5],
        [0, 9, 3, 8, 5, 3, 2, 4],
        [10, 8, 6, 2, -2, -5],
        [2, 5, 1, 0],
    ]
    print("Ejercicio 11.2: burbujeo")
    for i in lista:
        print("lista desordenada: ", i)
        print("lista ordenada: ", ord_burbujeo(i.copy()))
        print("######################################")

if __name__ == "__main__":
    main()