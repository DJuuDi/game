from pygame import *
from pygame.sprite import _Group

#створи вікно гри

window = display.set_mode((700,500))
FPS = 80
clock = time.Clock()
#задай фон сцени

bg = image.load('background.png')
bg = transform.scale(bg, (700,500))
#створи 2 спрайти та розмісти їх на сцені

image_1 = image.load('sprite1.png')
image_2 = image.load('sprite2.png')

class Player(sprite.Sprite):
    def __init__(self, sprite_img, width, height, x, y):
        self.image = transform.scale(sprite_img, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player_1 = Player(player1_img, 70, 70, 300, 300)
player_2 = Player(player2_img, 70, 70, 500, 300)
#оброби подію «клік за кнопкою "Закрити вікно"»
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    
    window.blit(bg, (0,0))
    window.blit(player_1.image,player_1.rect)
    window.blit(player_2.image,player_2.rect)
    display.update()
    clock.tick(FPS)