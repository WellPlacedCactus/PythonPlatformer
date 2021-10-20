
'''

Nathan Vu
April 2021

- pip install pygame
- pip install Pillow

'''

import pygame
from levels import LevelHandler

class Game:

	def __init__(self):
		
		pygame.init()
		pygame.display.set_caption('PyPlatformer')

		self.screen = pygame.display.set_mode([1280, 720])

		self.fps_clock = pygame.time.Clock()
		self.running = True

		self.level_handler = LevelHandler()
		self.loop()

	def tick(self):
		self.level_handler.tick()

	def draw(self):
		self.screen.fill((255, 255, 255))
		self.level_handler.draw(self.screen)
		pygame.display.flip()

	def loop(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						self.running = False

			self.tick()
			self.draw()
			self.fps_clock.tick(60)

		pygame.quit()


if __name__ == '__main__':
	Game()
