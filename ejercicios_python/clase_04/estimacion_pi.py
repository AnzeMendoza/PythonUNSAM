import random
from pprint import pprint

def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def estimar_pi(N = 10000000):
    M = sum([ 1 for i in [ generar_punto() for _ in range(N)] if (i[0]**2 + i[1]**2)<1 ])
    return (4*M/N),N

def main():
    pi_estimado, N = estimar_pi() 
    print(f'Se estimo el valor de pi a {pi_estimado}, con N: {N} cantidad de iteraciones')

if __name__ == "__main__":
    main()