print('Loading menu') # for my understand i give this line
import os

script_path = os.path.dirname(os.path.realpath(__file__))
print('location', script_path) # where my file are located
os.chdir(script_path)

import sprites as sp # it will load sprite
import defaults as df # i made my window and some color in defaults.py file, here i am calling that
import pygame
import re
import time
import generic as gen
import var
import adjustments # import adjustments
import map # import map
import imp # import imp
import device
import buttons as btns


class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.backfile = var.assetsDir + 'backgrounds/side_scroller.png' # building of menu screen with background
        self.play_file = var.assetsDir + 'play_red.png' # load of button image
        self.menu_file = var.assetsDir + 'Buttonmenu.png'
        self.adj_file = var.assetsDir + 'Button_adj.png'
        self.cancel_file = var.assetsDir + 'Button_cancel.png'
        self.play_txt = "Play" # load of text
        self.cancel_text = "Exit"
        self.adj_txt = "Settings"

        self.backMusicFile = var.assetsDir + 'sounds/[Naruto Shippuuden Original Soundtrack 2] 18 - Kokuten (192  kbps).ogg' # load of background music
        # device.audio.play_music()

    def run(self):
        mapsback = sp.Sprite2()
        mapsback.file = self.backfile
        mapsback.w = df.display_width # background width will be equal to display width
        mapsback.h = df.display_height # background height will be equal to display height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        playBtn = btns.Button(self.play_file, df.display_width * 0.3, df.display_height * 0.8, 50, 50)
        playBtn.hover_text = self.play_txt

        setBtn = btns.Button(self.adj_file, df.display_width * 0.5, df.display_height * 0.8, 50, 50)
        setBtn.hover_text = self.adj_txt

        canBtn = btns.Button(self.cancel_file, df.display_width * 0.7, df.display_height * 0.8, 50, 50)
        canBtn.hover_text = self.cancel_text

        self.loadMusic()
        self.playBackMusic()

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.stopEngine = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.stopEngine = True

            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)

            if playBtn.onClick(pygame.mouse): # play button will enter map screen
                imp.reload(map)

                time.sleep(0.1)
                mapsScreen = map.AddScreen()
                mapsScreen.run()
                self.loadMusic()
                self.playBackMusic()

            if canBtn.onClick(pygame.mouse): # cancel button will quit game
                self.stopEngine = True
                break

            if setBtn.onClick(pygame.mouse): # click of settings button will load adjustments.py filr
                imp.reload(adjustments)
                adjScreen = adjustments.AddScreen()
                time.sleep(0.1)
                adjScreen.run()
                self.loadMusic()
                self.playBackMusic()

            pygame.display.update()
            var.clock.tick(var.fps)
