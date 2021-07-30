from mine import *
import random
import sys


def getHeightBelow(x, y, z):
    if isPE:
        return min(mc.getHeight(x, z), y)
    else:
        y0 = y - 255
        while y > y0:
           if mc.getBlock(x, y, z) != block.AIR.id:
               return y
           y -= 1
        return min(mc.getHeight(x, z), y)


def rectangularPrism(x1, y1, z1, x2, y2, z2, distribution):
    x1 = int(round(x1))
    y1 = int(round(y1))
    z1 = int(round(z1))
    x2 = int(round(x2))
    y2 = int(round(y2))
    z2 = int(round(z2))
    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            for z in range(min(z1, z2), max(z1, z2)+1):
                if isinstance(distribution, Block):
                    mc.setBlock(x, y, z, distribution)
                else:
                    r = random.random()
                    for p, b in distribution:
                        r -= p
                        if r < 0:
                            mc.setBlock(x, y, z, b)
                            break
def wall(x1,y1,z1, x2,y2,z2, baseHeight, altHeight, distribution):
    x = x1
    z = z1

    while True:
        if (x-x1+z-z1) % 2 == 0:
            height = altHeight
        else:
            height = baseHeight
        y0 = getHeightBelow(x,y1,z)
        rectangularPrism(x,y0,z,x,y1+height,z,distribution)
        if x >= x2 and z >= z2:
            return
        if x < x2:
            x = x + 1
        if z < z2:
            z = z + 1
