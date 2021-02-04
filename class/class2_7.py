from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getPos()
mc.setSign(x,y,z,63,8,"start fight",'or',\
           'finish fight')  