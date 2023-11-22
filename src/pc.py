from DSEngine import *
import game
from pygame import Vector2
desktop=Image2D("Assets/desktop.png",position=pygame.Vector2(2.5,0))
gamebutton=Button("",image="Assets/GAMEApp_Sprite.png",position=desktop.position+Vector2(1280-720/2.5,0),size=(720/2.5,720/2.5))
# gamebutton.visible=False
gamebutton.debug=True
print(gamebutton.size,gamebutton.color_rect)
def init():
    desktop.init(game.window)
    gamebutton.init(game.window)
    print(game.window.layers)
    
def frame(keys):
    if game.window.key_just_pressed(key_to_scancode("q")):
        changescene("main"+str(game.COUNTER.num))
    if gamebutton.pressed:
        changescene("platformer")