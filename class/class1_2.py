from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
x,y,z = mc.player.getTilePos()
while True:
    time.sleep(0.5)
    mc.setBlock(x,y,z,46)
    mc.setBlock(x,y-1,z,152)