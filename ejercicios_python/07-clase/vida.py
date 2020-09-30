from datetime import datetime


def calcular_segundos_vividos(fecha_nacimiento):
    ''' Calcula el tiempo en segundo con la fecha actual.
    pre: pasar dia en formato dd/mm/aaa
    post: retorna un numero redondeado.
    '''
    parse_fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
    return round((datetime.now() - parse_fecha_nacimiento).total_seconds())


def main():
    FECHA = "29/10/2011"
    print("Ejercicio 7.1: Segundos vividos")
    print(
        "Son los segundos vividos hasta el dia de hoy: ",
        calcular_segundos_vividos(FECHA),
    )


if __name__ == "__main__":
    main()
