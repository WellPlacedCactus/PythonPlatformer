
import pygame

class Camera():

	def __init__(self):
		self.xx = 0
		self.yy = 0

	def focus(self, ent):
		ww, hh = pygame.display.get_window_size()

		self.xx += (ent.x - self.xx - (ww - ent.w) / 2) / 10
		self.yy += (ent.y - self.yy - (hh - ent.h) / 2) / 10
