print('Loading Sound and Video') # only for my understanding so that i don't messed up my code
import pygame
import var
import datetime
import defaults as df # importing defaults
import os

class AddWin():
    def _init_(self):
        pygame.init()
        pygame.display.set_caption('Arif & Redoan') # display caption set

class AddSound(AddWin):
    def __init__(self):
        AddWin._init_(self)
        pygame.mixer.pre_init(frequency=44100, size=-32, channels=2, buffer=4096) # need to defined this for pygame sound
        pygame.init()
        assetsDir = var.assetsDir
        if not os.path.isfile(assetsDir + 'comical_liquid_gel_splat.ogg'): # getting sound from sound directory
            print('ERROR No Sound exist in ', assetsDir + 'comical_liquid_gel_splat.ogg')
        else:
            print('file exists')
        self.sound_err = pygame.mixer.Sound(file=assetsDir + 'sounds/327736__distillerystudio__error-03.ogg')
        self.sound_err.set_volume(0.5)

        self.sound_loser = pygame.mixer.Sound(file=assetsDir + '113988__kastenfrosch__verloren.ogg') # player defeated sound
        self.sound_loser.set_volume(0.5)
        self.sound_winer = pygame.mixer.Sound(file=assetsDir + '270528littlerobotsoundfactoryjingle-win-00.ogg')
        self.sound_winer.set_volume(0.5)

        self.music_enabled = True # need to be true for music enabled
        self.sound_enabled = True # for sound
        self.music_theme = var.assetsDir + ""

        self.sound_glass_break = pygame.mixer.Sound(file=assetsDir + 'sounds/338692__natemarler__glass-break-small_short.wav')
        print('sound created')


class Ranking(): # this will generate upper part of my game
    def __init__(self):

        self.experience = 0
        self.respawn = 0
        self.killed = 0 # initial killed was o
        self.shelter = 100 # shelter health 100
        self.damage = 0 # initial damage is o
        self.level = 0
        self.life = 100 # initial life is 100
        self.damage = 0 # initial damage is 0
        print('instance of Ranking')
        self.map_name = ''
        self.map = ''
        self.total = 0
        self.winner = False # initial winner set to false
        self.maps = []
        self.default_bullets_avaiable = 100 # bullets available
        self.default_health_available = 100 # bullets health
        self.default_health_available = self.default_health_available
        self.bullet_available = self.default_bullets_avaiable
        self.dead_player = False


    def add_damage(self, damage_rate): # damage rate will be count here

        self.damage += damage_rate # damage rate will increase
        self.life -= damage_rate # life will decrease
        # print('Damage', round(self.damage, 0), int(self.life))

    def add_kill(self): # kill of zombie will count as 1
        self.killed += 1 # killed number will increase
        self.experience += 1

    def new_level(self): # it will unlock new level by my condition
        self.killed = 0
        self.damage = 0
        if self.life <= 0:
            self.life = 100

    def end_level(self): # end level will print below message on the window
        if self.dead_player:
            print('End Level', round(self.damage, 1), int(self.life))
            self.dead_player = False #to start gaming as a alive player
            return True

        if self.killed == self.total:
            if datetime.datetime.now() - df.dead_time > datetime.timedelta(seconds=df.delay):
                return True
            return False

        return False

stats = Ranking()
audio = AddSound()
