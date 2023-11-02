import pygame
import os

Width, Height = 900, 500
WIN = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(Width//2 - 5, 0, 10, Height)

FPS = 60
VEL = 5
Bullet_VEL = 7 
MAX_Bullets = 3
ROCKET_Width, Rocket_Height = 55, 40

Rocket_Two_HIT = pygame.USEREVENT + 1
Rocket_One_HIT = pygame.USEREVENT + 2

ROCKET_ONE_IMAGE = pygame.image.load(os.path.join('Assets', 'Rocket 1.png'))   
ROCKET_ONE_IMAGE = pygame.transform.rotate(pygame.transform.scale(ROCKET_ONE_IMAGE, (ROCKET_Width, Rocket_Height)), 90)
ROCKET_TWO_IMAGE = pygame.image.load(os.path.join('Assets', 'Rocket 2.png'))
ROCKET_TWO_IMAGE = pygame.transform.rotate(pygame.transform.scale(ROCKET_TWO_IMAGE, (ROCKET_Width, Rocket_Height)), 270)

def draw_window(red, yellow, Rocket_One_bullets, Rocket_Two_bullets):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(ROCKET_ONE_IMAGE, (yellow.x, yellow.y))
    WIN.blit(ROCKET_TWO_IMAGE, (red.x, red.y))

    for bullet in Rocket_One_bullets:
          pygame.draw.rect(WIN, RED, bullet)

    for bullet in Rocket_Two_bullets:
          pygame.draw.rect(WIN, YELLOW, bullet)

    pygame.display.update() 

def ROCKET_ONE_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: # LEFT
            yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # RIGHT
            yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0 - 15: # UP
            yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < Height: # DOWN
            yellow.y +=  VEL    

def ROCKET_TWO_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # LEFT
            red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL - red.width - 360 < BORDER.x: # RIGHT
            red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #  
            red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < Height: # DOWN
            red.y +=  VEL

def handle_bullets(Rocket_Two_bullets, Rocket_One_bullets, yellow, red):
      for bullet in Rocket_Two_bullets:
            bullet.x += Bullet_VEL
            if red.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(Rocket_Two_HIT))
                  Rocket_Two_bullets.remove (bullet)

      for bullet in Rocket_One_bullets:
            bullet.x += Bullet_VEL
            if yellow.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(Rocket_One_HIT))
                  Rocket_One_bullets.remove (bullet)
                 

        
def main():
    red = pygame.Rect(700, 300, ROCKET_Width, Rocket_Height)
    yellow = pygame.Rect(100, 300, ROCKET_Width, Rocket_Height)      
   
    Rocket_One_bullets = []
    Rocket_Two_bullets = []


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LCTRL and len(Rocket_Two_bullets) < MAX_Bullets:
                       bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2, 2, 10, 5)
                       Rocket_Two_bullets.append(bullet)
                       
                 if event.key == pygame.K_RCTRL and len(Rocket_One_bullets) < MAX_Bullets:
                       bullet = pygame.Rect(red.x, red.y + red.height//2, 2, 10, 5)
                       Rocket_One_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        ROCKET_ONE_handle_movement(keys_pressed, yellow)
        ROCKET_TWO_handle_movement(keys_pressed, red)
        draw_window(red, yellow, Rocket_One_bullets, Rocket_Two_bullets)
    
    pygame.quit()

if __name__ == "__main__":
    main()