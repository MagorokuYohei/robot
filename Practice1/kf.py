# -*-coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn
import math
from numpy import linalg as la

def KF(A,B,C,R,Q,T,U,Z):
    mu   = np.mat([ [0],[-50],[0] ])
    sigm = np.mat([[0,0,0],[0,0,0],[0,0,0]])
    M = [mu]
    for i in range(T):
        mu_ = A*mu+B*U[i]
        sigm_ = R + A*sigm*A.T

        S = C*sigm_*C.T + Q
        Y = Z[i+1] - C*mu_

        K = sigm_*C.T*la.inv(S)
        mu = mu_ + K*Y
        sigm = sigm_ - K*C*sigm_
        M.append(mu)
    return M

def main():
    #カルマンフィルタ
    A =np.mat([[1,0,0], [0,1,0],[0,0,1]])
    B =np.mat([[1,0,0], [0,1,0],[0,0,1]])
    C =np.mat([[1,0,0], [0,1,0],[0,0,1]])
    R =np.mat([[1,0,0], [0,1,0],[0,0,1]])
    Q =np.mat([[2,0,0], [0,2,0],[0,0,2]])

    fig = plt.figure(figsize=(10,10))
    #状態ベクトル
    x = np.mat([ [0],[-50],[0] ])
    X = [x]
    #制御ベクトル
    v = 100
    w = 2
    r = float(v)/w
    time = 1
    u = np.mat([[-1*r*math.sin(math.radians(x[2]))+ r*math.sin(math.radians(x[2] + time*w))],
                        [r*math.cos(math.radians(x[2]))- r*math.cos(math.radians(x[2] + time*w))],
                        [w*time]])

    U = [u]
    #観測ベクトル
    z = x
    Z = [z]
    #試行回数
    T = 20
    for num in range(T):
        x = A*x + B*u + np.random.multivariate_normal([0,0,0], R,1).T
        z = C*x + np.random.multivariate_normal([0,0,0], Q,1).T
#        x = x+u
        u = np.mat([[-1*r*math.sin(math.radians(x[2]))+ r*math.sin(math.radians(x[2] + time*w))],
                            [r*math.cos(math.radians(x[2]))- r*math.cos(math.radians(x[2] + time*w))],
                            [w*time]])
        X.append(x)
        Z.append(z)
        U.append(u)


    K = KF(A,B,C,R,Q,T,U,Z)

    a,b,c = np.array(np.concatenate(X,axis=1))
    plt.plot(a,b, 'rs-')
    a2,b2,c2 = np.array(np.concatenate(Z,axis=1))
    plt.plot(a2,b2, 'bx-')
    a3,b3,c3 = np.array(np.concatenate(K,axis=1))
    plt.plot(a3,b3, 'go-')


#    plt.xlim(-100,100)
#    plt.ylim(-100,100)
    plt.show()

    print "観測値　誤差　%f" % (sum((a-a2)**2 + (b-b2)**2)/T)
    print "カルマン　誤差　%f" % (sum((a-a3)**2 + (b-b3)**2)/T)

if __name__=="__main__":
    main()
