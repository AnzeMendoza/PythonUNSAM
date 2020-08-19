
def invertir_lista(lista):
    invertida = []
    tamamio = len(lista)
    for i in range(0, tamamio ):
        invertida.append(lista[tamamio-1-i])
    return invertida

def main():
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))

if __name__ == "__main__":
    main()
