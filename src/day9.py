from DSEngine import *
from DSEngine.etypes import Window
from game import size_multiplyer,window,WIDTH,HEIGHT,COUNTER,SPR_SIZE,removetask

day=9
bedspeak=""
dresserspeak=""
trashspeak=""
doorspeak=""

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

class Tasklist:
    def __init__(self) -> None:
        self.tasks=[]
        self.window=None
        pass
    def update(self):
        for e in removetask:
            self.remove(e)
            if e in removetask:removetask.remove(e)
        if self.window!=None:
            for e in range(len(self.tasks)):
                pos=0
                for i in range(e):
                    pos+=self.tasks[i].color_rect.height
                task=self.tasks[e]
                task.position.y=pos
                if not task in window.layers[task.layer]:
                    task.init(self.window)
    def addtask(self,str):
        task=Text2D(str,position=pygame.Vector2(0,0))
        self.tasks.append(task)
        
        self.update()
    def remove(self,str):
        task=None
        for e in self.tasks:
            if e.text==str:
                task=e
        if task!=None:
            if task in window.layers[task.layer]:
                task.remove(self.window)
            self.tasks.remove(task)
            self.update()
    def init(self,window):
        self.window=window
        for e in self.tasks:
            e.init(self.window)
        self.update()



class Speech(Text2D):
    def __init__(self,text,window) -> None:
        super().__init__(text)
        self.window=window
        self.position=pygame.Vector2(WIDTH,HEIGHT)/2-pygame.Vector2(self.color_rect.size)/2+pygame.Vector2(0,200)
        self.init(window)
    def render(self, window: Window):
        super().render(window)
        self.position.y-=0.5
        self.text_surface.set_alpha((self.position.y-HEIGHT/2)/200*255)
        if self.text_surface!=None and self.text_surface.get_alpha()<=0:
            self.remove(self.window)
        
        





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
    daycounter=Text2D("Day "+str(day))
    daycounter.position=pygame.Vector2(WIDTH,HEIGHT)-pygame.Vector2(daycounter.color_rect.width,daycounter.color_rect.height)
    
    left_wall=Rect2D(position=pygame.Vector2(room.position.x+47.5,room.position.y),size=(pygame.Vector2(1,HEIGHT)))
    right_wall=Rect2D(position=pygame.Vector2(middle.x+720-47.5,room.position.y),size=(pygame.Vector2(1,HEIGHT)))
    left_wall.visible,right_wall.visible=False,False
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
        global COUNTER
        COUNTER.num+=1
        changescene("main"+str(COUNTER.num))
        
    if interacts_with(computer):
        changescene("pc")
    if interacts_with(door):
        Speech(doorspeak,window)
        
    if interacts_with(trash):
        trash.changeimage("Assets/trash.png")
        tasklist.remove("trash")
        Speech(trashspeak,window)


def mainroom(keys):
    

    sprite.visible=True
    bed.visible=True

    movement(keys)
    interactions(keys)
    

    
    
    
    



