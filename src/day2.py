from DSEngine import *
from DSEngine.etypes import Window
from game import size_multiplyer,window,WIDTH,HEIGHT,COUNTER,SPR_SIZE,removetask,Tasklist,Speech

day=1
bedspeak="Might as well keep it tidy."
dresserspeak="A pain, but it needs to get done."
trashspeak="This stuff just keeps piling up."
doorspeak="It's locked..."
chat=["OutbackAddy:","OutbackAddy ", "sent an image", " ","Isn't the view","from there ","so pretty???","","I thought you'd"," like it :D"," ","Have you been","doing okay?"]
anachat="yea im ok"
down1 = Image2D(filename="Assets/Player/Ana_sprite1.png", position=Vector2(150, 55))
down2 = Image2D(filename="Assets/Player/Ana_sprite2.png", position=Vector2(150, 55))
down3 = Image2D(filename="Assets/Player/Ana_sprite3.png", position=Vector2(150, 55))
down = Spritesheet(*([down2] * 12 + [down3] * 12))
up1 = Image2D(filename="Assets/Player/Ana_sprite4.png", position=Vector2(150, 55))
up2 = Image2D(filename="Assets/Player/Ana_sprite5.png", position=Vector2(150, 55))
up3 = Image2D(filename="Assets/Player/Ana_sprite6.png", position=Vector2(150, 55))
up = Spritesheet(*([up2] * 12 + [up3] * 12))
right1 = Image2D(filename="Assets/Player/Ana_sprite7.png", position=Vector2(150, 55))
right2 = Image2D(filename="Assets/Player/Ana_sprite8.png", position=Vector2(150, 55))
right3 = Image2D(filename="Assets/Player/Ana_sprite9.png", position=Vector2(150, 55))
right = Spritesheet(*([right2] * 12 + [right3] * 12))
left1 = Image2D(filename="Assets/Player/Ana_sprite10.png", position=Vector2(150, 55))
left2 = Image2D(filename="Assets/Player/Ana_sprite11.png", position=Vector2(150, 55))
left3 = Image2D(filename="Assets/Player/Ana_sprite12.png", position=Vector2(150, 55))
left = Spritesheet(*([left2] * 12 + [left3] * 12))
middle=Vector2(WIDTH/2-720/2,0)






        
        





def load():
    global door,left_wall,right_wall,daycounter,animationsheet,sprite,bed,bedarea,startpos,computer,room,trash,closet,tasklist
    tasklist=Tasklist()
    animationsheet = AnimationSheet(default=down1, down=down, up=up, left=left, right=right)
    sprite = AnimatedSprite2D(layer=1, sheet=animationsheet, position=middle+Vector2(150, 55),size=Vector2(6,32-20)*size_multiplyer,offset=Vector2(13,20)*size_multiplyer)
    bed = Image2D("Assets/bed2.png", layer=1,position=middle+Vector2(0,64*size_multiplyer))
    bedarea=Area2D()
    bedarea.rect=bed.rect
    startpos = sprite.position
    computer = Image2D("Assets/PcDesk_sprite.png",position=middle)
    room=Image2D("Assets/Room_sprite.png",position=middle)
    door=Area2D(position=pygame.Vector2(0,64*size_multiplyer),size=pygame.Vector2(32*size_multiplyer))
    
    room.area=True
    room.debug=False
    trash=Image2D("Assets/trash2.png",position=middle+Vector2(32*size_multiplyer,0))
    trash.area=True
    closet=Image2D("Assets/dresser2.png",position=middle+Vector2(64*size_multiplyer),offset=Vector2(8*size_multiplyer,0))
    daycounter=Text2D("Day "+str(day),font=pygame.font.Font("munro.ttf",40))
    daycounter.position=pygame.Vector2(WIDTH,HEIGHT)-pygame.Vector2(daycounter.color_rect.width,daycounter.color_rect.height)
    
    left_wall=Rect2D(position=pygame.Vector2(room.position.x+47.5,room.position.y),size=(pygame.Vector2(1,HEIGHT)))
    right_wall=Rect2D(position=pygame.Vector2(middle.x+720-47.5,room.position.y),size=(pygame.Vector2(1,HEIGHT)))
    left_wall.visible,right_wall.visible=False,False
    tasklist.addtask("bed")
    tasklist.addtask("closet")
    tasklist.addtask("trash")
    tasklist.addtask("game")
    
load()
def mainroominit():
    
    tasklist.init(window)
    room.init(window)
    bed.init(window)
    # text.init(window)
    sprite.position=middle+Vector2(150, 55)
    computer.init(window)
    closet.init(window)
    trash.init(window)
    sprite.init(window)
    daycounter.init(window)
    left_wall.init(window)
    right_wall.init(window)


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
            COUNTER.num+=1
            changescene("main"+str(COUNTER.num))
        else:
            bed.changeimage("Assets/bed.png")
            tasklist.remove("bed")
            Speech(bedspeak,window)
    if interacts_with(computer):
        changescene("pc")
    if interacts_with(door):
        Speech(doorspeak,window)
        
    if interacts_with(closet):
        closet.changeimage("Assets/dresser1.png")
        tasklist.remove("closet")
        Speech(dresserspeak,window)
    if interacts_with(trash):
        trash.changeimage("Assets/trash.png")
        tasklist.remove("trash")
        Speech(trashspeak,window)


def mainroom(keys):
    

    sprite.visible=True
    bed.visible=True

    movement(keys)
    interactions(keys)
    

    
    
    
    



