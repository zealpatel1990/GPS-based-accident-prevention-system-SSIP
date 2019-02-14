import serial
import pygame
from time import sleep

#pygame.mixer.init()
thresold = 0.0005 #in degree i.e.  approx 55meter
testco = [[23.107804, 72.594511],[23.106114, 72.595450]] #1 location is M block and second is A block
testspeed = [35,25]

#from stepper import stepper
#stper= stepper([22, 17, 23]) #[stepPin, directionPin, enablePin]STEPPER

#ser = serial.Serial ("/dev/ttyAMA0", 9600)
while True:
    try:
        data = raw_input()
#        data = ser.readline()              #read serial port
        if data.find('GPGGA') != -1:
            ggadata = data.split(',')
            utcrawtimeg = ggadata[1]
            latg = float(ggadata[2][:2])+(float(ggadata[2][2:])/60)
            longg = float(ggadata[4][:3])+(float(ggadata[4][3:])/60)
            if data[3]=='S':
                latg = -1*latg
            if data[5]=='W':
                longg = -1*longg
            print '\nTime in UTC',utcrawtimeg[:2]+':'+utcrawtimeg[2:4]+':'+utcrawtimeg[4:]
            print 'latitude:',latg,'longitude:' ,longg
        elif data.find('GPRMC') != -1:
            rmcdata = data.split(',')
            utcrawtimer = rmcdata[1]
            latr = float(rmcdata[3][:2])+(float(rmcdata[3][2:])/60)
            longr = float(rmcdata[5][:3])+(float(rmcdata[5][3:])/60)
            if data[4]=='S':
                latr = -1*latr
            if data[6]=='W':
                longr = -1*longr
#            print latr,longr
        elif data.find('GPVTG') != -1:
            vtgdata = data.split(',')
            speedv= float(vtgdata[7])
            print 'speed : ',speedv,"km/h"
            if (testco[0][0]-thresold)<latg<(testco[0][0]+thresold) and (testco[0][1]-thresold)<longg<(testco[0][1]+thresold):
                #you are location 1 enter your control code
                #print speedv,testspeed
                if speedv>testspeed[0]:
                    print "^^^^^^^OVER SPEEDING AT LOCATION 1^^^^^^^^\n"
                    #stper.step(3200, "right"); #steps, dir, speed, stayOn
                            
            if (testco[1][0]-thresold)<latg<(testco[1][0]+thresold) and (testco[1][1]-thresold)<longg<(testco[1][1]+thresold):
                #you are location 2 enter your code here
                print testspeed,speedv
                if speedv>testspeed[1]:
                    print "OVER SPEEDING AT LOCATION 2\n\n"
        sleep(0.02)
    except KeyboardInterrupt:
        print ("\n\n*******************\nQuiting Program")
        sleep(1)
        break;
    except:
        print ("Not Enough GPS Data")
        continue
