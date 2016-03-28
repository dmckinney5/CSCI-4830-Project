import socket
import sys
from threading import Thread
#Define our number of threads    
NUMTHREADS = 32
def client():
    #set up our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect to the port the server is listening on
    server_address = ('localhost', 8888)
    print ('connecting to %s port %s' % server_address)
    s.connect(server_address)

    try:
   
    # Send data
        message = 'Test Message'
        print('sending message')
        
        s.sendto(message.encode(),server_address)

    finally:
        print('closing socket')
        s.close()

if __name__ == "__main__":
    
    for i in range(NUMTHREADS):
        thread = Thread(target = client)
        thread.start()
    for i in range(NUMTHREADS):
        thread.join()
        print('thread finished...exiting')