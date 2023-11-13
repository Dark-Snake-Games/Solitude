"""
The main game file. This contains the room and all assets and processes.
"""

from DSEngine import *
from pygame import Vector2
from pygame.display import update


# from random import randint
COUNTER=0
TITLE = "Project: Solitude"
HEIGHT = 720
WIDTH = 1280
SPR_SIZE = {
    "width": 24,
    "height": 32
}

window = Window(title=TITLE, fps=60, size=(WIDTH, HEIGHT), bg=(100, 100, 100))
audio_man = AudioManager()
#import scenes here 
from mainroom import *
from test import *
from platformr import *
# text = Text2D("Hello World", position=Vector2(550, 335))










def main():
    
    setscenes( {  "main0": scene(mainroom, mainroominit),    "scenetest": scene(test, testinit)})
    setmainwindow(window)
    resetwindow()
    changescene("main0")
    
    for e in range(1,10):
        addscene("main"+str(e),scene(mainroom, mainroominit))
    addscene("platformer",scene(platformer,platformerinit))
    addscene("main10",scene(quit,quit))
    global TITLE, HEIGHT, WIDTH

    while window.running:
        keys = window.frame()
        runscene(keys)
        if keys[27]:
            return 1


if __name__ == "__main__":
    main()
