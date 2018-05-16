from udpdata import get_udpdata
from gps_value import *
from time import sleep
import os
def clc():
    os.system('cls')

gx = 23.106950
gy = 72.594929
one_m = 0.00000898
area_cover = 350 * one_m
gx_max = gx + area_cover 
gx_min = gx - area_cover
gy_max = gy + area_cover
gy_min = gy - area_cover

#gx_max,gx_min,gy_max,gy_min
while(1):
    try:
        while(1):
            d=get_udpdata()
            if len(d)>150: break
        livex = get_gpsx(d)
        livey = get_gpsy(d)
        clc()
##        print livex , livey 
        if gx_max>livex>gx_min and gy_max>livey>gy_min:
            ####put gpio code below
            print "Arre bhai! bhai! bhai bhai!"
        else:
            print "no problem"


        
    except:
        print 'error'
        continue
