import numpy as np
import matplotlib.pyplot as plt 

def muestra_histograma(path_temperaturas):
    temperaturas = np.load(path_temperaturas)
    plt.hist(temperaturas, bins=25)
    plt.show()

def main():
    muestra_histograma('./Data/temperaturas.npy')

if __name__ == "__main__":
    main()