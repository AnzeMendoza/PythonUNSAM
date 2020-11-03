def factorial_recursivo(n):
    if n < 2:
        return 1
    return n * factorial_recursivo(n-1)


def factorial_iterativo(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n-=1
    return resultado


def potencia_iterativo(b,n):
    resultado = 1
    
    while n > 0:
        resultado *= b
        n-=1
    return resultado


def potencia_recursivo(b,n):
    
    if n == 0:
        return 1
    return b * potencia_recursivo(b, n-1)


def potencia_recursivo_optimizado(b, n):
    if n == 0:
        return 1
    if not(n % 2):
        p = potencia_recursivo_optimizado(b, n//2)
        return p*p
    else:
        p = potencia_recursivo_optimizado(b, (n-1)//2)
        return p*p*b
        

def fibonacci_recursivo(n):
    
    if n < 2:
        return n
    return fibonacci_recursivo(n-1)+fibonacci_recursivo(n-2)

def fibonacci_iterativo(n):
    resultado = 0
    
    if n < 2:
        return n
    
    num_anterior1 = 0
    num_anterior2 = 1
    
    for i in range(2, n+1):
        resultado = num_anterior1 + num_anterior2
        num_anterior1 = num_anterior2
        num_anterior2 = resultado
    
    return resultado

def sumar_lista(lista_numeros):
    
    if not len(lista_numeros):
        return 0
    
    return lista_numeros[0]+sumar_lista(lista_numeros[1:])


def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
    return res

    

def promediar(lista):
    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1
    
        if  len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad
    
    suma, cantidad = promediar_aux(lista)
    return suma/cantidad

def hoja_iso(n):
    if n >=0 and n <=10:
        return 0, 0
    
    def hoja_iso_(n, i=841, j=1189):
        fila = 0
        columna = 0
        if n < 1:
            if not (n % 2):
                fila, columna = hoja_iso_(n+1, fila//2, columna//2)
            else:
                columna, fila = hoja_iso_(n+1 , columna//2, fila//2)
        return fila, columna

def hoja(n):
    def hoja_(n, i=100):
        count =1
        
def generador_secuencia(n):
    ancho = 26
    largo = 37
    contador = 10
    
    if n == 0:
        return 594, 841
    
    else:
        print(contador, ancho, largo)
        contador_r, ancho, largo = generador_secuencia(n-1)
        contador+=contador_r
        return contador, ancho*2, largo*2
    return ancho, largo
        
    

def main():
    # print(f"5!: {factorial_recursivo(5)}")
    # print(f"5!: {factorial_iterativo(5)}")

    # print(f"2^5: {potencia_iterativo(2, 10)}")
    # print(f"2^5: {potencia_recursivo(2, 10)}")
    # print(f"2^5: {potencia_recursivo_optimizado(2, 10)}")
    
    # print(f"elemento n de Fibonacci: {fibonacci_recursivo(10)}")
    # print(f"elemento n de Fibonacci: {fibonacci_iterativo(10)}")
    
    # print(f"suma recursiva: {sumar_lista([1,2,3,4,5])}")
    
    # print(promediar([1,2,3,4,5]))
    
    
    print(generador_secuencia(3))
    
if __name__ == '__main__':
    main()