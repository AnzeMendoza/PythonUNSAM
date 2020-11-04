from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns

def ejercicio_seaborn():
    """Ejercicio 11.10
    Suele tardar unos 10 segundos en levantar el grafico.
    """
    iris_dataset = load_iris()
    # creamos un dataframe de los datos de flores
    # etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
    iris_dataframe = pd.DataFrame(
        iris_dataset["data"], columns=iris_dataset.feature_names
    )

    iris_dataframe["target"] = iris_dataset["target"]

    sns.pairplot(iris_dataframe, hue="target")


def main():
    ejercicio_seaborn()


if __name__ == "__main__":
    main()
