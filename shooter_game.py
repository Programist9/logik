# Импорты
import pygame
from random import randint
pygame.init()
# Создание 
win_h = 500
win_w = 700
window = pygame.display.set_mode((win_w, win_h))
background = pygame.transform.scale(
     pygame.image.load("galaxy.jpg"),
     (win_w, win_h) )
pygame.display.set_caption('                                                                                          Space')
# Обновление экрана управление
clock = pygame.time.Clock()
# Музыка
pygame.mixer.music.load('space.ogg')
pygame.mixer.music.set_volume(0.03)
pygame.mixer.music.play(-1)
fire_sound = pygame.mixer.Sound('fire.ogg')
fire_sound.set_volume(0.1)
reload_sound = pygame.mixer.Sound('reload.mp3')
reload_sound.set_volume(0.4)
lose_sound = pygame.mixer.Sound('lose.mp3')
lose_sound.set_volume(0.4)
win_sound = pygame.mixer.Sound('win.mp3')
win_sound.set_volume(0.4)
# Классы
class game_sprite():
    def __init__(self,x,y,w,h,image):
        self.rect = pygame.Rect(x,y,w,h)
        image = pygame.transform.scale(image,(w,h))
        self.image = image
    def update(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
class player(game_sprite):
    def __init__(self,x,y,w,h,image,speed):
        self.rect = pygame.Rect(x,y,w,h)
        image = pygame.transform.scale(image,(w,h))
        self.image = image
        self.speed = speed

    def move(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_d]:
            if self.rect.right <= 680:
                self.rect.x += self.speed
        if k[pygame.K_a]:
            if self.rect.x >= 20:
                self.rect.x -= self.speed
    def shoot():
            fire_sound.play()
            self_bullet = bullet(Player.rect.x, Player.rect.y, 20, 40,bullet_img,6)

    def update(self):
        window.blit(self.image, (self.rect.x,self.rect.y))    
class enemy(game_sprite):
    def __init__(self,x,y,w,h,image,speed):
        super().__init__(x,y,w,h,image)
        self.speed = speed
    def move(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y >= win_h:
            lost += 1
            self.rect.x = randint(50, win_w - 50)
            self.rect.y = 0
bullets = []
class bullet(game_sprite):
    def __init__(self,x,y,w,h,image,speed):
        super().__init__(x,y,w,h,image)
        self.speed = speed
        bullets.append(self)
    def move(self):
        self.rect.y -= self.speed
        if self.rect.y <= -20:
            bullets.remove(self)
# Переменые
player_x = 310
lost = 0
game = True
finish = False
FPS = 60
reload = 0
player_y = 390
score = 0
bullets_left = 5
# текст
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 80)
# Персонажи создаются
bullet_img = pygame.image.load('bullet.png')
player__img = pygame.image.load('rocket.png')
Player = player(player_x,player_y,40,70,player__img,4)
enemy_img = pygame.image.load('asteroid.png')
enemies = []
for i in range(5):
    Enemy = enemy(randint(50, win_w - 50), randint(-100, 0), 60, 60, enemy_img, randint(1,3))
    enemies.append(Enemy)
# Игровой цикл
while game:
    if finish == False:
        window.blit(background, (0,0))
        Player.move()
        Player.update()
        for Enemy in enemies:
            Enemy.move()
            Enemy.update()
            if Player.rect.colliderect(Enemy.rect) or lost >= 10:
                finish = True
                text3 = 'GAME OVER'
                text7 = 'R для перезапуска'
                text_surface3 = font2.render(text3, True, (255, 0, 0))
                text_rect3 = text_surface3.get_rect(center=(win_w // 2, win_h // 2))
                window.blit(text_surface3, text_rect3)
                lose_sound.play()
                text_surface7 = font.render(text7, True, (255, 0, 0))
                text_rect7 = text_surface3.get_rect(center=(win_w // 2, win_h // 2 + 50))
                window.blit(text_surface7, text_rect7)
            for Bullet in bullets:
                if Bullet.rect.colliderect(Enemy.rect):
                    score += 1
                    Enemy.rect.x, Enemy.rect.y = randint(50,win_w-50),randint(-100,0)
                    bullets.remove(Bullet)
        for Bullet in bullets:
            Bullet.move()
            Bullet.update()
        if score >= 30:
            finish = True
            text4 = 'YOU WIN'
            text_surface4 = font2.render(text4, True, (0, 255, 0))
            text_rect4 = text_surface4.get_rect(center=(win_w // 2, win_h // 2))
            window.blit(text_surface4, text_rect4)
            win_sound.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and finish:
            Player.rect.x = player_x
            Player.rect.y = player_y
            for Enemy in enemies:
                Enemy.rect.y = randint(-100,-20)
                Enemy.rect.x = randint(50, win_w - 50)
                Enemy.speed = randint(1,3)
            finish = False
            lost = 0
            score = 0
            bullets_left = 5
            bullets.clear()
        if bullets_left > 0:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not finish and reload >= 20:
                player.shoot()
                reload = 0
                bullets_left -= 1
            else:
                reload += 10
        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and not finish and bullets_left == 0:
            reload_sound.play()
            bullets_left = 5

    text = f'Пропущено: {lost}'
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(win_w // 7 - 5, 55))

    text1 = f'Счёт: {score}'
    text_surface1 = font.render(text1, True, (255, 255, 255))
    text_rect1 = text_surface1.get_rect(center=(win_w // 15, 20))

    text5 = f'Пули: {bullets_left}'
    text_surface5 = font.render(text5, True, (255, 255, 255))
    text_rect5 = text_surface5.get_rect(center=(win_w - 70, 20))
    window.blit(text_surface5, text_rect5)

    text6 = 'Перезарядка на Е'
    text_surface6 = font.render(text6, True, (255, 0, 0))
    text_rect6 = text_surface6.get_rect(center=(win_w - 110, 60))
    if bullets_left == 0:
        window.blit(text_surface6, text_rect6)

    window.blit(text_surface, text_rect)
    window.blit(text_surface1, text_rect1)
    pygame.display.update()
    clock.tick(FPS)