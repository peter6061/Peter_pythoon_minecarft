from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import random
x,y,z = mc.player.getTilePos()
blen = 4
for i in range(4):
    for j in range(4):
        num = random.randint(1,6)
        if num == 1:
            mc.setBlocks(x,y,z,x+blen,y,z,1)
            x = x+blen
        elif num == 2:
            mc.setBlocks(x,y,z,x-blen,y,z,1)
            x = x-blen
        elif num == 3:
            mc.setBlocks(x,y,z+blen,x,y,z,1)
            z = z+blen
        elif num == 4:
            mc.setBlocks(x,y,z-blen,x,y,z,1)
            z = z-blen
        elif num == 5:
            mc.setBlocks(x,y+blen,z,x,y,z,1)
            y = y+blen
        else:
            mc.setBlocks(x,y-blen,z,x,y,z,1)
            y = y-blen