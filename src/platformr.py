import platformer.game as platform
import game
from DSEngine import *

def platformerinit():
    platform.SURFACE.init(game.window)
    platform.tosurfaceinit()

def platformer(_keys):
    if platform.tosurface()==1:
        game.COUNTER+=1
        changescene("main2")