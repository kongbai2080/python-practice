import pygame

from settings import Settings

from rocket import Rocket

import game_functions as gf

def run_game():    
    
    pygame.init()
    lr_settings = Settings()
    screen = pygame.display.set_mode(
        (lr_settings.screen_width,lr_settings .screen_height))  #

    pygame.display.set_caption('Rocket') #
    
    rocket = Rocket(lr_settings,screen)
    
    
    while True:
        
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(lr_settings,screen,rocket)
    
run_game()
    

