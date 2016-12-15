#code
# 100 - 500 client -> server
#100 start
#200 Broadcast location player
#201 Broadcast new location bomb
#300 Broadcast player dead
#400 End game

# 800 - 900
# 
# 800 player send location it's self
# 801 player send location new bomb
# 900 player send status dead

import json


class PackageServer():
	"""docstring for Package"""
	def __init__(self):
		# super(Package, self).__init__()
		pass
	def createPackageInitGame(self, _playerName, _x, _y):
		self.data = {'code':100, 'playerName':_playerName, 'x':_x, 'y':_y}
		return self.data

	def createPackagePlayerLoc(self, _player1Name, _player1Status, _player1X, _player1Y, _player2Name, _player2Status, _player2X, _player2Y):
		self.data = {'code':200, 'player1Name': _player1Name, 'player1Status': _player1Status, 'player1X': _player1X, 'player1Y': _player1Y, 'player2Name': _player2Name, 'player2Status': _player2Status, 'player2X': _player2X, 'player2Y': _player2Y}
		return self.data

	def createPackageNewBomb(self, _x, _y):
		self.data = {'code':201, 'x':_x, 'y':_y}
		return self.data

	def createPackagePlayerDead(self, _playerName):
		self.data = {'code':300, 'playerName':_playerName}
		return self.data
	
	def createPackageEndGame(self, _playerName):
		self.data = {'code':400, 'playerName':_playerName}
		return self.data

	def deSerialization(self, data):
		return json.loads(data)

	def serialization(self, data):
		return json.dumps(data)


# package = PackageServer()
# pack = package.createPackageEndGame("Thoni")
# serializationP = package.serialization(pack)
# print serializationP
# print package.deSerialization(serializationP)