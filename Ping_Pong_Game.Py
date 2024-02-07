from pygame import *

class Gamesprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
    def update_y(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

    def update_x(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

window = display.set_mode((700, 500))
window.fill((200, 200, 255))
display.set_caption('ping pong game')

racket_1 = Player('racket.png', 30, 200, 4, 50, 150)
racket_2 = Player('racket.png', 620, 200, 4, 50, 150)
tennis_ball = Gamesprite('Ball.png', 200, 200, 4, 50, 50)
game = True
clock = time.Clock()
FPS = 60
finish = False

font.init()
font1 = font.Font(None, 70)
win1 = font1.render('Right PLayer WINS!!!!', True, (0, 200, 200))
win2 = font1.render('Left Player WINS!!!!', True, (0, 200, 200))

speed_x = 8
speed_y = 6

player1_score = 0
player2_score = 0

font2 = font.Font(None, 25)
 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.fill((200, 200, 255))
        window.blit(font2.render(str(player1_score), True, (200, 0, 200)), (30, 30))
        window.blit(font2.render(str(player2_score), True, (200, 0, 200)), (620, 30))
        racket_1.update_x()
        racket_2.update_y()
        tennis_ball.rect.x += speed_x
        tennis_ball.rect.y += speed_y
        if sprite.collide_rect(racket_1, tennis_ball) or sprite.collide_rect(racket_2, tennis_ball):
            speed_x *= -1
            speed_y *= 1

        if tennis_ball.rect.y > 500 - 50 or tennis_ball.rect.y <0:
            speed_y *= -1

        if tennis_ball.rect.x < 0:
            finish = True
            #window.blit(win1, (200, 200))
            player2_score += 1
            window.blit(font2.render(str(player2_score), True, (200, 0, 200)), (620, 30))

        
        if tennis_ball.rect.x > 700:
            finish = True 
           # window.blit(win2, (200, 200))
            player1_score += 1
            window.blit(font2.render(str(player1_score), True, (200, 0, 200)), (30, 30))  

        if player1_score == 10:
            tennis_ball = Gamesprite('Ball.png', 100000, 200, 4, 50, 50)
            window.blit(win2, (200, 200))
            finish = True
        
        if player2_score == 10:
            tennis_ball = Gamesprite('Ball.png', 100000, 200, 4, 50, 50)
            window.blit(win1, (200, 200))
            finish = True

        racket_1.reset()
        racket_2.reset()
        tennis_ball.reset()
    else:
        tennis_ball = Gamesprite('Ball.png', 200, 200, 4, 50, 50)
        finish = False
    display.update()
    clock.tick(FPS)

