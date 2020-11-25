import pygame
import defaults as df
import datetime # for time

print('Loading vars')
assetsDir = 'assets/' # I made like this so that sprites can be found easily

map_gap = df.display_height * 0.08 # This map gap, because i have total 14 map

gameDisplay = pygame.display.set_mode( (  df.display_width, df.display_height ) ) # By calling defaults i set the window here

fps = 30 # frame rate

# map_settings = [ "", 0,assetsDir + "map1.jpg"]

clock = pygame.time.Clock()
t0 = datetime.datetime.now()
# total = 10
