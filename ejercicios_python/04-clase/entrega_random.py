import random
from collections import Counter
from pprint import pprint 

#############################################################################################################
def tirar(dados = 5):
    tirada = [random.randint(1,6) for _ in range(dados)]
    return tirada

def es_generala(lista):
    for i in range(1,5):
        if lista[0] != lista[i]:
            return False
    return True

def generala_servida():
    N = 100000
    # salio_generala_servida = [es_generala(tirar()) for i in range(N)]
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

def es_generala_v2():
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
    print(f'Tiré {N} veces, de las cuales {cont} saqué generala.')
    print(f'Podemos estimar la probabilidad de sacar generala con {prob:.6f}.')

#############################################################################################################
def suma_envido(lista):
    sumatoria = 0
    size = len(lista) 
    if size>2:
        lista = sorted([ i for i in lista if i<8])
        if len(lista)>2:
            lista.pop(0)
            size-=1
    if size>1:
        for i in lista:
            if i<8:
                sumatoria+=i
        return sumatoria+20
    else:
        return lista[0] if lista[0]<8 else 0

def generar_mano():
    numeros = [ i for i in range(1,13) if (i<8 or i>9) ]
    palos = ['Basto', 'Oro', 'Copa', 'Espada']
    mazo = [( palo, numero) for palo in palos for numero in numeros]
    random.shuffle(mazo)
    return [ {'palo':palo, 'valor':valor} for palo, valor in [mazo.pop() for _ in range(3)]]

def cuenta_puntos_envido(mano):
    palos = list(set((mano[i]['palo']) for i in range (3)))
    diccionario_de_palos = { palo: [m['valor'] for m in mano if m['palo'] == palo] for palo in palos}
    puntos = { palo:suma_envido(diccionario_de_palos[palo]) for palo in palos }
    return max(puntos.values())

def estimacion_envido_mayor_30(N=100000):
    manos = [ generar_mano() for _ in range(N)]
    contador_mayor_30 = sum([ cuenta_puntos_envido(mano)>30 for mano in manos ])
    print(f'Jugue {N} veces, de las cuales {contador_mayor_30} tuvieron envido mayor a 30.')
    print(f'Podemos estimar la probabilidad de envido mayor a 30 es {(contador_mayor_30/N):.6f}.')

def main():
    estimacion_envido_mayor_30()

if __name__ == "__main__":
    main()