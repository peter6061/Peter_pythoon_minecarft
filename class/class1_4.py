from mcpi.minecraft import Minecraft as mcs
import time
mc = mcs.create()
a = 0
while True:
    time.sleep(1)
    mc.postToChat('t = '+str(a))
    a = a+1