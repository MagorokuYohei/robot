# -*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn

def main():
    mu1 = [5,5]
    mu2 = [2,2]

    cov = [[1,100],[100,1]]

    x1,y1 = np.random.multivariate_normal(mu1,cov,100).T
    print x1
    print y1
    plt.axis([-10,10,-10,10],size=20)
    plt.scatter(x1,y1)
    plt.show()
    plt.close()

if __name__=='__main__':
    main()
