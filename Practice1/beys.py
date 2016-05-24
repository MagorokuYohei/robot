# -*- config: utf-8 -*-

def main():
    #Door is open/close
    D_open  = 0.5
    D_close = 0.5

    #Sensor
    Se_open_D_open = 0.8
    Se_close_D_open= 0.2
    Se_open_D_close = 0.21
    Se_close_D_close= 0.8

    #action Push or Stay
    P_D_open_Df_Open   = 1
    P_D_close_Df_open  = 0
    P_D_open_Df_close  = 0.8
    P_D_close_Df_close = 0.2

    S_D_open_Df_open   = 1
    S_D_close_Df_open  = 0
    S_D_open_Df_close  = 0
    S_D_close_Df_close = 1

    #robot find opened_door(x0=D_open or D_close) and stay
    #bel(1) = sigm{p(x1|u,x0)bel(x0)}
    #bel(1) = p(x1|S_D_open_Df_open)bel(D_open) + p(x1|S_D_close_Df_open)bel(x0)
    #bel = D_open
    bel_open = S_D_open_Df_open*D_open + S_D_open_Df_close*D_close
    print bel_open
    bel_close = S_D_close_Df_open*D_open + S_D_close_Df_close*D_close
    print bel_close

    # Add sensor error Sensor_Open
    bels_open  = Se_open_D_open*bel_open
    bels_close = Se_open_D_close*bel_close
    sig = 1/(bels_open+bels_close)
    bels_open = bels_open*sig
    bels_close= bels_close*sig
    print bels_open
    print bels_close

    # Next motion Push Sensor open
    bel_open  = P_D_open_Df_Open*bels_open + P_D_open_Df_close*bels_close
    bel_close = P_D_close_Df_open*bels_open + P_D_close_Df_close*bels_close
    bels_open = Se_open_D_open*bel_open
    bels_close= Se_open_D_close*bel_close
    sig = 1/(bels_open+bels_close)
    bels_open = bels_open*sig
    bels_close= bels_close*sig
    print bels_open
    print bels_close



if __name__ == '__main__':
    main()
