import socket
import sys
import time
from threading import Thread
#Define our number of threads    
NUMTHREADS = 16
start = time.time()
def client():
   
    #set up our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    #connect to the port the server is listening on
    server_address = ('localhost', 8080)
    print ('connecting to %s port %s' % server_address)
   
    s.connect(server_address)
    try:
    # Send our request
        message = "GET test.html"
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
    print("--- %s seconds ---" % (time.time() - start))
