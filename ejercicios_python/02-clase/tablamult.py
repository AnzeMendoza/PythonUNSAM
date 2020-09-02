
def tabla_multiplicar():
    cuenta = 0
    headers = tuple([i for i in range(10) ])
    subrayado = ('-'*54)
    print('%9d%5d%5d%5d%5d%5d%5d%5d%5d%5d' % headers)
    print('%55s' % subrayado)

    for i in range(10):
        print(f'{i:>3d}:{cuenta:>5d}',end='')
        for _ in range(9):
            cuenta += i
            print(f'{cuenta:>5d}',end='')
        print('') # genera el salto de linea.
        cuenta = 0

def main():
    tabla_multiplicar()

if __name__ == "__main__":
    main()
