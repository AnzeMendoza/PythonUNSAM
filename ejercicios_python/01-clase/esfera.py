from math import pi
   
def esfera():
    ''' Calcula el volumen de una esfera.
        In: radio
        Out: imprime por pantalla el volumen.
    '''
    print("ingrese el radio de una esfera: ", end="")
    radio = int(input())
    print(f'El volumen de la esfera es : {(4/3) * pi * radio**3}')

def main():
    esfera()
    
if __name__ == '__main__':
    main()