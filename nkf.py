# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math
import seaborn
from numpy import linalg as la

def L_dist(x,L):
    return np.sqrt( (x[0]-L[0])**2 + (x[1]-L[1])**2 )
def L_deg(x,L):
    return np.degrees(np.arctan2((x[1]-L[1]),(x[0]-L[0])))


def main():
    x = np.mat([ [0],[0],[0], [0],[0]])#初期位置&ランドマーク観測位置
    X = [x]
    U = []
    J = []
    Z = []

    L = np.mat([ [0],[2.5]])#ランドマーク位置

    v = 5
    w = 2
    if w == 0:
        r = float(v)
        w=0.1
    else:
        r = float(v)/w


    time = 0
    T = 400#観測数

    #航行データ作成
    for i in range(T):
        l_dist =  L_dist(x,L)
        l_deg  = L_deg(x,L)
        if l_deg < -360:
            l_deg = L_deg(x,L)+360
        elif l_deg >360:
            l_deg = L_deg(x,L)-360

        x[3] = l_dist
        x[4] = l_deg-x[2]
        z = np.mat([ [0.0],[0.0] ])#初期位置&ランドマーク観測位置
        z[0] = l_dist
        z[1] = l_deg

#        print l_deg
#        print z

        u = np.mat([[-1*r*math.sin(math.radians(x[2]))+ r*math.sin(math.radians(x[2] + time*w))],
                        [r*math.cos(math.radians(x[2]))- r*math.cos(math.radians(x[2] + time*w))],
                        [time*w],
                        [0],
                        [0]])
        j = np.mat([[1,0,-1*r*math.cos(math.radians(x[2]))+ r*math.cos(math.radians(x[2] + time*w)),0,0],
                    [0,1,-1*r*math.sin(math.radians(x[2]))- r*math.sin(math.radians(x[2] + time*w)),0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1]
                    ])

        x = x + u
        if x[2] < -360:
            x[2] = x[2]+ 360
        elif x[2] > 360:
            x[2] = x[2]-360

        X.append(x)
        U.append(u)
        J.append(j)
        Z.append(z)
        time += 0.01

#    print Z
    #EKF作成
    x = np.mat([[0],[0],[0],[0],[0]])
    sigm = np.mat([[1,0,0,0,0],
                    [0,1,0,0,0],
                    [0,0,1,0,0],
                    [0,0,0,1,0],
                    [0,0,0,0,1]])
    R = np.mat([[1,0,0,0,0],
                [0,1,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0]])
    omg = np.mat([[1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [0,0,0,0,1]])
    F   = np.mat([[1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [0,0,0,0,1]])
    r_m = np.mat([[0.],[0.]])
    _h = np.mat([[0.],[0.]])
#    H = np.mat([[0.,0.,0.,0.,0.],[0.,0.,0.,0.,0.]])
    Q = np.mat([[1,0],
                [0,1]])
    inv = np.mat([[1,0],
                [0,1]])

    for i in range(T):
        _mu = x + U[i]
        _sigm = J[i]*sigm*J[i].T + np.random.multivariate_normal([0,0,0,0,0], R, 1).T

        r_m[0] = Z[i][0] *np.cos(Z[i][1]+_mu[2])
        r_m[1] = Z[i][0] *np.sin(Z[i][1]+_mu[2])
        omg = Z[i]-r_m
        q   = omg.T*omg
#        _h[0]= np.sqrt(q)
#        _h[1]= np.arctan2(omg[1],omg[0])-_mu[2]
        H = np.mat([[-1*np.sqrt(q)*omg[0]/q, -1*np.sqrt(q)*omg[1]/q, 0 , np.sqrt(q)*omg[0]/q, np.sqrt(q)*omg[1]/q],
                    [omg[1]/q, -1*omg[0]/q, -q/q, -omg[1]/q, omg[0]/q]
                    ])
        Hh = H*F
        S = Hh*_sigm*Hh.T + Q
        K  = _sigm*Hh.T
        
        _mu_l = _mu




    a,b,c,d,e = np.array(np.concatenate(X,axis=1))
    plt.plot(L[0], L[1], 'bo')#ランドマーク

    plt.plot(a,b, 'r-')
    plt.show()

if __name__ == '__main__':
    main()
