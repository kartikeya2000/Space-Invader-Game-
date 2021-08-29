import pygame
import random
import math
from pygame import mixer

#initilize a pygame 
pygame.init()

#adding background image 
background = pygame.image.load("spacebg.jpg")

#Background sound 
mixer.music.load("TRG_Banks_-_Grandpas_great_escape.mp3")
mixer.music.play(-1)

#create a screen 
screen  = pygame.display.set_mode((800,600))

#Title and Icon
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load("project.png")
pygame.display.set_icon(icon)

#player
playerimg = pygame.image.load("space-invaders.png")
playerX = 360
playerY = 550
playerX_change = 0


#bullet
bulletimg = pygame.image.load("bullet.png")
bulletX= 0
bulletY = 520
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"


#enemy
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("monster.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg,(x, y))

def iscollosion(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+ math.pow(enemyY-bulletY,2))
    if distance<27:
        return True 
    else:
        return False 

def show_score(x,y):
    score = font.render("score :" + str(score_value), True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True,(255,255,255))
    screen.blit(over_text,(200,250))


#score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",20)
textX = 10
textY = 10

#Game over text
over_font = pygame.font.Font("freesansbold.ttf",64)

#game loop 
running = True
while running :

    # rgb = red, green,blue
    screen.fill((0,0,0))
  
    #Background persist
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False


        #if keystroke is pressed check whether its right or left 
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("Arrow+Swoosh+2.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)  

        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0
            
    playerX+=playerX_change

    #hitting players boundries conditions
    if playerX <=0:
        playerX =0
    if playerX >= 770:
        playerX = 770


    #enemy movement 
    for i in range(num_of_enemies):

        #Game over 
        if enemyY[i] > 250:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        if enemyX[i] >= 770:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

           
        #collosion
        collosion  = iscollosion(enemyX[i],enemyY[i],bulletX,bulletY)
        if collosion:
            #explosion_sound = mixer.Sound("")
            #explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,800)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i], i)

    #Bullet Movement
    if bulletY <= 0:
        bulletY = 520
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
   
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()





