from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y+2,z,8)
    time.sleep(0.01)
    