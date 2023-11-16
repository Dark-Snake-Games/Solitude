from DSEngine import *
from game import window,WIDTH,HEIGHT,COUNTER,SPR_SIZE
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

animationsheet = AnimationSheet(default=down1, down=down, up=up, left=left, right=right)
sprite = AnimatedSprite2D(layer=1, sheet=animationsheet, position=Vector2(150, 55),size=Vector2(20,32-20),offset=Vector2(6,20))
bedsheet = AnimationSheet(default=Image2D("Assets/bed.png"), size=Vector2(64, 1))
rect0 = AnimatedSprite2D(sheet=bedsheet, layer=1)
bedarea=Area2D()
bedarea.rect=rect0.rect
startpos = sprite.position
computer = Image2D("Assets/computer.png",position=pygame.Vector2(96,0))


def mainroominit():
    
    rect0.init(window)
    # text.init(window)
    sprite.position=Vector2(150, 55)
    computer.init(window)
    sprite.init(window)

def mainroom(keys):
    
    acc = Vector2(0.0, 0.0)

    sheet_to_play=""

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
    if sprite.is_colliding_with(bedarea) and keys[key_to_scancode("e")]:
        global COUNTER
        COUNTER+=1
        changescene("main"+str(COUNTER))
    if sprite.is_colliding_with(computer) and keys[key_to_scancode("e")]:
        changescene("platformer")

    acc.x = keys[key_to_scancode("d")] - keys[key_to_scancode("a")] # * window.delta
    acc.y = keys[key_to_scancode("s")] - keys[key_to_scancode("w")] # * window.delta

    if acc==Vector2(0,0):
        sheet_to_play=""
    if sheet_to_play !="" and (not sprite.playing or sprite.sheet_name != sheet_to_play):
        sprite.play_sheet(sheet_to_play)
    elif sheet_to_play=="":
        sprite.frame=sprite.sheet_length
        sprite.playing=False
    sprite.move(acc)

    sprite.position.x = max(0, min(sprite.position.x, WIDTH/2 - SPR_SIZE["width"]))
    sprite.position.y = max(0, min(sprite.position.y, HEIGHT/2 - SPR_SIZE["height"]))



