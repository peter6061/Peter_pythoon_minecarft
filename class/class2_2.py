from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
import random
x,y,z = mc.player.getTilePos()
while True:
    time.sleep(1)
    color = random.randint(0,15)
    mc.setBlocks(x,y,z,x+10,y,z+10,95,color)
