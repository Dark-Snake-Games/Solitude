"""
The main game file. This contains the room and all assets and processes.
"""

from DSEngine import *
from pygame.display import update
#from os import chdir
from subprocess import run
#run(['cd', 'src/'])
#chdir("src")

size_multiplyer=7.5
# from random import randint
class counterobject:
    def __init__(self,num) -> None:
        self.num=num
        pass
COUNTER=counterobject(0)
TITLE = "Project: Solitude"
HEIGHT = 720
WIDTH = 1280
SPR_SIZE = {
    "width": 24*size_multiplyer,
    "height": 32*size_multiplyer
}

window = Window(title=TITLE, fps=60, size=(WIDTH, HEIGHT), bg=(0, 0, 0))
audio_man = AudioManager()
m1 = None
m2 = None
removetask=[]


class Tasklist:
    def __init__(self,position=Vector2(0,0)) -> None:
        self.tasks=[]
        self.window=None
        self.position=position
        pass
    def update(self):
        
        if self.window!=None:
            for e in range(len(self.tasks)):
                pos=0
                for i in range(e):
                    if type(self.tasks[i])==Text2D:
                        pos+=self.tasks[i].color_rect.height
                    elif type(self.tasks[i]) == Image2D:
                        pos+=self.tasks[i].rect.height
                task=self.tasks[e]
                task.position=self.position+Vector2(0,pos)
                if not task in window.layers[task.layer]:
                    task.init(self.window)
    def addtask(self,str):
        task=Text2D(str,position=pygame.Vector2(0,0),font=pygame.font.Font("munro.ttf",40))
        self.tasks.append(task)
        
        self.update()
    def remove(self,str:str):
        task=None
        for e in self.tasks:
            if type(e)==Text2D and e.text==str:
                task=e
        if task!=None:
            if task in window.layers[task.layer]:
                task.remove(self.window)
            self.tasks.remove(task)
            self.update()
    def removeobject(self,task):
        if task in window.layers[task.layer]:
            task.remove(self.window)
            self.tasks.remove(task)
            self.update()
    def removelist(self,window:Window):
        for e in self.tasks:
            e.remove(window)
        self.window=None
    def init(self,window):
        self.window=window
        for e in self.tasks:
            e.init(self.window)
        self.update()

class Speech(Text2D):
    def __init__(self,text,window,color=(255, 255, 255)) -> None:
        super().__init__(text,font=pygame.font.Font("munro.ttf",40),color=color)
        self.window=window
        self.position=pygame.Vector2(WIDTH,HEIGHT)/2-pygame.Vector2(self.color_rect.size)/2+pygame.Vector2(0,200)
        self.init(window)
    def render(self, window: Window):
        super().render(window)
        self.position.y-=0.5
        self.text_surface.set_alpha((self.position.y-HEIGHT/2)/200*255)
        if self.text_surface!=None and self.text_surface.get_alpha()<=0:
            self.remove(self.window)



#import scenes here 
import day1
import day2
import day3
import day5
import day9
import day16
import day23
import dayIDK
from test import *
from platformr import *

days=[day1,day2,day3,day5,day9,day16,day23,dayIDK]

import pc
# text = Text2D("Hello World", position=Vector2(550, 335))










def main():
    pygame.mixer.init()
    setscenes( {"scenetest": scene(test, testinit)})
    setmainwindow(window)
    resetwindow()
    for e in range(len(days)):
    # e = 1
        addscene("main"+str(e),scene(days[e].mainroom,days[e].mainroominit))
    changescene("main0")
    
    
    addscene("platformer",scene(platformer,platformerinit))
    addscene("main10",scene(quit,quit))
    addscene("pc",scene(pc.frame,pc.init))
    global TITLE, HEIGHT, WIDTH

    while window.running:
        keys = window.frame()
        runscene(keys)
        if keys[27]:
            return 1


if __name__ == "__main__":
    main()
