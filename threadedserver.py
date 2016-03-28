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
def client_handler(conn):
    #Sending message to connected client
    #message = "Welcome to the Server, please type your message\n"
    #conn.sendto(message.encode(),(HOST, PORT)) 
    test = open("test.txt",'w',1024)
    
    
    #Receiving from client
    data = conn.recv(1024)
    print(data.decode())

 
#Listen infinitiely long for new clients, delegate new thread to handle client request. 
while 1 < 2:

    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    threads = []
    for i in range(5):
        t = threading.Thread(target=client_handler,args=(conn,))
        threads.append(t)
        t.start()

    for i in range(5):
    	threads[i].join()
 
s.close()