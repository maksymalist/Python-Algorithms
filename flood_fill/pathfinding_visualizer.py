import pygame
import random
import time

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

GRID_X, GRID_Y = 30, 30

matrix = [[0 for x in range(GRID_X)] for y in range(GRID_Y)]


pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)


def draw_grid():
    block_size = 20
    for idx, x in enumerate(matrix):
        for idx2, y in enumerate(x):
            if y == 0:
                rect = pygame.Rect(idx*block_size, idx2*block_size,block_size, block_size)
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
            elif y == 1:
                rect = pygame.Rect(idx*block_size, idx2*block_size,block_size, block_size)
                pygame.draw.rect(SCREEN, RED, rect, 0)
            elif y == 2:
                rect = pygame.Rect(idx*block_size, idx2*block_size,block_size, block_size)
                pygame.draw.rect(SCREEN, BLUE, rect, 0)
            elif y == 3:
                rect = pygame.Rect(idx*block_size, idx2*block_size,block_size, block_size)
                pygame.draw.rect(SCREEN, GREEN, rect, 0)

def add_markers(x, y, x2, y2):
    matrix[x][y] = 3
    matrix[x2][y2] = 3


def draw_wall(x, y):
    matrix[x][y] = 1

def flood_fill(x ,y, old, new, update_matrix):
    print(x, y)
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
        return
    # secondly, check if the current position equals the old value
    if matrix[y][x] != old:
        update_matrix()
        return
    # thirdly, set the current position to the new value
    matrix[y][x] = new
    # fourthly, attempt to fill the neighboring positions
    flood_fill(x+1, y, old, new, update_matrix)
    flood_fill(x-1, y, old, new, update_matrix)
    flood_fill(x, y+1, old, new, update_matrix)
    flood_fill(x, y-1, old, new, update_matrix)

add_markers(random.randint(0, GRID_X-1), random.randint(0, GRID_Y-1), random.randint(0, GRID_X-1), random.randint(0, GRID_Y-1))

def main():
    global matrix
    key_down = False

    while True:
        draw_grid()
        pygame.display.flip()
        if key_down:
            pos = pygame.mouse.get_pos()
            x = pos[0] // 20
            y = pos[1] // 20
            draw_wall(x, y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                key_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                key_down = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    def update_matrix():
                        draw_grid()
                        pygame.display.flip()
                    flood_fill(0, 0, 0, 2, update_matrix)


if __name__ == '__main__':
    main()