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
def clientThread(conn, prod, price):
	#Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n')
	myMoney = 100
	myProducts = np.zeros(len(prod)).tolist()
	#infinite loop so that function do not terminate and thread do not end.
	while True:
		#Receiving from client
		data = conn.recv(1024)
		if not data: 
			break
		
		command=data.split()
		reply = "OK... "

		if command[0] == "/quit":
			break
		elif command[0] == "/money":
			print "money:", myMoney
		elif command[0] == "/buy":
			print "buy", command[1], command[2]
			if (command[1] in prod):
				try:
					productNumber=int(command[2])
				except IndexError, ValueError:
					print "Quantity is Not a number, try again !"
				productIndex=prod.index(command[1])
				totalPrice = productNumber * price[productIndex]
				print productIndex, totalPrice
				if totalPrice <= myMoney:
					myMoney = myMoney - totalPrice 
					myProducts[productIndex] = myProducts[productIndex] + productNumber
					reply = "Transaction done !"
				else:
					reply= "Not enough money !"
			else:
				reply = "Unknown product !"
				print reply 
		elif command[0] == "/sell":
			print "sell", data[6:]
		elif command[0] == "/product":
			# /product <name> <>
			print "product", data[9:]
		elif command[0] == "/status":
			products=[str(yourp[0])+" "+str(yourp[1]) for yourp in zip(*[prod, myProducts])]
			status=str("Your account currently has " + str(myMoney) + " unit, you owe " + str(products))
			reply = reply + status
			print status
		else:
			pass
		reply = reply + "\n"
		conn.sendall(reply)
	#came out of loop
	conn.close()
