# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def main():
    fig = plt.figure()

    x=0
    y=0
    pos  = np.matrix([[x],[y],[1]] )
    a=1
    b=1
    c=1
    d=1
    tx=2
    ty=2
    afin = np.matrix([[a, b, tx],[c, d, ty], [0, 0 ,1]])
    temp = afin.dot(pos)

    print temp
    nX = temp[0]
    nY = temp[1]

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y, color="k", marker="o")
    plt.plot(nX, nY, color="r", marker="s")
    # 始点(0.2,0.2)で幅が0.2, 高さが0.4の長方形を描画
    #rect = plt.Rectangle((0.2,0.2),0.2,0.4,fc="#7700FF")
    #ax.add_patch(rect)
    plt.show()

if __name__ == '__main__':
    main()
