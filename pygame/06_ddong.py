# -*- coding: utf-8 -*-
import pygame
import random
pygame.init()
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥(율)피하기-코드플레이")

clock = pygame.time.Clock()

bg = pygame.image.load("pygame/source/bg.png")

character = pygame.image.load("pygame/source/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xPos = (screen_width / 2) - (character_width / 2)
character_yPos = screen_height - character_height
to_x = 0
# to_y = 0

enemy = pygame.image.load("pygame/source/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xPos = random.randint(0, (screen_width - enemy_width))
enemy_yPos = 0

enemy_speed = 1


running = True 
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:      
                to_x -= 1
            # elif event.key == pygame.K_DOWN:
            #     to_y += 1
            elif event.key == pygame.K_RIGHT:
                to_x += 1
            # elif event.key == pygame.K_UP:
            #     to_y -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            # elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            #     to_y = 0

    character_xPos += to_x * dt
    # character_yPos += to_y * dt

    if character_xPos < 0:
        character_xPos = 0
    elif character_xPos > screen_width - character_width:
        character_xPos = screen_width - character_width

    if character_yPos < 0:
        character_yPos = 0
    elif character_yPos > screen_height - character_height:
        character_yPos = screen_height - character_height

    enemy_yPos += enemy_speed
    if enemy_yPos > screen_height:
        enemy_yPos = enemy_height * -1
        enemy_xPos = random.randint(0, (screen_width - enemy_width))
        enemy_speed = random.randint(5, 15)

    character_rect = character.get_rect()
    character_rect.left = character_xPos
    character_rect.top = character_yPos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xPos
    enemy_rect.top = enemy_yPos     

    if character_rect.colliderect(enemy_rect):
        print("충돌! 충돌!(박율은못생김 ㄹㅇㅋㅋㄹㅃㅃ)") #   박율은 못생김 ㄹㅇㅋㅋㄹㅃㅃ
        running = False

    screen.blit(bg, (0, 0))
    screen.blit(character, (character_xPos, character_yPos))
    screen.blit(enemy, (enemy_xPos, enemy_yPos))

    pygame.display.update()

# 종료
pygame.quit()