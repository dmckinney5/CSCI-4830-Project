import socket
import sys

 
HOST = '127.0.0.1'
PORT = 8080 
 
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
s.listen(512)
print('Socket Listening')
 
#wait for clients fo foeva
while 1 < 2:
    #accept connection
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    #handle request
    data = conn.recv(1024)
    test = data.decode().split()
    #log the request
    with open('RequestLogNonCon.txt', 'a') as f:
            f.write(test[0] +' '+ test[1] +" at: "+' '.join(map(str,addr))+ "\n")
            #f.write(' '.join(map(str,addr))+ "\n")
    #send confirmation, close connection   
    sendOff = "Request Recorded from "+ ''.join(map(str,addr)) + " connection closing"
    #conn.send(sendOff.encode())
    conn.send('HTTP/1.0 200 OK\n'.encode())
    conn.send('Content-Type: text/html\n'.encode())
    conn.send(sendOff.encode()) # header and body should be separated by additional newline
    conn.close()
    
 
s.close()
