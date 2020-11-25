print('loading Adjustments') # it will give sequence for running the game
import sprites as sp # importing sprites
import defaults as df # importing defaults
import pygame
import re
import time
import generic as gen # import of generic file
import var # import var
import device # import device
import buttons as btns # import buttons

class AddScreen(gen.Xscreen): # building of game interface
    def __init__(self):
        gen.Xscreen.__init__(self)
        """
        all of this file will find some image from assets directory and print some text in menu screen.
        on the bottom of screen.
        if user press settings new item will be available
        
        """

        self.background_file = var.assetsDir + 'backgrounds/maps_table.jpg' # loading of background

        self.enable_file = var.assetsDir + 'enabled.png' # button sprites
        self.disable_file = var.assetsDir + 'disabled.png' # disabled button sprite

        self.buy_file = var.assetsDir + 'buy_yes.png' # new button
        self.back_txt = "Return" # text
        self.music_enable_txt = "Enabled" # load of text
        self.music_disable_txt = "Disabled" # load of text
        self.sound_disable_txt = "Disabled" # text
        self.sound_enable_txt = "Enabled" # text
        self.opt_txt = "Settings" # settings
        self.music_txt = "Music" # music text
        self.sound_txt = "Sounds" # sound text

        self.text_info_y = df.display_height*0.8 # where text will be shown
        self.header_position = (df.display_width * 0.1, 0) # header position
        self.font1.path = "assets/fonts/Roboto-Black.ttf" # text font
        self.font1.font_size = 40 # font size
        self.font1.set_font()
        self.button_size = 50 # button size
        self.music_text_x = df.display_width * 0.1 # for music text in settings
        self.music_text_y = df.display_height * 0.2 # music text in settings
        self.sound_text_x = df.display_width * 0.1 # for sound text in settings
        self.sound_text_y = df.display_height * 0.3 # for sound text in settings

        self.music_button_x = df.display_width * 0.7 # for music button
        self.music_button_y = self.music_text_y
        self.music_button2_x = df.display_width * 0.8 # for music button
        self.music_button2_y = self.music_text_y

        self.sound_button_x = df.display_width * 0.7
        self.sound_button_y = self.sound_text_y
        self.sound_button2_x = df.display_width * 0.8
        self.sound_button2_y = self.sound_text_y

        self.exit_button_x = df.display_width * 0.5 - 100 * 0.5
        self.exit_button_y = df.display_height * 0.8


    def run(self):

        mapsback = sp.Sprite2()
        mapsback.file = self.background_file
        mapsback.w = df.display_width
        mapsback.h = df.display_height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0


        btnEnableMusic = btns.Button(self.enable_file, self.music_button_x, self.music_button_y, self.button_size, self.button_size)
        btnDisableMusic = btns.Button(self.disable_file, self.music_button2_x, self.music_button2_y, self.button_size,self.button_size)
        btnEnableSound = btns.Button(self.enable_file, self.sound_button_x, self.sound_button_y, self.button_size,self.button_size)
        btnDisableSound = btns.Button(self.disable_file, self.sound_button2_x, self.sound_button2_y, self.button_size,self.button_size)
        exitBtn = btns.Button(self.buy_file, self.exit_button_x, self.exit_button_y, 100, 100)

        btnEnableMusic.shadow_h = 50
        btnDisableMusic.shadow_h = 50
        btnEnableSound.shadow_h = 50
        btnEnableSound.shadow_h = 50
        exitBtn.shadow_h = 50

        btnDisableMusic.hover_text = self.music_disable_txt # hovering of text will give some color layer
        btnEnableMusic.hover_text = self.music_enable_txt
        btnDisableSound.hover_text = self.sound_disable_txt
        btnEnableSound.hover_text = self.sound_enable_txt
        exitBtn.hover_text = self.back_txt

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # press ESC will exit the game
                        self.stopEngine = True

            var.gameDisplay.fill(df.white) # from var.py import of white color
            self.draw_sprite2(mapsback)

            if exitBtn.onClick(pygame.mouse): # exit button on click
                self.stopEngine = True
                time.sleep(0.1)

            if btnDisableMusic.onClick(pygame.mouse): # disable music on click
                device.audio.music_enabled = False
                # device.audio.play_music()
                self.playBackMusic()
                time.sleep(0.1)

            if btnEnableMusic.onClick(pygame.mouse): # enable music on click
                device.audio.music_enabled = True
                self.playBackMusic()
                time.sleep(0.1)

            if btnDisableSound.onClick(pygame.mouse): # disable sound on click
                device.audio.sound_enabled = False
                # device.audio.play_music()
                time.sleep(0.1)

            if btnEnableSound.onClick(pygame.mouse): # enable sound on click
                device.audio.sound_enabled = True
                # device.audio.play_music()
                time.sleep(0.1)


            self.message_display(self.opt_txt,self.header_position ) # display the message on screen
            self.message_display(self.music_txt, (self.music_text_x, self.music_text_y))
            self.message_display(self.sound_txt,  (self.sound_text_x, self.sound_text_y))

            pygame.display.update()
            var.clock.tick(20)
