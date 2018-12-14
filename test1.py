import pyglet

import random
from pyglet.window import key

window = pyglet.window.Window(width=1000, height=600)
megaman = pyglet.resource.image('2.png')
megaman.anchor_x = megaman.width // 2
megaman.anchor_y = 0

ball = pyglet.resource.image('fire.png')
ball.anchor_x = ball.width // 2
ball.anchor_y = ball.height


class Game(object):
    def __init__(self):
        self.megaman_x = window.width // 2
        self.megaman_y = 0
        self.ball_x = window.width // 2
        self.ball_y = window.height
        self.score = 0
        self.gameover = False


game = Game()

score_label = pyglet.text.Label(str(game.score),
                                x=window.width // 2, # origin - left
                                y=window.height // 2, # origin - bottom
                                anchor_x='center',
                                anchor_y='center')


@window.event
def on_key_press(motion, modifiers):
    if motion == key.MOTION_RIGHT:
        game.megaman_x += 10
    if motion == key.MOTION_LEFT:
        game.megaman_x -= 10



@window.event
def on_draw():
    if not game.gameover:
        window.clear()
        megaman.blit(game.megaman_x, game.megaman_y)
        ball.blit(game.ball_x, game.ball_y)
        score_label.text = str(game.score)
        score_label.draw()
    else:
        window.clear()
        score_label.text = 'Game Over\nScore: %d' % game.score
        score_label.draw()

def ball_drop(dt):
    # if colision?
    if abs(game.ball_x - game.megaman_x) < 30 and abs(game.ball_y -
            game.megaman_y) < 30:
        game.gameover = True
        return

    # if we need to reset the ball?
    if game.ball_y <= 10:
        game.ball_x = random.randint(0, window.width)
        game.ball_y = window.height
        game.score += 1
    else:
        game.ball_y -= 3



pyglet.clock.schedule(ball_drop)
pyglet.app.run()
