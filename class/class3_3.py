from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
import random
while True:
    time.sleep(0.00001)
    x,y,z = mc.player.getPos()
    x = x+random.uniform(1,10)
    y = y+random.uniform(1,10)
    z = z+random.uniform(1,10)
    mc.spawnEntity(x+1,y+20,z,93)
