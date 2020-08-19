def busqueda_u_elemento(lista, item):
    indice = -1
    for i in range(0, len(lista)):
        if lista[i] == item:
            indice = i
    return indice

def buscar_n_elemento(lista, item):
    contador = 0
    for i in range(0, len(lista)):
        if lista[i] == item:
            contador += 1
    return contador

def maximo(lista = None):

    try:
        if lista == None or len(lista) == 0 :
            raise RuntimeError

        maximo = lista[0]
        for i in range(1, len(lista)):
            if maximo < lista[i]:
                maximo = lista[i]
        return maximo
    except RuntimeError:
        return "Lista esta vacia o es inexistente"

def main():
    print(maximo([]))

if __name__ == "__main__":
    main()
