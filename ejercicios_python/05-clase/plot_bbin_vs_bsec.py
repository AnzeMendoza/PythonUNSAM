import random

def busqueda_binaria(lista):
    lista.sort()
    medio = len(lista)//2
    print(medio)



    

def main():
    print(busqueda_binaria([random.randint(0,100) for _ in range(10)]))

if __name__ == "__main__":
    main()