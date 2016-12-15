# 100 Game Dimulai
# 200 Broadcast posisi player
# 201 Broadcast posisi bomb baru
# 300 Player Mati


#player Status
# 0 Mati
# 1 Bernyawa

class PackageServer():
	"""docstring for Package"""
	def __init__(self):
		super(Package, self).__init__()
		self.player1Status = ""
		self.player2Status = ""
		self.player3Status = ""
		self.player4Status = ""
		self.player1X = ""
		self.player2X = ""
		self.player3X = ""
		self.player4X = ""

		self.player1Y = ""
		self.player2Y = ""
		self.player3Y = ""
		self.player4Y = ""

		self.player1Name = ""
		self.player2Name = ""
		self.player3Name = ""
		self.player4Name = ""

		self.x = ""
		self.y = ""

		self.playerName = ""
		self.code = ""

	def createPackageBomb(self, coorX, coorY):
		self.code = 201
		self.bombX = coorX
		self.bombY = coorY

	def getCodePackage(self):
		return self.code

	def getPackageBomb(self):
		return x,y

	def createPackagePlayerDead(self, playerName):
		self.code = 300
		self.name = playerName

	def getPackagePlayerDead(self):
		return self.name
	
	def createPackagePlayerLoc(self, _player1Status, _player1Name, _player1X, _player1Y,_player2Status, _player2Name, _player2X, _player2Y,_player3Status, _player3Name, _player3X, _player3Y,_player4Status, _player4Name, _player4X, _player4Y):
		self.code = 200
		self.player1Status = _player1Status
		self.player1Name = _player1Name
		self.player1X = _player1X
		self.player1Y = _player1Y

		self.player2Status = _player2Status
		self.player2Name = _player2Name
		self.player2X = _player2X
		self.player2Y = _player2Y

		self.player3Status = _player3Status
		self.player3Name = _player3Name
		self.player3X = _player3X
		self.player3Y = _player3Y

		self.player4Status = _player4Status
		self.player4Name = _player4Name
		self.player4X = _player4X
		self.player4Y = _player4Y

	def getPackagePlayerLoc(self):
		return self.player1Status, self.player1Name, self.player1X, self.player1Y,self.player2Status, self.player2Name, self.player2X, self.player2Y,self.player3Status, self.player3Name, self.player3X, self.player3Y,self.player4Status, self.player4Name, self.player4X, self.player4Y

	def createPackageInitGame(self, _playerName, _x, _y):
		self.code = 100
		self.playerName = _playerName
		self.x = _x
		self.y = _y

	def getPackageInitGame():
		return self.playerName, self.x, self.y