# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn

def main():
    x = np.mat([ [0],[0],[0] ])#初期位置
    X = [x]
    #制御ベクトル
    v = 5
    w = 0.1
    if w == 0:
        r = float(v)
    else:
        r = float(v)/w


    time = 0
    u = np.mat([[-1*r*math.sin(math.radians(x[2]))+ r*math.sin(math.radians(x[2] + time*w))],
                        [r*math.cos(math.radians(x[2]))- r*math.cos(math.radians(x[2] + time*w))],
                        [w*time]])

    T = 100#観測数
    for i in range(T):
        x = x + u
        print r
        X.append(x)
        time += 0.01
        u = np.mat([[-1*r*math.sin(math.radians(x[2]))+ r*math.sin(math.radians(x[2] + time*w))],
                        [r*math.cos(math.radians(x[2]))- r*math.cos(math.radians(x[2] + time*w))],
                        [w*time]])

    a,b,c = np.array(np.concatenate(X,axis=1))
    plt.plot(a,b, 'r-')
    plt.show()

if __name__ == '__main__':
    main()
