# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

def main():

    sigmas = 1
    myus = 0
    x = np.arange(-5., 5., 0.001)
    y = (1./np.sqrt(2*np.pi*sigmas)) * np.exp(-(x - myus)**2/2/sigmas)
    plt.plot(x, y)
    plt.show()

if __name__ =="__main__":
    main()
