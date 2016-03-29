import socket
import sys
import threading
#implementation tutorial found on http://www.binarytides.com/
#Designate localhost, and which port to listen on 
HOST = '127.0.0.1'
PORT = 8888 
# we will use the lock to protect our file access
lock = threading.Lock()
#create socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')
 
try:
    #bind socket to host and port
    s.bind((HOST, PORT))

except socket.error as msg:
    #commonly get port already in use error message
    print(msg)
    sys.exit()
     
print('Socket Binded')
 
#Listen on the socket
s.listen(20)
print('Socket Listening')
 

#Handle incoming client requests
def client_handler(conn,addy): 
    #Receiving from client
    data = conn.recv(1024)
    #attempt to snag lock
    lock.acquire()
    try:
        #if lock grabbed
        with open('RequestLog.txt', 'a') as f:
            #write our message, and the address it was received from
            f.write(data.decode() +" at: ")
            f.write(' '.join(map(str,addy))+ "\n")
    
    finally:
        #release lock
        lock.release()
        #generate and send closing message. close connection
        closing = "Request Recorded from "+ threading.currentThread().getName()+ " at "  + ''.join(map(str,addy)) + " connection closing"
        conn.send(closing.encode())    
        conn.close()
 
#Listen infinitiely long for new clients, delegate new thread to handle client request. 
while 1 < 2:
	#accept new connection 
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread,pass function for thread to run, and the tuple of thread arguments
    t = threading.Thread(target=client_handler,args=(conn,addr))
    t.start()
 
s.close()