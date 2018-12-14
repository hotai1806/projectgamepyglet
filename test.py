# Global variables
import pyglet
window = pyglet.window.Window(800, 600)
label = pyglet.text.Label("123", font_size=45, y=400, x=400)

sprite = pyglet.sprite.Sprite(image)
car1 = pyglet.image.load("../picture/car.jpg")
car = pyglet.sprite.Sprite(car1)
# Event callbacks

# Game loop (loop? Why loop?)
def update(_):
    global score, lives, space, change
    print(score)
    if score == 0 and change == 0:
        smile_f.image = image_f
        getRandomDict(5)
        change = 1
    if score == 5 and change == 1:
        smile_f.image = image_f1
        changeSpeed(maindict['positive'] + maindict['negative'])
        getRandomDict(10)
        change = 2
    if score == 20 and change == 2:
        smile_f.image = image_f2
        changeSpeed(maindict['positive'] + maindict['negative'])
        getRandomDict(10)
        change = 0
    angle_radians = -math.radians(randint(200,201))
    force_x = math.sin(angle_radians)
    ok = sprite
    if space > 0 and lives > 0:
        for i in maindict['positive'] + maindict['negative']:
            temp = (i.x + i.x + i.width)/2
            left = smile_f.position[0]
            right = smile_f.position[0] + smile_f.width
            if i.y >= smile_f.height:
                if temp < -30:
                    i.x == width
                elif temp > height + 30:
                    i.x == 0
                i.x += force_x * i.rotation
                i.y -= i.velocity_y
            elif i.y < smile_f.height and i.y > -10:
                if temp > left and temp < right:
                        if i in maindict['positive']:
                            score += 1
                            sound2.play()
                            score_label.text="Score: %s" % score
                            i.y = height
                            clock.schedule_interval(callback, 3)
                            i.x = randint(0, width) + 30
                            if i.velocity_y < i.velocity_x:
                                i.velocity_y += randint(0,1)
                            elif i.velocity_y >= i.velocity_x:
                                i.velocity_y -= randint(0,1)
                        else:
                            if lives > 0:
                                lives -= 1
                            sound1.play()
                            live_label.text="Lives: %s" % lives
                            ok.x = 0
                            ok.y = 0
                            ok.batch = main_batch
                            i.y = height
                            clock.schedule_interval(callback, 5)
                            i.x = randint(0, width) + 30
                            if i.velocity_y < i.velocity_x:
                                i.velocity_y += randint(0,1)
                            elif i.velocity_y >= i.velocity_x:
                                i.velocity_y -= randint(0,1)
                else:
                    i.y -= i.velocity_y
            else:
                if lives == 0:
                    i.y = -100
                else:
                    i.y = height
                    i.x = randint(0, width) + 30
                    if i.velocity_y < i.velocity_x:
                        i.velocity_y += randint(0,1)
                    elif i.velocity_y >= i.velocity_x:
                        i.velocity_y -= randint(0,1)
                        i.rotation = random.choice([1,-1])


@window.event
def on_draw():
    window.clear()
    label.draw()
    sprite.draw()
    sprite.uppdate(car)

pyglet.clock.schedule(game_loop)
pyglet.app.run()
