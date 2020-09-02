
def hipoteca():
    saldo = 500000.0
    tasa = 0.05
    pago_mensual = 2684.11
    total_pagado = 0.0
    contador_meses = 0
    
    while saldo != 0:
        if contador_meses >= 61 and contador_meses <= 108:
            saldo = saldo * (1+tasa/12) - pago_mensual - 1000
            total_pagado += pago_mensual + 1000
        elif saldo > pago_mensual:
            saldo = saldo * (1+tasa/12) - pago_mensual
            total_pagado += pago_mensual
        else:
            total_pagado += saldo
            saldo = 0
    
        contador_meses += 1
        print(f'{contador_meses} {round(total_pagado, 2)} {round(saldo,2)}')
    
    print('Total pagado', round(total_pagado, 2))
    print("meses: ", contador_meses)

def main():
    hipoteca()
    
if __name__ == '__main__':  
    main()
