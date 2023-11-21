"""
The main game file. This contains the room and all assets and processes.
"""

from DSEngine import *
from pygame.display import update

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
removetask=[]
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
import pc
# text = Text2D("Hello World", position=Vector2(550, 335))










def main():
    setscenes( {"scenetest": scene(test, testinit)})
    setmainwindow(window)
    resetwindow()
    days=[day1,day2,day3,day5,day9,day16,day23,dayIDK]
    for e in range(len(days)):
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
