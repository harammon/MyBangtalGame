from bangtal import *

scene0 = Scene("nodap", "images/로건.jfif")
scene1 = Scene("메인화면", "images/메인화면.jpg")
scene2 = Scene("훈련", "images/훈련.jpg")
scene2_1 = Scene("훈련", "images/훈련.jpg")
scene3 = Scene("수료", "images/훈련_몽쉘.jpg")
scene4 = Scene("밥도둑", "images/검정배경.png")
scene5 = Scene("미군식단", "images/미군식단.jpg")
scene6 = Scene("냉동", "images/냉동.jfif")
scene7 = Scene("내무반", "images/내무반.jfif")
scene8 = Scene("영창", "images/헌병.jfif")
scene9 = Scene("전역신고", "images/전역신고.jpg")

scene1.sound = Sound("audios/멋진사나이.mp3")
scene4.sound = Sound("audios/푸른소나무.mp3")
scene7.sound = Sound("audios/전선을간다.mp3")
scene9.sound = Sound("audios/여기에섰다.mp3")

scene0.sound = Sound("audios/새드.mp3")
scene5.sound = Sound("audios/새드.mp3")
scene8.sound = Sound("audios/새드.mp3")


startButton1 = Object("images/start.png")
startButton1.locate(scene1, 590, 100)
startButton1.show()

endButton1 = Object("images/end.png")
endButton1.locate(scene0, 590, 100)
endButton1.show()

endButton2 = Object("images/end.png")
endButton2.locate(scene5, 590, 100)
endButton2.show()

endButton3 = Object("images/end.png")
endButton3.locate(scene8, 590, 100)
endButton3.show()

quizButton1 = Object("images/퀴즈.png")
quizButton1.locate(scene2, 300, 100)
quizButton1.setScale(0.3)
quizButton1.show()

quizButton2 = Object("images/퀴즈.png")
quizButton2.locate(scene2_1, 300, 100)
quizButton2.setScale(0.3)
quizButton2.show()

nextButton1 = Object("images/next.png")
nextButton1.locate(scene3, 590, 100)
nextButton1.show()

nextButton2 = Object("images/next.png")
nextButton2.locate(scene4, 590, 100)
nextButton2.show()

nextButton3 = Object("images/next.png")
nextButton3.locate(scene6, 590, 100)
nextButton3.show()

tape = Object("images/테이프.png")
tape.locate(scene7, 720, 95)
tape.setScale(0.15)
tape.show()

goonbun = Object("images/군번줄.png")
goonbun.locate(scene7, 490, 260)
goonbun.setScale(0.15)
goonbun.show()

cap = Object("images/전역모.png")
cap.locate(scene7, 90, 210)
cap.setScale(0.11)
cap.show()

completeButton = Object("images/전역.png")
completeButton.locate(scene7, 1000, 100)
completeButton.setScale(0.3)
completeButton.show()

clearButton = Object("images/완료.png")
clearButton.locate(scene9, 560, 100)
clearButton.setScale(0.8)
clearButton.show()

answerNumber1 = []
for index in range(3):
    number = Object("images/답_" + str(index + 1) + ".png")
    number.locate(scene2, (500+index*200), 100)
    number.setScale(0.15)
    number.show()
    answerNumber1.append(number)

answerNumber2 = []
for index in range(3):
    number = Object("images/답_" + str(index + 1) + ".png")
    number.locate(scene2_1, (500+index*200), 100)
    number.setScale(0.15)
    number.show()
    answerNumber2.append(number)

answerFood1 = []
for index in range(3):
    food = Object("images/식사" + str(index + 1) + ".jfif")
    food.locate(scene4, (10+index*400), 200)
    food.setScale(0.8)
    food.show()
    answerFood1.append(food)

badgeList = []
for index in range(3):
    badge = Object("images/계급장_" + str(index + 1) + ".jpg")
    badge.setScale(0.8)
    badgeList.append(badge)

badgeList[0].locate(scene3, 700, 500)
badgeList[0].show()

badgeList[1].locate(scene6, 700, 500)
badgeList[1].show()

badgeAdd = Object("images/계급장_2.jpg")
badgeAdd.setScale(0.2)
badgeAdd.locate(scene7, 345, 680)
badgeAdd.show()

badgeMiddle = Object("images/계급장_4.jpg")
badgeMiddle.defineCombination(badgeList[1], badgeAdd)

badgeList[2].defineCombination(badgeMiddle, tape)

badge1 = False
badge2 = False
badge3 = False
badgeFinal = False
ownGoonbun = False
ownCap = False



def startButton1_onMouseAction(x, y, action):
    showMessage("문제를 풀어야 진급할 수 있습니다.")
    scene2.enter()
startButton1.onMouseAction = startButton1_onMouseAction

def endButton1_onMouseAction(x, y, action):
    endGame()
endButton1.onMouseAction = endButton1_onMouseAction
endButton2.onMouseAction = endButton1_onMouseAction
endButton3.onMouseAction = endButton1_onMouseAction
clearButton.onMouseAction = endButton1_onMouseAction

def nextButton1_onMouseAction(x, y, action):
    global badge1
    if badge1:
        scene4.enter()
        showMessage("밥도둑 메뉴는?")
    else:
        showMessage("이병 계급장이 필요합니다.")
nextButton1.onMouseAction = nextButton1_onMouseAction

