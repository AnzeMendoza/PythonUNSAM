import csv
from pprint import pprint

def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = tamamio(lista)
    while i > 0:    # tomo el último elemento
        i = i-1
        invertida.append(lista.pop(i))  #
    return invertida

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

def subrayado(titulo=None):
    if titulo == None:
        print("#"*80)
    else:
        lenght = int((80-tamamio(titulo))/2)
        cadena = '#'*lenght+titulo+'#'*lenght
        tit = (cadena+'#' if tamamio(cadena)!=80 else cadena)
        print(tit)

def propagar_al_vecino(l):
    modif = False
    n = tamamio(l)
    for i,e in enumerate(l):
        if e==1 and i<n-1 and l[i+1]==0:
            l[i+1] = 1
            modif = True
        if e==1 and i>0 and l[i-1]==0:
            l[i-1] = 1
            modif = True
    return modif

def propagar(l):
    m = l.copy()
    veces=0
    while propagar_al_vecino(l):
        veces += 1

    print(f"Repetí {veces} veces la función propagar_al_vecino.")
    print(f"Con input {m}")    
    print(f"Y obtuve  {l}")
    return m

def main():

    # ''' Interesante ver que los parametros de las funciones se pasan por 
    #     referencia y no por valor, se ve que al hacer un pop() desde dentro
    #     de la funcion modifica esa variable.
    # '''
    # subrayado('Ejercicio 4.1: Debugger')
    # l = [1, 2, 3, 4, 5]
    # m = invertir_lista(l)
    # print(f'Entrada {l}\nSalida: {m}')
    # subrayado()

    # subrayado('Ejercicio 4.2: Más debugger')
    # camion = leer_camion("Data/camion.csv")
    # pprint(camion)

    subrayado('Ejercicio 4.3: Propagar por vecinos')
    propagar([0,0,0,0,1])
    propagar([0,0,1,0,0])
    propagar([1,0,0,0,0])

if __name__ == "__main__":
    main()
