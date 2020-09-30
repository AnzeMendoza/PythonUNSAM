import os
import sys


def listar_imgs(extension = '.png'):
    ''' Lista todas las imagenes con extension png.
    pre: es ejcutable solamente desde consola.
    post: Solamente imprime, no retorna nada.
    '''
    PATH = 1
    EXTENSION = 1
    if len(sys.argv) == 2:
        for _, _, files in os.walk(sys.argv[PATH]):
            for file in files:
                if os.path.splitext(file)[EXTENSION] == extension:
                    print(file)
    else:
        print("No se ingreso el path correctamente")


def main():
    print("Ejercicio 7.5: Recorrer el árbol de archivos")
    # ejemplo: > python listar_imgs.py Data
    listar_imgs()


if __name__ == "__main__":
    main()
