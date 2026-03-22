"""
Manual Snake Game using Pygame

This script implements a classic Snake game where the player
controls the snake using arrow keys.

Project: AI Snake Game (Manual Mode)
"""

import pygame
import random
import sys
from pygame.locals import *

# -------------------------------
# Collision Detection Function
# -------------------------------
def collide(x1, x2, y1, y2, w1, w2, h1, h2):
    """
    Checks if two rectangles collide
    """
    return (x1 + w1 > x2 and x1 < x2 + w2 and
            y1 + h1 > y2 and y1 < y2 + h2)


# -------------------------------
# Game Over Function
# -------------------------------
def game_over(screen, score):
    """
    Displays final score and exits game
    """
    font = pygame.font.SysFont('Arial', 30)
    text = font.render(f'Your score was: {score}', True, (0, 0, 0))
    screen.blit(text, (10, 270))
    pygame.display.update()

    pygame.time.wait(2000)
    sys.exit(0)


# -------------------------------
# Initialize Game
# -------------------------------
pygame.init()

# Screen setup
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Snake initial position (body segments)
xs = [290, 290, 290, 290, 290]
ys = [290, 270, 250, 230, 210]

direction = 0  # 0=DOWN, 1=RIGHT, 2=UP, 3=LEFT
score = 0

# Apple position
apple_pos = (random.randint(0, 590), random.randint(0, 590))

# Snake and apple visuals
snake_block = pygame.Surface((20, 20))
snake_block.fill(RED)

apple_block = pygame.Surface((10, 10))
apple_block.fill(GREEN)

# Font and clock
font = pygame.font.SysFont('Arial', 20)
clock = pygame.time.Clock()


# -------------------------------
# Main Game Loop
# -------------------------------
while True:
    clock.tick(10)  # Control game speed

    # ---------------------------
    # Event Handling
    # ---------------------------
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != 0:
                direction = 2
            elif event.key == K_DOWN and direction != 2:
                direction = 0
            elif event.key == K_LEFT and direction != 1:
                direction = 3
            elif event.key == K_RIGHT and direction != 3:
                direction = 1

    # ---------------------------
    # Self Collision Check
    # ---------------------------
    for i in range(len(xs) - 1, 1, -1):
        if collide(xs[0], xs[i], ys[0], ys[i], 20, 20, 20, 20):
            game_over(screen, score)

    # ---------------------------
    # Apple Collision
    # ---------------------------
    if collide(xs[0], apple_pos[0], ys[0], apple_pos[1], 20, 10, 20, 10):
        score += 1
        xs.append(700)  # Add new segment off-screen
        ys.append(700)
        apple_pos = (random.randint(0, 590), random.randint(0, 590))

    # ---------------------------
    # Wall Collision
    # ---------------------------
    if xs[0] < 0 or xs[0] > 580 or ys[0] < 0 or ys[0] > 580:
        game_over(screen, score)

    # ---------------------------
    # Move Snake Body
    # ---------------------------
    for i in range(len(xs) - 1, 0, -1):
        xs[i] = xs[i - 1]
        ys[i] = ys[i - 1]

    # Move head
    if direction == 0:
        ys[0] += 20
    elif direction == 1:
        xs[0] += 20
    elif direction == 2:
        ys[0] -= 20
    elif direction == 3:
        xs[0] -= 20

    # ---------------------------
    # Drawing
    # ---------------------------
    screen.fill(WHITE)

    # Draw snake
    for i in range(len(xs)):
        screen.blit(snake_block, (xs[i], ys[i]))

    # Draw apple
    screen.blit(apple_block, apple_pos)

    # Draw score
    score_text = font.render(str(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()