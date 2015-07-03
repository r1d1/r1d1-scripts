#!/usr/bin/python

# Client/server python
# and mostly from http://www.binarytides.com/code-chat-application-server-client-sockets-python/
# and http://www.binarytides.com/python-socket-programming-tutorial/

import socket               # Import socket module
import sys
from thread import *
import numpy as np
# ====================================================================================
#Function for handling connections. This will be used to create threads
def clientThread(conn):
	#Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n')
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		#Receiving from client
		data = conn.recv(1024)
		reply = 'OK...' + data
		if not data: 
			break
		conn.sendall(reply)
	#came out of loop
	conn.close()
