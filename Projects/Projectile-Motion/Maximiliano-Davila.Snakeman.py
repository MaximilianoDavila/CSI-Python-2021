
from random import random, randrange
import pygame
import time
import random
pygame.init()


yellow = (255, 255, 102) #score
black = (0, 0, 0) #food
red = (213, 50, 80) #background color
green = (0, 255, 0) #snake
blue = (50, 153, 213) #game over

dis_width = 900
dis_height = 800

dis = pygame.display.set_mode((dis_width,dis_height))

pygame.display.set_caption('Snake game by JD')
game_over=False


snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None,30)

def message(mg, color):
    meg = font_style.render(mg, True, color)
    dis.blit(meg,[dis_width/4, dis_height/2])

def GameRestart():
    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    foodx = round(random.randrange(0, dis_width - snake_block) / 10) *10
    foody = round(random.randrange(0, dis_width - snake_block) / 10) *10


    while not game_over:

        while game_close == True:
            dis.fill(yellow)
            message("You have lost,try again. Press M-quit or l-Play again ", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_l:
                        GameRestart()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

      
        x1 += x1_change
        y1 += y1_change
        dis.fill(yellow)
        pygame.draw.rect(dis, black, [foodx, foody, snake_block, snake_block]) # crea el snake y lo ubica en la pantalla
        pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
        pygame.display.update()


        clock.tick(snake_speed)

# pygame.display.update()
# time.sleep(5)
    pygame.quit()
    quit()

GameRestart()