"""
    El archivo informe.py del Ejercicio 9.2.
    El archivo camion.py del Ejercicio 9.3 (o Ejercicio 9.14) que va a jugar en la revisión de pares.
    El archivo vigilante.py del Ejercicio 9.7.
    El archivo ticker.py del Ejercicio 9.12 (o del Ejercicio 9.15).
    Y, opcionalmente, el archivo simulacion.py del Ejercicio 9.19.
"""

#%%
#Ejercicio 9.1

"""Al llegar a sobrepasar la cantidad de elementos iterables, lanza una 
excepción.
"""
a = [1,9,4,25,16]

iter_a = a.__iter__()
for i in range(6):
    print(iter_a.__next__())

#%%
f = open('Data/camion.csv')

f.__iter__()

next(f)

#%%
#Ejercicio 9.2
