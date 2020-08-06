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

def maximo(lista):
    
    if len(lista) == 0:
        raise Exception('Lista vacia')
    
    maximo = lista[0]

    for i in range(1,len(lista)):
        if maximo < lista[i]:
            maximo = lista[i]
    return maximo

def invertir_lista(lista):
    invertida = []
    tamamio = len(lista)
    for i in range(0, tamamio ):
        invertida.append(lista[tamamio-1-i])
    return invertida

def tabla_multiplicar():
    cuenta = 0
    for i in range(0,10):
        for j in range(0,10):
            cuenta += i
            print(f'{cuenta}\t',end='')
        print('')
        cuenta = 0


def main():
    tabla_multiplicar()

if __name__ == "__main__":
    main()
