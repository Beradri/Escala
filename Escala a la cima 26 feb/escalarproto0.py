import pygame
from pygame.locals import *
import sys

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
ancho_pantalla = 600
alto_pantalla = 600
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Cargar imágenes
nivel1 = pygame.image.load("nivel 1.png").convert_alpha()
persona = pygame.image.load("persona.png").convert_alpha()

# Ajustar posición del nivel
offset_nivel = nivel1.get_height() - alto_pantalla

# Posición inicial del personaje
posicion_personaje = [300, 522]

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Dibujar el nivel y el personaje en la pantalla
    pantalla.blit(nivel1, (0, 0), (0, offset_nivel, ancho_pantalla, alto_pantalla))
    pantalla.blit(persona, posicion_personaje)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el tiempo
    pygame.time.Clock().tick(60)
