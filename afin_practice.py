# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
from pylab import *


def matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos):
    afin = np.array([[a, b, tx],[c, d, ty], [0, 0 ,1]])
    x_pos = []
    y_pos = []
    temp = afin.dot(pos0)
    x_pos.append(temp[0])
    y_pos.append(temp[1])
    temp = afin.dot(pos1)
    x_pos.append(temp[0])
    y_pos.append(temp[1])
    temp = afin.dot(pos2)
    x_pos.append(temp[0])
    y_pos.append(temp[1])
    temp = afin.dot(pos3)
    x_pos.append(temp[0])
    y_pos.append(temp[1])

    print x_pos
    print y_pos

    plt.title(title)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.fill(pre_x_pos,pre_y_pos,color="#454521",alpha=0.5)
    plt.fill(x_pos,y_pos,color="#00FF00",alpha=0.5)

def main():
    fig = plt.figure()
    x=0
    y=0
    x_l = 2
    y_l = 2
    pos0  = np.array([[x],[y],[1]] )
    pos1  = np.array([[x],[y+2],[1]] )
    pos2  = np.array([[x+2],[y+2],[1]] )
    pos3  = np.array([[x+2],[y],[1]] )

    pre_x_pos =[pos0[0],pos1[0],pos2[0],pos3[0]]
    pre_y_pos =[pos0[1],pos1[1],pos2[1],pos3[1]]

    title = "Translation"
    a  = 1
    b  = 0
    c  = 0
    d  = 1
    tx = 5
    ty = 5
    plt.subplot(231)
    matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos)

    title = "Mirroring"
    a  = -1
    b  = 0
    c  = 0
    d  = -1
    tx = 0
    ty = 0
    plt.subplot(232)
    matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos)

    title = "Rotation"
    ag = math.radians(45)
    a  = np.cos(ag)
    b  = np.sin(ag)*-1
    c  = np.sin(ag)
    d  = np.cos(ag)
    tx = 0
    ty = 0
    plt.subplot(233)
    matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos)

    title = "Motion"
    ag = math.radians(45)
    a  = np.cos(ag)
    b  = np.sin(ag)*-1
    c  = np.sin(ag)
    d  = np.cos(ag)
    tx = 5
    ty = 5
    plt.subplot(234)
    matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos)

    title = "Similarity"
    a  = 2
    b  = -2
    c  = 2
    d  = 2
    tx = 2
    ty = 2
    plt.subplot(235)
    matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos)

    title = "Scale difference"
    m  = 5
    a  = 1 + m/2
    b  = 0
    c  = 0
    d  = 1 - m/2
    tx = 0
    ty = 0
    plt.subplot(236)
    matrin(title, a, b, c, d, tx, ty, pos0, pos1, pos2, pos3, pre_x_pos, pre_y_pos)

    title = "shear"
    s  = 5
    a  = 1
    b  = s/2
    c  = s/2
    d  = 1
    tx = 0
    ty = 0

    plt.show()


if __name__ == '__main__':
    main()
