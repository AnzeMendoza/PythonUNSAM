def buscar_en_lista(lista, valor, izquierda, derecha = None):
    try:
        if derecha == None:
            return lista.index(valor, izquierda)
        else:
            return lista.index(valor, izquierda, derecha)
    except:
        return -1

def propaga(lista):
    print(f'entrada: {lista}')
    lista.append(-1)
    izquierda = 0
    derecha = buscar_en_lista(lista,-1,izquierda)

    while izquierda <= derecha:
        if buscar_en_lista(lista, 1, izquierda, derecha) > 0:
            for i in range(izquierda, derecha):
                lista[i] = 1
        izquierda = derecha + 1
        derecha = buscar_en_lista(lista,-1, izquierda)
    lista.pop()
    print(f'salida: {lista}')
            
def main():
    propaga([ 0, 0, 0, -1, 0, 1, -1, 0, 0, 0, -1, 0, 0, 0, 0])

if __name__ == "__main__":
    main()