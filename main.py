import pygame

import random



# Initialize Pygame

pygame.init()



# Define some colors

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

GRAY = (128, 128, 128)

RED = (255, 0, 0)

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)



# Set the width and height of the screen

SCREEN_WIDTH = 400

SCREEN_HEIGHT = 600

BLOCK_SIZE = 30  # The size of each block in the game



# Create the screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



# Set the caption of the window

pygame.display.set_caption('Tetris')



# Create the font to display text

font = pygame.font.SysFont("arial", 24)



# Define the game board

board_width = 10

board_height = 20

board = [[0] * board_width for i in range(board_height)]



# Define the shapes of the blocks

shapes = [

    [[1, 1, 1], [0, 1, 0]],

    [[2, 2], [2, 2]],

    [[0, 3, 3], [3, 3, 0]],

    [[4, 4, 0], [0, 4, 4]],

    [[5, 5], [5, 5]],

    [[6, 0], [6, 6], [0, 6]],

    [[0, 7], [7, 7], [7, 0]],

]

colors = [GREEN, BLUE, RED, GRAY, WHITE, BLUE, RED]



# Define the current block

current_shape = random.choice(shapes)

current_x = board_width // 2 - len(current_shape[0]) // 2

current_y = 0

current_color = random.choice(colors)



# Define the score and level

score = 0

level = 1



# Define the game loop

clock = pygame.time.Clock()

game_over = False

while not game_over:



    # Handle events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            game_over = True



    # Move the current block down

    current_y += 1



    # Check for collisions with the game board

    for i in range(len(current_shape)):

        for j in range(len(current_shape[0])):

            if current_shape[i][j] != 0 and (current_y + i >= board_height or board[current_y + i][current_x + j] != 0):

                # Lock the block in place

                for i2 in range(len(current_shape)):

                    for j2 in range(len(current_shape[0])):

                        if current_shape[i2][j2] != 0:

                            board[current_y + i2 - 1][current_x + j2] = current_color



                # Check for completed rows and remove them

                complete_rows = 0

                for i in range(board_height):

                    if all(board[i]):

                        board.pop(i)

                        board.insert(0, [0] * board_width)

                        complete_rows += 1



                # Update the score based on the number of completed rows

                if complete_rows == 1:

                    score += 100

                elif complete_rows == 2:

                    score += 200

                elif complete_rows == 3:

                    score += 300

                elif complete_rows == 4:

                    score += 400



                # Increase the level if the score is high enough

                if score >= level * 1000:

                    level += 1



                # Choose a new block

                current_shape = random.choice(shapes)

                current_x = board_width // 2 - len(current_shape[0]) // 2

                current_y = 0

                current_color = random.choice(colors)



    # Draw the game board

    screen.fill(BLACK)

    for i in range(board_height):

        for j in range(board_width):

            if board[i][j] != 0:

                pygame.draw.rect(screen, colors[board[i][j] - 1], (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))



    # Draw the current block

    for i in range(len(current_shape)):

        for j in range(len(current_shape[0])):

            if current_shape[i][j] != 0:

                pygame.draw.rect(screen, current_color, ((current_x + j) * BLOCK_SIZE, (current_y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))



    # Draw the score and level

    score_text = font.render(f"Score: {score}", True, WHITE)

    screen.blit(score_text, (10, SCREEN_HEIGHT - 50))

    level_text = font.render(f"Level: {level}", True, WHITE)

    screen.blit(level_text, (SCREEN_WIDTH - 100, SCREEN_HEIGHT - 50))



    # Update the screen

    pygame.display.flip()



    # Set the framerate

    clock.tick(level * 2)



# Quit Pygame

pygame.quit()
