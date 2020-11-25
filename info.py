print('Loading Info')
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import device # import of device
import text as txg
import buttons as btns

class AddScreen(gen.Xscreen):
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.background_file = var.assetsDir + 'backgrounds/maps_table.jpg' # backgrounds will load
        self.buy_file = var.assetsDir + 'buy_yes.png'
        print('info screen created')
        self.font1.font_size = 30
        self.font1.set_font()

    def run(self):

        mapsback = sp.Sprite2()
        mapsback.file = self.background_file
        mapsback.w = df.display_width
        mapsback.h = df.display_height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        exitBtn = btns.Button(self.buy_file, df.display_width * 0.5 - 50, df.display_height * 0.8, 100, 100)

        while not self.stopEngine:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    device.audio.sound_bullet.play
                    pygame.quit()
                    quit()

            var.gameDisplay.fill(df.white).conver()
            self.draw_sprite2(mapsback)

            if exitBtn.onClick(pygame.mouse):
                    self.stopEngine = True
                    time.sleep(1)


            yt = 10
            text = 'Arif and Redoan final project' # some text
            self.font1.color = df.green
            self.message_display(text, (50, yt))

            pygame.display.update()
            var.clock.tick(20)