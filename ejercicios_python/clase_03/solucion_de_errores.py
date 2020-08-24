# -*- coding: utf-8 -*-
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Solamente analiza el primer elemento de la cadena
#    elimine el else, ya que necesito recorrer toda la cadena.
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1 
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Falso no pertenece al keyword de Python, le agregue ':' tanto a
# los if, como while y dentro del if tenia una asignacion y no una comparacion.
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False
print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))
#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: una variable int no se puede iterar, lo que hice fue ver el tipo
# de varible que es expresion y convertirlo a string si es entero.
def tiene_uno(expresion):
    
    if type(expresion) != 'str':
        expresion = str(expresion)
    n = len( expresion )
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
#%%
# Ejercicio 3.3.
# Comentario: la funcion suma() no esta retornando ningun valor, o sea que
# esa c no es la misma que la c que esta fuera de la misma. Otro problema es
# que no se esta asignando la variable c.
def suma(a,b):
    c = a + b
    return c
    
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
# Ejercicio 3.3.
# Comentario: Lo que se estaba haciendo es copiar en todos los values de las 
# key la ultima fila que se estaba leyendo, o sea que el ultimo que ingresaba
# reemplaza a todos los anteriores. Lo que hice para solucionarlo fue
# con zip asociar un key:value y despues convertirlo a dict.
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado,fila))
            camion.append(registro)
    return camion

camion = leer_camion("Data/camion.csv")
pprint(camion)
#%%
