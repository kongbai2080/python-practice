import sys

import pygame

def check_keydown_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
		print(event.key)#12-4
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
		print(event.key)#12-4
	elif event.key == pygame.K_UP:
		ship.moving_up = True
		print(event.key)#12-4
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
		print(event.key)#12-4

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False	
		
def check_events(ship):
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
			elif event.type == pygame.KEYDOWN:
				check_keydown_events(event, ship)
					
			elif event.type == pygame.KEYUP:
				check_keyup_events(event, ship) 
				
def update_screen(ai_settings, screen, ship):
	screen.fill(ai_settings.bg_color)	
	ship.blitme()
			
	pygame.display.flip()
