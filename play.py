
import sprites as sp
import defaults as df
import pygame
# import re
import time
import generic as gen
import var
import device
import final # import of final screen
# import random
import pause
import imp
import datetime
import zombies as zmb
import text as txg # import text


class AddScreen(gen.Xscreen):
    def __init__(self, map):
        gen.Xscreen.__init__(self)
        self.map = map


        self.zombie_txt_pos = (0,0) # zombie text position
        self.exp_txt_pos = (df.display_width*0.2, 0)
        self.life_txt_pos = (df.display_width*0.4, 0)
        self.map_txt_pos = (df.display_width*0.6, 0)
        self.time_txt_pos = (df.display_width*0.7, 0)
        self.bullet_txt_pos = (df.display_width*0.85, 0)
        self.display_text_pos_home = (df.display_width * 0.2, df.display_height * 0.5 + 50)
        self.display_text_pos = (df.display_width * 0.1 , df.display_height * 0.4 + 50)
        self.display_text_pos_hel = (df.display_width * 0.2, df.display_height * 0.7 + 50)

        self.font1 = txg.TextGame()
        self.font1.font_size = 30
        self.font1.color = df.violet
        self.font1.set_font()

        self.font2 = txg.TextGame()
        self.font2.font_size = 60
        self.font2.color = df.red
        self.font2.set_font()
        self.display_text_pos_lost = self.bullet_txt_pos
        self.display_text_pos_win = self.bullet_txt_pos



    def run(self):
        imp.reload(sp)
        imp.reload(final)
        imp.reload(zmb)
        imp.reload(pause)

        print('\n')


        mapsback = sp.Sprite2()
        mapsback.file = self.map.filename
        mapsback.w = df.display_width
        mapsback.h = df.display_height
        mapsback.set_image()
        mapsback.rect.x = 0
        mapsback.rect.y = 0

        info_winner = sp.Sprite2()
        info_winner.file = var.assetsDir + 'enabled.png'
        info_winner.w = 200
        info_winner.h = 150

        info_winner.set_image()
        info_winner.rect.x = df.display_width * 0.5 - info_winner.w * 0.5
        info_winner.rect.y = df.display_height * 0.5 - info_winner.h * 0.5
        self.display_text_pos_win = (df.display_width * 0.5 - 100, info_winner.rect.y + info_winner.h )
        self.display_text_pos_home = (df.display_width * 0.2, self.display_text_pos_win[1] + 80)
        self.display_text_pos_hel = (df.display_width * 0.2, self.display_text_pos_home[1] + 80)

        info_loser = sp.Sprite2()
        info_loser.file = var.assetsDir + 'disabled.png'
        info_loser.w = 200
        info_loser.h = 150

        info_loser.set_image()
        info_loser.rect.x = df.display_width * 0.5 - info_winner.w * 0.5
        info_loser.rect.y = df.display_height * 0.5 - info_winner.h * 0.5
        self.display_text_pos_lost = (df.display_width * 0.1, info_loser.rect.y + info_loser.h*1.1)

        horde = zmb.Horde()
        horde.map_gap = self.map.gap
        horde.limit = self.map.total
        horde.born()

        device.stats.total = self.map.total

        hel = sp.Vehicle()
        hel.load_images()
        hel.loadSound()

        weapon = sp.Weapon()
        weapon.bullet_available = device.stats.bullet_available
        weapon.load_bullets()

        device.stats.new_level()
        total_time = 0

        home = sp.House()
        home.load_images()
        home.gap = self.map.gap
        home.set_position()
        dt = 1

        freeAmmo = []
        pygame.mixer.music.stop()

        while not self.stopEngine:
            time_start = pygame.time.get_ticks()
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        hel.u = -5
                    if event.key == pygame.K_RIGHT:
                        hel.u = 6
                    if event.key == pygame.K_UP:
                        hel.v = -8*0.5
                    if event.key == pygame.K_DOWN:
                        hel.v = 9

                    if event.key == pygame.K_SPACE:
                        weapon.get_loc(hel)
                        weapon.shoot_bullet()


                    if event.key == pygame.K_ESCAPE:
                        pauseScreen = pause.AddScreen()
                        # time.sleep(0.1)
                        time_pause = pygame.time.get_ticks()
                        pauseScreen.run()
                        dt_pause = pygame.time.get_ticks()  - time_pause
                        time_start += dt_pause
                        if pauseScreen.stopPlay:
                            self.stopEngine = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        hel.u = 0
                        hel.v = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        hel.u = 0
                        hel.v = 0
                    hel.playSound()

            var.gameDisplay.fill(df.black)
            self.draw_sprite2(mapsback)
            home.animate() #call home animation

            hel.animate(dt)  # callls animation defs


            weapon.moveBullets(dt)


            for enemy in horde.enemies:
                if enemy.dead:
                    horde.enemies.remove(enemy)
                    continue

                enemy.animate(dt)
                # enemy.startJump = True


                if enemy.rect.colliderect(home.rect):
                    enemy.preattack = True
                    enemy.running = False

                    if enemy.endHit:
                        home.decrease_life(enemy.damage_rate)
                        enemy.endHit = False

                        if home.life <= 0:
                            device.stats.dead_player = True
                            break

                        if device.audio.sound_enabled:
                            enemy.playAttackSound()
                            # device.audio.sound_attack.play()

                if enemy.rect.colliderect(hel.rect):
                    enemy.preattack = True
                    enemy.running = False
                    # enemy.rect.x -=5
                    if enemy.endHit:
                        hel.decrease_life(enemy.damage_rate)
                        enemy.endHit = False

                        if hel.life<=0:
                            device.stats.dead_player = True
                            break

                        if device.audio.sound_enabled:
                            enemy.playAttackSound()

                if enemy.eyes.rect.colliderect(hel.rect):
                    enemy.startJump = True
                else:
                    enemy.startJump = False
                # Collision detection
                if len(weapon.freeBullets)>0: # if len of free bullets>0
                    for bullet in weapon.freeBullets:
                        if enemy.rect.colliderect(bullet.rect):
                            if enemy.jumping:
                                enemy.v = 0

                            if device.audio.sound_enabled:
                                bullet.playShootSound()

                            if enemy.alive: # enemy alive
                                enemy.descrease_life() # decrease of life
                                if not enemy.alive:
                                    device.stats.add_kill()
                                    df.dead_time = datetime.datetime.now()
                                    if enemy.prize:
                                        enemy.ammo.rect.x = enemy.rect.x + enemy.rect.w*1.1
                                        enemy.ammo.rect.y = enemy.rect.y + enemy.rect.h -enemy.ammo.h
                                        enemy.ammo.u = hel.u*0.1
                                        enemy.ammo.v = 0
                                        freeAmmo.append(enemy.ammo)

                            weapon.freeBullets.remove(bullet)

            for box in freeAmmo:
                box.move(dt)
                box.draw()
                if box.rect.colliderect(hel.rect):
                    print('extra ammo')
                    box.playGrabSound()
                    freeAmmo.remove(box)
                    weapon.load_extra_bullet(20)

                    break


            if device.stats.end_level():

                self.stopEngine = True


                if home.life > 0 and hel.life > 0:
                    if home.life == 100 and hel.life == 100:
                        display_text = 'Perfect!:)'
                        self.message_display2(display_text, self.display_text_pos_win)
                    else:
                        display_text = 'Home' + str(int(home.life))
                        self.message_display2(display_text, self.display_text_pos_home)

                        display_text = 'Vehicle' + str(int(hel.life))
                        self.message_display2(display_text, self.display_text_pos_hel)


                    self.draw_sprite2(info_winner)
                    if device.audio.sound_enabled: device.audio.sound_winer.play()

                    # print(var.map_settings[2])
                    pygame.display.update()
                    time.sleep(2)
                    # if re.search("map14", var.map_settings[2], flags=0):
                    if device.stats.level == 14:
                        finalScreen = final.AddScreen()
                        finalScreen.run()

                    device.stats.winner = True
                    device.stats.bullet_available = len(weapon.magazine) + 20

                else:
                    self.draw_sprite2(info_loser)

                    display_text = 'Try Again!'
                    self.message_display2(display_text, self.display_text_pos_lost)

                    if device.audio.sound_enabled: device.audio.sound_loser.play()
                    pygame.display.update()
                    time.sleep(3)
                    device.stats.winner = False

                #check point

            self.sent_msg(weapon, total_time, home.life)
            pygame.display.update()

            total_time += dt
            if total_time > 1000000: total_time = 0

            dt = pygame.time.get_ticks() - time_start

    def sent_msg(self, weapon,total_time, home_life):
        self.draw_selected((0, 0), (df.display_width, 40), 90, df.white)
        self.font1.color = df.green
        self.message_display('Zombies:' + str(device.stats.total - device.stats.killed),  self.zombie_txt_pos)
        self.font1.color = df.blue
        self.message_display('Killed:' + str(int(device.stats.experience)), self.exp_txt_pos)
        self.font1.color = df.white
        self.message_display('Home:' + str(int(home_life)), self.life_txt_pos)
        self.font1.color = df.orange
        self.message_display('Map:' + str(device.stats.level),self.map_txt_pos)
        self.font1.color = df.gold
        self.message_display('Time:' + str(int(total_time/1000)), self.time_txt_pos)
        self.font1.color = df.black
        self.message_display('Bullets:' + str(len(weapon.magazine)), self.bullet_txt_pos)
        self.font1.color = df.red

    def message_display2(self, text, center):
        self.font2.center = center
        self.font2.color = df.green
        self.font2.display_text(text)

