from math import pi
   
def esfera():
    print("ingrese el radio de una esfera: ", end="")
    radio = int(input())
    print((4/3) * pi * radio**3)


def main():
    esfera()
    
if __name__ == '__main__':  
    main()
