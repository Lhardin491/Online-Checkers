import pyglet
from pyglet.gl import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
BOARD_SIZE = 640

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

@window.event
def on_draw():
    window.clear()
    draw_board()

def draw_board():
    for i in range(12):
        for j in range(12):
            scale = BOARD_SIZE // 8
            draw_square(i * scale, j * scale, scale, scale, 255 if (i + j) % 2 == 1 else 0, 0, 0)

def draw_square(x, y, w, h, r, g, b):
     pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
        [0, 1, 2, 0, 2, 3],
        ('v2i', (x, y,
                 x + w, y,
                 x + w, y + h,
                 x, y + h))
        ,('c3B', (r, g, b, r, g, b, r, g, b, r, g, b))
        ) 

pyglet.app.run()
