import socket
import sys
import threading
#implementation tutorial found on http://www.binarytides.com/
#Designate localhost, and which port to listen on 
HOST = '127.0.0.1'
PORT = 8888 

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
    lock = threading.Lock()
    #t = threading.currentThread()
    #print(t)
    lock.acquire()
    try:
        with open('RequestLog.txt', 'a') as f:
            f.write(data.decode() +" at: ")
            f.write(' '.join(map(str,addy))+ "\n")
    
    finally:
        lock.release()
        sendOff = "Request Recorded from "+ threading.currentThread().getName()+ " at "  + ''.join(map(str,addy)) + " connection closing"
        conn.send(sendOff.encode())    
        conn.close()
 
#Listen infinitiely long for new clients, delegate new thread to handle client request. 
while 1 < 2:

    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    threads = []
    
    t = threading.Thread(target=client_handler,args=(conn,addr))
    t.start()
 
s.close()