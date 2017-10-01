import pyglet
from pyglet.gl import *
from math import degrees, cos, sin
from board import *
from gamestate import *

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
BOARD_SIZE = 640
BOARD_OFFSET_X = (WINDOW_WIDTH - BOARD_SIZE) // 2
BOARD_OFFSET_Y = (WINDOW_HEIGHT - BOARD_SIZE) // 2
SQUARE_SIZE = BOARD_SIZE // 8
CHECKER_RADIUS = (SQUARE_SIZE - 10) // 2

config = pyglet.gl.Config(alpha_size=8, double_buffer=True)
window = pyglet.window.Window(config=config, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
state = GameState()

@window.event
def on_draw():
    window.clear()
    draw_board()
    for checker in state.get_checkers():
        draw_checker(checker.x, checker.y, checker.color)
    for coordinate in state.get_ghosts():
        draw_checker(coordinate[0], coordinate[1], "red", ghost=True)

def draw_board():
    for i in range(8):
        for j in range(8):
            color = (170, 30, 30) if (i + j) % 2 == 1 else (30, 30, 30)
            draw_square((i * SQUARE_SIZE) + BOARD_OFFSET_X, (j * SQUARE_SIZE) + BOARD_OFFSET_Y, SQUARE_SIZE, SQUARE_SIZE, *color)

def draw_square(x, y, w, h, r, g, b):
     pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (x, y,
                 x + w, y,
                 x + w, y + h,
                 x, y + h))
        ,('c3B', [r, g, b] * 4)
        ) 

def draw_checker(x, y, color, ghost=False):
    draw_x, draw_y = board_to_screen(x, y) 
    if ghost:
        draw_color = (255, 255, 255)
    elif color == 'red':
        draw_color = (255, 0, 0)
    elif color == 'black':
        draw_color = (70, 70, 70)

    draw_circle(draw_x, draw_y, CHECKER_RADIUS, draw_color)

def screen_to_board(x, y):
    board_x = (x - BOARD_OFFSET_X) // SQUARE_SIZE
    board_y = (y - BOARD_OFFSET_Y) // SQUARE_SIZE
    return (board_x, board_y)

def board_to_screen(board_x, board_y):
    x = (board_x * SQUARE_SIZE + BOARD_OFFSET_X) + (SQUARE_SIZE // 2)
    y = (board_y * SQUARE_SIZE + BOARD_OFFSET_Y) + (SQUARE_SIZE // 2)
    return (x, y)

def draw_circle(x, y, r, color):
    verticies = [x, y]
    for theta in range(360):
        verticies.append(int(x + (r * cos(degrees(theta)))))
        verticies.append(int(y + (r * sin(degrees(theta)))))

    pyglet.graphics.draw(len(verticies) // 2, pyglet.gl.GL_TRIANGLE_FAN, ('v2i', verticies), ('c3B', [*color] * (len(verticies) // 2)))


@window.event
def on_mouse_release(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        board_x, board_y = screen_to_board(x, y)
        print("{}, {}".format(board_x, board_y))
        if 0 <= board_x < 8 and 0 <= board_y < 8:
            state.gen_valid_moves(board_x, board_y)


pyglet.app.run()
