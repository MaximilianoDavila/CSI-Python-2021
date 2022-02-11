
import pygame
pygame.init()


yellow = (255, 255, 102) #score
black = (0, 0, 0) #food
red = (213, 50, 80) #background color
green = (0, 255, 0) #snake
blue = (50, 153, 213) #game over

dis = pygame.display.set_mode((900, 800))

pygame.display.set_caption('Snake game by JD')
game_over=False

x1 = 400
y1 = 400

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                 x1_change = 10
                 y1_change = 0
            elif event.key == pygame.K_UP:
                 x1_change = 0
                 y1_change = -10
            elif event.key == pygame.K_DOWN:
                 x1_change = 0
                 y1_change = 10
    x1 += x1_change
    y1 += y1_change
    dis.fill(yellow)
    pygame.draw.rect(dis, blue, [x1, y1, 10, 10]) # crea el snake y lo ubica en la pantalla
    pygame.display.update()


    clock.tick(30)
pygame.quit()
quit()