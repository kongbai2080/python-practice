import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
#	alien = Alien(ai_settings, screen)
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	while True:
		
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_aliens(aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()		
