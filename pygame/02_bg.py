# -*- coding: utf-8 -*-
import pygame
pygame.init()
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))
#타이틀 제목

pygame.display.set_caption("똥(율)피하기-코드플레이")
 
#ㅇㅁㅈ불러오기
bg = pygame.image.load("pygame/source/bg.png")

#이벤트루프-종료까지대기
running = True #실행중인지확인
while running:
    for event in pygame.event.get():  #키마이벤트를 계속확인
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))
    pygame.display.update()
# 종료
pygame.quit()