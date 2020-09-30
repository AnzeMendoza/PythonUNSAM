import pandas as pd
import numpy as np
import os
import seaborn as sns

def main():
    directorio = 'Data'
    archivo = 'arbolado-publico-lineal-2017-2018.csv'
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    
    fname = os.path.join(directorio, archivo)
    df_lineal = pd.read_csv(fname)[cols_sel]

#    imprime todo el dataframe
    print(df_lineal[cols_sel])
    contador_ejemplares = df_lineal['nombre_cientifico'].value_counts().head(10)
    print(contador_ejemplares)
    
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]
    
    print(df_lineal_seleccion)
    
    df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')
    
    # sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')
    
if __name__ == '__main__':
    main()