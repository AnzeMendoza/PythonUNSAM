import random

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    print(lista)
    if verbose:
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos

def donde_insertar(lista, x, verbose = False):
    '''donde_insertar
    Precondición: la lista está ordenada
    Devuelve r si x no está en lista, que es la posicion a insertar el elemento;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(lista)
        print('[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos if pos>0 else medio 

def main():
    print('Ejercicio 5.11: Búsqueda binaria')
    print((donde_insertar(sorted([random.randint(0, 9) for _ in range(10)]), 5)))
    print('Ejemplo dado en la parte teorica')
    print(donde_insertar([0,2,4,6], 4, verbose=True))

if __name__ == '__main__':
    main()