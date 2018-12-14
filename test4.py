import pyglet



window = pyglet.window.Window(800, 600)

image = pyglet.image.load('../picture/cham.jpg')
sprite = pyglet.sprite.Sprite(image,30,30)
background = pyglet.image.load('../picture/.jpg')
@window.event
def on_draw():
    window.clear()
    sprite.draw()



@window.event
def on_key_press(key,modifiers):
    if(key == pyglet.window.key.UP):
        sprite.y+=100
    elif(key == pyglet.window.key.DOWN):
        sprite.y-=100
    elif(key == pyglet.window.key.LEFT):
        sprite.x-=100
    elif(key == pyglet.window.key.RIGHT):
        sprite.x+=100

def loop_map():
    if()
    pass

@window.event
def on_mouse_press(x, y, button, modifiers):
  if button == mouse.LEFT:
    position['x'] = x
    position['y'] = y

pyglet.app.run()
