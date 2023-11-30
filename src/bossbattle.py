from DSEngine import *
import game
import os
import pygame
c=None
text=Text2D("Boss Battle Unlocked! Want to play\nthe final level of the game?",position=Vector2(0,0),font=pygame.font.Font("munro.ttf",60))
yes=Button("yes",font=pygame.font.Font("munro.ttf",90),color=(0,0,0))
no=Button("no",font=pygame.font.Font("munro.ttf",160))

class Reflect(Image2D):
    def __init__(self, filename: str, window):
        super().__init__(filename, 2)
        self.alpha=0
        self.image.convert_alpha()
        self.increase=True
        self.image2=Image2D("Assets/monitor.png")
        self.stop=0
    def render(self, window: Window):
        self.image.set_alpha(self.alpha)
        if self.increase:
            self.alpha+=3
        elif self.stop<=0:
            self.alpha-=3
            if self.alpha<=0:
                self.remove(self.window)
        else:
            self.stop-=1
        if self.increase and self.alpha>=255:
            self.increase=False
            self.stop=60*20
        super().render(window)
        self.image2.render(window)
class noReflect(Image2D):
    def __init__(self, filename: str, window):
        super().__init__(filename, 2)
        self.alpha=0
        self.image.convert_alpha()
        self.increase=True
        self.stop=0
    def render(self, window: Window):
        self.image.set_alpha(self.alpha)
        if self.increase:
            self.alpha+=3
        elif self.stop<=0:
            self.alpha-=3
            if self.alpha<=0:
                self.remove(self.window)
        else:
            self.stop-=1
        if self.increase and self.alpha>=255:
            self.increase=False
            self.stop=60*20
        super().render(window)

def init():
    global c
    c = None
    text.position=Vector2(game.WIDTH,game.HEIGHT*0.9)/2-text.size/2
    yes.position=text.position+Vector2(0,text.size.y*1.25)
    no.position=text.position+text.size+Vector2(-no.size.x,0)
    text.init(game.window)
    yes.init(game.window)
    no.init(game.window)
    pygame.mixer.music.stop()
def frame(keys):
    global c
    if os.path.exists("assets/1.sav"):
        f = open("assets/1.sav")
        c = int(f.read())
        if c != None:
            if c:
                yes.pressed = True
            if not c:
                no.pressed = True
    if yes.pressed:
        f = open("assets/1.sav", "w")
        f.write(str(True))
        resetwindow()
        crash=Text2D("game crahsed",position=yes.position)
        crash.init(game.window)
        refl=Reflect("Assets/clearreflect.png",game.window)
        refl.init(game.window)
        while refl in game.window.layers[2]:
            game.window.frame()
            if refl.stop>0 and crash in game.window.layers["GUI"]:
                crash.remove(game.window)
        exit()
    if no.pressed:
        f = open("assets/1.sav", "w")
        f.write(str(False))
        resetwindow()
        game.window.frame()
        pygame.mixer.music.load("Assets/door.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        refl=noReflect("Assets/goodend.png",game.window)
        refl.init(game.window)
        while refl in game.window.layers[2]:
            game.window.frame()
        exit()
            
    pass

    