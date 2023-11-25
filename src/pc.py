from DSEngine import *
import game
from pygame import Vector2
desktop=Image2D("Assets/desktop.png",position=Vector2(2.5,0))

gamebutton=Button("",image="Assets/GAMEApp_Sprite.png",position=Vector2(1280-32*7.5,0))
chaosbutton=Button("",image="Assets/ChaosApp_Sprite.png",position=Vector2(0,0))
contractbutton=Button("",image="Assets/ContractApp_Sprite.png",position=Vector2(0,32*7.5))

gameicon=Button("",image="Assets/GAMEIcon_sprite.png",position=Vector2(1280/2-7*7.5,720-18*7.5))
chaosicon=Button("",image="Assets/ChaosIcon_sprite.png",position=Vector2(1280/2+9*7.5,720-18*7.5))
contracticon=Button("",image="Assets/ContractIcon_sprite.png",position=Vector2(1280/2-23*7.5,720-18*7.5))

powerbutton=Button("",image="Assets/PowerButton_sprite.png",position=Vector2(1280-19*7.5,720-18*7.5))
# powerbutton.position-=powerbutton.size
daytext=Text2D("day",color=(0,0,0),position=Vector2(5*7.5,720),font=pygame.font.Font("munro.ttf",size=80))
daytext.position.y-=daytext.size.y +2*7.5
chaoswindow=Image2D("Assets/Chaos_textbox.png",position=Vector2(1280,720)/2)
chaoswindow.position-=chaoswindow.size/2+Vector2(0,7.5*6)
chaoschat=game.Tasklist(position=chaoswindow.position+Vector2(16*7.5,7*7.5))
chats=[]
anachat=False
chaoschat.tasks=[Text2D("wewew")]
closechaosbutton=Button(" ",position=chaoswindow.position,size=Vector2(7.5*9,7.5*7))
closechaosbutton.visible=False
chaossendbutton=Button("",position=Vector2(chaoswindow.position+Vector2(0,chaoswindow.rect.height))-Vector2(0,8*7.5),size=Vector2(chaoswindow.rect.width,8*7.5))


def init():
    global scroll,anachat,chats
    
    anachat=False
    scroll=0
    desktop.init(game.window)
    gamebutton.init(game.window)
    chaosbutton.init(game.window)
    contractbutton.init(game.window)
    gameicon.init(game.window)
    chaosicon.init(game.window)
    contracticon.init(game.window)
    powerbutton.init(game.window)
    daytext.text="DAY"+str(game.days[game.COUNTER.num].day)
    daytext.update()
    daytext.init(game.window)
    # for e in chats:
    #     chats.remove(e)
    chats=[]
    for e in game.days[game.COUNTER.num].chat:
        if  "<img>" in e:
            imagepath=e.replace("<img>","")
            image=Image2D(imagepath,2)
            image.debug=False
            chats.append(image)
        else:chats.append(Text2D(e,color=(0,0,0),font=pygame.font.Font("munro.ttf",size=80)))
    
def frame(keys):
    global scroll,anachat
    if powerbutton.pressed:
        changescene("main"+str(game.COUNTER.num))
    if gamebutton.pressed or gameicon.pressed:
        changescene("platformer")
    if chaosbutton.pressed and not chaoswindow in game.window.layers[1]:
        chaoschat.init(game.window)
        chaoswindow.init(game.window)
        closechaosbutton.init(game.window)
        chaossendbutton.init(game.window)
        print("addchaos")
    if closechaosbutton.pressed and chaoswindow in game.window.layers[1]:
        chaoschat.removelist(game.window)
        chaoswindow.remove(game.window)
        closechaosbutton.remove(game.window)
        chaossendbutton.remove(game.window)
        closechaosbutton.pressed=False
        for e in chats:
            if e in game.window.layers["GUI"]:
                e.remove(game.window)
    if chaossendbutton.pressed:
        if not anachat:
            anachat=True
            chats.append(Text2D("Ana-tisocial:",color=(0,50,120),font=pygame.font.Font("munro.ttf",size=60)))
            
            chats.append(Text2D(game.days[game.COUNTER.num].anachat,color=(0,50,120),font=pygame.font.Font("munro.ttf",size=60)))
            scroll=len(chats)-4
    if game.window.key_just_pressed(key_to_scancode("w")) and chaoswindow in game.window.layers[1]:
        scroll-=1
    if game.window.key_just_pressed(key_to_scancode("s")) and chaoswindow in game.window.layers[1]:
        scroll+=1
        
    if scroll+4>len(chats):
        scroll-=1
    if scroll<0:
        scroll=0
    scroll2=scroll+4
    if scroll2>len(chats):
        scroll2=len(chats)
    chaoschat.tasks=chats[scroll:scroll2]
    chaoschat.update()
    for e in chats:
        if not e in chaoschat.tasks and e in game.window.layers[e.layer]:
            e.remove(game.window)