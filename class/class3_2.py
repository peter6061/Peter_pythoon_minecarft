from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getPos()
while True:
    hits = mc.events.pollProjectileHits()
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        #mc.player.setPos(x,y,z)
        #mc.setBlock(x,y,z,46)
        #mc.setBlock(x,y-1,z,152)
        mc.createExplosion(x,y,z,50)