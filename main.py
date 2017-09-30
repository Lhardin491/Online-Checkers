import pyglet

if __name__ == '__main__':
    window = pyglet.window.Window()
    label = pyglet.text.Label("Let\'s play a game!",
                               font_name='Times New Roman',
                               font_size=36,
                               x=window.width//2, y=window.height//2,
                               anchor_x='center', anchor_y='center')
    @window.event
    def on_draw():
        window.clear()
        label.draw()
    pyglet.app.run()

    @window.event
    def on_draw():
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glBegin(GL_TRIANGLES)
        glVertex2f(0, 0)
        glVertex2f(window.width, 0)
        glVertex2f(window.width, window.height)
        glEnd()   
