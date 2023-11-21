from DSEngine import *
import game
from pygame import Vector2
desktop=Image2D("Assets/desktop.png",position=Vector2(1280/2-1080/2,0))
gamebutton=Button("",position=desktop.position+Vector2(1080-720/2.5,0),size=(720/2.5,720/2.5))
gamebutton.visible=False
def init():
    desktop.init(game.window)
    gamebutton.init(game.window)
    print(game.window.layers)
def frame(keys):
    if game.window.key_just_pressed(key_to_scancode("q")):
        changescene("main"+str(game.COUNTER))
    if gamebutton.pressed:
        changescene("platformer")