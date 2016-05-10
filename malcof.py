# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

def main():
    weather = np.array([[0.8, 0.2, 0],[0.4, 0.4, 0.2], [0.2, 0.6 ,0.2]])
    pre_w = random.randint(0,2)
    num = 0

    f = open('./malcof.txt', 'w')
    while num < 10000:
        num += 1
        rdm = random.randint(1,10)
        if pre_w == 0:
            if 1 <= rdm and rdm <= 8:
                w = 0
            elif 9 <= rdm:
                w = 1
        elif pre_w == 1:
                if 1 <= rdm and rdm <= 4:
                    w = 0
                elif 5 <= rdm and rdm <= 8:
                    w = 1
                elif 9 <= rdm:
                    w = 2
        elif pre_w == 2:
            if 1 <= rdm and rdm <= 2:
                w = 0
            elif 3 <= rdm and rdm <= 8:
                w = 1
            elif 9 <= rdm:
                w = 2

        if w == 0:
#            print "Sun"
            str = "Sun\n"
        elif w == 1:
#            print "Crowd"
            str = "Cloudy\n"
        elif w == 2:
#            print "Rain"
            str = "Rain\n"
        pre_w = w

        f.writelines(str) # シーケンスが引数。

    f.close()

    s_num = 0
    c_num = 0
    r_num = 0
    num   = 0

    for line in open("malcof.txt", "r"):
        num += 1
#        sys.stdout.write(line)
        if line == 'Sun\n':
            s_num += 1
        elif line == 'Cloudy\n':
            c_num += 1
        elif line == 'Rain\n':
            r_num += 1

    print '%d\n%d\n%d\n%d' % (num, s_num, c_num, r_num)


if __name__ == '__main__':
    main()
