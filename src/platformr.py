import platformer.game as platform
import game
from DSEngine import *

def platformerinit():
    game.window.zoom=pygame.Vector2(1,1)
    platform.tosurfaceinit()
    
    platform.SURFACE.init(game.window)
    

def platformer(_keys):
    if platform.tosurface()==1:
        
        changescene("pc")