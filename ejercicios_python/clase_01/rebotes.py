
def rebotes(altura = 100, contador = 10):
    while contador > 0:
        altura = altura*(3/5)
        print( round(altura,4) )
        contador -= 1

def main():
    rebotes()
    
if __name__ == '__main__':  
    main()
