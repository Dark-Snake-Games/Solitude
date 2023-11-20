from DSEngine import *
import game
from pygame import Vector2
desktop=Image2D("Assets/desktop.png",position=Vector2(1280/2-1080/2,0))

def init():
    desktop.init(game.window)
def frame(keys):
    if keys[key_to_scancode("q")]:
        changescene("main"+str(game.COUNTER))