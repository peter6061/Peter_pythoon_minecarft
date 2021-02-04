from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
x,y,z = mc.player.getTilePos()
line1 = []
line2 = []
line3 = []
for i in range(3):
    line1.append(i+1)

for j in range(3):
    line2.append((j+1)*2)

for k in range(3):
    line3.append((k+1)*3)
mc.setSign(x,y,z,63,0,str(line1),str(line2),str(line3))