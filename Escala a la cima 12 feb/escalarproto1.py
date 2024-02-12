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

# Posición inicial del personaje
posicion_personaje = [300, 200]  # Posición ajustada para mostrar el personaje por encima del nivel

# Velocidad del personaje
velocidad_personaje = 5

# Ajustar posición del nivel
offset_nivel = nivel1.get_height() - alto_pantalla

# Colores
color_granate = (136, 0, 21)

# Variables de salto
salto = False
fase_salto = 0
altura_salto = 0
velocidad_salto = 5

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_a or evento.key == K_LEFT:
                if posicion_personaje[0] > 0:
                    posicion_personaje[0] -= velocidad_personaje
            elif evento.key == K_d or evento.key == K_RIGHT:
                if posicion_personaje[0] < ancho_pantalla - persona.get_width():
                    posicion_personaje[0] += velocidad_personaje
            elif evento.key == K_SPACE:
                if not salto:
                    salto = True
                    fase_salto = 0

    # Función de salto
    if salto:
        if fase_salto == 0:  # Fase de subida
            altura_salto -= velocidad_salto
            if altura_salto <= -100:
                fase_salto = 1
        else:  # Fase de caída
            altura_salto += velocidad_salto
            if altura_salto >= 0:
                salto = False
                altura_salto = 0

    # Función de caída
    if not salto:
        # Verificar colisión con color granate
        collision = False
        for i in range(persona.get_height()):
            for j in range(persona.get_width()):
                if posicion_personaje[1] + i + altura_salto - offset_nivel < nivel1.get_height() and posicion_personaje[0] + j < nivel1.get_width():
                    if nivel1.get_at((posicion_personaje[0] + j, posicion_personaje[1] + i + altura_salto - offset_nivel)) == color_granate:
                        collision = True
                        break
            if collision:
                break
        if not collision:
            posicion_personaje[1] += 1

    # Dibujar el nivel y el personaje en la pantalla
    pantalla.blit(nivel1, (0, -offset_nivel))  # Ajustar la posición del nivel para mostrarlo correctamente
    pantalla.blit(persona, (posicion_personaje[0], posicion_personaje[1] + altura_salto))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el tiempo
    pygame.time.Clock().tick(60)

#Arreglar error, CGPT
