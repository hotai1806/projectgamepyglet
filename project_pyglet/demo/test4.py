import pyglet



window = pyglet.window.Window(800, 600)

image = pyglet.image.load('../picture/cham.jpg')
sprite = pyglet.sprite.Sprite(image,30,30)

@window.event
def on_draw():
    window.clear()
    sprite.draw()



@window.event
def on_key_press(key,modifiers):
    if(key == pyglet.window.key.UP):
        sprite.y+=10
    elif(key == pyglet.window.key.DOWN):
        sprite.y-=10
    elif(key == pyglet.window.key.LEFT):
        sprite.x+=10
    elif(key == pyglet.window.key.RIGHT):
        sprite.x-=10
pyglet.app.run()
