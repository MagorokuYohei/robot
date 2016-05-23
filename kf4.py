#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn

def main():

    N = 200
    #状態は常に一定
    x = 5
    #観測誤差は標準偏差2の正規分布に従う
    mu = x
    sigma  = 2

    #カルマン初期値
    kmu   = 0#初期状態
    ksigm = 0#初期共分散
    R     = 0.00001 #雑音
    Q     = 0.01

    l_x = []
    l_y = []
    l_x.append(0)
    l_x.append(N)
    l_y.append(5)
    l_y.append(5)
    plt.plot(l_x,l_y, 'k-', label='real')

    k_x = []
    k_y = []
    for i in range(0, N):
        x = random.normalvariate(mu, sigma)
        t = i
        plt.plot(t,x, 'ro-')

        kmu_ = kmu
        ksigm_ = ksigm + R

        K = ksigm_/(ksigm_ + Q)
        kmu = kmu_ + K*(x - kmu_)
        ksigm = (1-K)*ksigm_
        k_x.append(i)
        k_y.append(kmu)

        print   ksigm
        print   K

    plt.plot(k_x,k_y, 'b-')

    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()

if __name__=='__main__':
    main()
