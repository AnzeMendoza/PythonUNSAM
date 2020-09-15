#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 02:10:11 2020

@author: sucho
"""
import fileparse
import gzip
with gzip.open('Data/camion.csv.gz', 'rt') as file:
     camion = fileparse.parse_csv(file, types=[str,int,float])
lines = ['name,cajones,precio', 'Lima,100,34.23', 'Naranja,50,91.1', 'Mburucuya,75,45.1']
camion = fileparse.parse_csv(lines, types=[str,int,float])

print(camion)
camion = fileparse.parse_csv('Data/camion.csv', types=[str,int,float])
print(camion)