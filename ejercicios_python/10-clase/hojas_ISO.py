def promediar(lista):
    """Devuelve el promedio de los elementos de una lista de números."""

    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad

    suma, cantidad = promediar_aux(lista)
    return suma / cantidad

def hoja_ISO(n):
    def hoja_ISO_aux(n):
        ancho=841
        largo=1189
        if n==0:
           ancho=841
           largo=1189
        else:
            if n%2==0:
                ancho=ancho//2
                largo=largo
            else:
                largo=largo//2
                ancho=ancho
            ancho, largo = hoja_ISO_aux(n-1)
        return ancho, largo

def hoja_iso2(n):
    ancho = 832
    largo = 1189

    def hoja_iso2_(m):
        if n == m:
            res = hoja_iso2_(m-1)
            return res
        res = hoja_iso2_(m-1)
        return res
    return ancho, largo

def factorial(n):
    if n < 2:
        return 1
    return n*factorial(n-1)

def hojas(n):
    """Devuelve la medida de la hoja An según las normas ISO.
    Pre: n es un número entero positivo.
    Pos: la medida se imprime en pantalla y devuelve una tupla."""
    
    # MACHETE
    # AN: ancho x alto (las tomo verticales)
    # el sistema ISO propaga el ancho 
    # para el alto y la mitad del alto 
    # para el ancho a medida que aumenta N
    # A0: 841 x 1189
    # A1: 594 x 841
    # A2: 420 x 594
    # A3: 297 x 420
    # A4: 210 x 297
    # A5: 148 x 210
    
    def hojas_aux(n, ancho=841, alto=1189):
        """Función auxiliar para no modificar 
        la firma de la envoltorio, hojas(n)"""
        
        if n == 0:
            # caso base
            anch = alto//2
            alt = ancho
        else:
            # caso general
            anch, alt = hojas_aux(n-1, alto//2, ancho)
        return anch, alt
    
    if n == 0: # el caso n=0 no lo pide el enunciado
        # pero la implementación es trivial en este código
        ancho, alto = 841, 1189
    else:
        ancho, alto = hojas_aux(n-1)
    
    print(f'Según las normas ISO la hoja A{n} mide: {ancho}x{alto}')
    
    return (ancho, alto)

def main():
    for i in range(11):
        print(hojas(i))


if __name__ == '__main__':
    main()