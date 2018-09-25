import pyaudio
import numpy as np
import socket
import sys



CHUNK = 4096          # number of data points to read at a time
RATE = 44100          # time resolution of the recording device (Hz)
SECONDS = 30
THRESHOLD = 600


HOST="127.0.0.1" # Server IP 
PORT=10008       # Server Port




# Initialize pyaudio class
p=pyaudio.PyAudio() 


# Create a stream with microphone
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK) #uses default input device





try:

    # Create a socket object 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


    try:
        # Connect to server
        s.connect((HOST,PORT))
        print('Connected to Server......')
    except socket.error() as msg:
        print(msg)
        sys.exit()
    
    # Record audio from microphone for 5 seconds     
    for i in range(SECONDS):
    	
    	speak = False
        for j in range( RATE / CHUNK ):
            # Convert signal into numpy array
            data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
            # Finding peak in each sample and double it
            peak=np.average(np.abs(data))*2
            # Compute number of bars to display it
            #bars="#"*int(50*peak/2**16)
            if peak > THRESHOLD :
                s.sendall(str(1))
            else:
                s.sendall(str(0))
                
         
    
    
    	speak = False
    	
    	
    	
    	
    	
    # Stop the stream gracefully
    stream.stop_stream()

finally:
    # Close the stream
    stream.close()

    # Terminate pyaudio class 
    p.terminate()    
    
    s.close()
