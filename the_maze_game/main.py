from pygame import *
import pygame
# import time

height = 700
width = 900

win = display.set_mode((width,height))
display.set_caption("Labyrinth")
win.fill((51,255,255))

class game_sprite(sprite.Sprite):
    def __init__(self, picture, x, y, speed):
        super().__init__()
        self.image = image.load(str(picture))
        self.image = transform.scale(self.image, (50,50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    

class Player(game_sprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 28:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < 872:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 28:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 872:
            self.rect.y += self.speed 
    def collide(self):
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y

class Enemy(game_sprite):
    def move(self):
        self.rect.x += self.speed
        # self.rect.y += self.speed
        if self.rect.x <= width-70:
            self.speed = 1
        if self.rect.x >= 70:
            self.speed = -1

class Wall():
    def __init__(self, color, x, y, width, height):
        self.color = color
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        


cyborg = Enemy("cyborg.png", 300, 300, 0)
hero = Player("hero.png", 500, 500, 4)
color = (0,0,0)

treasure = game_sprite("trophy-1.png", 800,600,0)

wall1 = Wall(color, 0, 0, width, 30)
wall2 = Wall(color, 0, 0, 28, height)
wall3 = Wall(color, width-28, 0, 28, height)
wall4 = Wall(color, 0, height-28, width, 28)
wall5 = Wall(color, 260, 0, 28, 305)
wall6 = Wall(color, 525, 0, 28, 160)
wall7 = Wall(color, 0, 415, 100, 28)
wall8 = Wall(color, 350, 545, 28, 180)
wall9 = Wall(color, 530, 545, 28, 180)
wall10 = Wall(color, 715, 548, 200, 28)
wall11 = Wall(color, 440, 533, 200, 28)
wall12 = Wall(color, 100, 533, 185, 28)
wall13 = Wall(color, 795, 280, 100, 28)
wall14 = Wall(color, 260, 405, 28, 155)
wall15 = Wall(color, 440, 430, 28, 115)
wall16 = Wall(color, 612, 430, 28, 125)
wall17 = Wall(color, 260, 406, 110, 28)
wall18 = Wall(color, 529, 417, 196, 28)
wall19 = Wall(color, 173, 277, 28, 170)
wall20 = Wall(color, 348, 279, 28, 156)
wall21 = Wall(color, 528, 279, 28, 155)
wall22 = Wall(color, 705, 145, 28, 300)
wall23 = Wall(color, 795, 283, 28, 155)
wall24 = Wall(color, 90, 277, 285, 28)
wall25 = Wall(color, 440, 278, 110, 28)
wall26 = Wall(color, 90, 88, 28, 215)
wall27 = Wall(color, 90, 85, 118, 28)
wall28 = Wall(color, 175, 174, 110, 28)
wall29 = Wall(color, 363, 142, 100, 28)
wall30 = Wall(color, 435, 145, 28, 160)
wall31 = Wall(color, 618, 142, 28, 153)
wall32 = Wall(color, 618, 142, 198, 28)

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, 
        wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16,
        wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24,
        wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32]

font.init()
font = font.Font(None, 50)
text_lose = font.render("You lose", True, (0,0,0))
text_win = font.render("You win", True, (0,0,0))

clock = time.Clock()
FPS = 60
run = True
while run:

    # print(pygame.mouse.get_pos())

    for i in event.get():
        if i.type == QUIT:
            run = False

    win.fill((51,255,255))

    hero.update()
    hero.reset()

    cyborg.move()
    cyborg.reset()

    treasure.reset()

    for w in walls:
        w.draw()   

    if sprite.collide_rect(hero, cyborg):
        win.blit(text_lose, (width/2, height/2))

    if sprite.collide_rect(hero, treasure):
        win.blit(text_win, (width/2, height/2))

    for a in walls:
        if hero.rect.colliderect(a.rect):
            win.blit(text_lose, (width/2, height/2))
        # time.sleep(10)
        # run = False

    display.update()
    clock.tick(60)


    