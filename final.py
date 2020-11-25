import sprites as sp # import of sprite
import pygame
import var
import random
import time
import generic as gen # import of generic
import defaults as df
import device
import zombies as zmb # import of defaults
print('Loading final')
class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        print('final screen created')
        self.font1.color = df.orange # text color on screen
        self.font1.font_size = 40 # font size
        self.font1.set_font()
        self.backMusicFile = var.assetsDir + 'sounds/[Naruto Shippuuden Original Soundtrack 2] 18 - Kokuten (192  kbps).ogg' # final screen background music


    def run(self): # background running

        mapsback = sp.Sprite2()
        mapsback.file = var.assetsDir + 'backgrounds/final.png' # load of background image
        mapsback.w = df.display_width # width will be same as display width
        mapsback.h = df.display_height # height will be same as display height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        total_time = 0

        horde = zmb.Horde() # zombie horde class will be use here from zombies.py
        horde.map_gap = 10
        horde.limit = 100
        horde.born()


        self.loadMusic()
        self.playBackMusic()
        dt = 50
        while not self.stopEngine: # for stopping the window need to setup this line of code in pygame
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # press of escape will end the game
                        self.stopEngine = True
            var.gameDisplay.fill(df.black)
            self.draw_sprite2(mapsback)


            for enemy in horde.enemies:
                enemy.animate(dt)
                # print(enemy.rect.x)


            self.draw_selected((35,80), (df.display_width, 50), 100, df.white)
            self.message_display('Thanks to our Honourable laoshi Zhang Yi', (340, 80)) # this line will be print on final screen window
            dt = pygame.time.get_ticks() - time_start

            pygame.display.update()
            # var.clock.tick(var.fps)
            total_time += dt

