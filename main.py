import pygame
import random
from constant import *
from armas import *
from enemies import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extra-SScape")

# --- Imágenes ---
player_img = pygame.image.load("Imagenes/nave.png").convert_alpha()
meteor_img = pygame.image.load("Imagenes/meteorito.png").convert_alpha()
background_img = pygame.image.load("Imagenes/espacio.png").convert()

# --- Redimensionar imágenes ---
player_img = pygame.transform.scale(player_img, PLAYER_SIZE)
meteor_img = pygame.transform.scale(meteor_img, (50, 50))

# --- Jugador ---
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE[0] // 2,
                     HEIGHT - PLAYER_SIZE[1] - 10,
                     PLAYER_SIZE[0], PLAYER_SIZE[1])

# --- Listas de objetos ---
meteors = []
projectiles = []

# --- Puntuación ---
score = 0
font = pygame.font.Font(None, 36)

# --- Control de disparos ---
last_shot = pygame.time.get_ticks()

# --- Reloj ---
clock = pygame.time.Clock()

# --- Bucle principal ---
running = True
while running:
    current_time = pygame.time.get_ticks()

    # --- Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Disparo
            if event.key == pygame.K_SPACE and current_time - last_shot > SHOOT_DELAY:
                last_shot = current_time
                if len(projectiles) < 5:
                    projectiles.append(projectile(player.centerx - 2, player.top))

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
    if len(meteors) < 5:
        size = random.choice(["grande", "mediano", "pequeño"])
        m = Meteor(
            random.randint(0, WIDTH - METEOR_SIZE[size][0]),
            -METEOR_SIZE[size][1],
            size, meteor_img)
        meteors.append(m)

    # --- Actualizar proyectiles ---
    for p in projectiles[:]:
        p.move()
        if p.rect.bottom < 0:
            projectiles.remove(p)

    # --- Actualizar meteoritos y colisiones ---
    for m in meteors[:]:
        m.move()
        if m.rect.top > HEIGHT:
            meteors.remove(m)
            continue

        # Colisión con proyectiles
        for p in projectiles[:]:
            if m.rect.colliderect(p.rect):
                # Eliminar proyectil y meteorito
                projectiles.remove(p)
                meteors.remove(m)
                score += m.get_points()

                # Fragmentar meteorito
                new_meteors = m.split()
                meteors.extend(new_meteors)
                break  # Salir del bucle de proyectiles para evitar error

        # Colisión con jugador
        if player.colliderect(m.rect):
            running = False
            break

    # --- Dibujar en pantalla ---
    screen.blit(background_img, (0, 0))
    screen.blit(player_img, player)

    for m in meteors:
        m.draw(screen)

    for p in projectiles:
        p.draw(screen)

    # --- Mostrar puntuación ---
    score_text = font.render(f"Puntuación: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
