import pygame

width = 300
height = 600
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
bg = pygame.Surface((width, height))
font = pygame.font.Font("./assets/Roboto-Regular.ttf", 24)

sunstrike = pygame.image.load('./assets/sunstrike.png')
tornado = pygame.image.load('./assets/tornado.png')
icewall = pygame.image.load('./assets/icewall.png')
ghostwalk = pygame.image.load('./assets/ghostwalk.png')
forgespirit = pygame.image.load('./assets/forgespirit.png')
emp = pygame.image.load('./assets/emp.png')
deafenningblast = pygame.image.load('./assets/deafenningblast.png')
coldsnap = pygame.image.load('./assets/coldsnap.png')
chaosmeteor = pygame.image.load('./assets/chaosmeteor.png')
alacrity = pygame.image.load('./assets/alacrity.png')

abilities = {'sunstrike': sunstrike, 'tornado': tornado, 'icewall': icewall, 'ghostwalk': ghostwalk,
             'forgespirit': forgespirit, 'emp': emp, 'deafenningblast': deafenningblast,
             'coldsnap': coldsnap, 'chaosmeteor': chaosmeteor, 'alacrity': alacrity}

quas = pygame.image.load('./assets/quas.png')
wex = pygame.image.load('./assets/wex.png')
exort = pygame.image.load('./assets/exort.png')

pygame.mixer.music.load('./assets/music.mp3')
pygame.mixer.music.play()

invoke = pygame.mixer.Sound('./assets/invoke.ogg')

pygame.display.set_caption('QWE Trainer')
pygame.display.set_icon(pygame.image.load('./assets/icon.ico'))
