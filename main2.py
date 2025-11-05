import pygame
import random

pygame.init()

# --- Configuración de ventana ---
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extra-SScape - Horizontal Mode")

# --- Colores ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Jugador ---
player_width = 50
player_height = 50
player = pygame.Rect(10, HEIGHT // 2 - player_height // 2,
                     player_width, player_height)

# --- Imagenes --- 

player_img = pygame.image.load("Imagenes/nave.png").convert_alpha()
meteorito_img = pygame.image.load("Imagenes/meteorito.png").convert_alpha()
espacio_img = pygame.image.load("Imagenes/espacio.png").convert_alpha()


# --- Dimensiones de Img ---
player_size = (80, 50)
meteorito_size = (30, 30)

# --- Redimensión ---
player_img = pygame.transform.scale(player_img, player_size)
meteorito_img = pygame.transform.scale(meteorito_img, meteorito_size)
# --- Meteoritos ---
meteor_width = 30
meteor_height = 30
meteors = []

# --- Score ---
score = 0
font = pygame.font.Font(None, 36)
score_timer = 0

# --- Reloj ---
clock = pygame.time.Clock()

# --- Bucle Principal ---
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Movimiento del jugador ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5
    
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= 5
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += 5

    # --- Generación de meteoritos ---
    if len(meteors) < 10:
        meteor = pygame.Rect(WIDTH - meteor_width,
                             random.randint(0, HEIGHT - meteor_height),
                             meteor_width, meteor_height)
        meteors.append(meteor)

    # --- Movimiento de meteoritos ---
    for meteor in meteors[:]:
        meteor.x -= random.randint(3, 10)
        if meteor.right < 0:
            meteors.remove(meteor)
            score += 10  # +10 puntos por esquivar

    # --- Colisión ---
    for meteor in meteors:
        if player.colliderect(meteor):
            running = False  # Fin del juego

    # --- Actualización de Score por tiempo ---
    score_timer += clock.get_time()
    if score_timer >= 1000:  # cada segundo
        score += 1
        score_timer = 0

    # --- Dibujar ---
    screen.fill(BLACK)
    
    screen.blit(espacio_img, (0, 0))
    
    for meteor in meteors:
        screen.blit(meteorito_img, meteor)
        #pygame.draw.rect(screen, RED, meteor)
    
    screen.blit(player_img, player)
    #pygame.draw.rect(screen, WHITE, player)





    # Mostrar puntuación
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # --- Actualizar pantalla ---
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
