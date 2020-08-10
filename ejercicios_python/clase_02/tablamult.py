
def tabla_multiplicar():
    cuenta = 0
    for i in range(0,10):
        print(f'{cuenta}\t',end='')
        for j in range(0,9):
            cuenta += i
            print(f'{cuenta}\t',end='')
        print('') # genera el salto de linea.
        cuenta = 0

def main():
    tabla_multiplicar()

if __name__ == "__main__":
    main()
