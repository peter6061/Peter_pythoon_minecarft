from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
def planttree(x,y,z,mc):
        mc.setBlocks(x+1,y+5,z+1,x-1,y+3,z-1,18)
        mc.setBlocks(x,y+4,z,x,y,z,17)
x,y,z = mc.player.getPos()
for i in range(0,10):
    for j in range(10):
        for h in range(5):
            planttree(x-i*5,y+h*5,z+j*5,mc)