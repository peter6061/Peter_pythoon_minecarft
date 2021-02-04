from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
from random import randint
x,y,z = mc.player.getTilePos()
computer = randint(0,15)
for i in range(16):
    for j in range(16):
        color = randint(0,15)
        mc.setBlock(x+i,y-1,z+j,35,color)

while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if computer == data:
            mc.postToChat('you got it')
            break
        elif computer < data:
            mc.postToChat('too big')
        else:
            mc.postToChat('too small')
        
