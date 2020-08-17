import csv
import sys

def costo_camion(path):
    costo = 0
    with open(path, 'rt', encoding="utf8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            costo += (int(row[1]) if row[1] != '' else 0)*float(row[2])
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
