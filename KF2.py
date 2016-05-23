# -*-coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la
import seaborn

def lkf(T, Y, U, mu0, sigm0, A, B, C, R,Q):
    #初期推定値
    mu = mu0
    sigm = sigm0
    #状態推定値
    M = [mu]

    for i in range(T):
        mu_ = A*mu + B*U[i]
        sigm_ = R + A*sigm * A.T

        S = C*sigm_*C.T + Q
        yi= Y[i+1] - C*mu_

        K = sigm_ * C.T * la.inv(S)

        mu = mu_ + K*yi
        sigm = sigm_ - K*C*sigm_
        M.append(mu)

    return M

def main():
    #カルマンフィルタ係数
    A = np.mat([[1,0],[0,1]])
    B = np.mat([[1,0],[0,1]])
    C = np.mat([[1,0],[0,1]])
    R = np.mat([[1,0],[0,1]])
    Q = np.mat([[2,0],[0,2]])


    #観測数
    T = 10

    #状態初期値、入力
    x = np.mat([[0],[0]])
    u= np.mat([[2],[2]])

    X = [x]#状態
    Y = [x]#観測

    U = [u]#制御

    for i in range(T):
        x = A*x + B*u #+ np.random.multivariate_normal([0,0], R, 1).T
        X.append(x)
        y = C*x + np.random.multivariate_normal([0,0], Q, 1).T
        Y.append(y)
        U.append(u)

    #LKF
    #初期値
    mu0   = np.mat([[0],[0]])
    sigm0 = np.mat([[0,0],[0,0]])
    M = lkf(T, Y, U, mu0, sigm0, A, B, C, R, Q)
    a, b = np.array(np.concatenate(X,axis=1))
    plt.plot(a,b,'rs-',label="Real_Value")
    a2, b2 = np.array(np.concatenate(Y,axis=1))
    plt.plot(a2,b2,'g^-',label='Sensor_Value')
    a3, b3 = np.array(np.concatenate(M,axis=1))
    plt.plot(a3,b3,'bo-',label='Kalman_Filter')
    plt.legend(loc='lower right')
    plt.figtext(0.15,0.8, "Sensor sigm : %f"%(sum((a-a2)**2 + (b-b2)**2)/100))
    plt.figtext(0.15,0.7, "Kalman sigm : %f"%(sum((a-a3)**2 + (b-b3)**2)/100))

#    print sum((a-a2)**2 + (b-b2)**2)/100
#    print

    plt.show()

if __name__=='__main__':
    main()
