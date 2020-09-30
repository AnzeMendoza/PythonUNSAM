import pandas as pd
import numpy as np
import os


def my_boxplot_especie(path_parque, path_vereda, especie ,columna):
    """Hace el boxplot de la columna que uno le pase como parametro
    pre: el path tanto de parque como de vereda, tiene que estar en un nivel de carpetas.
    post: ejecutando desde consola no muestra los plots.
    """
    parse_path_parque = os.path.split(path_parque)
    parse_path_vereda = os.path.split(path_vereda)
    df_parques = pd.read_csv(os.path.join(parse_path_parque[0], parse_path_parque[1]))
    df_veredas = pd.read_csv(os.path.join(parse_path_vereda[0], parse_path_vereda[1]))

    df_tipas_parques = df_parques[df_parques["nombre_cie"] == especie].copy()
    df_tipas_parques.loc[:, "ambiente"] = np.array(["parque"] * len(df_tipas_parques))

    df_tipas_veredas = df_veredas[
        df_veredas["nombre_cientifico"] == especie
    ].copy()
    df_tipas_veredas.loc[:, "ambiente"] = ["vereda"] * len(df_tipas_veredas)

    df_tipas_veredas.rename(
        columns={
            "altura_arbol": "altura_tot",
            "diametro_altura_pecho": "diametro",
            "nombre_cientifico": "nombre_cie",
        },
        inplace=True,
    )

    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    df_tipas.boxplot(columna, by="ambiente")


def main():
    my_boxplot_especie(
        "Data/arbolado-en-espacios-verdes.csv",
        "Data/arbolado-publico-lineal-2017-2018.csv",
        "Tipuana Tipu",
        "altura_tot",
    )
    my_boxplot_especie(
        "Data/arbolado-en-espacios-verdes.csv",
        "Data/arbolado-publico-lineal-2017-2018.csv",
        "Tipuana Tipu",
        "diametro",
    )


if __name__ == "__main__":
    main()
