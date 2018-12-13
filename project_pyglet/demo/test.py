# Global variables
import pyglet
window = pyglet.window.Window(800, 600)
label = pyglet.text.Label("123", font_size=45, y=400, x=400)
image = pyglet.image.load('../picture/maxresdefault.jpg')
sprite = pyglet.sprite.Sprite(image)
car1 = pyglet.image.load("../picture/car.jpg")
car = pyglet.sprite.Sprite(car1)
# Event callbacks


# Game loop (loop? Why loop?)
def game_loop(_):
    label.text = str(int(label.text) + 1)

def update(dt):
    fenetre.push_handlers(keys)
    left = keys[pyglet.window.key.LEFT]
    right = keys[pyglet.window.key.RIGHT]
    up = keys[pyglet.window.key.UP]
    down = keys[pyglet.window.key.DOWN]
    if up and down:
        None
    elif up:
        fusee.y += (dt * 100)
    elif down:
        fusee.y -= dt * 100
    if right and left:
        None
    elif right:
        fusee.rotation += dt * 300
    elif left:
        fusee.rotation -= dt * 300


@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()
    sprite.uppdate(car)

pyglet.clock.schedule(game_loop)
pyglet.app.run()
