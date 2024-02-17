# Импорты
import pygame
from random import randint
pygame.init()
# Создание 
win_h = 500
win_w = 700
window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption('                                                                                          Ping-Pong')
clock = pygame.time.Clock()
# pygame.mixer.music.load('space.ogg')
# pygame.mixer.music.set_volume(0.03)
# pygame.mixer.music.play(-1)
# win_sound = pygame.mixer.Sound('win.mp3')
# win_sound.set_volume(0.4)
class game_sprite():
    def __init__(self,x,y,w,h,image):
        self.rect = pygame.Rect(x,y,w,h)
        image = pygame.transform.scale(image,(w,h))
        self.image = image
    def update(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
game = True
finish = False
FPS = 60
while game:
    if finish == False:
        window.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)