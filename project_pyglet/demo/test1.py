import pyglet

# Create and open a window
window = pyglet.window.Window(200, 200)



fusee_img = pyglet.image.load('../picture/parallax-mountain-mountains.png')
fusee_img.anchor_x = fusee_img.width
fusee_img.anchor_y = fusee_img.height
fusee = pyglet.sprite.Sprite(fusee_img, x=100, y=100)

keys = pyglet.window.key.KeyStateHandler()
def update(dt):
    # Move 10 pixels per second
    sprite.x += dt * 10

# Call update 60 times a second
pyglet.clock.schedule_interval(update, 1/60.)

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



pyglet.clock.schedule_interval(update, 1 / 120.0)
#
def pos_image(image, x,y):
   """Sets an image's anchor point to its center"""
   image.anchor_x = x
   image.anchor_y = y
pos(player_image,player_image.width//2,)

@fenetre.event
def on_draw():
    fenetre.clear()
    fusee.draw()


pyglet.app.run()
