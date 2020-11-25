import sprites as sp
import defaults as df
import var as var
import pygame
import time
import text as txg


all_snow = pygame.sprite.Group()

class Button(sp.Sprite2): # button and it's color

    def __init__(self, filename, x, y, w, h):
       
        sp.Sprite2.__init__(self)
        self.file = filename
        self.w = w
        self.h = h
        self.set_image()
        self.rect.x = x
        self.rect.y = y

        self.hover_text = 'Back'
        self.click_text = 'Loading'
        self.txt_w = df.display_width # where the text will be on screen
        self.txt_h = 30
        self.txt_x = df.display_width*0.1
        self.txt_y = df.display_height - self.txt_h*2
        self.txt_color= df.gray # text color
        self.hover_color = df.orange # color layer over text
        self.click_color = df.red # click color( red rectangle on click)
        self.shadow_w = df.display_width # will be shadow effect
        self.shadow_h = 150 # shadow will be 150 on height
        self.shadow_x = 0
        self.shadow_y = self.txt_y
        self.shadow_color = df.white
        self.index = 0
        self.highlighted = False
        self.clicked = False
        self.max_frame = 10
        self.animating = False
        self.txt_x_d = self.txt_x
        self.txt_y_d = self.txt_y

        self.shadow_x_d = self.shadow_x
        self.shadow_y_d = self.shadow_y
        self.shadow_color = df.green

        self.font_btn = txg.TextGame()
        self.font_btn.font_size = 50
        self.font_btn.set_font()
        self.font_btn.center = (self.txt_x, self.txt_y)
        self.font_btn.color = df.white

    def draw_sprite2(self):
        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def highlight(self, color): # rect the highlight color
        s = pygame.Surface((self.rect.w, self.rect.h))
        s.set_alpha(150)
        s.fill(color)
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y, 1, self.rect.h])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x, self.rect.y + self.rect.h, self.rect.w, 1])
        pygame.draw.rect(var.gameDisplay, color, [self.rect.x+self.rect.w, self.rect.y, 1, self.rect.h])
        var.gameDisplay.blit(s, (self.rect.x, self.rect.y))


    def new_shadow(self, color):
        s = pygame.Surface((self.txt_w, self.shadow_h))
        s.set_alpha(150) # alpha value will give more brightness
        s.fill(color)
        var.gameDisplay.blit(s, (self.shadow_x, self.shadow_y)) # need to blit on screen so that color can be seen

    def new_msg(self, text): # print of new msg
        self.new_shadow(self.shadow_color)
        self.font_btn.display_text(text)


    def onClick(self, mouse):

        if self.rect.collidepoint(mouse.get_pos()) == 1:
            self.highlight(self.hover_color)

            self.new_msg(self.hover_text)
            # self.highlighted = True

            if mouse.get_pressed()[0]: # after clicking animation will start
                self.animating = True
                self.clicked = True
                print('button clicked', self.file)
                self.index = 0
                time.sleep(0.5)
        else:
            self.highlight_color = self.hover_color

        if self.animating:self.animate()

        self.draw_sprite2()
        if self.animating  or not self.clicked:


            return False #continue running
        else:
            self.clicked = False
            return True #clicken event is true

    def animate(self):
        self.index +=1
        if self.index < self.max_frame:
            self.highlight(self.click_color)
            self.txt_x += 100
            #self.txt_y += 1
            self.shadow_x += 100
            #self.shadow_y += 1
            self.animating = True
        else:
            self.animating = False
            self.txt_x = self.txt_x_d
            self.txt_y  = self.txt_y_d
            self.shadow_x = self.shadow_x_d
            self.shadow_y = self.shadow_y_d


class Imap(Button): # previously defined
    def __init__(self,filename, x, y, level, gap,blocked, total_enemies):
        w = 50
        h = 50
        Button.__init__(self, filename, x, y, w, h)

        self.level = level
        self.blocked = blocked
        self.total = total_enemies
        self.gap = gap
        self.map_name = ""
        self.filename  = ""
        self.bfilename = var.assetsDir + "icons8-lock-100.png"

        self.lockpad = sp.Sprite2()
        self.lockpad.file = self.bfilename
        self.lockpad.w = int(w*0.5)
        self.lockpad.h = int(h*0.5)
        self.lockpad.set_image()
        self.lockpad.rect.x = x
        self.lockpad.rect.y = y

        self.hover_text = 'Level ' + str(level) + '   /   ' + str(total_enemies) + ' Zombies' # number of zombies and level will be seen in map screen (below part of screen)
        self.font_btn.color = df.red



    def set_map(self):
        if self.level ==1 :
            self.map_name = 'forest.jpg' # level 1 map background

            self.gap = df.display_height * 0.1020 # change of value will change home position on right side

        if self.level ==2 :
            self.map_name = 'blood.png' # level 2 map background
            self.gap = df.display_height * 0.1230
        if self.level ==3 :
            self.map_name = 'parallax background for nature tileset.jpg' # level 3 map background
            self.gap = df.display_height * 0.195
        if self.level ==4 :
            self.map_name = 'green.jpg' # level 4 map background
            self.gap = df.display_height * 0.0762
        if self.level ==5 :
            self.map_name = 'classic1.jpg' # level 5 map background
            self.gap = df.display_height * 0.2063
        if self.level ==6 :
            self.map_name = 'classic2.jpg' # level 6 map background
            self.gap = df.display_height * 0.126
        if self.level ==7 :
            self.map_name = 'night_lanterns.jpg' # level 7 map background
            self.gap = df.display_height * 0.143
        if self.level ==8 :
            self.map_name = 'china.png' # level 8 map background
            self.gap = df.display_height * 0.12
        if self.level ==9 :
            self.map_name = 'snow1.jpg' # level 9 map background
            self.gap = df.display_height * 0.17
        if self.level ==10 :
            self.map_name = 'snow2.jpg' # level 10 map background
            self.gap = df.display_height * 0.176
        if self.level ==11 :
            self.map_name = 'horror2.jpg' # level 11 map background
            self.gap = df.display_height * 0.195
        if self.level ==12 :
            self.map_name = 'horror1.jpg' # level 12 map background
            self.gap = df.display_height * 0.1555
        if self.level ==13 :
            self.map_name = 'volcanoes.jpg' # level 13 map background
            self.gap = df.display_height * 0.171
        if self.level ==14 :
            self.map_name = 'zombie.png' # level 14 map background
            self.gap = df.display_height * 0.075


        self.filename = var.assetsDir + "backgrounds/" + self.map_name



    def draw_block(self):
        if self.blocked:
           var.gameDisplay.blit(self.lockpad.image, (self.rect.x, self.rect.y))


