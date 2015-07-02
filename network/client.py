#!/usr/bin/python 

# This is client.py file
# from  http://www.tutorialspoint.com/python/python_networking.htm

import socket               # Import socket module
import fileinput
import sys

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
command=''
output=''
inputSign='> '


while command != '/quit':
	#print s.recv(1024)
	command = raw_input(inputSign)
	#print command
	if command == '/help':
	#	print 'cas 1'
		output = "/help : affiche ce texte\n/say : dire\n/quit : quitter"
	elif command[0:4] == '/say':
	#	print 'cas 2'
		output=host+' dit : '+command[4:]
	else:
	#	print 'cas 3'
		output=command
	print output
	#s.send(inputSign+command)

s.close                     # Close the socket when done
