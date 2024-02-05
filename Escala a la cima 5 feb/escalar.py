import pygame
from pygame.locals import *
import sys
import time
import random

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
posicion_personaje = [300, 550]

# Velocidad y dirección del personaje
velocidad_personaje = 5
direccion_personaje = 0  # 0: quieto, 1: izquierda, 2: derecha

# Variables de salto
saltando = False
altura_salto = 0
salto_normal = 50
salto_reducido = 30
tiempo_salto = 1.5
tiempo_salto_reducido = 15
tiempo_salto_actual = 0

# Colores
color_granate = (136, 0, 21)
color_verde = (34, 177, 76)
color_azul = (0, 162, 232)

# Desplazamiento vertical del nivel
offset_nivel = 0

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == KEYDOWN:
            if evento.key == K_a:
                direccion_personaje = 1
            elif evento.key == K_d:
                direccion_personaje = 2
            elif evento.key == K_SPACE and not saltando:
                saltando = True

        elif evento.type == KEYUP:
            if evento.key == K_a or evento.key == K_d:
                direccion_personaje = 0

    # Actualizar posición del personaje
    if direccion_personaje == 1 and posicion_personaje[0] > 0:
        posicion_personaje[0] -= velocidad_personaje
    elif direccion_personaje == 2 and posicion_personaje[0] < ancho_pantalla - persona.get_width():
        posicion_personaje[0] += velocidad_personaje

    # Verificar colisiones durante el salto
    if saltando:
        if tiempo_salto_actual > 0:
            tiempo_salto_actual -= 1
            if nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() + altura_salto - offset_nivel)) in [color_granate, color_verde, color_azul]:
                saltando = False
                altura_salto = 0
        else:
            saltando = False
            altura_salto = 0

    # Dibujar el nivel y el personaje en la pantalla
    pantalla.blit(nivel1, (0, -offset_nivel))
    pantalla.blit(persona, (posicion_personaje[0], posicion_personaje[1] - offset_nivel))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el tiempo
    pygame.time.Clock().tick(60)

    # Restablecer dirección de salto después del tiempo de salto reducido
    if tiempo_salto_actual == 0:
        tiempo_salto_actual = tiempo_salto_reducido
        salto_normal = 50

    # Saltar
    if saltando:
        altura_salto += salto_normal
        if nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() + altura_salto - offset_nivel)) == color_verde:
            altura_salto += 600 - salto_normal  # Salto directo al verde
            saltando = False
        elif nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() + altura_salto - offset_nivel)) == color_azul:
            salto_normal = 30  # Salto reducido en azul

    # Actualizar el desplazamiento vertical del nivel
    offset_nivel += velocidad_personaje


#Arreglar