#! /usr/bin/env jython
from __future__ import with_statement
import socket
import sys
import threading 
#implementation tutorial found on http://www.binarytides.com/
#Designate localhost, and which port to listen on 
HOST = '127.0.0.1'
PORT = 8080 
# we will use the lock to protect our file access
lock = threading.Lock()

class Server(object):

	def __init__(self,hostname,port):
		self.hostname = hostname
		self.port = port
	def start(self):
		self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print('Socket Created')
		s = self.socket.bind((self.hostname,self.port))
		print('Socket Binded')
		self.socket.listen(20)
		print('Socket Listening')

		while 1 < 2:
			conn, addy = self.socket.accept()
			print('Connected with ' + addy[0] + ':' + str(addy[1]))
			t = threading.Thread(target=client_handler, args=(conn,addy))
			t.start()
			#conn.close()


	#s.close()






#Handle incoming client requests
def client_handler(conn,addy): 
    #Receiving from client
    data = conn.recv(4096)
    #attempt to snag lock
    lock.acquire()
    try:
        #if lock grabbed
        with open('RequestLog.txt', 'a') as f:
            #write our message, and the address it was received from
            f.write(data.decode() +" at: ")
            f.write(''.join(map(str,addy))+ "\n")
    
    finally:
        #release lock
        conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())
        file = open("test.html","rb")
        while True:
            toSend = file.read(65536)
            if not toSend:
                break  # EOF
            conn.sendall(toSend)
        
        lock.release()
        conn.close()
   
    

if __name__ == "__main__":
    server = Server(HOST, PORT)
    try:
        server.start()
    finally:
    	exit()
