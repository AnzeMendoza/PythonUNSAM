# vigilante.py
import os
import time


def leer_archivo(path):
    """Lectura de archivo en tiempo real.
    pre: recibe el path de un archivo, no tiene fin, termina matando el proceso.
    """
    f = open("Data/mercadolog.csv")
    f.seek(0, os.SEEK_END)  # Mover el índice 0 posiciones desde el EOF
    return f


def vigilar(path):
    """Lectura de un archivo resuelto por medio de un generador.
    pre: el proceso no termina si no se mata el proceso.
    """
    file = leer_archivo(path)
    while True:
        line = file.readline()
        if line == "":
            time.sleep(0.5)  # Esperar un rato y
            continue  # vuelve al comienzo del while
        yield line


def main():
    import informe

    camion = informe.leer_camion("Data/camion.csv")

    for line in vigilar("Data/mercadolog.csv"):
        fields = line.split(",")
        nombre = fields[0].strip('"')
        precio = float(fields[1])
        volumen = int(fields[2])

        if nombre in camion:
            print(f"{nombre:>10s} {precio:>10.2f} {volumen:>10d}")


if __name__ == "__main__":
    main()
