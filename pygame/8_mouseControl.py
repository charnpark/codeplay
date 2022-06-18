# -*- coding: utf-8 -*-
from turtle import circle

from pygame import MOUSEMOTION
import pygame

######################################################
# 파이게임 초기설정 (반드시 초기에 세 해야하는것)
pygame.init()

#화면크기 설정
screen_width = 480 # 가로크기
screen_height = 640 # 세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 (GUI 제목창)
pygame.display.set_caption("마우스컨트롤")

#오브젝트 그리기
circleX_pos = 0
circleY_pos = 0

sound_a = pygame.mixer.Sound("pygame/source/A Bass.wav")
sound_b = pygame.mixer.Sound("pygame/source/A Elec Bass.wav")
sound_c = pygame.mixer.Sound("pygame/source/Pop.wav")

#FPS
clock = pygame.time.Clock()
########################################################    
# 1.사용자가 추가하는 내용물들 초기화 (배경, 스프라이트, 좌표, 속도, 폰트, 시간 등)



#이벤트 반복 시작 - 스크래치의 무한반복과 같음
running = True #실행중인지 확인
while running:
    dt = clock.tick(60) #게임화면이 초당 리프레시되는 횟수

    #2 이벤트 처리(키보드 마우스 등 화면조작 관련)
    for event in pygame.event.get(): #키마 이벤트를 지속적으로 체크
        if event.type == pygame.QUIT: #창닫는 이벤트
            running = False

        if event.type == pygame.MOUSEMOTION:
            print ("mouseMotion")
            print(pygame.mouse.get_pos())
            circleX_pos, circleY_pos = pygame.mouse.get_pos()
            screen.fill((11, 55, 26))
            pygame.draw.circle(screen, (255, 0, 255), (circleX_pos, circleY_pos), 10)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print ("버튼을 누르셧습니다")
            print(pygame.mouse.get_pos())
            print(event.button)
            if event.button == 1:
                print("좌클")
                sound_a.play()
            elif event.button == 3:
                print("우클")
                sound_b.play()
            elif event.button == 3:
                print("휠클")
                sound_c.play()
            elif event.button == 3:
                print("휠업")
            elif event.button == 3:
                print("휠다운")

        if event.type == pygame.MOUSEBUTTONUP:
            print("mouseMotion")
            pass

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌처리

    # 5. 화면에그리기
    pygame.display.update() # 게임화면을 새로고침해줌.

#종료시간  살짝 늦추기
pygame.time.delay(2000)

#종료하기
pygame.quit()