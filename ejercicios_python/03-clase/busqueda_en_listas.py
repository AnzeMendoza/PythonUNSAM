def buscar_u_elemento(lista, item):
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
    print('ejercicio 3.6')
    print(buscar_u_elemento([1,2,3,2,3,4],1))
    print(buscar_u_elemento([1,2,3,2,3,4],2))
    print(buscar_u_elemento([1,2,3,2,3,4],3))
    print(buscar_u_elemento([1,2,3,2,3,4],5))
    print('ejercicio 3.7')
    print(maximo([1,2,7,2,3,4]))
    print(maximo([1,2,3,4]))
    print(maximo([-5,4]))
    print(maximo([-5,-4]))

if __name__ == "__main__":
    main()
