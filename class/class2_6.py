from mcpi.minecraft import Minecraft as mcs
mc = mcs.create()
username = input("username?")
message = input()
mc.postToChat("<"+username+">"+' '+message)