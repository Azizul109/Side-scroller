print('Loading map')
import sprites as sp
import defaults as df
import pygame
import re
import time
import generic as gen
import var
import play
import imp
import device
import buttons as btns



class AddScreen(gen.Xscreen): #creating map screen
    def __init__(self):
        gen.Xscreen.__init__(self)
        self.background_file = var.assetsDir + 'backgrounds/maps.jpg' # backgrounds of map
        self.buy_file = var.assetsDir + 'buy_yes.png' # yes button


        self.map1_file = var.assetsDir + 'icons/zombie_head.png' # for locking each level i use this( from folder)
        self.map2_file = self.map1_file # map2_file will check for map1_file location
        self.map3_file = self.map1_file
        self.map4_file = self.map1_file
        self.map5_file = self.map1_file
        self.map6_file = self.map1_file
        self.map7_file = self.map1_file
        self.map8_file = self.map1_file
        self.map9_file = self.map1_file
        self.map10_file = self.map1_file
        self.map11_file = self.map1_file
        self.map12_file = self.map1_file
        self.map13_file =self.map1_file
        self.map14_file = self.map1_file
        self.exit_file = var.assetsDir + 'Button_exit.png' # for exiting the map screen
        self.musicBackFile = var.assetsDir + 'sounds/Naruto Shippuden OST - Departure To The Front Lines (192  kbps).ogg' # loading background music






    def run(self): # where each map will be position on the map screen
        print('running maps')
        icon_map1_x = 0.8
        icon_map1_y = 0.7
        icon_map2_x = 0.8
        icon_map2_y = 0.6
        icon_map3_x = 0.7
        icon_map3_y = 0.6
        icon_map4_x = 0.7
        icon_map4_y = 0.4
        icon_map5_x = 0.85
        icon_map5_y = 0.1
        icon_map6_x = 0.7
        icon_map6_y = 0.15
        icon_map7_x = 0.6
        icon_map7_y = 0.1
        icon_map8_x = 0.15
        icon_map8_y = 0.3
        icon_map9_x = 0.4
        icon_map9_y = 0.1
        icon_map10_x = 0.3
        icon_map10_y = 0.2
        icon_map11_x = 0.1
        icon_map11_y = 0.6
        icon_map12_x = 0.2
        icon_map12_y = 0.7
        icon_map13_x = 0.3
        icon_map13_y = 0.5
        icon_map14_x = 0.35
        icon_map14_y = 0.75

        mapsback = sp.Sprite2()
        mapsback.file = self.background_file
        mapsback.w = df.display_width # map width will be equal to display width
        mapsback.h = df.display_height # map height will be equal to display height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        if not len(device.stats.maps)>0:
            maps = []
            maps.append(btns.Imap(self.map1_file, df.display_width*icon_map1_x, df.display_height*icon_map1_y, 1, 20, False, 10 )) # setting zombie number.
            maps.append(btns.Imap(self.map2_file, df.display_width*icon_map2_x, df.display_height*icon_map2_y, 2, 20, False, 10 )) # number of zombie can be changed
            maps.append(btns.Imap(self.map3_file, df.display_width*icon_map3_x, df.display_height*icon_map3_y, 3, 20, False, 12 )) # if i change 12 then zombie number will be changed in each map
            maps.append(btns.Imap(self.map4_file,df.display_width*icon_map4_x, df.display_height*icon_map4_y, 4, 20, False, 12 )) # If i made parameter true then map will be blocked
            maps.append(btns.Imap(self.map5_file, df.display_width*icon_map5_x, df.display_height*icon_map5_y, 5, 20, False, 14 )) # currently all map is unlock
            maps.append(btns.Imap(self.map6_file, df.display_width*icon_map6_x, df.display_height*icon_map6_y, 6, 20, False, 14 ))
            maps.append(btns.Imap(self.map7_file, df.display_width*icon_map7_x, df.display_height*icon_map7_y, 7, 20, False, 16 ))
            maps.append(btns.Imap(self.map8_file, df.display_width*icon_map8_x, df.display_height*icon_map8_y, 8, 20, False, 16 ))
            maps.append(btns.Imap(self.map9_file, df.display_width*icon_map9_x, df.display_height*icon_map9_y, 9, 20, False, 18 ))
            maps.append(btns.Imap(self.map10_file, df.display_width*icon_map10_x, df.display_height*icon_map10_y, 10, 20, False, 18 ))
            maps.append(btns.Imap(self.map11_file, df.display_width*icon_map11_x, df.display_height*icon_map11_y, 11, 20, False, 19 ))
            maps.append(btns.Imap(self.map12_file, df.display_width*icon_map12_x, df.display_height*icon_map12_y, 12, 20, False, 19 ))
            maps.append(btns.Imap(self.map13_file, df.display_width*icon_map13_x, df.display_height*icon_map13_y, 13, 20, False, 20 )) # zombie number is 20
            maps.append(btns.Imap(self.map14_file, df.display_width*icon_map14_x, df.display_height*icon_map14_y, 14, 20, False, 20 )) # final map


        else:
            maps = device.stats.maps
        button_back = btns.Button(self.exit_file, df.display_width*0.5, df.display_height*0.8, 50, 50)
        button_back.hover_text = 'Back'
        self.loadMusic()
        self.playBackMusic()

        total_time = 0
        while not self.stopEngine:
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    print('Exit maps')
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print('S')

            var.gameDisplay.fill(df.white)
            self.draw_sprite2(mapsback)

            if button_back.onClick(pygame.mouse):
                self.stopEngine = True

            for m in maps: # map blocked
                if m.blocked:
                    m.highlight(df.gold) # color from var.py
                else:
                    m.highlight(df.green)
                if m.onClick(pygame.mouse):


                    device.stats.level = m.level
                    m.set_map()
                    device.stats.map_name = m.filename

                    if not m.blocked:
                        imp.reload(play)
                        playScreen = play.AddScreen(m)


                        playScreen.run() # condition for making text map is blocked
                        self.playBackMusic()
                        if device.stats.winner:
                            index = device.stats.level
                            if index > 0:
                                if index < len(maps):
                                    print('unblocking the next map') # next map is unlocking
                                    maps[index].blocked =False
                                    device.stats.maps = maps
                    else:
                        m.hover_text = "Map is blocked!"
                        print('map Blocked:',m.filename)

                m.draw_block()
            pygame.display.update() # now need to diplay the window again

            var.clock.tick(var.fps)

        print('Leaving Map screen')
