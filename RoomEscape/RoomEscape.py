from bangtal import *

scene1 = Scene('열쇠의 방', 'Images/배경-1.png')


door1 = Object("Images/문-오른쪽-닫힘.png")
door1.locate(scene1, 800, 270)
door1.show()
door1.closed = True

key = Object('Images/열쇠.png')
key.setScale(0.2)
key.locate(scene1, 800, 150)
key.show()

flowerpot2 = Object('Images/화분.png')
flowerpot2.locate(scene1, 150, 150)
flowerpot2.show()

flowerpot3 = Object('Images/화분.png')
flowerpot3.locate(scene1, 350, 150)
flowerpot3.show()

flowerpot = Object('Images/화분.png')
flowerpot.locate(scene1, 550, 150)
flowerpot.show()

flowerpot4 = Object('Images/화분.png')
flowerpot4.locate(scene1, 750, 150)
flowerpot4.show()

flowerpot5 = Object('Images/화분.png')
flowerpot5.locate(scene1, 950, 150)
flowerpot5.show()

scene2 = Scene('16진수의 방', 'Images/배경-2.png')

door2 = Object('Images/문-왼쪽-열림.png')
door2.locate(scene2, 320, 270)
door2.show()

door3 = Object('Images/문-오른쪽-닫힘.png')
door3.locate(scene2, 910, 270)
door3.show()

keypad = Object('Images/키패드.png')
keypad.locate(scene2, 885, 420)
keypad.show()

switch = Object('Images/스위치.png')
switch.locate(scene2, 880, 400)
switch.show()

password = Object('Images/암호.png')
password.locate(scene2, 50, 300)
password.setScale(0.2)

scene3 = Scene('무지의 방', 'Images/배경-1.png')

muji = Object('Images/무지.png')
muji.locate(scene3, 200, 170)
muji.setScale(0.3)
muji.show()

keypad2 = Object('Images/키패드.png')
keypad2.locate(scene3, 800, 250)
keypad2.setScale(18.0)
keypad2.show()

scene4 = Scene('라이언의 방', 'Images/배경-2.png')

lion = Object('Images/라이언.png')
lion.locate(scene4, 200, 170)
lion.setScale(0.3)
lion.show()

keypad3 = Object('Images/키패드.png')
keypad3.locate(scene4, 800, 250)
keypad3.setScale(18.0)
keypad3.show()


doorx = Object("Images/문-오른쪽-열림.png")
doorx.locate(scene1, 800, 270)


door1.closed = True
def door1_onMouseAction(x, y, action):
    if door1.closed:
        if key.inHand():
            door1.setImage('Images/문-오른쪽-열림.png')
            door1.closed = False
        else:
            showMessage('열쇠가 필요해---')
    else:
        scene2.enter()
door1.onMouseAction = door1_onMouseAction

def key_onMouseAction(x, y, action):
    key.pick()
key.onMouseAction = key_onMouseAction



flowerpot4.moved = False
def flowerpot4_onMouseAction(x, y, action):
    if flowerpot4.moved == False:
        if action == MouseAction.DRAG_LEFT:
            flowerpot4.locate(scene1,650,150)
            flowerpot4.moved = True
        elif action == MouseAction.DRAG_RIGHT:
            flowerpot4.locate(scene1,850,150)
            flowerpot4.moved = True
flowerpot4.onMouseAction = flowerpot4_onMouseAction

flowerpot2.click = True
flowerpot.click = True
flowerpot3.click = True
flowerpot5.click = True

def flowerpot2_onMouseAction(x, y, action):
    if flowerpot2.click:
        showMessage('아 뭐야 흔들지마!')
flowerpot2.onMouseAction = flowerpot2_onMouseAction

def flowerpot_onMouseAction(x, y, action):
    if flowerpot.click:
        showMessage('내가 그렇게 좋아...?ㅎㅎ')
flowerpot.onMouseAction = flowerpot_onMouseAction

def flowerpot3_onMouseAction(x, y, action):
    if flowerpot3.click:
        showMessage('아 뭐야 건들지마!')
flowerpot3.onMouseAction = flowerpot3_onMouseAction


def flowerpot5_onMouseAction(x, y, action):
    if flowerpot5.click:
        showMessage('날 왜 건드는거야...? ㅠㅠ')
flowerpot5.onMouseAction = flowerpot5_onMouseAction


def door2_onMouseAction(x, y, action):
    scene1.enter()
door2.onMouseAction = door2_onMouseAction

door3.locked = True
door3.closed = True
def door3_onMouseAction(x, y, action):
    if door3.locked:
        showMessage('문이 잠겨있다.')
    elif door3.closed:
        door3.setImage('Images/문-오른쪽-열림.png')
        door3.closed = False
    else:
        scene3.enter()
door3.onMouseAction = door3_onMouseAction

def door3_onKeypad():
    door3.locked = False
    showMessage("철커덕!!! 문이 열렸다.")
door3.onKeypad = door3_onKeypad

def keypad_onMouseAction(x, y, action):
    showKeypad('CAED', door3)
keypad.onMouseAction = keypad_onMouseAction
    

switch.lighted = True
def switch_onMouseAction(x, y, action):
    switch.lighted = not switch.lighted
    if switch.lighted:
        scene2.setLight(1)
        password.hide()
    else:
        scene2.setLight(0.2)
        password.show()
switch.onMouseAction = switch_onMouseAction

muji.click = True
muji.locked = True
def muji_onMouseAction(x, y, action):
    if muji.click == True and muji.locked == True:
        showMessage('경제협력개발기구를 의미하는 단어를 쳐')
        muji.click == False
    elif muji.click == False and muji.locked == True:
        showMessage('경제협력개발기구를 의미하는 단어를 쳐')
    else:
        scene4.enter()
muji.onMouseAction = muji_onMouseAction

def keypad2_onMouseAction(x, y, action):
    showKeypad('OECD', muji)
keypad2.onMouseAction = keypad2_onMouseAction

def muji_onKeypad():
    muji.locked = False
    showMessage("정답입니다. 무지를 눌러주세요")
muji.onKeypad = muji_onKeypad

lion.click = True
lion.locked = True
def lion_onMouseAction(x, y, action):
    if lion.click:
        showMessage('I ???? computer science... and I ???? you...')
        if lion.locked == False:
            endGame()
lion.onMouseAction = lion_onMouseAction

def keypad3_onMouseAction(x, y, action):
    showKeypad('LOVE', lion)
keypad3.onMouseAction = keypad3_onMouseAction

def lion_onKeypad():
    lion.locked = False
    lion.setImage('Images/문-왼쪽-열림.png')
    showMessage("정답입니다. 숨겨진 문을 눌러주세요 게임 끝!")
lion.onKeypad = lion_onKeypad


startGame(scene1)