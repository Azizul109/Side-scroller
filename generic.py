
import pygame
import var
import text as txg # import of text
import defaults as df
import device # import of device
print('Loading Xscreen')

class Xscreen():
    def __init__(self):
        self.stopEngine = False

        self.musicBack = []

        self.font1 = txg.TextGame()
        self.font1.font_size = 10
        self.font1.path = "assets/fonts/OpenSans-Light.ttf" # fond for map
        self.font1.set_font()
        # for loading map screen backgrouns sound
        self.backMusicFile = var.assetsDir + 'sounds/Naruto Shippuden OST - Departure To The Front Lines (192  kbps).ogg'

    def loadMusic(self):
        self.backMusic = pygame.mixer.music.load(self.backMusicFile)
        pygame.mixer.music.set_volume(0.5)


    def playBackMusic(self): # play back music
        if device.audio.music_enabled:
            # print('device:music enabled')
            if pygame.mixer.music.get_busy():
                pygame.mixer.stop()

            pygame.mixer.music.play(-1)

        else:
            print('device:music disabled')
            pygame.mixer.music.pause()
            pygame.mixer.music.stop()

    def draw_sprite2(self, sprite):
        var.gameDisplay.blit(sprite.image, (sprite.rect.x, sprite.rect.y))


    def message_display(self, text, center): # text message will be display on screen
        self.font1.center = center
        self.font1.display_text(text)
        # label = self.font.render(text, 1, color)
        # var.gameDisplay.blit(label, center)


    def draw_selected(self, pos, dim, alpha, color):
        s = pygame.Surface(dim)
        s.set_alpha(alpha)
        s.fill(color)
        var.gameDisplay.blit(s, pos)

    def run(self):
        while not self.stopEngine:
            print('running empty engine')
            self.stopEngine = True

