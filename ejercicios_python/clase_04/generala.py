import random
from collections import Counter
from pprint import pprint 

#############################################################################################################
def tirar(dados = 5):
    tirada = [random.randint(1,6) for _ in range(dados)]
    return tirada

def generala_no_servida():
    ''' Lo que hice fue contar en la primera tirada cual dado salio mas veces, luego en la proxima tirada hacia tiradas de
        5 - (cantidad de repeticiones de mi numero con mas salidas), asi dos veces, por ultimo conte cuando esas repeticiones llegaban a 5
        ya sea en la segunda como en la tercer tirada.
    '''
    N = 100000
    cont = 0
    for _ in range(N):
        dados = tirar()
        repeticiones = Counter(dados)
        valor_maximo, veces_repetidas = repeticiones.most_common(1)[0]
        for _ in range(2):
            dados = tirar(5-veces_repetidas)
            repeticiones = Counter(dados)
            veces_repetidas += repeticiones[valor_maximo]
        if veces_repetidas == 5:
            cont+=1

    prob = cont/N
    print(f'Tire {N} veces, de las cuales {cont} saque generala.')
    print(f'Podemos estimar la probabilidad de sacar generala con {prob:.6f}.')


def main():
    generala_no_servida()

if __name__ == "__main__":
    main()