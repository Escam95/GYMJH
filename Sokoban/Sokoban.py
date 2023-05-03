import Constants as c
import pygame as pg
import pygame.image

pg.init()
window = pg.display.set_mode((c.LEVEL_WIDTH * c.TILE_SIZE, c.LEVEL_HEIGHT * c.TILE_SIZE))
clock = pg.time.Clock
image = pygame.image.load("Images/sokoban_tilesheet.png")
game_running = True

level = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 2, 1, 0, 2, 1, 2, 0, 1],
    [1, 2, 2, 1, 0, 2, 1, 2, 0, 1],
    [1, 2, 2, 1, 0, 2, 1, 2, 0, 1],
    [1, 2, 2, 1, 0, 2, 1, 2, 0, 1],
    [1, 2, 2, 1, 0, 2, 1, 2, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

position = (1, 2)
direction = 0

tiles = [
    (11, 6),
    (7, 6),
    (1, 0),
    (10, 5),
    (3, 4),
    (0, 6),
    (0, 4),
    (3, 6)
]


def game_input():
    global game_running
    for event in pygame.event.get():
        if event.type == pg.QUIT:
            game_running = False


def game_update():
    ...


def game_output():
    for y in range(0, c.LEVEL_HEIGHT):
        for x in range(0, c.LEVEL_WIDTH):
            draw_tile(0, x, y)
            tile = level[y][x]
            draw_tile(tile, x, y)
    draw_player()
    pg.display.flip()


def draw_tile(tile, x, y):
    pos = (x * c.TILE_SIZE, y * c.TILE_SIZE)
    tx, ty = tiles[tile]
    rectangle = (tx * c.TILE_SIZE, ty * c.TILE_SIZE, c.TILE_SIZE, c.TILE_SIZE)
    window.blit(image, pos, rectangle)


def draw_player():
    draw_tile(direction + 4, position[0], position[1])


while game_running:
    game_input()
    game_update()
    game_output()
