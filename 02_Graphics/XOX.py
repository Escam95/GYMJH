import pygame

BACKGROUND_COLOR = (120, 123, 125)
PIECE_COLOR = (160, 163, 165)
SQUARE_COLOR = (60, 63, 65)
SQUARE_HOVER_COLOR = (75, 78, 80)
BOARD_SIZE = 30
SQUARE_SIZE = 33

board = []
player = 0

for y in range(0, BOARD_SIZE, 1):
    row = []
    for x in range(0, BOARD_SIZE, 1):
        row.append(0)
    board.append(row)

current_square = (-1, -1)

window = pygame.display.set_mode((BOARD_SIZE*SQUARE_SIZE, BOARD_SIZE*SQUARE_SIZE))


def game_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEMOTION:
            on_mouse_motion(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            on_mouse_up()


def on_mouse_motion(event):
    global current_square
    mx, my = event.pos
    x = mx // SQUARE_SIZE
    y = my // SQUARE_SIZE
    current_square = (x, y)


def on_mouse_up():
    global player
    x, y = current_square
    if board[y][x] == 0:
        board[y][x] = player + 1
        player = (player + 1) % 2


def game_update():
    ...


def draw_x(x, y):
    pygame.draw.line(window, PIECE_COLOR, (x * SQUARE_SIZE + 4, y * SQUARE_SIZE + 4),
                     ((x + 1) * SQUARE_SIZE - 6, (y + 1) * SQUARE_SIZE - 6), 2)
    pygame.draw.line(window, PIECE_COLOR, ((x + 1) * SQUARE_SIZE - 6, y * SQUARE_SIZE + 4),
                     (x * SQUARE_SIZE + 4, (y + 1) * SQUARE_SIZE - 6), 2)


def draw_o(x, y):
    pygame.draw.circle(window, PIECE_COLOR, (
        x * SQUARE_SIZE + SQUARE_SIZE//2, y * SQUARE_SIZE + SQUARE_SIZE//2
    ), SQUARE_SIZE//2 - SQUARE_SIZE//8, 2)


def game_output():
    window.fill(BACKGROUND_COLOR)
    for y in range(0, BOARD_SIZE, 1):
        for x in range(0, BOARD_SIZE, 1):
            if current_square == (x, y):
                color = SQUARE_HOVER_COLOR
            else:
                color = SQUARE_COLOR
            pygame.draw.rect(window, color, (x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE - 2, SQUARE_SIZE - 2))
            if board[y][x] == 2:
                draw_x(x, y)
            if board[y][x] == 1:
                draw_o(x, y)
    pygame.display.flip()


while True:
    game_input()
    game_update()
    game_output()
