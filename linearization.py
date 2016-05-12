# -*-coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn
def main():
    x = np.arange(-10,10,0.01)
    mu   = 0
    sigm = 1

    px = (1/ np.sqrt(2*np.pi*sigm*sigm))*np.exp(( -(x-mu)**2 )/( (2*sigm*sigm) ))

    a = 1
    b = 1
    y = a*x+b


    py = (1/np.sqrt(2*np.pi*a*a*sigm*sigm)) * np.exp( (-(y-(a*mu)-b )**2 )/(2*sigm*sigm*a*a) )
    print y
    print py
    plt.subplot(224)
    plt.xlim(-10,10)
    plt.ylim(0,1)
    plt.plot(x,px,"k-")
    plt.subplot(221)
    plt.xlim(0,1)
    plt.ylim(-10,10)
    plt.plot(py,y,"k-")
    plt.subplot(222)
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.plot(x,y,"k-")


    plt.show()

if __name__=="__main__":
    main()
