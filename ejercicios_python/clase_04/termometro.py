import random
from pprint import pprint

def mediana(lista):
    lista = sorted(lista)
    tamanio = len(lista)
    if tamanio%2:
        median = lista[tamanio//2]
    else:
        median = (lista[tamanio//2 -1] + lista[tamanio//2])/2
    return median

def termometro(temperatura_medida, mu, sigma):
    temperaturas_normalizadas = [ random.normalvariate(mu, sigma)  for _ in range(99)]
    temperaturas_simuladas = [ temperatura_medida+temp for temp in temperaturas_normalizadas]
    
    print('maximo: ', round(max(temperaturas_simuladas),2))
    print('minimo: ', round(min(temperaturas_simuladas),2))
    print('promedio: ', round(sum(temperaturas_simuladas)/99 , 2))
    print('mediana: ', round(mediana(temperaturas_simuladas), 2))

def main():
    termometro(37.5, 0, 0.2)
if __name__ == "__main__":
    main()