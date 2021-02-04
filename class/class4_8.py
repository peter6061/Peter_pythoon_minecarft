from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
from time import sleep
import random
ID = mc.getPlayerEntityId('YuanShin_TW')
while True:
    sleep(1)
    x,y,z = mc.player.getTilePos()
    mineral = [14,15,16,56,73,129]
    style = random.choice(mineral)
    mc.setBlocks(x+1,y+3,z+1,x-1,y-3,z-1,style)