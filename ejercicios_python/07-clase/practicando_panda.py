import pandas as pd
import os
import seaborn as sns

#%%
directorio = 'Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

#imprime todo el dataframe
print(df)

#%%
# imprime a los primeros 5 del dataframe, se le puede indicar cuantos mostrar
print(df.head())

#%%
# imprime el nombre de las columnas del dataframe.
print(df.columns)

#%%
# hacemos uso del metodo describe que nos muestra las columnas de interes.
print(df[['altura_tot', 'diametro', 'inclinacio']].describe())

#%%
# el metodo unique, me devuelve una np.array con los nombres de todos los
# registros que aparecen en esa columna sin repetición.

print(df['nombre_com'].unique())

#%%
# genero un array booleado el cual me puede servir para contar por ejemplo.

# retorna un array de booleanos que cumplen esa condición
print(df['nombre_com'] == 'Ombú')

# sumo los True que hay en el array.
print((df['nombre_com'] == 'Ombú').sum())

#%%
# el uso del metodo value_counts no ayudara a contar elementos de una columna
# del dataframe

cant_ejemplares = df['nombre_com'].value_counts()
print(cant_ejemplares)

#%%
# podemos utilizarlo para seleccionar las filas que coinciden

df_jacarandas = df[df['nombre_com'] == 'Jacarandá']
print(df_jacarandas)
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
print(df_jacarandas)
print(df_jacarandas.describe())

df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()

print(df_jacarandas)

#%%
# pandas tiene para hacer plots
df_jacarandas.plot.scatter(x = 'diametro', y = 'altura_tot')

#%%
# Se utiliza mas sns para hacer plots mas profesionales
sns.scatterplot(data = df_jacarandas, x = 'diametro', y = 'altura_tot')

#%% 
# filtros por indice y posición
print(cant_ejemplares.index)

#%%
# Podemos acceder a una fila de un DataFarme o una Serie tanto a través de su 
# posición como a través de su índice. Para acceder con el índice usá loc[] 
# como en los siguientes ejemplos:
print(df.loc[165])

#%% 
# Para acceder por número de posición usá iloc
print(df_jacarandas.iloc[0])

#%% 
df_jacarandas_diam = df_jacarandas['diametro']
print(type(df_jacarandas_diam))

#%% 
# 
import numpy as np
import pandas as pd

idx = pd.date_range('20200923 14:00', periods = 120, freq = 'min')
s1 = pd.Series(np.random.randint(-1,2,120), index = idx)
s2 = s1.cumsum()
s2.plot()

w = 5 # ancho en minutos de la ventana
s3 = s2.rolling(w).mean()
s3.plot()

df_series_23 = pd.DataFrame([s2, s3]).T  # armo un dataframe con ambas series
df_series_23.plot()

#%% 
# Ejemplo: 12 personas caminando 8 horas

import pandas as pd
import numpy as np

horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()

df_walk_suav.to_csv('caminata_apostolica.csv')