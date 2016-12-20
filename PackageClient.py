import json
import State

class PackageClient():
    def __init__(self):
        # super(Package, self).__init__()
        pass

    #fungsi untuk create game
    def createGame(self,_room):
        self.data={'code':1,'room':_room}
        return self.data

    #fungsi untuk menghubungkan ke room client-server
    def connectToRoom(self,_room):
        self.data = {'code': 2, 'room': _room}
        return self.data

    #fungsi inisialisasi game
    def startGame(self,_room):
        self.data = {'code':100,'room':_room}
        return self.data

    #menyimpan lokasi
    def location(self,_x,_y,_player,_room):
        self.data = {'code':200,'playerName':_player,'x':_x,'y':_y,'room':_room}
        return self.data

    #apabila player terkena bomb
    def createPackagePlayerDead(self, _playerName,_room):
        self.data = {'code': 300, 'playerName': _playerName, 'room' :_room}
        return self.data

    #membuat bomob pada lokasi (x,y)
    def createPackageBomb(self,_x,_y,_room):
        self.data = {'code':201, 'room':_room,'x':_x,'y':_y}
        return self.data
    
    #
    def deSerialization(self, data):
        return json.loads(data)

    def serialization(self, data):
        return json.dumps(data)

    #fungsi untuk mengirim lokasi bomb dari player satu ke player lainnya
    def SendNewLocBomb(self, _playerName, room):
        self.data = {'code': 201, 'playerName': _playerName, 'room': _room}
        return self.data
