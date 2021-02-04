from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
mc.player.setTilePos(0,100,0)
print(mc.player.getTilePos())