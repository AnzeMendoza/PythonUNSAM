import fileparse

def hacer_informe(lista_camion, precios):
    informe = []
    diccionario_precios = dict(precios)
    for camion in lista_camion:
        informe.append(tuple((camion['nombre'],camion['cajones'], camion['precio'], diccionario_precios[camion['nombre']]-camion['precio'])))
    return informe

def imprime_headers(headers):
    subrayado = []
    for _ in range(len(headers)):
        subrayado.append('-'*10)
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % tuple(subrayado))

def imprime_tabla(lista):
    for nombre, cajones, precio, cambio in lista:
        precio_billete = '$'+str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio_billete:>10s} {cambio:>10.2f}')

def leer_camion(path):
     return fileparse.parse_csv(path,  select=['nombre','cajones','precio'], types=[str,int,float])

def leer_precio(path):
    return fileparse.parse_csv(path, types=[str,float], has_headers=False)

def imprimir_informe():
    camiones = leer_camion('./Data/camion.csv')
    precios_frutas = leer_precio('./Data/precios.csv')
    informe = hacer_informe(camiones, precios_frutas)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    imprime_headers(headers)
    imprime_tabla(informe)

def main():
    imprimir_informe()

if __name__ == "__main__":
    main()