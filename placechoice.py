import pygame
import sys
import random
import time
import pprint

pygame.init()
f = open("output.txt","a")

BLACK = (0,0,0)
main_bg = pygame.image.load("./img/back_ground/main_bg.jpg")
students = [
    None,
    pygame.image.load("./img/students/bok.png"),
    pygame.image.load("./img/students/bongme.png"),
    pygame.image.load("./img/students/doohong.png"),
    pygame.image.load("./img/students/drangonlim.png"),
    pygame.image.load("./img/students/honghaksa.png"),
    pygame.image.load("./img/students/kgarry.png"),
    pygame.image.load("./img/students/kke0402.png"),
    pygame.image.load("./img/students/tape3276.png"),
    pygame.image.load("./img/students/yoonchae.png"),
    pygame.image.load("./img/students/boss.png"),
    pygame.image.load("./img/students/capark.png"),
    pygame.image.load("./img/students/gangganggang.png"),
    pygame.image.load("./img/students/gardenlee.png"),
    pygame.image.load("./img/students/gugoeun.png"),
    pygame.image.load("./img/students/heonsukoon.png"),
    pygame.image.load("./img/students/jeongggyu.png"),
    pygame.image.load("./img/students/jingi.png"),
    pygame.image.load("./img/students/kanghh.png"),
    pygame.image.load("./img/students/kimyechon.png"),
    pygame.image.load("./img/students/maknae.png"),
    pygame.image.load("./img/students/onesang.png"),
    pygame.image.load("./img/students/psw9502.png"),
    pygame.image.load("./img/students/sojuhanjan.png"),
    pygame.image.load("./img/students/thearsenal.png"),
    pygame.image.load("./img/students/youjinnesang.png"),
]

students_name = [None, "복현우","최봉준","정두홍","임용구","홍성주","김재훈", 
                "김고은","김수민","윤채영","장유진","박선민","강경민",
                "이정원","구고운","장현수","정규영","김진기","강현후",
                "김예운","전온겸","김해인","박준영","강병규","김해수","손유진"]

start_button = pygame.image.load("./img/object/button.png")
start_button_click = pygame.image.load("./img/object/button_click.png")
stop_button = pygame.image.load("./img/object/stop.png")
stop_button_click = pygame.image.load("./img/object/stop_click.png")
main_button = pygame.image.load("./img/object/start.png")
main_button_click = pygame.image.load("./img/object/start_click.png")
title_bg = pygame.image.load("./img/object/title.png")
mua = pygame.image.load("./img/object/mua.png")
who_t = pygame.image.load("./img/object/who_t.png")

effect_bgm = [
    pygame.mixer.Sound("./bgm/casino_wheel.wav"),
    pygame.mixer.Sound("./bgm/bgm_2.wav"),
]

pocket_effet = [
    pygame.mixer.Sound("./bgm/pock_effet2.mp3"),
    pygame.mixer.Sound("./bgm/pocket_effet3.mp3"),
    pygame.mixer.Sound("./bgm/effect_pocket1.mp3"),
]

back_bgm = pygame.mixer.Sound("./bgm/victory.mp3")
go_monster = pygame.mixer.Sound("./bgm/go_monsternew2.mp3")
coin_bgm = pygame.mixer.Sound("./bgm/coin_bgm.mp3")
fight_monster = pygame.mixer.Sound("./bgm/fight_monster.mp3")

mid_lis = [(0,1),(0,4),(1,1),(1,4),(2,1),(2,4),(3,1),(3,4),(4,4)]

display = (1920,1080)
map_x = 6
map_y = 5

gameDisplay = pygame.display.set_mode(display)
pygame.display.set_caption("대전 2반 자리 바꾸기")
clock = pygame.time.Clock()
font_1 = pygame.font.SysFont("malgungothic",90)

place = [[0 for _ in range(map_x)] for _ in range(map_y)]
final = [[0 for _ in range(map_x)] for _ in range(map_y)]
place[0][1], place[0][3], place[4][0], place[4][1], place[4][2], place[4][3] = 8, -1, -1, -1, -1, -1

visited = [False for _ in range(len(students))]
len_v = len(visited)
visited[8] = True
visited[0] = True
class Button:  # 버튼
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()  # 마우스 좌표
        click = pygame.mouse.get_pressed()  # 클릭여부
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # 마우스가 버튼안에 있을 때
            gameDisplay.blit(img_act, (x_act, y_act))  # 버튼 이미지 변경
            if click[0] and action is not None:  # 마우스가 버튼안에서 클릭되었을 때
                time.sleep(0.2)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))

class Button_2:  # 버튼
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None, arg=()):
        mouse = pygame.mouse.get_pos()  # 마우스 좌표
        click = pygame.mouse.get_pressed()  # 클릭여부
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # 마우스가 버튼안에 있을 때
            gameDisplay.blit(img_act, (x_act, y_act))  # 버튼 이미지 변경
            if click[0] and action is not None:  # 마우스가 버튼안에서 클릭되었을 때
                time.sleep(0.2)
                action(arg)
        else:
            gameDisplay.blit(img_in, (x, y))

