from DSEngine import *
from game import size_multiplyer,window,WIDTH,HEIGHT,COUNTER,SPR_SIZE


down1 = Image2D(filename="Assets/Player/tile000.png", position=Vector2(150, 55))
down2 = Image2D(filename="Assets/Player/tile001.png", position=Vector2(150, 55))
down3 = Image2D(filename="Assets/Player/tile002.png", position=Vector2(150, 55))
down = Spritesheet(*([down2] * 12 + [down3] * 12))
up1 = Image2D(filename="Assets/Player/tile003.png", position=Vector2(150, 55))
up2 = Image2D(filename="Assets/Player/tile004.png", position=Vector2(150, 55))
up3 = Image2D(filename="Assets/Player/tile005.png", position=Vector2(150, 55))
up = Spritesheet(*([up2] * 12 + [up3] * 12))
left1 = Image2D(filename="Assets/Player/tile006.png", position=Vector2(150, 55))
left2 = Image2D(filename="Assets/Player/tile007.png", position=Vector2(150, 55))
left3 = Image2D(filename="Assets/Player/tile008.png", position=Vector2(150, 55))
left = Spritesheet(*([left2] * 12 + [left3] * 12))
right1 = Image2D(filename="Assets/Player/tile009.png", position=Vector2(150, 55))
right2 = Image2D(filename="Assets/Player/tile010.png", position=Vector2(150, 55))
right3 = Image2D(filename="Assets/Player/tile011.png", position=Vector2(150, 55))
right = Spritesheet(*([right2] * 12 + [right3] * 12))

def load():
    global animationsheet,sprite,bed,bedarea,startpos,computer,room,trash,closet
    animationsheet = AnimationSheet(default=down1, down=down, up=up, left=left, right=right)
    sprite = AnimatedSprite2D(layer=1, sheet=animationsheet, position=Vector2(150, 55),size=Vector2(6,32-20)*size_multiplyer,offset=Vector2(13,20)*size_multiplyer)
    bed = Image2D("Assets/bed2.png", layer=1,position=pygame.Vector2(0,64*size_multiplyer))
    bedarea=Area2D()
    bedarea.rect=bed.rect
    startpos = sprite.position
    computer = Image2D("Assets/PcDesk_sprite.png")
    room=Image2D("Assets/Room_sprite.png")
    room.area=True
    trash=Image2D("Assets/trash2.png",position=Vector2(32*size_multiplyer,0))
    trash.area=True
    closet=Image2D("Assets/dresser2.png",position=Vector2(64*size_multiplyer),offset=pygame.Vector2(8*size_multiplyer,0))

def mainroominit():
    load()
    room.init(window)
    bed.init(window)
    # text.init(window)
    sprite.position=Vector2(150, 55)
    computer.init(window)
    closet.init(window)
    trash.init(window)
    sprite.init(window)


def movement(keys):
    
    acc = Vector2(0.0, 0.0)

    sheet_to_play=""
    
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
    acc.x = keys[key_to_scancode("d")] - keys[key_to_scancode("a")] # * window.delta
    acc.y = keys[key_to_scancode("s")] - keys[key_to_scancode("w")] # * window.delta
    acc*=size_multiplyer
    
    
    if acc==Vector2(0,0):
        sheet_to_play=""
    if sheet_to_play !="" and (not sprite.playing or sprite.sheet_name != sheet_to_play):
        sprite.play_sheet(sheet_to_play)
    elif sheet_to_play=="":
        sprite.frame=sprite.sheet_length
        sprite.playing=False
    
    
    sprite.move(acc)
    
    sprite.position.x = max(0, min(sprite.position.x, WIDTH/window.zoom.x - SPR_SIZE["width"]))
    sprite.position.y = max(0, min(sprite.position.y, HEIGHT/window.zoom.y - SPR_SIZE["height"]))

def interacts_with(thing:Rect2D):
    keys=window.pressed_keys
    return sprite.is_colliding_with(thing) and window.key_just_pressed(key_to_scancode("e"))

def interactions(keys):
    if interacts_with(bed):
        if bed.name=="Assets/bed.png":
            global COUNTER
            COUNTER+=1
            changescene("main"+str(COUNTER))
        else:
            bed.changeimage("Assets/bed.png")
    if interacts_with(computer):
        changescene("platformer")
    if interacts_with(closet):
        closet.changeimage("Assets/dresser1.png")
    if interacts_with(trash):
        trash.changeimage("Assets/trash.png")


def mainroom(keys):
    

    sprite.visible=True
    bed.visible=True

    movement(keys)
    interactions(keys)
    

    
    
    
    



