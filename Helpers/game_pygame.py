import pygame
import sys

# Initialize pygame
pygame.init()

# Constants for grid size and cell size
GRID_SIZE = 3
CELL_SIZE = 100

# Create the window
WINDOW_SIZE = (GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Interactive Grid")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create a 3x3 grid
grid = [[" " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            if grid[row][col] == " ":
                grid[row][col] = "X"

    screen.fill(WHITE)

    # Draw the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            pygame.draw.rect(
                screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1
            )
            if grid[row][col] == "X":
                font = pygame.font.Font(None, 36)
                text = font.render("X", True, RED)
                screen.blit(
                    text,
                    (col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2, row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2),
                )

    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()
