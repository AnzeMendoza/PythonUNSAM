def pascal(n, k):
    """Calcula el coheficiente de el triangulo de Pascal en forma recursiva.
    pre: tanto n como k deben ser numeros enteros, cero incluido.
    """
    if n == k or k == 0:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)


def main():
    print("Ejercicio 10.9: Pascal")
    print(pascal(0, 0))
    print(pascal(1, 0))
    print(pascal(2, 1))
    print(pascal(3, 3))


if __name__ == "__main__":
    main()
