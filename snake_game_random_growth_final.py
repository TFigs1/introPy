#Video Demonstrating Code
# https://www.youtube.com/watch?v=0x6pdK3fwLk #

import pygame
import time
import random

pygame.init()

# Constants
window_width = 600
window_height = 400
snake_block = 10
snake_speed = 15

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Create the game window
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont(None, 35)
game_over_font = pygame.font.SysFont(None, 75)

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    value = font.render("Your Score: " + str(score), True, white)
    game_window.blit(value, [0, 0])

# Function to display "Game Over" message
def game_over_message():
    over_msg = game_over_font.render("Game Over", True, red)
    game_window.blit(over_msg, [window_width / 6, window_height / 3])
    Your_score(snake_length - 1)
    pygame.display.update()
    time.sleep(2)

# Main game loop
def gameLoop():
    global game_over
    global game_close

    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2

    # Initial movement direction
    x1_change = 0
    y1_change = 0

    # Initial snake length
    snake_length = 1

    # List to store the coordinates of the snake
    snake_list = []

    # Initial food position
    foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_window.fill(black)
            game_over_message()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(black)
        pygame.draw.rect(game_window, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # If the length of the snake exceeds, delete the first element
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(snake_length - 1)

        pygame.display.update()

        # If the snake eats the food, generate a new food position
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, window_height - snake_block) / 10.0) * 10.0
            snake_length += random.randint(1, 40)  # Randomly increase snake length

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game loop
gameLoop()

