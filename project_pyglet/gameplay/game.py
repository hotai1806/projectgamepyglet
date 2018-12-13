# Global variables
import pyglet
window = pyglet.window.Window(800, 600)
label = pyglet.text.Label("0", font_size=45, y=400, x=400)
image = pyglet.image.load('../picture/maxresdefault.jpg')
sprite = pyglet.sprite.Sprite(image)

# Event callbacks
@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()

# Game loop (loop? Why loop?)
def game_loop(_):
    label.text = str(int(label.text) + 1)

pyglet.clock.schedule(game_loop)
pyglet.app.run()
