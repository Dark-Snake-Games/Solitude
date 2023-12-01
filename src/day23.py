from DSEngine import *
from DSEngine.etypes import Window
import pygame
from game import size_multiplyer,window,WIDTH,HEIGHT,COUNTER,SPR_SIZE,removetask,Tasklist,Speech

day=23
bedspeak="Should I bother?"
dresserspeak="dresser"
trashspeak="Why do I bother if there’s always more..."
doorspeak="I don't want to."
chat=["Please I’m getting","really scared for","you.","Talk to me","About anything","i won't be mad.","Ana","I’m here, okay?","I won’t drag you ","anywhere that will","make you unhappy,","I promise."]
anachat="Addy..."
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
middle=Vector2(WIDTH/2,HEIGHT/2)

loadedfirsttime=False




        
        

class Reflect(Image2D):
    def __init__(self, filename: str, window):
        super().__init__(filename, 2)
        self.alpha=0
        self.image.convert_alpha()
        self.increase=True
        self.image2=Image2D("Assets/monitor.png")
    def render(self, window: Window):
        self.image.set_alpha(self.alpha)
        if self.increase:
            self.alpha+=3
        else:
            self.alpha-=3
            if self.alpha<=0:
                self.remove(self.window)
        if self.alpha>=255:
            self.increase=False
        super().render(window)
        self.image2.render(window)
        print(self.alpha)



def load():
    global door,left_wall,right_wall,daycounter,animationsheet,sprite,bed,bedarea,startpos,computer,room,trash,closet,tasklist
    room=Image2D("Assets/Room_sprite4.png",position=middle)
    room.position=middle-Vector2(room.size)/2
    tile=room.size.x/3
    tasklist=Tasklist()
    animationsheet = AnimationSheet(default=down1, down=down, up=up, left=left, right=right)
    sprite = AnimatedSprite2D(layer=1, sheet=animationsheet, position=middle-Vector2(16,16)*7.5,size=Vector2(6,32-20)*size_multiplyer,offset=Vector2(13,20)*size_multiplyer)
    bed = Image2D("Assets/bed2.png", layer=1,position=room.position+Vector2(0,tile*2))
    print(bed.position)
    bedarea=Area2D()
    bedarea.rect=bed.rect
    startpos = sprite.position
    computer = Image2D("Assets/PcDesk_sprite.png",position=room.position)
    
    door=Area2D(position=room.position+pygame.Vector2(tile*2,0),size=pygame.Vector2(tile))
    
    room.area=True
    room.debug=False
    trash=Image2D("Assets/trash2.png",position=room.position+Vector2(tile,0))
    trash.area=True
    closet=Image2D("Assets/dresser2.png",position=room.position+Vector2(tile*2),offset=Vector2(8*size_multiplyer,0))
    daycounter=Text2D("Day "+str(day),font=pygame.font.Font("munro.ttf",40))
    daycounter.position=pygame.Vector2(WIDTH,HEIGHT)-pygame.Vector2(daycounter.color_rect.width,daycounter.color_rect.height)
    
    left_wall=Rect2D(position=pygame.Vector2(room.position.x+47.5,room.position.y),size=(pygame.Vector2(1,HEIGHT)))
    right_wall=Rect2D(position=pygame.Vector2(room.position.x+720-47.5,room.position.y),size=(pygame.Vector2(1,HEIGHT)))
    left_wall.visible,right_wall.visible=False,False
    tasklist.addtask("game")
    
load()
def mainroominit():
    global loadedfirsttime
    if not loadedfirsttime:loadedfirsttime=True
    else:
        refl=Reflect("Assets/reflect.png",window)
        refl.init(window)
        while refl in window.layers[2]:
            window.frame()
    for e in removetask:
            tasklist.remove(e)
            if e in removetask:removetask.remove(e)
    tasklist.init(window)
    room.init(window)
    bed.init(window)
    # text.init(window)
    computer.init(window)
    closet.init(window)
    trash.init(window)
    sprite.init(window)
    daycounter.init(window)
    left_wall.init(window)
    right_wall.init(window)
    door.init(window)
    

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
        if tasklist.tasks==[]:
            global COUNTER
            COUNTER.num+=1
            changescene("main"+str(COUNTER.num))
    if interacts_with(computer):
        boot_sfx = pygame.mixer.Sound("Assets/SFX_PC_ON.mp3")
        chan3 = pygame.mixer.find_channel()
        chan3.queue(boot_sfx)
        tasklist.removelist(window)
        changescene("pc")
    if interacts_with(door):
        door_sfx = pygame.mixer.Sound("Assets/SFX_DOOR_RATTLE.mp3")
        chan2 = pygame.mixer.find_channel()
        chan2.queue(door_sfx)
        Speech(doorspeak,window)
        


def mainroom(keys):
    

    sprite.visible=True
    bed.visible=True

    movement(keys)
    interactions(keys)
    

    
    
    
    



