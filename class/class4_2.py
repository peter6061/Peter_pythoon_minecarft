from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
number = 1
for i in range(8):
    x,y,z = mc.player.getTilePos()
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
    number = number*2
    mc.postToChat(number)
    time.sleep(3)
    
    
    