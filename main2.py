import pygame
import random

pygame.init()

# --- Configuración de ventana ---
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Extern_A - Horizontal Mode")

# --- Colores ---
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# --- Imágenes ---
player_img = pygame.image.load("Imagenes/A2.png").convert_alpha()
meteorito_img = pygame.image.load("Imagenes/eye1.png").convert_alpha()
espacio_img = pygame.image.load("Imagenes/sk3.png").convert_alpha()

# --- Redimensión de imágenes ---
player_img = pygame.transform.scale(player_img, (30, 30))
meteorito_img = pygame.transform.scale(meteorito_img, (80, 80))

font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# --- Función principal del juego ---
def game_loop():
    player = pygame.Rect(10, HEIGHT // 2 - 25, 50, 50)
    meteors = []
    score = 0
    score_timer = 0

    running = True
    while running:
        # --- Eventos ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Salir completamente del juego

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
        if len(meteors) < 6:
            meteor = pygame.Rect(
                WIDTH - 30,
                random.randint(0, HEIGHT - 30),
                30, 30
            )
            meteors.append(meteor)

        # --- Movimiento de meteoritos ---
        for meteor in meteors[:]:
            meteor.x -= random.randint(3, 10)
            if meteor.right < 0:
                meteors.remove(meteor)
                score += 10

        # --- Colisión ---
        for meteor in meteors:
            if player.colliderect(meteor):
                # Reiniciar el juego automáticamente
                return game_loop()  # ← reinicia todo desde cero

        # --- Aumento de score por tiempo ---
        score_timer += clock.get_time()
        if score_timer >= 1000:
            score += 1
            score_timer = 0

        # --- Dibujar ---
        screen.blit(espacio_img, (0, 0))
        for meteor in meteors:
            screen.blit(meteorito_img, meteor)
        screen.blit(player_img, player)

        # --- Mostrar puntuación ---
        score_text = font.render(f"Puntuación: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        # --- Actualizar pantalla ---
        pygame.display.flip()
        clock.tick(60)

# --- Iniciar el juego ---
game_loop()
pygame.quit()
