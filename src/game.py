from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit
#from random import randint





default_title = "Project: Solitude"
height = 720
width = 1280
sprite_size = {
    "width": 24,
    "height": 32

}


#moved variables from main to here
#
#
window = Window(title=default_title, fps=60, size=(width, height), bg=(100, 100, 100))
audio_man = AudioManager()

down1 = Image2D(filename="Assets/Player/tile000.png", position=Vector2(150, 55))
down2 = Image2D(filename="Assets/Player/tile001.png", position=Vector2(150, 55))
down3 = Image2D(filename="Assets/Player/tile002.png", position=Vector2(150, 55))
down = Spritesheet(down2,down2,down2,down2,down2,down2,down2,down2,down2,down2,down2,down2,\
                    down3,down3,down3,down3,down3,down3,down3,down3,down3,down3,down3,down3,)
up1 = Image2D(filename="Assets/Player/tile003.png", position=Vector2(150, 55))
up2 = Image2D(filename="Assets/Player/tile004.png", position=Vector2(150, 55))
up3 = Image2D(filename="Assets/Player/tile005.png", position=Vector2(150, 55))
up = Spritesheet(up2,up2,up2,up2,up2,up2,up2,up2,up2,up2,up2,up2,\
                    up3,up3,up3,up3,up3,up3,up3,up3,up3,up3,up3,up3,)
left1 = Image2D(filename="Assets/Player/tile006.png", position=Vector2(150, 55))
left2 = Image2D(filename="Assets/Player/tile007.png", position=Vector2(150, 55))
left3 = Image2D(filename="Assets/Player/tile008.png", position=Vector2(150, 55))
left = Spritesheet(left2,left2,left2,left2,left2,left2,left2,left2,left2,left2,left2,left2,\
                    left3,left3,left3,left3,left3,left3,left3,left3,left3,left3,left3,left3,)
right1 = Image2D(filename="Assets/Player/tile009.png", position=Vector2(150, 55))
right2 = Image2D(filename="Assets/Player/tile010.png", position=Vector2(150, 55))
right3 = Image2D(filename="Assets/Player/tile011.png", position=Vector2(150, 55))
right = Spritesheet(right2,right2,right2,right2,right2,right2,right2,right2,right2,right2,right2,right2,\
                    right3,right3,right3,right3,right3,right3,right3,right3,right3,right3,right3,right3,)

animationsheet = AnimationSheet(default=down1, down=down, up=up, left=left, right=right)
sprite = AnimatedSprite2D(layer=1, sheet=animationsheet, position=Vector2(150, 55))
# text = Text2D("Hello World", position=Vector2(550, 335))
bedsheet=AnimationSheet(default=Image2D("Assets/bed.png"), size=Vector2(64, 1))
rect0 = AnimatedSprite2D(sheet=bedsheet, layer=1)
startpos = sprite.position
#
#
#end of variables moved from main()
rect=Rect2D()

def resetwindow():
    global window
    window.layers={1:[], 2:[], 3:[], 4:[], 5:[], 6:[],
                       7:[], 8:[], 9:[], 10:[], "GUI":[]}

def fakeinit():
    pass

class scene:
    def __init__(self,scene,init=fakeinit,stop=resetwindow) -> None:
        self.init, self.scene, self.stop = init, scene, stop

scn="scenetest"
def changescene(Scn:str):
    global scn
    scenes[scn].stop()
    scn=Scn
    scenes[scn].init()
    
    
def testinit():
    
    rect.init(window)
def test(keys):
    # bedsheet.visible=False
    # sprite.visible=False
    # rect0.visible=False
    if keys[key_to_scancode(" ")]:
        global scn
        changescene("main")
        print(scn)
    
def mainroominit():
    
    rect0.init(window)
    # text.init(window)
    sprite.init(window)

def mainroom(keys):
    
    acc = Vector2(0.0, 0.0)

    sheet_to_play="" #sheet will be played after these if commands 
    #so it wont switch between the animations every frame that makes animation stop on holding
    #two buttons
    
    bedsheet.visible=True
    sprite.visible=True
    rect0.visible=True
    
    if keys[key_to_scancode("d")]:
        sprite.sprites.default = right1
        
        sheet_to_play="right"
    if keys[key_to_scancode("a")]:
        sprite.sprites.default = left1
        sheet_to_play="left"
    if keys[key_to_scancode("w")]:
        sprite.sprites.default = up1
        sheet_to_play="up"
    if keys[key_to_scancode("s")]:
        sprite.sprites.default = down1
        sheet_to_play="down"
    if keys[key_to_scancode("t")]:
        global scn
        changescene("scenetest")
        print(scn)
    
    
    acc.x = (keys[key_to_scancode("d")]-keys[key_to_scancode("a")])#*window.delta
    acc.y = (keys[key_to_scancode("s")]-keys[key_to_scancode("w")])#*window.delta
    
    if acc==Vector2(0,0): sheet_to_play=""
    if sheet_to_play !="" and (not sprite.playing or sprite.sheet_name != sheet_to_play):
        sprite.play_sheet(sheet_to_play)
    elif sheet_to_play=="":
        sprite.frame=sprite.sheet_length
        sprite.playing=False
    sprite.move(acc)
    # print(f"Sprite position: {sprite.position}")

    if sprite.position.x < 0:
        sprite.position.x = 0
    if sprite.position.x > width - sprite_size["width"]:
        sprite.position.x = width - sprite_size["width"]
    if sprite.position.y < 0:
        sprite.position.y = 0
    if sprite.position.y > height - sprite_size["height"]:
        sprite.position.y = height - sprite_size["height"]

#usage of scenechanger
#use the name of the key as the scene name
#to add functions to a scene use scene(scene,init,stop) or just scene(scene) use their names without the brackest("()") example: scene(sceneinit,thescene)

#to change scene use changescene(name:str)
scenes={"main":scene(mainroom,mainroominit), "scenetest":scene(test,testinit)}

def main():
    
    global default_title, height, width#, sprite_width
    rect.init(window)

    while window.running:
        keys = window.frame()
        scenes[scn].scene(keys)
        
        if keys[27]:
            return 1

if __name__ == "__main__":
    main()