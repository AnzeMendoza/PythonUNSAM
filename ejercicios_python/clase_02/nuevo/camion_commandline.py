import csv

def costo_camion(path):
    costo = 0
    with open(path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        headers
        for row in rows:
            costo += int(row[1])*float(row[2])
    return costo

def main():
    costo = costo_camion('Data/camion.csv')
    print (f'Costo total: { costo }')

if __name__ == "__main__":
    main()