import json
import State

class PackageServer():
    def __init__(self):
        # super(Package, self).__init__()
        pass

    def createPackageResponse(self,msg,status):
        self.data = {'code':0, 'message':msg,'success':status}
        return self.data

    def createPackageInitGame(self, __room, _playerName, _x, _y):
        self.data = {'code': 100, 'playerName': _playerName,'room':__room, 'x': _x, 'y': _y}
        return self.data

    def createPackageStartGame(self, _room):
        self.data = {'code': 110, 'room': _room, 'state':State.State.RUNNING}
        return self.data

    def createPackagePlayerLoc(self, _player1Name, _player1Status, _player1X, _player1Y, _player2Name, _player2Status,
                               _player2X, _player2Y):
        self.data = {'code': 200, 'player1Name': _player1Name, 'player1Status': _player1Status, 'player1X': _player1X,
                     'player1Y': _player1Y, 'player2Name': _player2Name, 'player2Status': _player2Status,
                     'player2X': _player2X, 'player2Y': _player2Y}
        return self.data

    def createPackageNewBomb(self, _x, _y, _playerName, _room):
        self.data = {'code': 201, 'x': _x, 'y': _y}
        return self.data

    def createPackagePlayerDead(self, _playerName):
        self.data = {'code': 300, 'playerName': _playerName}
        return self.data

    def createPackageEndGame(self, _playerName):
        self.data = {'code': 400, 'playerName': _playerName}
        return self.data

    def deSerialization(self, data):
        return json.loads(data)

    def serialization(self, data):
        return json.dumps(data)
