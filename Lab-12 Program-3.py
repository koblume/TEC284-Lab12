from mcpi_addons.minecraft import Minecraft

mc = Minecraft.create()
import time

pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y - 1, pos.z, 12)
time.sleep(1)