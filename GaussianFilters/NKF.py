#-*-coding:utf-8-*-

from matplotlib import pyplot as plt
import numpy as np
import seaborn
def sensor(x,L):
    s = np.array([[0.],[0.]])
    s[0] = get_dist(x,L)
    s[1] = get_deg(x,L)
    return s

def get_dist(x,L):
    return np.sqrt((x[0]-L[0])**2 + (x[1]-L[1])**2)
def get_deg(x,L):
    return np.degrees(np.arctan2((L[1]-x[1]),(L[0]-x[0]))) - x[2]

def main():
    #初期状態ｘ(x,y,θ)
    x = np.array([[0.0],[0.0],[0.0]])
    #ランドマーク初期位置L1(-10,-10)L2(10,　10)
    L1 = np.array([[-10],[-10]])
    L2 = np.array([[10],[10]])

    z1 = sensor(x,L1)
    z2 = sensor(x,L2)

    T = 43#観測回数
    time = 0

    X = [x]
    Z1 = [z1]
    Z2 = [z2]
    v = 5.
    w = 1.
    r = v/w
    for i in range(0,T):
        u = np.array([[-r*np.sin(np.radians(float(x[2])))+r*np.sin(np.radians(float(x[2]+w*time)))],
                      [r*np.cos(np.radians(float(x[2])))-r*np.cos(np.radians(float(x[2]+w*time)))],
                      [w*time]])
        x = x + u

        z1 = sensor(x,L1)
        z2 = sensor(x,L2)

        z1_pos = np.array([[x[1]+z1[0]*np.sin(float(np.radians(x[2]+z1[1])))],
                           [x[0]+z1[0]*np.cos(float(np.radians(x[2]+z1[1])))]])

        z2_pos = np.array([[x[1]+z2[0]*np.sin(float(np.radians(x[2]+z2[1])))],
                           [x[0]+z2[0]*np.cos(float(np.radians(x[2]+z2[1])))]])

        Z1.append(z1_pos)
        Z2.append(z2_pos)

        time += 0.1
        X.append(x)

    plt.figure(figsize=(10,10))
    a, b, c = np.array(np.concatenate(X,axis=1))
    plt.plot(a,b, 'r-', label='real_path')
    plt.plot(L1[0],L1[1], 'bs-', label='LandMark_1')
    plt.plot(L2[0],L2[1], 'bs-', label='LandMark_2')
    plt.xlim(-15,15)
    plt.ylim(-15,15)
    plt.legend()
    plt.show()

if __name__=='__main__':
    main()
