import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extra-SScape")

#Colores Disponibles

BLACK					=			(  0,   0,   0)
DARK_BLUE				=			(  0,   0, 100)
BLUE					=			(  0,   0, 255)
DARK_GREEN			    =			(  0, 100,   0)
GREENISH_BLUE			=			(  0, 100, 100)
LIGHT_TURQUOISE		    =			(  0, 100, 255)
GREEN					=			(  0, 255,   0)
WATERY_GREEN			=			(  0, 255, 100)
CYAN					=			(  0, 255, 255)

RED						=			(255,   0,   0)
DARK_PINK				=			(255,   0, 100)
PINK					=			(255,   0, 255)
ORANGE			   	    =			(255, 100,   0)
RED_PINK				=			(255, 100, 100)
MAGENT				    =			(255, 100, 255)
YELLOW					=			(255, 255,   0)
LIGHT_YELLOW			=			(255, 255, 100)
WHITE					=			(255, 255, 255)

REDDISH_BROWN		    =			(100,   0,   0)
PURPLE					=			(100,   0, 100)
MUSTARD				    =			(100,   0, 255)
GREENISH_BROWN		    =			(100, 100,   0)
GREY					=			(100, 100, 100)
TURQUOISE				=			(100, 100, 255)

#Jugador

player_width = 50
player_height = 50
player = pygame.Rect(WIDTH // 2 - player_width // 2,
                     HEIGHT - player_height -10, player_width, player_height)

#Meteoritos

meteor_width = 30
meteor_height = 30
meteors = []

#Score
score = 0
font = pygame.font.Font(None, 36)  # Fuente por defecto tamaño 36
score_timer = 0  # Contador de tiempo para incrementar puntos

#Tiempo-Reloj
clock = pygame.time.Clock()


#Bucle Principal

runnining = True
while runnining:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            runnining = False

#Teclas

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5
    
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5

#Generación de Meteoritos
    if len(meteors) < 15:
        meteor = pygame.Rect(random.randint(0, WIDTH - meteor_width), 
                             0, meteor_width, meteor_height)  
        meteors.append(meteor) 


# Movimiento de Meteoros
    for meteor in meteors[:]:
        meteor.y += random.randint(1,10)
        if meteor.top > HEIGHT:
            meteors.remove(meteor)
            score += 1 

# Detector de Colisiones

    for meteor in meteors:
        if player.colliderect(meteor):
            runnining = False

#Color de pantalla

    screen.fill(BLACK)

#Character

    pygame.draw.rect(screen, WHITE, player)

#Draw Meteritos

    for meteor in meteors:
        pygame.draw.rect(screen, RED, meteor)

#Play Score
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))


#Actualizacion de pantalla
    pygame.display.flip()

#Frames

    clock.tick(60)

#Quit

pygame.quit()