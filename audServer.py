# Python Server
import socket
import sys
import time
import numpy as np
import matplotlib.pyplot as plt


CHUNK=4096

# IP address for the Server
HOST="127.0.0.1"

# Port number for Server
PORT=10008

stime=0


def processRealTimeData(conn):
    total=0
    while True:
        chunk = conn.recv(CHUNK)
        if not chunk :
            break
        else:
            print(int(time.time()),':','#'*5*int(chunk))
            
        
			
			







try:
    # Create socket object
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    try:
        # Try to bind server with host(ip or hostname), port
        s.bind((HOST,PORT))
    
        # Display message 
        print('     Server Started      ')


    # Error occurred while binding    
    except socket.error() as msg:
        print('Error:',msg)
        sys.exit()
    
    
    # Server start listening for connection    
    s.listen(1)
    print('    Listening on Port: %s' % PORT)


    # Incoming connection
    conn,addr=s.accept()
    print('Connected by ',addr)
    stime = time.time()

    processRealTimeData(conn)
    print(' Data processing complete ')
finally:
    conn.close()
    s.close()