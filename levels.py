
import pygame
import time
from PIL import Image
from camera import Camera
from entities import Entity, Player

TILESIZE = 32

class Level:

	def __init__(self, walls, portals, px, py):
		self.walls = walls
		self.portals = portals

		self.camera = Camera()
		self.player = Player(px, py, TILESIZE, TILESIZE)

		self.time = time.time()
		self.elapsed = 0

		self.font = pygame.font.SysFont(None, 24)

	def tick(self):
		self.elasped = round(time.time() - self.time)
		self.player.tick(self.walls)

	def draw(self, screen):
		ww, hh = pygame.display.get_window_size()

		for wall in self.walls:
			if (wall.x > self.camera.xx - TILESIZE and
                wall.y > self.camera.yy - TILESIZE and
				wall.x < self.camera.xx + ww and
				wall.y < self.camera.yy + hh):
					pygame.draw.rect(screen, (0, 0, 0), (
						wall.x - self.camera.xx,
						wall.y - self.camera.yy,
						wall.w,
						wall.h
					))

		self.player.draw(screen, self.camera)

		text = self.font.render(f'seconds: {self.elasped}', True, (0, 0, 0))
		screen.blit(text, (35, 35))

class LevelHandler:

	def __init__(self):
		self.levels = [
			self.load_level('level1')
		]
		self.index = 0

	def load_level(self, name):
		walls = []
		portals = []
		px = 0
		py = 0

		image = Image.open('levels/' + name + '.png', 'r')
		width, height = image.size
		rgb_image = image.convert('RGB')

		for y in range(height):
			for x in range(width):
				r, g, b = rgb_image.getpixel((x, y))
		
				# walls
				if r == 0 and g == 0 and b == 0:
					walls.append(Entity(
						x * TILESIZE,
						y * TILESIZE,
						TILESIZE,
						TILESIZE
					))

				# portals
				if r == 144 and g == 255 and b == 144:
					portals.append(Entity(
						x * TILESIZE,
						y * TILESIZE,
						TILESIZE,
						TILESIZE
					))

				# spawn
				if r == 255 and g == 0 and b == 0:
					px = x * TILESIZE
					py = y * TILESIZE

		return Level(walls, portals, px, py)

	def tick(self):
		self.levels[self.index].tick()

	def draw(self, screen):
		self.levels[self.index].draw(screen)
