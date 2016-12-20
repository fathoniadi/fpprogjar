import BomberMan
import sys
import PackageClient

print ("BOMBERMAN GAME MULTIPLAYER")
print ("==========================")
print ("1 Create Game")
print ("2 Connect Game")
print ("3 Start Game")
print ("Menu > ")
packageclient=PackageClient.PackageClient()
bomberman=BomberMan.BomberMan()
connected=False

while(1):
    inp=input()
    if (int(inp)==1):
        print ("Silahkan masukkan id room (angka bebas)")
        print ("Room id : ")
        room=input()
        response=bomberman.initRoom(room)
        response = packageclient.deSerialization(response)
        #print response
        if (response['code'] == 0):
            print(response['message'])


    if (int(inp)==2):
        print ("Silahkan masukkan id room")
        print ("Room id : ")
        room=input()
        response=bomberman.connectRoom(room)
        response=packageclient.deSerialization(response)
        if (response['code']==0):
            print (response['message'])
            if (response['success']):
                connected=True

    if (int(inp)==3):
        print ("Starting game....")
        if (connected):
            bomberman.startGame()
            while 1:
                bomberman.update()