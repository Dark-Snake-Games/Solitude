from DSEngine import *
from game import *
rect = Rect2D(position=Vector2(-20,-20),offset=Vector2(20,20))
def testinit():
    rect.init(window)

def test(keys):
    # bedsheet.visible=False
    # sprite.visible=False
    # rect0.visible=False
    if keys[key_to_scancode(" ")]:
        global SCN
        changescene("main")
        