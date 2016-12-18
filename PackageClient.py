import pickle
import State

class PackageClient():
    def __init__(self):
        # super(Package, self).__init__()
        pass

    def createGame(self,_room):
        self.data={'code':1,'room':_room}
        return self.data

    def connectToRoom(self,_room):
        self.data = {'code': 2, 'room': _room}
        return self.data

    def startGame(self,_room):
        self.data = {'code':100,'room':_room}
        return self.data

    def location(self,_x,_y,_player,_room):
        self.data = {'code':200,'playerName':_player,'x':_x,'y':_y,'room':_room}
        return self.data

    def createPackagePlayerDead(self, _playerName):
        self.data = {'code': 300, 'playerName': _playerName}
        return self.data

    def deSerialization(self, data):
        return pickle.loads(data)

    def serialization(self, data):
        return pickle.dumps(data)
