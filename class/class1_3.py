from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
mc.setBlocks(x,y,z,x+20,y,z+20,1)
   