import numpy as np
import matplotlib.pyplot as plt


def ajuste_lineal_simple(x, y):
    """Retorna los coheficientes de la regresión lineal."""
    a = sum(((x - x.mean()) * (y - y.mean()))) / sum(((x - x.mean()) ** 2))
    b = y.mean() - a * x.mean()
    return a, b


def plot_dispercion(lista_x, lista_y):
    """Plot del Scatter"""
    plt.scatter(x=lista_x, y=lista_y)
    plt.title("gráfico de dispersión de Superficie-Alquiler")
    plt.xlabel("Superficie")
    plt.ylabel("Alquiler")

    plt.show()


def plot_recta(lista_x, lista_y):
    """Plot de la recta que ajusta a la dispersión."""
    a, b = ajuste_lineal_simple(lista_x, lista_y)
    grilla_x = np.linspace(min(lista_x), max(lista_x), num=100)
    grilla_y = grilla_x * a + b

    plt.plot(grilla_x, grilla_y, c="red")
    plt.show()
    return a, b


def error_cuadratico_medio(superficie, alquiler, a, b):
    """Imprime el calculo del error cuadratico medio."""
    errores = alquiler - (a * superficie + b)
    print("###################################")
    print(errores)
    print("ECM:", (errores ** 2).mean())
    print("###################################")


def main():
    print("Ejercicio 10.14: precio_alquiler ~ superficie")

    superficie = np.array([150.0, 120.0, 170.0, 80.0])
    alquiler = np.array([35.0, 29.6, 37.4, 21.0])

    plot_dispercion(superficie, alquiler)
    a, b = plot_recta(superficie, alquiler)
    error_cuadratico_medio(superficie, alquiler, a, b)


if __name__ == "__main__":
    main()
