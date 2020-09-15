def valor_absoluto(numero):
    """Calcula el valor absoluto de un numero real.
    pre: n debe ser flotante o entero.
    pos: devuelve el valor absoluto de n.
    """
    if numero >= 0:
        return numero
    else:
        return -numero


def suma_pares(lista_de_enteros):
    """Suma todos los numeros pares.
    pre: lista_de_enteros debe ser una lista de numeros enteros.
    pos: Devuelve un entero que corresponde a la suma de los numeros pares.
    """
    # su pre-condicion me parece que el nombre de el parametro de la funcion es
    # mas que descriptivo. Pero bueno lo agregue porque asi decia la teoria.
    acumulador_pares = 0
    for entero in lista_de_enteros:
        if entero % 2 == 0:
            acumulador_pares += entero
    return acumulador_pares
    # invariante de ciclo: acumulador_pares


def veces(valor, repeticiones):
    """Suma valor tantas veces como repeticiones indique.
    pre: repeticiones tiene que ser un numero natural incluyendo al 0.
    post: Retorna el mismo tipo de variable que valor.
    """
    res = 0
    nb = repeticiones
    while nb != 0:
        res += valor
        nb -= 1
    return res
    # invariantes de ciclo: res, nb.


def collatz(n):
    """Cuenta las veces que se itera hasta llegar a 1.
    pre: Debe ser un numero entero.
    post: Retorna un numero natural de las repeticiones.
    """
    res = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        res += 1
    return res
    # invariantes de ciclo: res, n.
