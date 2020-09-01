import numpy as np

def crear_album(cantidad_figuritas):
    ''' Crea una array con la cantidad de figuritas
    '''
    return np.zeros(cantidad_figuritas, dtype=int)

def album_completo(album):
    ''' Controla si alguna figu no esta en el album.
    '''
    return  len(album[album==0])==0

def comprar_figus(figus_total):
    ''' entrega de 1 figu por vez.
    '''
    return np.random.randint(0,figus_total)

def cuantas_figus(figus_total):
    '''  Retorna la cantidad de figus que se necesita para llenar un album.
    '''
    album = crear_album(figus_total)
    contador_figus_compradas = 0
    while not album_completo(album):
        album[comprar_figus(figus_total)-1] += 1
        contador_figus_compradas+=1
    return contador_figus_compradas

def estimacion_figus_compradas(n_repeticiones = 100, figus_total = 670):
    ''' Se promedia las figus que se necesita para llenar un album.
    '''
    lista_cuantas_figus = np.array([ cuantas_figus(figus_total) for _ in range(n_repeticiones) ])
    return np.ceil(lista_cuantas_figus.mean())


def main():
    print('Ejercicio 4.19:')
    print(f'Estimación para un album de 6 figus con 1000 repeticiones: {estimacion_figus_compradas(n_repeticiones=1000, figus_total=6)} figus fueron compradas')
    print('Ejercicio 4.20:')
    # se suele tardar unos 4 segundos
    print(f'Estimacion para un albun de 670 figus con 100 repeticiones: {estimacion_figus_compradas()} figus fueron compradas')

if __name__ == "__main__":
    main()
