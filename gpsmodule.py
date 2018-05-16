from time import sleep

while(1):
    data = raw_input()
    if data.find('GPGGA') != -1:
        ggadata = data.split(',')
        utcrawtimeg = ggadata[1]
        latg = float(ggadata[2][:2])+(float(ggadata[2][2:])/60)
        longg = float(ggadata[4][:3])+(float(ggadata[4][3:])/60)
        if data[3]=='S':
            latg = -1*latg
        if data[5]=='W':
            longg = -1*longg
        print 'Time in UTC',utcrawtimeg[:2]+':'+utcrawtimeg[2:4]+':'+utcrawtimeg[4:]
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
    #    print latr,longr
    elif data.find('GPVTG') != -1:
        vtgdata = data.split(',')
        speedv= vtgdata[7]
        print 'speed : ',speedv,"km/h\n"
