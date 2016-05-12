# -*-coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn
import math
def main():
    fig = plt.figure()
    v = 1
    w = 0.001
    r = float(v)/w
    print r
    x = 0
    y = 0
    deg = 90

    time = 1
    Status  = np.array([[x],[y],[deg]])
    N_Status = np.array([[0], [0], [0]])
    plt.xlim(-2,2)
    plt.ylim(-0.5,5)

    for num in range(1000):
        Control = np.array([[-1*r*math.sin(math.radians(Status[2]))+ r*math.sin(math.radians(Status[2] + time*w))],
                        [r*math.cos(math.radians(Status[2]))- r*math.cos(math.radians(Status[2] + time*w))],
                        [w*time]])
        N_Status = Status + Control
        Status   = N_Status
#        im = plt.plot(Status[0],Status[1],color="r", marker="o")
#        ims.append(im)
        plt.plot(Status[0],Status[1],color="r", marker="o")

#    ani = animation.ArtistAnimation(fig, ims)
    plt.show()

if __name__=="__main__":
    main()
