# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import *
from pylab import *


def main():
    fig = plt.figure(figsize=(10,10))
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

    title = ""
    a=0
    b=0
    c=0
    d=0
    tx=0
    ty=0

    print"Translation           :1"
    print"Mirroring at y-axis   :2"
    print"Rotation              :3"
    print"Motion                :4"
    print"Similarity            :5"
    print"Scale difference      :6"
    print"Shear                 :7"

    num = raw_input()

    if num == "1":
        title = "Translation"
        a  = 1
        b  = 0
        c  = 0
        d  = 1
        tx = 5
        ty = 5
    elif num == "2":
        title = "Mirroring"
        a  = -1
        b  = 0
        c  = 0
        d  = -1
        tx = 0
        ty = 0
    elif num == "3":
        title = "Rotation"
        ag = math.radians(45)
        a  = np.cos(ag)
        b  = np.sin(ag)*-1
        c  = np.sin(ag)
        d  = np.cos(ag)
        tx = 0
        ty = 0
    elif num == "4":
        title = "Motion"
        ag = math.radians(45)
        a  = np.cos(ag)
        b  = np.sin(ag)*-1
        c  = np.sin(ag)
        d  = np.cos(ag)
        tx = 5
        ty = 5
    elif num == "5":
        title = "Similarity"
        a  = 2
        b  = -2
        c  = 2
        d  = 2
        tx = 2
        ty = 2
    elif num == "6":
        title = "Scale difference"
        m  = 5
        a  = 1 + m/2
        b  = 0
        c  = 0
        d  = 1 - m/2
        tx = 0
        ty = 0
    elif num == "7":
        title = "shear"
        s  = 5
        a  = 1
        b  = s/2
        c  = s/2
        d  = 1
        tx = 0
        ty = 0







    afin = np.array([[a, b, tx],[c, d, ty], [0, 0 ,1]])

    print afin

    x_pos = []
    y_pos = []
    temp = afin.dot(pos0)
    xx0=temp[0]
    yy0=temp[1]
    x_pos.append(temp[0])
    y_pos.append(temp[1])
    temp = afin.dot(pos1)
    xx1=temp[0]
    yy1=temp[1]
    x_pos.append(temp[0])
    y_pos.append(temp[1])
    temp = afin.dot(pos2)
    xx2=temp[0]
    yy2=temp[1]
    x_pos.append(temp[0])
    y_pos.append(temp[1])
    temp = afin.dot(pos3)
    xx3=temp[0]
    yy3=temp[1]
    x_pos.append(temp[0])
    y_pos.append(temp[1])

    plt.title(title)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.fill(pre_x_pos,pre_y_pos,color="#454521",alpha=0.5)
    plt.fill(x_pos,y_pos,color="#00FF00",alpha=0.5)
    plt.show()

    print x_pos
    print y_pos

if __name__ == '__main__':
    main()
