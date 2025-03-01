import pandas as pd
import os

def mareas(path):
    ''' Se trato de super poner las dos señales de forma manual.
    pre: ver la ubicación correcta del archivo.
    post: se imprime por consola los deltas.
    '''
    parse_path = os.path.split(path)
    df_mareas = pd.read_csv(os.path.join(parse_path[0], parse_path[1]), index_col=['Time'], parse_dates=True)
    
    dh_25_12_2014 = df_mareas['12-25-2014':].copy()
    delta_t = -1 # tiempo que tarda la marea entre ambos puertos
    delta_h = 22 # diferencia de los ceros de escala entre ambos puertos
    pd.DataFrame([dh_25_12_2014['H_SF'].shift(delta_t) - delta_h, dh_25_12_2014['H_BA']]).T.plot()
    print(f'Delta t: {delta_t}')
    print(f'Delta h: {delta_h}')
    
def main():
    mareas('Data/OBS_SHN_SF-BA.csv')
    
if __name__ == '__main__':
    main()