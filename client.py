import socket
import sys
from threading import Thread
#Define our number of threads    
NUMTHREADS = 16
def client():
   
    #set up our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #connect to the port the server is listening on
    server_address = ('localhost', 8888)
    print ('connecting to %s port %s' % server_address)
   
    s.connect(server_address)
    try:
    # Send our request
        message = "Html Request To Be Added"        
        s.sendto(message.encode(),server_address)
    finally:
    	#receive confirmation
    	response = s.recv(1024)
    	print(response.decode())

    

if __name__ == "__main__":
    #generate our client requests (done to show sequential vs concurrent exectution)
    for i in range(NUMTHREADS):
        thread = Thread(target = client)
        thread.start()
    for i in range(NUMTHREADS):
        thread.join()
