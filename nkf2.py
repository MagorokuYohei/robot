# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import seaborn
from numpy import linalg as la
import math
import random

def L_dist(x,L):
    return np.sqrt( (x[0]-L[0])**2 + (x[1]-L[1])**2 )
def L_deg(x,L):
    return np.degrees(np.arctan2((x[1]-L[1]),(x[0]-L[0])))-x[2]
def z_pos(x,z):
    return x[0]+z[0]*np.cos(np.radians(x[2]-z[1])), x[1]+z[0]*np.sin(np.radians(x[2]-z[1]))
def reverse(X):
    D = np.array([[X[1][1], -X[0][1]],
                 [-X[1][0], -X[0][0]]])
    return (1/(X[0][0]*X[1][1]))*D

def main():
    x = np.array([[0],[0],[0]])#状態(x,y,deg)
    L = np.array([[0],[10]])#ランドマーク位置(x,y)
    z = np.array([[0.],[0.]])#ランドマーク観測値(r,deg)

    v = 20#速度
    w = 2#角速度
    T = 50#観測数
    time = 0
    #各種パラメータ保存リスト
    Ob = [x]
    X  = [x]
    U  = []
    Z  = []
    Z2 = []
    J  = []
    W  = []

    R = np.array([[0.01,0,0],[0,0.01,0],[0,0,0] ])#制御誤差
    o = x
    Q = np.array([[0.1,0.],[0.,0.1]])#制御誤差


    #観測値取得
    for i in range(T):
#        w = random.uniform(-5,5)
        if w == 0:
            w = 0.00001
        r = v/w
        W.append(w)
        time += 0.1
        #状態X
        u = np.array([[-1*r*np.sin(math.radians(x[2]))+ r*math.sin(np.radians(x[2] + time*w))],
                [r*np.cos(math.radians(x[2]))- r*np.cos(math.radians(x[2] + time*w))],
                [time*w]
                ])
        j = np.mat([[0,0,-1*r*np.cos(np.radians(x[2]))+ r*np.cos(np.radians(x[2] + time*w))],
                    [0,0,-1*r*np.sin(np.radians(x[2]))- r*np.sin(np.radians(x[2] + time*w))],
                    [0,0,0]])

        x = x + u + np.random.multivariate_normal([0,0,0], R, 1).T
        o = o + u
        if x[2] < -360:
            x[2] = x[2]+ 360
        elif x[2] > 360:
            x[2] = x[2]-360
        #観測Z
        z[0] = L_dist(x,L)
        z[1] = L_deg(x,L)#-x[2]
        if z[1] < -360:
            z[1] = z[1]+ 360
        elif z[1] > 360:
            z[1] = z[1]-360
        z   +=  np.random.multivariate_normal([0,0], Q, 1).T
#        print z
        Z2.append(z)

        print "x**************"
        print x
        print "z**************"
        print z

        fa,fb   = z_pos(x,z)
        z2 = np.array([[fa],[fb]])#ランドマーク観測値(r,deg)
        print "z2**************"
        print z2
        Ob.append(o)
        X.append(x)
        Z.append(z2)
        U.append(u)
        J.append(j)

    #EKF発動
    F = np.array([[1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0]])
    F2 = np.array([[1,0,0,0,0],
                   [0,1,0,0,0],
                   [0,0,1,0,0],
                   [0,0,0,1,0],
                   [0,0,0,0,1]])
    I = np.array([[1,0,0,0,0],
                  [0,1,0,0,0],
                  [0,0,1,0,0],
                  [0,0,0,1,0],
                  [0,0,0,0,1]])
    R2 = np.array([[0.01,0,0,0,0],
                   [0,0.01,0,0,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0],
                   [0,0,0,0,0]])#制御誤差

    mu = np.array([[0],[0],[0],[0],[0]])
    sigm = np.zeros((5,5))
    dam = np.zeros((2,2))
    omg = np.zeros((2,1))
    z_ = np.zeros((2,1))
    M = []
    time = 0
    for i in range(T):
        time += 0.1
        r = v/W[i]
        u = np.array([[-r*np.sin(math.radians(mu[2]))+ r*math.sin(math.radians(mu[2] + time*W[i]))],
                      [r*np.cos(math.radians(mu[2]))- r*np.cos(math.radians(mu[2] + time*W[i]))],
                      [time*W[i]]
                      ])
        mu_ = mu + (F.T).dot(u)
        u2 = np.array([[0,0,-r*np.cos(math.radians(mu[2]))+ r*math.cos(math.radians(mu[2] + time*W[i]))],
                      [0,0,-r*np.sin(math.radians(mu[2]))+ r*np.sin(math.radians(mu[2] + time*W[i]))],
                      [0,0,0]
                      ])
        G = I + (F.T).dot(u2.dot(F))
        sigm_ = G.dot(sigm.dot(G.T)) + (F.T).dot(R.dot(F))
        dlt = Z2[i]
        zx  = mu_[0] + (dlt[0]*np.cos(math.radians(dlt[1]+mu_[2])))
        zy  = mu_[1] + (dlt[0]*np.sin(math.radians(dlt[1]+mu_[2])))
        omg[0] = zx - mu_[0]
        omg[1] = zy - mu_[1]
        q   = (omg.T).dot(omg)
        z_[0]  = np.sqrt(q)
        z_[1]  = math.degrees(np.arctan2(omg[1],omg[0]))-mu_[2]
        if z[1] < -360:
            z[1] = z[1]+ 360
        elif z[1] > 360:
            z[1] = z[1]-360
        h   = np.array([[np.sqrt(q)*omg[0], -np.sqrt(q)*omg[1], 0, -np.sqrt(q)*omg[0], np.sqrt(q)*omg[1]],
                        [omg[1], omg[0], -1, -omg[1], -omg[0]]])
        H   = (1/q)*h.dot(F2)
        S   = H.dot(sigm_.dot(H.T)) + Q
        MAGO1 = S[0].T
        MAGO2 = S[1].T
        SS  = np.array([[MAGO1[0], MAGO1[1]],
                        [MAGO2[0], MAGO2[1]]])
        D = np.array([[SS[1][1], -SS[0][1]],
                     [-SS[1][0], -SS[0][0]]])
        SS = (1/(SS[0][0]*SS[1][1]))*D
        dam[0][0] = SS[0][0]
        dam[0][1] = SS[0][1]
        dam[1][0] = SS[1][0]
        dam[1][1] = SS[1][1]
#        SS  = reverse(SS)
        K   = sigm_.dot((H.T).dot(dam))
        mu  = mu_ + K.dot(dlt - z_)
#        print K
        if mu[2] < -360:
            mu[2] = mu[2]+ 360
        elif mu[2] > 360:
            mu[2] = mu[2]-360
        sigm = (I-K.dot(H)).dot(sigm_)
        M.append(mu)

    plt.plot(L[0],L[1],'ko')
    ra,rb,rc = np.array(np.concatenate(X,axis=1))
    plt.plot(ra,rb,'r-',label='Real_Path')
#    a,b,c = np.array(np.concatenate(Ob,axis=1))
#    plt.plot(a,b,'b-',label='Ideal_Path')
    za,zb = np.array(np.concatenate(Z,axis=1))
#    print za
    plt.plot(za,zb,'g-',label='Obseve_Path')
    ea,eb,ec,ed,ee = np.array(np.concatenate(M,axis=1))
    plt.plot(ea,eb,'y-',label='EKF_Path')
    plt.legend(loc='lower right')
    plt.show()

if __name__=='__main__':
    main()
