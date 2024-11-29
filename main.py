import pgzrun, random
TITLE="Recycle Paper Bags"
WIDTH=800
HEIGHT=600

CENTER_X=WIDTH/2
CENTER_Y=HEIGHT/2

CENTER=(CENTER_X, CENTER_Y)
gameover=False
gamecomplete=False

currentlevel=1
finallevel=10
items=["whiteeggs", "yelloweggs"]
h=[]

speed=10

def draw():
    screen.blit("bground", (0,0))
    for g in h:
        g.draw()

def getitems(numberofitems):
    newitem=["whiteeggs"]
    for i in range(0,numberofitems):
        randomoption=random.choice(items)
        newitem.append(randomoption)
    return newitem

def createitems(newitem):
    item=[]
    for i in newitem:
        a=Actor(str(i)+"img")
        item.append(a)
    return item

def layout(itemstolayout):
    numberofgaps=len(itemstolayout)+1
    gapsize=WIDTH/numberofgaps
    random.shuffle(itemstolayout)
    for index,object in enumerate(itemstolayout):
        newxposition=(index+1)*gapsize
        object.x=newxposition
