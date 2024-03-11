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
nivel_1 = pygame.image.load("nivel 1.png").convert_alpha()
persona = pygame.image.load("persona.png").convert_alpha()

# Definir el color granate
color_granate = (136, 0, 21)

# Crear máscara de color granate
color_granate_mask = pygame.mask.from_threshold(nivel_1, color_granate, (1, 1, 1, 255))

# Convertir imágenes en sprites
nivel_1_sprite = pygame.sprite.Sprite()
nivel_1_sprite.image = nivel_1
nivel_1_sprite.rect = nivel_1_sprite.image.get_rect()
persona_sprite = pygame.sprite.Sprite()
persona_sprite.image = persona
persona_sprite.rect = persona_sprite.image.get_rect()

# Posición inicial del personaje
posicion_personaje = [300, 522]

# Velocidad del personaje
velocidad_personaje = 0
velocidad_horizontal = 5
velocidad_salto = 10
gravedad = 0.5  # Factor de gravedad

# Variables de salto
salto = False
altura_salto = 0
velocidad_vertical = 0  # Agregar velocidad vertical

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_a or evento.key == K_LEFT:
                velocidad_personaje = -velocidad_horizontal
            elif evento.key == K_d or evento.key == K_RIGHT:
                velocidad_personaje = velocidad_horizontal
            elif evento.key == K_SPACE:
                if not salto:
                    salto = True
                    velocidad_vertical = -velocidad_salto  # Iniciar el salto con velocidad vertical hacia arriba
        elif evento.type == KEYUP:
            if evento.key == K_a or evento.key == K_LEFT or evento.key == K_d or evento.key == K_RIGHT:
                velocidad_personaje = 0

    # Movimiento horizontal del personaje
    posicion_personaje[0] += velocidad_personaje

    # Verificar colisión horizontal con el borde de la pantalla
    if (posicion_personaje[0] <= 0 and velocidad_personaje < 0) or \
            (posicion_personaje[0] + persona_sprite.rect.width >= ancho_pantalla and velocidad_personaje > 0):
        velocidad_personaje = 0

    # Verificar colisión horizontal con el color granate
    elif velocidad_personaje > 0:  # Movimiento hacia la derecha
        if not salto and color_granate_mask.overlap_area([persona_sprite.image.get_masks()], (posicion_personaje[0] + persona_sprite.rect.width, posicion_personaje[1] + persona_sprite.rect.height // 2)) > 0:
            velocidad_personaje = 0
    elif velocidad_personaje < 0:  # Movimiento hacia la izquierda
        if not salto and color_granate_mask.overlap_area([persona_sprite.image.get_masks()], (posicion_personaje[0], posicion_personaje[1] + persona_sprite.rect.height // 2)) > 0:
            velocidad_personaje = 0

    # Movimiento vertical del personaje (salto)
    if salto:
        altura_salto += velocidad_vertical
        velocidad_vertical += gravedad  # Aplicar gravedad
        if altura_salto >= 0:  # Si el personaje está en el suelo
            salto = False
            altura_salto = 0
            velocidad_vertical = 0  # Reiniciar velocidad vertical
        elif velocidad_vertical >= 0:  # Si el personaje está cayendo
            if color_granate_mask.overlap_area([persona_sprite.image.get_masks()], (posicion_personaje[0] + persona_sprite.rect.width // 2, posicion_personaje[1] + persona_sprite.rect.height + int(altura_salto))) > 0:
                salto = False
                altura_salto = 0
                velocidad_vertical = 0  # Reiniciar velocidad vertical

    # Dibujar el nivel y el personaje en la pantalla
    pantalla.fill((0, 0, 0))  # Limpiar pantalla
    pantalla.blit(nivel_1, (0, alto_pantalla - nivel_1.get_height()))  # Mostrar nivel
    pantalla.blit(persona, (posicion_personaje[0], posicion_personaje[1] + int(altura_salto)))  # Mostrar personaje

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el tiempo
    pygame.time.Clock().tick(60)



