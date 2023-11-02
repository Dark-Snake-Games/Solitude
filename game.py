from DSEngine import *
from pygame import Vector2
from pygame.display import update
from sys import exit
from random import randint
default_title = "Project: Solitude"

def main():
    global default_title
    window = Window(title=default_title, fps=60, size=(1280, 720), bg=(100, 100, 100))
    audio_man = AudioManager()
    image1 = Image2D(filename="Test.png", position=Vector2(150, 55))
    image2 = Image2D(filename="Test1.png", position=Vector2(150, 55))
    spritesheet1 = Spritesheet(image1, image1, image1, image1, image1, image2, image2, image2, image2, image2)
    spritesheet2 = Spritesheet(image2, image1)
    animationsheet = AnimationSheet(default=image1, normal=spritesheet1, back=spritesheet2)
    sprite = AnimatedSprite2D(sheet=animationsheet, position=Vector2(150, 55))
    text = Text2D("Hello World", position=Vector2(550, 335))
    startpos = sprite.position
    text.init(window)
    sprite.init(window)
    while window.running:
        keys = window.frame()
        #print(window.delta)
        acc = Vector2(0.0, 0.0)
        # if sprite.rect.right < (1280+startpos.x)+window.delta:
        #     dkey = keys[key_to_scancode("d")]*window.delta
        # else:
        #     dkey = 0
        # if sprite.rect.left > 0*window.delta:
        #     akey = keys[key_to_scancode("a")]*window.delta
        # else:
        #     akey = 0
        acc.x = (keys[key_to_scancode("d")]-keys[key_to_scancode("a")])*window.delta
        acc.y = (keys[key_to_scancode("s")]-keys[key_to_scancode("w")])*window.delta
        sprite.move(acc)
        if keys[27]:
            return 1

if __name__ == "__main__":
    main()