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
    down1 = Image2D(filename="Assets/Player/tile000.png", position=Vector2(150, 55))
    down2 = Image2D(filename="Assets/Player/tile001.png", position=Vector2(150, 55))
    down3 = Image2D(filename="Assets/Player/tile002.png", position=Vector2(150, 55))
    down = Spritesheet(down2,down2,down2,down2,down2,down2,down2,down2,down2,down2,down2,down2,\
                        down3,down3,down3,down3,down3,down3,down3,down3,down3,down3,down3,down3,)
    up1 = Image2D(filename="Assets/Player/tile003.png", position=Vector2(150, 55))
    up2 = Image2D(filename="Assets/Player/tile004.png", position=Vector2(150, 55))
    up3 = Image2D(filename="Assets/Player/tile005.png", position=Vector2(150, 55))
    up = Spritesheet(up2,up2,up2,up2,up2,up2,up2,up2,up2,up2,up2,up2,\
                     up3,up3,up3,up3,up3,up3,up3,up3,up3,up3,up3,up3,)
    left1 = Image2D(filename="Assets/Player/tile006.png", position=Vector2(150, 55))
    left2 = Image2D(filename="Assets/Player/tile007.png", position=Vector2(150, 55))
    left3 = Image2D(filename="Assets/Player/tile008.png", position=Vector2(150, 55))
    left = Spritesheet(left2,left2,left2,left2,left2,left2,left2,left2,left2,left2,left2,left2,\
                       left3,left3,left3,left3,left3,left3,left3,left3,left3,left3,left3,left3,)
    right1 = Image2D(filename="Assets/Player/tile009.png", position=Vector2(150, 55))
    right2 = Image2D(filename="Assets/Player/tile010.png", position=Vector2(150, 55))
    right3 = Image2D(filename="Assets/Player/tile011.png", position=Vector2(150, 55))
    right = Spritesheet(right2,right2,right2,right2,right2,right2,right2,right2,right2,right2,right2,right2,\
                       right3,right3,right3,right3,right3,right3,right3,right3,right3,right3,right3,right3,)
    animationsheet = AnimationSheet(default=down1, down=down, up=up, left=left, right=right)
    sprite = AnimatedSprite2D(sheet=animationsheet, position=Vector2(150, 55))
    #text = Text2D("Hello World", position=Vector2(550, 335))
    rect0 = Rect2D(layer=1, position=Vector2(0, 0), size=Vector2(50, 50))
    startpos = sprite.position
    rect0.init(window)
    #text.init(window)
    sprite.init(window)
    while window.running:
        keys = window.frame()
        acc = Vector2(0.0, 0.0)
        if keys[key_to_scancode("d")]:
            sprite.sprites.default = right1
            if not sprite.playing or sprite.sheet_name != "right":
                sprite.play_sheet("right")
        if keys[key_to_scancode("a")]:
            sprite.sprites.default = left1
            if not sprite.playing or sprite.sheet_name != "left":
                sprite.play_sheet("left")
        if keys[key_to_scancode("w")]:
            sprite.sprites.default = up1
            if not sprite.playing or sprite.sheet_name != "up":
                sprite.play_sheet("up")
        if keys[key_to_scancode("s")]:
            sprite.sprites.default = down1
            if not sprite.playing or sprite.sheet_name != "down":
                sprite.play_sheet("down")
        acc.x = (keys[key_to_scancode("d")]-keys[key_to_scancode("a")])#*window.delta
        acc.y = (keys[key_to_scancode("s")]-keys[key_to_scancode("w")])#*window.delta
        acc *= 3
        sprite.move(acc)
        if keys[27]:
            return 1

if __name__ == "__main__":
    main()