import json
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

    def deSerialization(self, data):
        return json.loads(data)

    def serialization(self, data):
        return json.dumps(data)
