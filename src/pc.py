from DSEngine import *
import game
from pygame import Vector2
desktop=Image2D("Assets/desktop.png",position=Vector2(2.5,0))

gamebutton=Button("",image="Assets/GAMEApp_Sprite.png",position=Vector2(1280-32*7.5,0))
chaosbutton=Button("",image="Assets/ChaosApp_Sprite.png",position=Vector2(0,0))
contractbutton=Button("",image="Assets/ContractApp_Sprite.png",position=Vector2(0,32*7.5))

gameicon=Button("",image="Assets/GAMEIcon_sprite.png",position=Vector2(1280/2-7*7.5,720-18*7.5))
chaosicon=Button("",image="Assets/ChaosIcon_sprite.png",position=Vector2(1280/2+9*7.5,720-18*7.5))
contracticon=Button("",image="Assets/ContractIcon_sprite.png",position=Vector2(1280/2-23*7.5,720-18*7.5))

powerbutton=Button("",image="Assets/PowerButton_sprite.png",position=Vector2(1280-19*7.5,720-18*7.5))
# powerbutton.position-=powerbutton.size
daytext=Text2D("day",position=Vector2(0,720),font=pygame.font.Font("munro.ttf",size=40))
daytext.position.y-=daytext.size.y +2*7.5
def init():
    desktop.init(game.window)
    gamebutton.init(game.window)
    chaosbutton.init(game.window)
    contractbutton.init(game.window)
    gameicon.init(game.window)
    chaosicon.init(game.window)
    contracticon.init(game.window)
    powerbutton.init(game.window)
    daytext.text="DAY"+str(game.days[game.COUNTER.num].day)
    daytext.update()
    daytext.init(game.window)
def frame(keys):
    if powerbutton.pressed:
        changescene("main"+str(game.COUNTER.num))
    if gamebutton.pressed or gameicon.pressed:
        changescene("platformer")
    