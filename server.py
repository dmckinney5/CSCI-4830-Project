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
     
print('Socket bind complete')
 
#Start listening on socket
s.listen(16)
print('Socket now listening')
 
#Function for handling connections. This will be used to create threads
def client_handler(conn):
    #Sending message to connected client
    #message = "Welcome to the Server, please type your message\n"
    #conn.sendto(message.encode(),(HOST, PORT)) 
         
    #Receiving from client
    data = conn.recv(1024)
    #data.decode()
    #  TODO Print data, port of connected client etc to file
 
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
     
    client_handler(conn)
    
 
s.close()