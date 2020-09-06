import sys
import informe_funciones

def costo_camion(path):
    costo = 0
    rows = informe_funciones.leer_camion(path)
    for row in rows:
        costo += row['cajones']*row['precio']
    return costo

def main():
    if len(sys.argv) == 2:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = 'Data/camion.csv'

    costo = costo_camion(nombre_archivo)
    print(f'Costo total: { costo }')

if __name__ == "__main__":
    main()
