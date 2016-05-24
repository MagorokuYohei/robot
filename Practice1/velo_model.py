# -*-config: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import seaborn
import random

def main():
    fig = plt.figure(figsize=(10,10))
    v   = 5
    w   = 2.5
    t   = 0.1

    x   = 0
    y   = 0
    deg = 0

    plt.xlim(-2.5,2.5)
    plt.ylim(-0.5,4.5)
    ims =[]
    for num in range(1500):
#        w = random.randint(-90,90)
        if w==0:
            w=0.1
        r   = v * w**(-1)

        x2 = x + (-r*math.sin(math.radians(deg)) + r*math.sin(math.radians(deg + w*t)))
        y2 = y + (r*math.cos(math.radians(deg)) - r*math.cos(math.radians(deg + w*t)))
        deg2= deg + w*t
        x = x2
        y = y2
        deg= deg2
#        im = plt.plot(x2,y2,color="r", marker="o")
#        ims.append(im)
        plt.plot(x2,y2,color="r", marker="o",markersize="1")

#    ani = animation.ArtistAnimation(fig, ims)
    plt.show()

if __name__ == '__main__':
    main()
