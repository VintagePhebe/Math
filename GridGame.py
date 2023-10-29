import pygame
import sys

# Define grid parameters
GRID_WIDTH, GRID_HEIGHT = 18, 18  # Number of cells in each dimension
CELL_SIZE = 50  # Size of each cell in pixels
GRID_SIZE = GRID_WIDTH, GRID_HEIGHT

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)  # Gray color for grid lines

# Initialize Pygame
pygame.init()

# Create the screen
SCREEN_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Grid with Two States")

# Create a 2D array to represent the grid states (0 and 1)
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Variable to track post-run state
post_run = False

# Font settings for coordinate labels
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # Draw the grid cell
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE if grid[x][y] == 1 else BLACK, cell_rect)

            # Draw grid lines (thin gray lines)
            pygame.draw.rect(screen, GRAY, cell_rect, 1)

            # Draw X and Y coordinate labels (progressive numbers)
            x_label = font.render(str(x), True, WHITE)
            screen.blit(x_label, (x * CELL_SIZE + CELL_SIZE // 2 - 10, GRID_HEIGHT * CELL_SIZE - 20))
            y_label = font.render(str(y), True, WHITE)
            screen.blit(y_label, (GRID_WIDTH * CELL_SIZE - 20, y * CELL_SIZE + CELL_SIZE // 2 - 10))

# Main game loop
running = True
drawing = True  # Set to True initially
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not post_run:
            if event.button == 1:  # Left mouse button
                x, y = event.pos
                x //= CELL_SIZE
                y //= CELL_SIZE
                grid[x][y] = 1 - grid[x][y]  # Toggle the cell state
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            post_run = True  # Disable interaction

    screen.fill(BLACK)
    draw_grid()
    pygame.display.flip()


def add_newlines(input_list, num_newlines):
    # Create a new list containing num_newlines number of zeros
    newline = [0] * len(input_list[0])

    # Create a new list with the original content and the newlines
    result = input_list[:]
    for _ in range(num_newlines):
        result.append(newline[:])

    return result

# Quit Pygame
for sublist in grid:
    print(f'{sublist},')
pygame.quit()
sys.exit()

