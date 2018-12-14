import pyglet
from pyglet.window import key
window = pyglet.window.Window(900, 600)
class GameObject:
	def __init__(self, posx, posy, image = None):
		self.posx = posx
		self.posy = posy
		if image is not None:
			image = pyglet.image.load("../demo/" + image)
			self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y=self.posy)
	def draw(self):
		self.sprite.draw()




label = pyglet.text.Label('Welcomtomydeath')
player = GameObject(100, 100, "fire.png")
background = GameObject(-100, 1, "Game.jpg")
button_sprite = GameObject(135, 0, "pokemon-go-2.png")
opengaming = GameObject(-100,1,"asd.jpg")

open = False

@window.event
def on_draw():
		window.clear()
		background.sprite.draw()
		player.sprite.draw()

		button_sprite.draw()
maindict = {}
# def getRandomDict(number):
# 	global maindict
# 	maindict
	# enemy_list = []
	# for i in range(5):
	# 	enemy_list.append()
# @window.event
# def update(dt):
# 	player.sprite.x += 5*dt
# 	player.sprite.y += 5*dt


@window.event
def on_key_press(motion, modifiers):
	if motion == key.MOTION_RIGHT:
		player.sprite.x += 50
	if motion == key.MOTION_LEFT:
		player.sprite.x -= 50
	if motion == key.MOTION_UP:
		player.sprite.y += 50
	if motion == key.MOTION_DOWN:
	    player.sprite.y -= 50




def main():


	pyglet.app.run()

main()
#from pyglet.window import mouse

#@window.event
#def on_mouse_press(x, y, button, modifiers):
#    if button == mouse.LEFT:
#        print 'The left mouse button was pressed.'

# image = pyglet.image.load('cursor.png')
# cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
# window.set_mouse_cursor(cursor)
