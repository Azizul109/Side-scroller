import random
import var
import device
import defaults as df
import pygame
import sprites as sp


class Eyes(): # where zombie will look
    def __init__(self):
        self.size = (50, 50) # each file size
        self.position = (0, 0)

    def set(self): # set zombie on the screen
        self.rect = pygame.Rect(self.position, self.size)
        self.image = pygame.Surface(self.position)
        self.image.fill(df.red)
        # after this rect exist

    def update(self, position): # update the screen so that zombie will appear in screen
        self.position = position
        self.rect.x, self.rect.y = self.position

        # self.image = pygame.Surface(self.position)
        # print(self.rect.x)
        # pygame.draw.rect(var.gameDisplay, (255,0,0), self.rect, 3)
        # var.gameDisplay.blit(self.image, self.rect)


class Enemy(pygame.sprite.Sprite): # enemy sprite will load
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = [] # setting image array
        self.u = 0
        self.v = 0
        self.alive = True  # declares status
        self.col = False
        self.imagesRun = [] # images of zombie run will store in this array
        self.imagesDead = [] # dead images store
        self.imagesAttack = [] # attack images store
        self.imagesJump = [] # jump images store here
        self.rect = [] #rect on the screen
        # self.sound = device.audio.sound_hel
        asset_path = var.assetsDir + "/baldy" # zombie name baldy
        file_name = ['Run1.png', 'Run2.png', 'Run3.png', 'Run4.png', 'Run5.png', 'Run6.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (75, 77) # sprite size

        file_name = ['Dead1.png', 'Dead2.png', 'Dead3.png', 'Dead4.png', 'Dead5.png', 'Dead6.png', 'Dead7.png',
                     'Dead8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (96, 77) # dead file size

        file_name = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (52, 77) # Attack sprite size

        file_name = ['jump_1.png', 'jump_2.png', 'jump_3.png', 'jump_4.png', 'jump_5.png', 'jump_6.png', 'jump_7.png']
        self.filesJump = [asset_path + '/' + e for e in file_name]
        self.fileSizeJump = (48, 100) # jump file size

        self.startHit = False
        self.attack_delay = 15  # fps
        self.attack_count = 0
        self.damage_rate = 2
        self.endHit = False
        self.preattack = False # preattack  will be false
        self.running = True # start of running will be true
        self.index = 0
        self.dead = False
        self.life = 100
        self.dead_rate = 50
        self.loop_index = 0
        self.fps = 2
        self.prize = False
        self.g = 0.2

        self.jumpv = -30
        self.startJump = False
        self.jumping = False

        self.jumpSoundFile = 'assets/sounds/350902__cabled-mess__jump-c-01.wav' # loading zombie sound
        self.jumpSound = [] # jump sound store in this array
        self.attackSoundFile = 'assets/sounds/454836__misterkidx__zombie-attack-1.wav' # attack sound file
        self.attackSound = [] # array to store sound
        self.colSoundFile = var.assetsDir + 'sounds/408021__judith136__4-1.wav' # collide sound
        self.colSound = [] # collide store in this array

    def setEyes(self): # now time to rect on the window
        self.eyes = Eyes()
        self.eyes.size = (self.rect.w, df.display_height * 0.9)
        self.eyes.position = (0, 0)  # jet dummy
        self.eyes.set()

    def loadSound(self):
        self.jumpSound = pygame.mixer.Sound(file=self.jumpSoundFile)
        self.jumpSound.set_volume(0.15)
        self.attackSound = pygame.mixer.Sound(file=self.attackSoundFile)
        self.attackSound.set_volume(0.1)
        self.colSound = pygame.mixer.Sound(file=self.colSoundFile)
        self.colSound.set_volume(0.5)

    def playJumpSound(self):
        if device.audio.sound_enabled:
            self.jumpSound.play()

    def playAttackSound(self):
        if device.audio.sound_enabled:
            self.attackSound.play()

    def playCollision(self):
        if device.audio.sound_enabled:
            self.colSound.play()

    def load_images(self):
        # print('\n')
        for item in self.files_run:
            # print('loading file', item)
            images = pygame.image.load(item)
            self.imagesRun.append(pygame.transform.scale(images, self.fileSizeRun))

        self.image = self.imagesRun[0]
        self.rect = self.image.get_rect()
        self.rect.w = self.fileSizeRun[0]
        self.rect.h = self.fileSizeRun[1]

        for item in self.files_dead:
            # print('loading file', item)
            images = pygame.image.load(item)
            self.imagesDead.append(pygame.transform.scale(images, self.fileSizeDead))

        for item in self.files_attack:
            # print('loading file', item)
            images = pygame.image.load(item)
            self.imagesAttack.append(pygame.transform.scale(images, self.fileSizeAttack))

        for item in self.filesJump:
            # print('loading file', item)
            images = pygame.image.load(item)
            self.imagesJump.append(pygame.transform.scale(images, self.fileSizeJump))

        self.setEyes()

    def animate_preattack(self):
        # print('preattack')
        self.image = self.imagesAttack[0]
        # print("delay ", self.attack_count)
        if self.attack_count < self.attack_delay:
            # print('idle')
            self.image = self.imagesAttack[0]
            self.attack_count += 1
        else:
            self.startHit = True  # trigger hit
            self.attack_count = 0  # return new attack
            self.preattack = False

    def animate_hit(self):
        # print('hitting')
        # hitting animation

        if self.index < len(self.files_attack):
            self.image = self.imagesAttack[self.index]
            self.index += 1
        else:
            # stops hitting animation
            self.index = 0
            self.startHit = False
            self.running = True
            self.endHit = True
            # print('under attacking!')
            # if device.audio.sound_enabled: device.audio.sound_attack.play()
            # device.stats.add_damage(self.damage_rate)

        if self.rect.w != self.fileSizeAttack[0]: self.rect.w = self.fileSizeAttack[0]
        if self.rect.h != self.fileSizeAttack[1]: self.rect.h = self.fileSizeAttack[1]

    def animate_run(self):
        # print('running')
        if self.index < len(self.files_run):
            self.image = self.imagesRun[self.index]
            self.index += 1
            # print(self.index, len(self.files_run))

        else:
            self.index = 0
        # print(self.index)

        # stops running animation
        if self.rect.w != self.fileSizeRun[0]: self.rect.w = self.fileSizeRun[0]
        if self.rect.h != self.fileSizeRun[1]: self.rect.h = self.fileSizeRun[1]

    def animate_death(self):
        # print('dead')
        if self.u != 0:
            self.index = 0
            self.u = 0
            # print(self.files_dead,len(self.files_dead),self.index,'index')
        if self.index < len(self.files_dead):
            self.image = self.imagesDead[self.index]
            self.index += 1
            # print(self.rect.y)
        else:
            self.dead = True

        if self.rect.w != self.fileSizeDead[0]: self.rect.w = self.fileSizeDead[0]
        if self.rect.h != self.fileSizeDead[0]: self.rect.h = self.fileSizeDead[1]

    def animate(self, dt):
        if self.alive:  # lived animation - Run

            if self.running:
                if self.loop_index > self.fps:
                    self.animate_run()
                    self.loop_index = 0
                else:
                    self.loop_index += 1

                self.move(dt)

            if self.preattack:
                if self.loop_index > self.fps:
                    self.animate_preattack()
                    self.loop_index = 0
                else:
                    self.loop_index += 1

            if self.jumping:
                if self.loop_index > self.fps:
                    self.animate_jump()
                    self.loop_index = 0
                else:
                    self.loop_index += 1
                self.move(dt)

            if self.startHit:
                # if self.loop_index > self.fps:
                self.animate_hit()
                # self.loop_index = 0
            # else:
            # self.loop_index += 4

        else:
            if self.loop_index > self.fps:
                self.animate_death()
                self.loop_index = 0
            else:
                self.loop_index += 1
            self.move(dt)

        self.eyes.update((self.rect.x, self.rect.y - self.eyes.rect.h))
        # print(self.eyes.rect.y)

        var.gameDisplay.blit(self.image, (self.rect.x, self.rect.y))

    def animate_jump(self):
        if self.index < len(self.filesJump):
            self.image = self.imagesJump[self.index]
            self.index += 1
            # print(self.index, len(self.files_run))

        else:
            self.index = 0
        # print(self.index)

    def move(self, dt):
        # print(self.u)
        if self.rect.x + self.rect.w >= df.display_width:
            if self.u > 0:
                self.rect.x -= self.u
                self.u = -self.u

        # if self.rect.x < 0:
        #     if self.u < 0:
        #         self.rect.x -= self.u
        #         self.u = -self.u
        #         if device.audio.sound_enabled: device.audio.sound_bullet.play()

        if self.startJump and not self.jumping and self.alive:
            self.playJumpSound()
            self.v = self.jumpv
            self.startJump = False
            self.jumping = True
            self.running = False

        if self.rect.y >= self.floor:
            if self.v >= 0:
                # self.jump = False
                self.v = 0
                self.jumping = False
                self.running = True
            # else:

        else:
            self.v += self.g * dt / 10
        self.rect.y += self.g * self.v * dt / 10
        # print(self.rect.x)

        self.rect.x += self.u * dt / 10

    def descrease_life(self): # decrease of life
        self.life -= self.dead_rate
        if self.life <= 0:
            self.alive = False
            self.running = False



class MariaEnemy(Enemy): #another kind of zombie
    def __init__(self):
        Enemy.__init__(self)
        asset_path = var.assetsDir + "maria100" # female enemy

        file_name = ['run_1.png', 'run_2.png', 'run_3.png', 'run_4.png', 'run_5.png', 'run_6.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (63, 77) # file size of run sprite

        file_name = ['dead_1.png', 'dead_2.png', 'dead_3.png', 'dead_4.png', 'dead_5.png', 'dead_6.png', 'dead_7.png',
                     'dead_8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (112, 77) # size of dead zombie sprite

        file_name = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png', 'attack_6.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (57, 77) # attack zombie sprite

        file_name = ['jump_1.png', 'jump_2.png', 'jump_3.png', 'jump_4.png', 'jump_5.png', 'jump_6.png', 'jump_7.png']
        self.filesJump = [asset_path + '/' + e for e in file_name]
        self.fileSizeJump = (65, 100) # jump file sprite

        self.damage_rate = 2 # damage rate is lower then pirate zombie
        self.dead_rate = 50 # dead rate also big

        self.attackSoundFile = var.assetsDir + 'sounds/343928__reitanna__hiss3.wav'


class PirateEnemy(Enemy): # pirat zombie sprite
    def __init__(self):
        Enemy.__init__(self)
        asset_path = var.assetsDir + "pirat100"

        file_name = ['run_1.png', 'run_2.png', 'run_3.png', 'run_4.png', 'run_5.png', 'run_6.png']
        self.files_run = [asset_path + '/' + e for e in file_name]
        self.fileSizeRun = (70, 77) # pirate zombie run file size

        file_name = ['dead_1.png', 'dead_2.png', 'dead_3.png', 'dead_4.png', 'dead_5.png', 'dead_6.png', 'dead_7.png',
                     'dead_8.png']
        self.files_dead = [asset_path + '/' + e for e in file_name]
        self.fileSizeDead = (108, 77) # pirate zombie dead file size

        file_name = ['attack_1.png', 'attack_2.png', 'attack_3.png', 'attack_4.png', 'attack_5.png', 'attack_6.png']
        self.files_attack = [asset_path + '/' + e for e in file_name]
        self.fileSizeAttack = (50, 76) # attack file size

        file_name = ['jump_1.png', 'jump_2.png', 'jump_3.png', 'jump_4.png', 'jump_5.png', 'jump_6.png', 'jump_7.png']
        self.filesJump = [asset_path + '/' + e for e in file_name]
        self.fileSizeJump = (47, 100) # jump file size

        self.damage_rate = 3 # zombie damage rate
        self.dead_rate = 35 # this zombie is the most difficult to kill
        self.attackSoundFile = var.assetsDir + 'sounds/420250__redroxpeterpepper__monster-attack.ogg'


class Horde(): # important for generating zombie in the game

    def __init__(self):
        self.enemies = []
        self.limit = 0
        self.count = 0
        self.map_gap = 0
        self.time_to_born = []
        self.umax = 2

    def born(self):

        dx = -df.display_width / self.limit
        x = int(dx)

        for item in range(0, self.limit):
            random_enemy = int(random.random() * 1000)

            if random_enemy % 2 == 0: # randomize between 3 types of zombie
                enemy = MariaEnemy() # maria enemy will come or pirate enemy will come
                # enemy = Enemy()
                # enemy = PirateEnemy()
                enemy.u = 1
            #elif random_enemy % 3 == 0:
            #    enemy = ChildEnemy()
            #    enemy.u = 2
            elif random_enemy % 3 == 0:
                enemy = PirateEnemy() # pirate enemy will generate lower
                enemy.u = 1.2
            else:
                enemy = Enemy()
                enemy.u = 0.8

            enemy.load_images()
            enemy.floor = df.display_height - self.map_gap - enemy.rect.h - 10 * random.random()

            random_prize = int(random.random() * 100)
            if random_prize % 3 == 0:
                enemy.prize = True
                enemy.ammo = sp.Ammo()
                enemy.ammo.set_image()
                enemy.ammo.floor = enemy.floor
                enemy.ammo.loadSound()


            enemy.rect.y = enemy.floor
            enemy.rect.x = x
            x += dx
            # print(item)
            enemy.loadSound()
            self.enemies.append(enemy)

