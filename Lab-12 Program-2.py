from mcpi_addons.minecraft import Minecraft
mc = Minecraft.create()

x = 30;
y = 10;
z = -10;

mc.player.setTilePos

x = input("X Coordinate: ")
y = input("Y Coordinate: ")
z = input("Z Coordinate: ")

x = int(x);
y = int(y);
z = int(z);

width = 200
height = 400
length = 400

mc.setBlocks(x,y,z,x+width, y+height, z+length, 3)

mc.setBlocks(x,y,z,x+width, y+height, z+length, 0)