def nextButton2_onMouseAction(x, y, action):
    scene6.enter()
    showMessage("정답! 군대에서 맛있는 메뉴란 존재하지 않는다.")
nextButton2.onMouseAction = nextButton2_onMouseAction

def nextButton3_onMouseAction(x, y, action):
    global badge2
    if badge2:
        scene7.enter()
        showMessage("일병인 나, 빨리 전역할 수 있는 방법은? hint : 병장이 되어라!")
    else:
        showMessage("일병 계급장이 필요합니다.")
nextButton3.onMouseAction = nextButton3_onMouseAction



def quizButton1_onMouseAction(x, y, action):
    showMessage("Q.복무 기간이 가장 긴 곳은?                                   1.육군  2.해군  3.공군")
quizButton1.onMouseAction = quizButton1_onMouseAction

def quizButton2_onMouseAction(x, y, action):
    showMessage("Q.훈련병들은 왜 훈련을 받고 있을까?                              1.아직 시간이 남아서  2.강한 군인이 되기 위해  3.누가 잘 못해서")
quizButton2.onMouseAction = quizButton2_onMouseAction


def badge1_onMouseAction(x, y, action):
    global badge1
    badgeList[0].pick()
    badge1 = True
    showMessage("이병 계급장을 얻었습니다.")
badgeList[0].onMouseAction = badge1_onMouseAction

def badge2_onMouseAction(x, y, action):
    global badge2
    badgeList[1].pick()
    badge2 = True
    showMessage("일병 계급장을 얻었습니다.")
badgeList[1].onMouseAction = badge2_onMouseAction

def badgeAdd_onMouseAction(x, y, action):
    badgeAdd.pick()
    showMessage("일병 계급장을 얻었습니다.")
badgeAdd.onMouseAction = badgeAdd_onMouseAction


def answerNumber1_1_onMouseAction(x, y, action):
    showMessage("오답!")
    scene0.enter()
answerNumber1[0].onMouseAction = answerNumber1_1_onMouseAction
answerNumber1[1].onMouseAction = answerNumber1_1_onMouseAction

def answerNumber1_3_onMouseAction(x, y, action):
    showMessage("정답!")
    scene2_1.enter()
answerNumber1[2].onMouseAction = answerNumber1_3_onMouseAction


def answerNumber2_1_onMouseAction(x, y, action):
    showMessage("오답!")
    scene0.enter()
answerNumber2[1].onMouseAction = answerNumber2_1_onMouseAction
answerNumber2[2].onMouseAction = answerNumber2_1_onMouseAction

def answerNumber2_3_onMouseAction(x, y, action):
    showMessage("정답!")
    scene3.enter()
answerNumber2[0].onMouseAction = answerNumber2_3_onMouseAction


def answerFood_onMouseAction(x, y, action):
    showMessage("오답!")
    scene5.enter()
answerFood1[0].onMouseAction = answerFood_onMouseAction
answerFood1[1].onMouseAction = answerFood_onMouseAction
answerFood1[2].onMouseAction = answerFood_onMouseAction
 
def tape_onMouseAction(x, y, action):
    showMessage("테이프를 얻었다!")
    tape.pick()
tape.onMouseAction = tape_onMouseAction

def goonbun_onMouseAction(x, y, action):
    global ownGoonbun
    ownGoonbun = True
    goonbun.pick()
    showMessage("군번줄을 얻었습니다.")
goonbun.onMouseAction = goonbun_onMouseAction

def cap_onMouseAction(x, y, action):
    global ownCap
    ownCap = True
    cap.pick()
    showMessage("전역모를 얻었습니다.")
cap.onMouseAction = cap_onMouseAction



def badgeMiddle_onCombine():
    showMessage("테이프가 필요해!")
badgeMiddle.onCombine = badgeMiddle_onCombine

def badgeFinal_onCombine():
    global badgeFinal
    badgeFinal = True
    showMessage("드디어 병장이 됐다!")
badgeList[2].onCombine = badgeFinal_onCombine

def completeButton_onMouseAction(x, y, action):
    global badgeFinal
    if badgeFinal and ownGoonbun and ownCap:
        scene9.enter()
        showMessage("전역을 축하합니다!")
    else:
        scene8.enter()
        showMessage("Game Over  (hint : 전역을 하기 위한 물품이 필요합니다.)")
completeButton.onMouseAction = completeButton_onMouseAction


def onEnter_scene1():
    scene1.sound.play(True)
scene1.onEnter = onEnter_scene1


def onEnter_scene4():
    scene1.sound.stop()
    scene4.sound.play(True)
scene4.onEnter = onEnter_scene4

def onEnter_scene7():
    scene4.sound.stop()
    scene7.sound.play(True)
scene7.onEnter = onEnter_scene7

def onEnter_scene9():
    scene7.sound.stop()
    scene9.sound.play(True)
scene9.onEnter = onEnter_scene9


def onEnter_scene0():
    scene1.sound.stop()
    scene0.sound.play(True)
scene0.onEnter = onEnter_scene0

def onEnter_scene5():
    scene4.sound.stop()
    scene5.sound.play(True)
scene5.onEnter = onEnter_scene5

def onEnter_scene8():
    scene7.sound.stop()
    scene8.sound.play(True)
scene8.onEnter = onEnter_scene8

startGame(scene1)
