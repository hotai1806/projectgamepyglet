import pyglet
window = pyglet.window.Window()
counter=.0

def load_anim():
    arrImages=[]
    for i in range(4):
        tmpImg=pyglet.resource.image("car"+str(i)+".png")
        arrImages.append(tmpImg)
    return arrImages

def update_frames(dt):
    global counter
    counter=(counter+dt)%2

@window.event
def on_draw():
    print( counter)
    pyglet.gl.glClearColor(0,0,0,0)
    window.clear()
    frames[int(counter)].blit(00,20,0,
                              frames[int(counter)].width,
                              frames[int(counter)].height)


frames = load_anim()
pyglet.clock.schedule_interval(update_frames,1/10.0)
pyglet.app.run()

sprite = pyglet.sprite.Sprite(image)
sprite.dx = 10.0

def update(dt):
    sprite.x += sprite.dx * dt
pyglet.clock.schedule_interval(update, 1/60.0)
