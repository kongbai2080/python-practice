import pygame

class Settings():
	def __init__(self):
		
		self.screen_width = 480#1550#480
		self.screen_height = 700
		
#		self.bg_color = (0, 0, 0)
		self.bg_image = pygame.image.load('images/background.png')
		
		self.ship_speed_factor = 0.5

		self.bullet_speed_factor = 1
		self.bullet_width = 5
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
		
		self.alien_speed_factor = 1

