import sys
import random
import pygame
from pygame import mixer
from random import randrange
from helpers import gameOver, applePositionInside

pygame.init()
(width, height) = (1000, 800)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('snake')

pygame.display.flip()
sizeOfSquare = 32
(gameWidth, gameHeight) = (width // sizeOfSquare, height // sizeOfSquare)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
rainbow = ['RED', 'BLUE', 'PURPLE', 'GREEN']

snake = [[gameHeight // 2, gameWidth // 2]]
lengfSnake = 2
for i in range(lengfSnake):
    snake.append([(gameHeight // 2) + i, (gameWidth // 2) + i])
dir = 0
apple = [randrange(gameHeight), randrange(gameWidth)]

# pygame.display.update()
# clock = pygame.time.Clock()


mixer.init()

appleSound = mixer.Sound('eat_sound.mpga')
mixer.music.load('music.mp3')
mixer.music.set_volume(0.2)
mixer.music.play(-1)

fps = 60
delay = 2000000
count = 0
running = True

while running:
    if count != delay:
        count += 1
        continue
    count = 0
    print(snake[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and dir != 2:
                dir = 0
            elif event.key == pygame.K_d and dir != 3:
                dir = 1
            elif event.key == pygame.K_s and dir != 0:
                dir = 2
            elif event.key == pygame.K_a and dir != 1:
                dir = 3
    if dir == 0:
        snake.insert(0, [snake[0][0] - 1, snake[0][1]])
    elif dir == 1:
        snake.insert(0, [snake[0][0], snake[0][1] + 1])
    elif dir == 2:
        snake.insert(0, [snake[0][0] + 1, snake[0][1]])
    elif dir == 3:
        snake.insert(0, [snake[0][0], snake[0][1] - 1])
    if gameOver(snake[0][0], snake[0][1], gameHeight, gameWidth, snake):
        running = False
    if snake[0][0] == apple[0] and snake[0][1] == apple[1]:
        apple = applePositionInside(snake, gameHeight, gameWidth)

        # if apple spawn in snake spawn again
        appleSound.play()

    else:
        snake.pop()
    screen.fill((0, 0, 0))
    for snakePart in snake:
        pygame.draw.rect(screen, BLUE,
                         (snakePart[1] * sizeOfSquare, snakePart[0] * sizeOfSquare, sizeOfSquare, sizeOfSquare), 6)
    pygame.draw.rect(screen, RED,
                     (apple[1] * sizeOfSquare, apple[0] * sizeOfSquare, sizeOfSquare, sizeOfSquare))
    pygame.display.update()
