from pygame import *
import time as t
from random import randint
import random 
import pygame

wh = 1400
ww = 600

font.init()
pygame.init()

window = display.set_mode((wh,ww))
display.set_caption("Dinosaur game")

class game_sprite(sprite.Sprite):
    def __init__(self, x, y, w, h, s, p):
        self.x = x
        self.y = y
        self.s = s
        self.p = image.load(str(p))
        self.p = transform.scale(self.p, (w,h))
        self.rect = self.p.get_rect()
        self.jumping = False
        self.falling = False
        self.stop = True
        self.gravity = 7
        self.score = 0
    def draw(self):
        window.blit(self.p, (self.x, self.y))

class dinosaur(game_sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_SPACE] or keys[K_UP] and self.stop:
            self.Jumping()
        if self.jumping:
            self.y -= 10
            if self.y <= 200:
                self.Falling()
        elif self.falling:
            self.y += self.gravity * self.s
            if self.y >= 350:
                self.Stop()

    def animate(self, loop):
        self.setTexture((loop + 1) % 7)

    def Jumping(self):
        self.jumping = True
        self.stop = False

    def Falling(self):
        self.falling = True
        self.jumping = False

    def Stop(self):
        self.stop = True
        self.falling = False

    def setTexture(self, number):
        self.p = image.load(f"dino{number}.png")
        self.p = transform.scale(self.p, (100,100))

class obstacle(game_sprite):
    def move(self,x):
        self.x -= self.s
        if self.x <= 0:
            self.score += 1
            self.x = x

class Text():
    def __init__(self,x,y,w,h,color):
        self.x = x
        self.y = y
        self.rect = Rect(x,y,w,h)
        self.color = color
    def set_text(self, text, size, color):
        self.text = font.SysFont("verdana", size).render(text, True, color)
    def draw(self):
        window.blit(self.text, (self.x,self.y))

player = dinosaur(70,350,150,150,1,'dino1.png')

background = image.load("background.png")
background = transform.scale(background, (wh, ww))

score_label = Text(10,10,50,10,(0,0,0))
score_label.set_text("Score: ", 20, (0,0,0))

scorer = Text(80,10,50,10, (0,0,0))
scorer.set_text("0", 20, (0,0,0))

font1 = font.Font(None, 50)
text_win = font1.render("YOU WIN", True, (0,0,0))

counter = 0
clock_tick = time.Clock()

cactus1 = obstacle(random.randint(1200,1400),360,70,70,6,"cactus.png")
cactus2 = obstacle(random.randint(800,1000),360,70,70,6,"cactus.png")
cactus3 = obstacle(random.randint(400,600),360,70,70,6,"cactus.png")

obstacles = []

obstacles.append(cactus1)
obstacles.append(cactus2)
obstacles.append(cactus3)

run = True
while run:
    window.fill((255,255,255))

    window.blit(background, (0,0))
    key_quit = key.get_pressed()

    for e in event.get():
        if e.type == QUIT or key_quit[K_ESCAPE]:
            run = False

    player.draw()
    player.move()
    player.update()

    score_label.draw()
    scorer.draw()

    player.animate(counter)

    for c in obstacles:
        c.move(random.randint(1300,1400))
        c.draw()

    scorer.set_text(f"{counter // 10}", 20, (0,0,0))

    counter += 1
    clock_tick.tick(30)

    display.update()
