# -*-coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as la


def KF(A, B, C, R, Q, T, U, Z):
    mu   = np.mat([[0],[0]])
    sigm = np.mat([[0,0],[0,0]])

    M = [mu]

    for i in range(T):
        mu_ = A*mu+B*U[i]
        sigm_ = A*sigm*A.T + R
        S = C*sigm_*C.T + Q
        K = sigm_*C*la.inv(S)
        Y = Z[i+1]-C*mu_
        mu= mu_ + K*Y
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

    #状態ベクトルX
    x = np.mat([[0],[0]])
    X = [x]
    #制御ベクトルY(一定)
    u = np.mat([[0],[2]])
    U = [u]
    #計測ベクトルZ
    Z = [x]
    #試行回数T
    T = 10

    for i in range(T):
        x = A*x + B*u + np.random.multivariate_normal([0,0], R, 1).T
        X.append(x)
        z = C*x + np.random.multivariate_normal([0,0], Q, 1).T
        Z.append(z)
        U.append(u)

    K =KF(A, B, C, R, Q, T, U, Z)

    a, b = np.array(np.concatenate(X,axis=1))
    plt.plot(a,b,'rs-')
    a2, b2 = np.array(np.concatenate(Z,axis=1))
    plt.plot(a2,b2,'g^-')
    a3, b3 = np.array(np.concatenate(K,axis=1))
    plt.plot(a3,b3,'bo-')
    plt.xlim(-15,15)
    plt.ylim(0,30)
    plt.show()

if __name__=="__main__":
    main()
