import random
from collections import Counter

def suma_envido(lista):
    ''' Recibe una lista de numeros y cuenta los puntos de envido, es bastante general,
        tiene en cuenta que se juega sin flor.
    '''
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
    '''Genera un mazo y retorna 3 cartas que previamente han sido mezcladas.
    '''
    numeros = [ i for i in range(1,13) if (i<8 or i>9) ]
    palos = ['Basto', 'Oro', 'Copa', 'Espada']
    mazo = [( palo, numero) for palo in palos for numero in numeros]
    random.shuffle(mazo)
    return [ {'palo':palo, 'valor':valor} for palo, valor in [mazo.pop() for _ in range(3)]]

def cuenta_puntos_envido(mano):
    '''Recibe 3 cartas esta selecciona las del mismo palo y cuenta los puntos de envido.
    '''
    palos = list(set((mano[i]['palo']) for i in range (3)))
    diccionario_de_palos = { palo: [m['valor'] for m in mano if m['palo'] == palo] for palo in palos}
    puntos = { palo:suma_envido(diccionario_de_palos[palo]) for palo in palos }
    return max(puntos.values())

def estimacion_envido_mayor_30(N=100000):
    ''' Calcula la probabilidad de salga envido en una mano de truco, sin flor.
    '''
    manos = [ generar_mano() for _ in range(N)]
    contador_mayor_30 = sum([ cuenta_puntos_envido(mano)>30 for mano in manos ])
    print(f'Jugue {N} veces, de las cuales {contador_mayor_30} tuvieron envido mayor a 30.')
    print(f'Podemos estimar la probabilidad de envido mayor a 30 es {(contador_mayor_30/N):.6f}.')

def main():
    estimacion_envido_mayor_30()

if __name__ == "__main__":
    main()