from udpdata import get_udpdata
from time import sleep
bx =0
by =0
def get_time(data):
    temp= data.find(",")
    time= float(data[0:temp])
    return time

def get_gpsx(data):
    k = data.find(", 1,")
    temp= (data[k+4:])
    l = temp.find(",")
    gpsx = data[data.find(", 1,")+4:][:data[data.find(", 1,")+4:].find(",")]
    return float(gpsx)

def get_gpsy(data):
    l1= data.find(", 1,")
    d1= data[l1+4:]
    l2= d1.find(",")
    d2=d1[l2+1:]
    l3=d2.find(",")
    gpsy = data[data.find(", 1,")+4:][data[data.find(", 1,")+4:].find(",")+1:][:data[data.find(", 1,")+4:][data[data.find(", 1,")+4:].find(",")+1:].find(",")]
    return float(gpsy)
    

