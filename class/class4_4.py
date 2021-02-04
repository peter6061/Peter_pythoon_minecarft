from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
from time import sleep
while True:
    sleep(0.5)
    mc.executeCommand('time set 0')