class Button_3:  # 버튼
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None, arg=(), arg_1=(), arg_2= ()):
        mouse = pygame.mouse.get_pos()  # 마우스 좌표
        click = pygame.mouse.get_pressed()  # 클릭여부
        if x + width > mouse[0] > x and y + height > mouse[1] > y:  # 마우스가 버튼안에 있을 때
            gameDisplay.blit(img_act, (x_act, y_act))  # 버튼 이미지 변경
            if click[0] and action is not None:  # 마우스가 버튼안에서 클릭되었을 때
                time.sleep(0.2)
                action(arg, arg_1, arg_2)
        else:
            gameDisplay.blit(img_in, (x, y))

def draw_place(i):
    pygame.mixer.stop()
    while True :
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mixer.get_busy() == False:
            effect_bgm[random.choice(range(2))].play()
        gameDisplay.blit(main_bg,(0,0))
        place_draw()
        y, x = random.choice(range(map_y)), random.choice(range(map_x)) 
        if place[y][x] != 0 :
            continue
        if i <= 9 and (y,x) in mid_lis:
            if x > 2 :
                gameDisplay.blit(students[i],(230*x+450,170*y+150))
            else :
                gameDisplay.blit(students[i],(230*x+180,170*y+150))
            Button_3(stop_button, 900, 880, 125, 100, stop_button_click, 900, 880, stop_place, i, y, x)
            pygame.display.update()
            clock.tick(20)
        elif i > 9 and ((y,x) not in mid_lis) :
            if x > 2 :
                gameDisplay.blit(students[i],(230*x+450,170*y+150))
            else :
                gameDisplay.blit(students[i],(230*x+180,170*y+150))
            Button_3(stop_button, 900, 880, 125, 100, stop_button_click, 900, 880, stop_place, i, y, x)
            pygame.display.update()
            clock.tick(20)
        else :
            continue


def stop_place(i, y, x):
    pygame.mixer.stop()
    coin_bgm.play()
    global place
    place[y][x] = i
    main()

def stop_student(i):
    pygame.mixer.stop()
    pocket_effet[random.choice(range(3))].play()
    stop = True
    txt = font_1.render(students_name[i], True, BLACK)
    image_choice = pygame.transform.scale(students[i],(300,300))
    while stop :
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(main_bg,(0,0))   
        place_draw()     
        gameDisplay.blit(image_choice,(818,450))
        gameDisplay.blit(txt,(828,730))
        Button_2(start_button, 840, 900, 250, 100, start_button_click, 840, 900, draw_place, i)
        pygame.display.update()
        clock.tick(20)

def choice():
    global visited
    choice = True
    pygame.mixer.stop()
    go_monster.play()
    while choice :
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        i = random.choice(range(1,26))
        if not visited[i] :
            visited[i] = True
            image_choice = pygame.transform.scale(students[i],(300,300))
            txt = font_1.render(students_name[i], True, BLACK)
            gameDisplay.blit(main_bg,(0,0))
            place_draw()        
            gameDisplay.blit(image_choice,(818,450))
            gameDisplay.blit(txt,(828,730))
            Button_2(stop_button, 900, 880, 125, 100, stop_button_click, 900, 880, stop_student, i)
            pygame.display.update()
            clock.tick(20)
            visited[i] = False
    
def place_draw():
    global place
    for y in range(map_y):
        for x in range(map_x):
            if place[y][x] > 0 :
                if x > 2 :
                    gameDisplay.blit(students[place[y][x]],(230*x+450,170*y+150))
                else :
                    gameDisplay.blit(students[place[y][x]],(230*x+180,170*y+150))
        
def check_over():
    global visited
    for i in range(len_v):
        if not visited[i] :
            return False
    else :
        return True

def game_over():
    for y in range(map_y):
        for x in range(map_x):
            if place[y][x] > 0 :
                final[y][x] = students_name[place[y][x]]
            else :
                final[y][x] = 'X X X'
    with open("output.txt","w", encoding='utf-8') as f :
        for i in range(len(final)) :
            f.write(final[i].__repr__())
            f.write('\n')
        f.close()

    tmr = 0
    while True:
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        tmr += 1
        gameDisplay.blit(main_bg,(0,0))
        place_draw()
        if tmr >= 10 :
            gameDisplay.blit(mua,(0,0))
        if tmr == 10 :
            fight_monster.play()
        # gameDisplay.blit(students[1],(410,150))
        # gameDisplay.blit(students[1],(180,320))
        pygame.display.update()
        clock.tick(10)

def main(): # 메인 게임 함수
    global visited
    tmr = 0 # 시간 관리 변수
    ck_over = check_over()
    if ck_over :
        game_over()
    while True:
        tmr += 1 # 매 시간 1초 증가
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(main_bg,(0,0))
        place_draw()
        # gameDisplay.blit(students[1],(410,150))
        # gameDisplay.blit(students[1],(180,320))
        Button(start_button, 840, 900, 250, 100, start_button_click, 840, 900, choice)
        pygame.display.update()
        clock.tick(20)

def menu():
    tmr = 0
    
    while True:
        tmr += 1 # 매 시간 1초 증가
        for event in pygame.event.get(): # 윈도운 X 누를 시 나오게끔
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if pygame.mixer.get_busy() == False:
            back_bgm.play()
        gameDisplay.blit(main_bg,(0,0))
        gameDisplay.blit(title_bg,(0,0))
        # gameDisplay.blit(students[1],(410,150))
        # gameDisplay.blit(students[1],(180,320))
        Button(main_button, 840, 900, 250, 100, main_button_click, 840, 900, main)
        pygame.display.update()
        clock.tick(20)

if __name__ == "__main__":
    menu()
