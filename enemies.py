import pygame
from constant import *

class Meteor:
    def __init__(self, x, y, size, image):
        self.size = size
        self.image = image  # ✅ Guardamos la imagen para usarla al dividir
        self.rect = pygame.Rect(x, y, METEOR_SIZE[size][0], METEOR_SIZE[size][1])
        self.img = pygame.transform.scale(image, METEOR_SIZE[size])

        # Velocidad basada en tamaño
        self.speed = {
            "grande": 2,
            "mediano": 3,
            "pequeño": 5
        }[size]

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.img, self.rect)

    def split(self):
        """Divide el meteorito en fragmentos más pequeños si es posible."""
        if self.size == "grande":
            return [
                Meteor(self.rect.x - 20, self.rect.y, "mediano", self.image),
                Meteor(self.rect.x + 20, self.rect.y, "mediano", self.image)
            ]
        elif self.size == "mediano":
            return [
                Meteor(self.rect.x - 15, self.rect.y, "pequeño", self.image),
                Meteor(self.rect.x + 15, self.rect.y, "pequeño", self.image)
            ]
        else:
            return []  # Los meteoritos pequeños no se dividen más

    def get_points(self):
        """Devuelve los puntos otorgados al destruir el meteorito."""
        return {
            "grande": 100,
            "mediano": 50,
            "pequeño": 25
        }[self.size]
