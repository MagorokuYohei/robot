# -*-coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.animation as animation

def gaus(x,myu, sigm):
    return (1/np.sqrt(2*np.pi*sigm*sigm) * np.exp( -1* ((x-myu)**2)/(2*sigm*sigm) ))

def main():
    fig = plt.figure()
    ims = []
    d = [0, 2 ,5, 15]

    plt.title('point')
    plt.subplot(211)
    x = np.arange(-1,30,0.1)
    bunbun = 0.2
    y = gaus(x,d[0], bunbun) + gaus(x,d[1], bunbun) + gaus(x, d[2], bunbun) + gaus(x, d[3], bunbun)
    plt.plot(x, y)

    for a in range(0,11):
        if a ==d[0] or a ==d[1] or a ==d[2] or a ==d[3]:
            plt.plot(a, 2.5, marker='o', color='r')
    plt.xlim(-1, 30)
    plt.ylim(0, 6)

    plt.subplot(212)
    plt.title('move')
    bun = 0.8
    bun2=0
    bun3=0
    bun4=0
    bun5=0
    ct = 0

    pos2=0
    pos3=0
    pos4=0
    pos5=0

    gosa = 0.02

    sp = 2
    msp= float(1)/(float(10)/sp)
    for a in range(-10,150):
        bun += gosa
        pos = float(a)/(float(10)/sp)
        im = plt.plot(pos,2,color="k", marker="o")
        y2 = gaus(x, pos, bun)
        if pos ==d[0] or pos ==d[1] or pos ==d[2] or pos ==d[3]:
            ct +=1
        print pos
        print pos2
        print pos3
        print pos4
        print pos5
        print

        if ct >= 1:
            bun2 +=gosa
            pos2 +=msp
            y3 = gaus(x,d[0]+pos2, bunbun+bun2) + gaus(x,d[1]+pos2, bunbun+bun2) + gaus(x, d[2]+pos2, bunbun+bun2) + gaus(x, d[3]+pos2, bunbun +bun2)
            y2 += y3
        if ct >= 2:
            bun3 +=gosa
            pos3 +=msp
            y4 = gaus(x,d[0]+pos3, bunbun+bun3) + gaus(x,d[1]+pos3, bunbun+bun3) + gaus(x, d[2]+pos3, bunbun+bun3) + gaus(x, d[3]+pos3, bunbun +bun3)
            y2 += y4
        if ct >= 3:
            bun4 +=gosa
            pos4 +=msp
            y5 = gaus(x,d[0]+pos4, bunbun+bun4) + gaus(x,d[1]+pos4, bunbun+bun4) + gaus(x, d[2]+pos4, bunbun+bun4) + gaus(x, d[3]+pos4, bunbun +bun4)
            y2 += y5
        if ct >= 4:
            bun5 +=gosa
            pos5 +=msp
            y6 = gaus(x,d[0]+pos5, bunbun+bun5) + gaus(x,d[1]+pos5, bunbun+bun5) + gaus(x, d[2]+pos5, bunbun+bun5) + gaus(x, d[3]+pos5, bunbun +bun5)
            y2 += y6


        im += plt.plot(x,y2, 'k')
        ims.append(im)

    plt.xlim(-1, 30)
    plt.ylim(0, 6)

    ani = animation.ArtistAnimation(fig, ims)




    plt.show()


if __name__ == '__main__':
    main()
