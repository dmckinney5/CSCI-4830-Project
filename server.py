import socket
import sys
from _thread import *
 
HOST = '127.0.0.1'
PORT = 8888 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print(msg)
    sys.exit()
     
print('Socket Binded')
 
#Start listening on socket
s.listen(16)
print('Socket Listening')
 
#Function for handling connections. This will be used to create threads
#def client_handler(conn,addy):
 #   #receive the request
  #  data = conn.recv(1024)
    #log the request
   # with open('RequestLogNonCon.txt', 'a') as f:
    #        f.write(data.decode() +" at: ")
     #       f.write(' '.join(map(str,addy))+ "\n")
      # 
    #sendOff = "Request Recorded from "+ ''.join(map(str,addy)) + " connection closing"
    #conn.send(sendOff.encode())
    #conn.close()

 
#wait for clients fo foeva
while 1 < 2:

    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    data = conn.recv(1024)
    #log the request
    with open('RequestLogNonCon.txt', 'a') as f:
            f.write(data.decode() +" at: ")
            f.write(' '.join(map(str,addr))+ "\n")
       
    sendOff = "Request Recorded from "+ ''.join(map(str,addr)) + " connection closing"
    conn.send(sendOff.encode())
    conn.close()
    
 
s.close()