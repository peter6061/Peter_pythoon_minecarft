from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
import time
while True:
    x,y,z = mc.player.getTilePos()
    a = mc.getBlock(x+3,y-1,z)
    b = mc.getBlock(x-3,y-1,z)
    c = mc.getBlock(x,y-1,z-3)
    d = mc.getBlock(x,y-1,z+3)
    time.sleep(0.001)
    if a == 8 or b == 8 or c == 8 or d == 8 or \
        a == 9 or b == 9 or c == 9 or d == 9:
        mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,79)