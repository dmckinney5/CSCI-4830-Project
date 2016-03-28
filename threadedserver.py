import socket
import sys
from _thread import *
 
HOST = '127.0.0.1'
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
     
print('Socket Binded')
 
#Start listening on socket
s.listen(10)
print('Socket Listening')
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    message = "Welcome to the Server, please type your message\n"
    conn.sendto(message.encode(),(HOST, PORT)) #send only takes string
         
    #infinite loop so that function do not terminate and thread do not end.
    #while True:
         
    #Receiving from client
    data = conn.recv(1024)
    #data.decode()
    # Print data, port of connected client etc to file
    reply = "Message Received, closing connection\n"
    if not data: 
        reply = "Send Failure"
        #break
        
    #conn.sendall(reply.encode())    	
    #conn.close()
 
#now keep talking with the client
while 1 < 2:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()