import pygame
import sys
import time
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


def get_coordinates(grid):
    x = -1
    y = -1
    container_list = []
    for row in grid:
        x += 1
        for value in row:
            y += 1
            if value == 1:
                container_list.append([y, x])
        y = -1
    return container_list

def list_of_lists_to_dict(input_list):
    result_dict = {}
    for y, row in enumerate(input_list):
        for x, item in enumerate(row):
            result_dict[(x, y)] = item
    return result_dict

def get_key(input_list):
    return tuple(input_list)

def findAdiacentValues(coordinates, var1, var2):
    try:
        adiacent_value = (coordinates[0] + var1, coordinates[1] + var2)

        if adiacent_value == 1:
            return adiacent_value
    except KeyError:
        adiacent_value = 0
    return adiacent_value

def simulate_conways_game(grid):
    list_of_coordinates = get_coordinates(grid)
    dic_grid = list_of_lists_to_dict(grid)

    for coordinates in list_of_coordinates:
        value1 = findAdiacentValues(coordinates, -1, 0)
        value2 = findAdiacentValues(coordinates, -1, -1)
        value3 = findAdiacentValues(coordinates, -1, 1)
        value4 = findAdiacentValues(coordinates, 0, -1)
        value5 = findAdiacentValues(coordinates, 0, 1)
        value6 = findAdiacentValues(coordinates, 1, 0)
        value7 = findAdiacentValues(coordinates, 1, -1)
        value8 = findAdiacentValues(coordinates, 1, 1)

        tot_values = value8 + value7 + value6 + value5 + value4 + value3 + value2 + value1

        if tot_values == 2 or tot_values == 3:
            dic_grid[get_key(coordinates)] = 1
        else:
            dic_grid[get_key(coordinates)] = 0

    return dic_grid

def dic_to_list_of_lists(input_dict):
    max_x = max(key[0] for key in input_dict)
    max_y = max(key[1] for key in input_dict)

    result = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    for key, value in input_dict.items():
        result[key[1]][key[0]] = value

    return result


while post_run:
    time.sleep(2)
    new_dic = simulate_conways_game(grid)
    grid = dic_to_list_of_lists(new_dic)
    draw_grid()

# Quit Pygame
for sublist in grid:
    print(f'{sublist},')
pygame.quit()
sys.exit()

