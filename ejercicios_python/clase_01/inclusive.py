
def inclusive(frase = 'todos somos programadores'):
    
    palabras = frase.split()
    frase_a_imprimir = ''

    for palabra in palabras:
        frase_a_imprimir += palabra[:-2]+ (palabra[-2:].replace('o', 'e') if palabra.find('o',-2) > 0 else palabra[-2:]) + ' '
    
    print(frase_a_imprimir)

def main():
    inclusive()
    
if __name__ == '__main__':  
    main()
