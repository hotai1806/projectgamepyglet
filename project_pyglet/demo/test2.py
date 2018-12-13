import pyglet

# Create and open a window
window = pyglet.window.Window(200, 200)

# Load sprites
s0 = pyglet.resource.image('01.jpg')
s1 = pyglet.resource.image('02.jpg')
sprites = [s0, s1]

# Animation
anim = pyglet.image.Animation.from_image_sequence(sprites, 0.5, True)
sprite = pyglet.sprite.Sprite(anim)

@window.event
def on_draw():
  window.clear()
  sprite.draw()

if __name__ == '__main__':
  pyglet.app.run()
