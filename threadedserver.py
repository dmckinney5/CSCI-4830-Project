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
	#throws error if binding fails
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket Binded')
 
#Listen on the socket
s.listen(20)
print('Socket Listening')
 

#Handle incoming client requests
def client_handler(conn,addy):
    #Sending message to connected client
    #message = "Welcome to the Server, please type your message\n"
    #conn.sendto(message.encode(),(HOST, PORT)) 
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

    



 
#Listen infinitiely long for new clients, delegate new thread to handle client request. 
while 1 < 2:

    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    threads = []
    
    t = threading.Thread(target=client_handler,args=(conn,addr))
    threads.append(t)
    t.start()
 
s.close()