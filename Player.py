class Player():
    def __init__(self,posx,posy):
        self.x=posx
        self.y=posy

    def isDead(self,x,y):
        print ("POS PLAYER : "+str(self.x)+" "+str(self.y))
        print("POS BOM : " + str(x)+" "+str(y))
        print("POS PASS : "+str(x)+" "+str(y))
        if self.x <= x + 2 and self.x >= x - 2 and self.y==y :
            print("aaa")
            return True
        elif self.y <= y + 2 and self.y >= y - 2 and self.x==x :
            return True
        else:
            return False

