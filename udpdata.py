import socket, traceback
def get_udpdata():
     host = '' 
     port = 5555
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
     s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
     s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) 
     s.bind((host, port)) 
     try:
             message, address = s.recvfrom(8192)           
             return message
     except (KeyboardInterrupt, SystemExit): 
                   raise 
     except: 
                   traceback.print_exc()
