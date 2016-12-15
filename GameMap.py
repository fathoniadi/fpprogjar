class GameMap():
    def __init__(self):
        self.peta=[]

    def createMap(self,filePath):
        f=open(filePath,"r")
        line=f.read()
        line=line.split("\n")
        for i in range(len(line)):
            line[i]=line[i].split(" ")

        print(line)
        return line
