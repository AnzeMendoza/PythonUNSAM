import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()


def graficar_varios_randomwalk(pasos=100000):
    lista_caminantes = [randomwalk(10000) for _ in range(12)]
    lista_de_medias = [abs(i.mean()) for i in lista_caminantes]
    index_max = lista_de_medias.index(max(lista_de_medias))
    index_min = lista_de_medias.index(min(lista_de_medias))

    plt.subplot(2, 1, 1)
    plt.title("12 Caminatas al azar")
    for i in range(12):
        plt.plot(lista_caminantes[i])
        plt.ylim(-250.0, 250.0)

    plt.subplot(2, 2, 3)
    plt.title("La caminata que más se aleja")
    plt.plot(lista_caminantes[index_max])
    plt.ylim(-250.0, 250.0)
    plt.subplot(2, 2, 4)
    plt.title("La caminata que más se menos")
    plt.plot(lista_caminantes[index_min])
    plt.ylim(-250.0, 250.0)

    plt.show()


def main():
    graficar_varios_randomwalk()


if __name__ == "__main__":
    main()
