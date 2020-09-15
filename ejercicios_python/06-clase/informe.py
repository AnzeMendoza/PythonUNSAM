import fileparse


def leer_camion(path):
    lines = []
    with open(path, "rt") as file:
        lines = fileparse.parse_csv(
            file, select=["nombre", "cajones", "precio"], types=[str, int, float]
        )
    return lines


def leer_precio(path):
    lines = []
    with open(path, "rt") as file:
        lines = fileparse.parse_csv(file, types=[str, float], has_headers=False)
    return lines


def hacer_informe(lista_camion, precios):
    informe = []
    diccionario_precios = dict(precios)
    for camion in lista_camion:
        informe.append(
            tuple(
                (
                    camion["nombre"],
                    camion["cajones"],
                    camion["precio"],
                    diccionario_precios[camion["nombre"]] - camion["precio"],
                )
            )
        )
    return informe


def imprimir_headers(headers):
    subrayado = []
    for _ in range(len(headers)):
        subrayado.append("-" * 10)
    print("%10s %10s %10s %10s" % headers)
    print("%10s %10s %10s %10s" % tuple(subrayado))


def imprimir_tabla(lista):
    for nombre, cajones, precio, cambio in lista:
        precio_billete = "$" + str(precio)
        print(f"{nombre:>10s} {cajones:>10d} {precio_billete:>10s} {cambio:>10.2f}")


def imprimir_informe():
    camiones = leer_camion("./Data/camion.csv")
    precios_frutas = leer_precio("./Data/precios.csv")
    informe = hacer_informe(camiones, precios_frutas)
    headers = ("Nombre", "Cajones", "Precio", "Cambio")
    imprimir_headers(headers)
    imprimir_tabla(informe)


def main():
    imprimir_informe()


if __name__ == "__main__":
    main()
