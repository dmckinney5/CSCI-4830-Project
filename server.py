#! /usr/bin/env jython
from __future__ import with_statement
import socket
import sys
 
HOST = '127.0.0.1'
PORT = 8888
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created')
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error:
    exit()

print('Socket Binded')
 
#Start listening on socket
s.listen(20)
print('Socket Listening')
 
#wait for clients fo foeva

while 1 < 2:
    #accept connection
    conn, addr = s.accept()
    #print('Connected with ' + addr[0] + ':' + str(addr[1]))

    #handle request
    conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())
    data = conn.recv(4096)
    #log the request
    with open('RequestLogNonCon.txt', 'a') as f:
            f.write(data.decode() + " at: "+' '.join(map(str,addr))+ "\n")
    file = open("test.html","rb")
    while True:
        toSend = file.read(65536)
        if not toSend:
            break  # EOF
        conn.sendall(toSend)
    conn.close()
    
 
s.close()
