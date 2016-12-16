class Player():
    def __init__(self,posx,posy):
        self.x=posx
        self.y=posy
        self.file_player=""

    def initPlayer(self,data):
        self.x=data['x']
        self.y=data['y']
        self.file_player=data['playerName']

    def isDead(self,x,y):
        print ("POS PLAYER : "+str(self.x)+" "+str(self.y))
        print("POS BOM : " + str(x)+" "+str(y))
        print("POS PASS : "+str(x)+" "+str(y))
        if self.x <= x + 2 and self.x >= x - 2 and self.y==y :
            return True
        elif self.y <= y + 2 and self.y >= y - 2 and self.x==x :
            return True
        else:
            return False

