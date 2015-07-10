#!/usr/bin/python

# This is server.py file
# from  http://www.tutorialspoint.com/python/python_networking.htm
# and mostly from http://www.binarytides.com/code-chat-application-server-client-sockets-python/
# and http://www.binarytides.com/python-socket-programming-tutorial/

import socket               # Import socket module
import sys
from thread import *
import numpy as np
from serverFunctions import *
# ====================================================================================
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

# Trying to bind the socket :
try:
	s.bind((host, port))        # Bind to the port
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
# ====================================================================================

# Now wait for client connection. We should investigate the argument value
s.listen(10)

print "Socket listening ... ", host

nbOfConnections=0;

productList=["banana", "apple", "grape", "apricot", "mutton"]
basePrice = 3.5
priceList= np.trunc(100*(basePrice+np.random.randn(len(productList))))/100.0
#priceList= 2.0+np.around(np.random.randn(len(productList)), decimals=2)
priceList = priceList.tolist()

print productList, priceList

while True:
	c, addr = s.accept()     # Establish connection with client.
	nbOfConnections += 1;
	print 'Got connection from', addr, ' (', nbOfConnections,' people connected)'
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
	start_new_thread(clientThread ,(c, productList, priceList))
	#c.send('Thank you for connecting '+str(np.random.rand()))
	#c.close()                # Close the connection

print "Server closing ..."
s.close()

