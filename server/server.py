import PodSixNet.Channel
import PodSixNet.Server
from time import sleep    
class ClientChannel(PodSixNet.Channel.Channel):
	def Network(self, data):
		print data
	def Network_myaction(self, data):
		print("myaction:", data)

class BoxesServer(PodSixNet.Server.Server):
	channelClass = ClientChannel
	def __init__(self, *args, **kwargs):
		PodSixNet.Server.Server.__init__(self, *args, **kwargs)
	def Connected(self, channel, addr):
		print 'new connection: channel = ', channel

	def Game(self):
		counter = 0
		while True:
			counter+=1
			print counter
			sleep(1)

host = "127.0.0.1"
port = 8000

print "Starting server on "+host+" "+str(port)

boxesServe = BoxesServer(localaddr=(host, port))
print("boxesServe=",str(boxesServe))
while True:
	boxesServe.Game()
	sleep(0.01)