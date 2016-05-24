#-*- coding:utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import seaborn
from numpy import linalg as la

def main():
    """
    初期値(0,0)から移動量(1,1)で移動する

    位置情報を計測する
    誤差は、標準偏差1の正規分布に従う
    """
    x = np.mat([[0],[0]])#状態
    u = np.mat([[1],[1]])#制御
    T = 20#観測数
    mu   = x
    z    = x
    X = [x]
    M = [mu]
    Z = [z]

    sigm = np.mat([[0,0],
                   [0,0]])
    A    = np.mat([[1,0],
                   [0,1]])
    B    = np.mat([[1,0],
                   [0,1]])
    C    = np.mat([[1,0],
                   [0,1]])
    R    = np.mat([[0.01,0],
                   [0,0.01]])
    Q    = np.mat([[1,0],
                   [0,1]])
    I    = np.mat([[1,0],
                   [0,1]])

    for i in range(0, T):
        x = x + u
        X.append(x)

        mu_   = A*mu + B*u
        sigm_ = A*sigm*A.T + R
        z  = C*x + np.random.multivariate_normal([0,0], Q, 1).T
        K  = sigm_*C.T*(la.inv(C*sigm_*C.T+Q))
        mu = mu_ + K*(z - C*mu_)
        sigm = (I-K*C)*sigm_
        M.append(mu)
        Z.append(z)

    plt.figure(figsize=(10,10))
    a, b = np.array(np.concatenate(X,axis=1))
    plt.plot(a,b, 'ro-', label='real_path')

    a, b = np.array(np.concatenate(Z,axis=1))
    plt.plot(a,b, 'g*-', label='sensor_path')

    a, b = np.array(np.concatenate(M,axis=1))
    plt.plot(a,b, 'bs-', label='kalman_path')

    plt.legend(loc='lower right')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()



if __name__=='__main__':
    main()
