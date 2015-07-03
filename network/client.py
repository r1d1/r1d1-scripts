#!/usr/bin/python 

# This is client.py file
# from  http://www.tutorialspoint.com/python/python_networking.htm
# and mostly from http://www.binarytides.com/code-chat-application-server-client-sockets-python/
# and http://www.binarytides.com/python-socket-programming-tutorial/

import socket               # Import socket module
import fileinput
import sys

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12346                # Reserve a port for your service.

s.connect((host, port))
command=''
output=''
inputSign='> '

while command != '/quit':
	print "Server response :", s.recv(1024)
	#command = raw_input(inputSign)
	#print command
	#if command == '/help':
	#	print 'cas 1'
#		print "/help : affiche ce texte"
#		print "/say : dire"
#		print "/quit : quitter"
#	elif command[0:4] == '/say':
#	#	print 'cas 2'
#		print host+' dit : '+command[4:]
#	print output
	#s.send(inputSign+command)

s.close()
