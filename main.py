import pgzrun, random

TITLE="Save The Egg"
WIDTH=800
HEIGHT=500

CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2

CENTER=(CENTER_X, CENTER_Y)
gameover=False
gamestart=True

speed=10

currentlevel=1
finallevel=10
items=["egg"]

def draw():
    screen.blit("bground", (-200,-90))

def createitem(newitem):
    newitem=["egg"]
    a=Actor(str(i)+"img")
    for i in range(currentlevel):
        newitems.draw(newitem)

def layout(itemstolayout):
    numberofgaps=len(itemstolayout)+1
    gapsize=WIDTH/numberofgaps
    random.shuffle(itemstolayout)
    for index,object in enumerate(itemstolayout):
        newxposition=(index+1)*gapsize
        object.x=newxposition

def makeitems(numberofitems):
    a=getitems(numberofitems)
    b=createitems(a)

def animateitems(itemstoanimate):
    for k in itemstoanimate:
        duration=speed-currentlevel
        k.anchor=("center", "bottom")
        animation=animate(k,duration=duration,on_finished=handle_gameover,y=HEIGHT)
        animations.append(animation)

def handle_gameover():
    global gameover
    gameover=True

if currentlevel==finallevel:
    gamecomplete=[]


def gamecomplete():
    currentlevel==finallevel

def update():
    pass

pgzrun.go()