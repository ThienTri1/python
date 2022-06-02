from pygame import *
import random

font.init()

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire_sound = mixer.Sound('fire.ogg')

width = 1000
height = 700

win = display.set_mode((width, height))
display.set_caption("Shooter")

class game_sprite(sprite.Sprite):
    def __init__(self, w, h, x, y, speed, picture):
        self.w = w 
        self.h = h
        self.image = image.load(str(picture))
        self.image = transform.scale(self.image, (self.w,self.h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        super().__init__()
        self.x = x
        self.y = y
        self.speed = speed
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
    def delete(self):
        self.kill()

class Player(game_sprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed 
    def fire(self):
        bullet = Bullet(20,20,self.rect.centerx, self.rect.top, -5, 'bullet.png')
        bullets.add(bullet)

class Enemy(game_sprite):
    def update(self):
        self.rect.y += self.speed
        global missed
        if self.rect.y > height:
            self.rect.y = random.randint(0, 150)
            self.rect.x = random.randint(0, width)
            missed += 1

class Bullet(game_sprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

class Label():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = Rect(x,y,width,height)
        self.fill_color = color
    def set_text(self, text, fsize=12, text_color=(0,0,0)):
        self.image = font.SysFont('verdana', fsize).render(text, True, text_color)
    def draw(self, shift_x=0, shift_y=0):
        win.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

player = Player(100,100,400, 600, 10, 'rocket.png')

background = image.load('galaxy_2.jpg')
background = transform.scale(background, (width, height))

score = 0
missed = 0
goal = 1

score_text = Label(0,0,50,50,(255,255,255))
score_text.set_text("Your score: ", 36, (255,255,255))

scorer = Label(0,0,50,50, (255,255,255))
scorer.set_text("0", 36, (255,255,255))

missed_text = Label(0,0,50,50,(255,255,255))
missed_text.set_text("Missed: ", 36, (255,255,255))

misser = Label(0,0,50,50,(255,255,255))
misser.set_text(str(missed), 36, (255,255,255))

enemies = sprite.Group()
for e in range(1,6):
    enemy = Enemy(100,100, random.randint(0, width-100), random.randint(0, 150), 3, 'ufo_1.png')
    enemies.add(enemy)

font.init()
font1 = font.Font(None, 50)
text_lose = font1.render("YOU LOSE", True, (255,255,255))
text_win = font1.render("YOU WIN", True, (255,255,255))

bullets = sprite.Group()
finish = False
run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.fire()
                fire_sound.play()
    if not finish:
        collides = sprite.groupcollide(enemies, bullets, True, True)
        for c in collides:
            score += 1
            scorer.set_text(str(score), 36, (255,255,255))
            enemy = Enemy(100, 100, random.randint(0, width-50), random.randint(0, 150), 2, 'ufo_1.png')
            enemies.add(enemy)

        win.blit(background, (0,0))

        score_text.draw(20,20)
        scorer.draw(230,20)

        missed_text.draw(20,80)
        misser.set_text(str(missed), 36, (255,255,255))
        misser.draw(200, 80)

        player.reset()
        player.move()

        enemies.draw(win)
        enemies.update()
        
        bullets.update()
        bullets.draw(win)

        if missed >= 10 or sprite.spritecollide(player, enemies, False):
            finish = True
            win.blit(background, (0,0))
            win.blit(text_lose, (400, 350))

        if score >= 20: 
            finish = True
            win.blit(background, (0,0))
            win.blit(text_win, (400, 350))

        display.update()

