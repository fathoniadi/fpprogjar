import sys
from time import sleep
from sys import stdin, exit

from PodSixNet.Connection import connection, ConnectionListener

# This example uses Python threads to manage async input from sys.stdin.
# This is so that I can receive input from the console whilst running the server.
# Don't ever do this - it's slow and ugly. (I'm doing it for simplicity's sake)
from thread import *

class Client(ConnectionListener):
	def __init__(self, host, port):
		self.Connect((host, port))
		print "Chat client started"
		print "Ctrl-C to exit"
		# get a nickname from the user before starting
		# print "Enter your nickname: ",
		# connection.Send({"action": "nickname", "nickname": stdin.readline().rstrip("\n")})
		# launch our threaded input loop
		t = start_new_thread(self.InputLoop, ())
	
		
	
	def inputLoop(self):
		# horrid threaded input loop
		# continually reads from stdin and sends whatever is typed to the server
		connection.Pump()
		self.Pump()
		counter = 0
		while 1:
			counter +=1
			print counter
			connection.Send({"action": "message", "message": counter})
	
	#######################################
	### Network event/message callbacks ###
	#######################################
	
	# def Network_players(self, data):
	# 	print "*** players: " + ", ".join([p for p in data['players']])
	
	def Network_message(self, data):
		print data['message']
	
	# built in stuff

	def Network_connected(self, data):
		print "You are now connected to the server"
	
	def Network_error(self, data):
		print 'error:', data['error'][1]
		connection.Close()
	
	def Network_disconnected(self, data):
		print 'Server disconnected'
		exit()

host = "127.0.0.1"
port = "8000"
c = Client(host, int(port))
while 1:
	c.inputLoop()
	sleep(0.001)
