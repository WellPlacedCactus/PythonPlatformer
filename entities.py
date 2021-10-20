
import pygame

class Entity:

	def __init__(self, x, y, w, h):
		self.xxx = x
		self.yyy = y

		self.x = x
		self.y = y
		self.w = w
		self.h = h


class Player(Entity):

	def __init__(self, x, y, w, h):
		super().__init__(x, y, w, h)

		self.vx = 0
		self.vy = 0
		self.vm = 10
		self.acc = 1

		self.cj = False
		self.jp = 17

	def inp(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_LEFT]:
			self.vx -= self.acc
			if self.vx < -self.vm:
				self.vx = -self.vm
		else:
			if self.vx < 0:
				self.vx += self.acc
				if self.vx > 0:
					self.vx = 0

		if keys[pygame.K_RIGHT]:
			self.vx += self.acc
			if self.vx > self.vm:
				self.vx = self.vm
		else:
			if self.vx > 0:
				self.vx -= self.acc
				if self.vx < 0:
					self.vx = 0

		if keys[pygame.K_UP] or keys[pygame.K_LCTRL]:
			if self.cj:
				self.cj = False
				self.vy -= self.jp

		if keys[pygame.K_r]:
			self.vx = 0
			self.vy = 0
			self.x = self.xxx
			self.y = self.yyy
			self.cj = False

	def movex(self, walls):
		self.x += self.vx

		for wall in walls:
			if self.collision(self, wall):
				if self.vx < 0:
					if self.x < wall.x + wall.w:
						self.vx = 0
						self.x = wall.x + wall.w
				if self.vx > 0:
					if self.x > wall.x - self.w:
						self.vx = 0
						self.x = wall.x - self.w

	def movey(self, walls):
		self.vy += 1
		self.y += self.vy

		ww, hh = pygame.display.get_window_size()

		for wall in walls:
			if self.collision(self, wall):
				if self.vy < 0:
					if self.y < wall.y + wall.h:
						self.vy = 0
						self.y = wall.y + wall.h
				if self.vy > 0:
					if self.y > wall.y - self.h:
						self.vy = 0
						self.y = wall.y - self.h
						self.cj = True

	def tick(self, walls):
		self.inp()
		self.movex(walls)
		self.movey(walls)

	def draw(self, screen, camera):
		camera.focus(self)
		pygame.draw.rect(screen, (144, 255, 144), (
			self.x - camera.xx,
			self.y - camera.yy,
			self.w, self.h))

	def collision(self, r1, r2):
		if (r1.x < r2.x + r2.w and
			r1.x + r1.w > r2.x and
			r1.y < r2.y + r2.h and
			r1.y + r1.h > r2.y):
			return True
		else:
			return False

