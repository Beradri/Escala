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
posicion_personaje = [ancho_pantalla // 2 - persona.get_width() // 2, 522]

# Velocidad del personaje
velocidad_personaje = 5
velocidad_horizontal = 0  # Velocidad horizontal inicial

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
                velocidad_horizontal = -velocidad_personaje
            elif evento.key == K_d or evento.key == K_RIGHT:
                velocidad_horizontal = velocidad_personaje
            elif evento.key == K_SPACE:
                if not salto:
                    salto = True
                    fase_salto = 0
        elif evento.type == KEYUP:
            if evento.key == K_a or evento.key == K_LEFT or evento.key == K_d or evento.key == K_RIGHT:
                velocidad_horizontal = 0  # Detener movimiento horizontal al soltar la tecla

    # Movimiento horizontal continuo
    posicion_personaje[0] += velocidad_horizontal

    # Función de salto
    if salto:
        if fase_salto == 0:  # Fase de subida
            altura_salto -= velocidad_salto
            if altura_salto <= -100:
                fase_salto = 1
        else:  # Fase de caída
            # Verificar colisión con color granate durante la caída
            if posicion_personaje[1] + persona.get_height() + altura_salto < nivel1.get_height():
                if nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() + altura_salto - offset_nivel)) == color_granate:
                    salto = False
                    altura_salto = 0
            altura_salto += velocidad_salto
            if altura_salto >= 0:
                salto = False
                altura_salto = 0

    # Verificar colisión lateral con color granate
    if velocidad_horizontal > 0:  # Movimiento hacia la derecha
        if posicion_personaje[0] + persona.get_width() >= ancho_pantalla:
            posicion_personaje[0] = ancho_pantalla - persona.get_width()
        else:
            y_check = posicion_personaje[1] + persona.get_height() // 2 + altura_salto - offset_nivel
            if 0 <= y_check < nivel1.get_height() and nivel1.get_at((posicion_personaje[0] + persona.get_width(), y_check)) == color_granate:
                posicion_personaje[0] -= velocidad_personaje
    elif velocidad_horizontal < 0:  # Movimiento hacia la izquierda
        if posicion_personaje[0] <= 0:
            posicion_personaje[0] = 0
        else:
            y_check = posicion_personaje[1] + persona.get_height() // 2 + altura_salto - offset_nivel
            if 0 <= y_check < nivel1.get_height() and nivel1.get_at((posicion_personaje[0], y_check)) == color_granate:
                posicion_personaje[0] += velocidad_personaje

    # Verificar colisión vertical con color granate
    if salto:  # Verificar colisión durante el salto
        if fase_salto == 0:  # Fase de subida
            if 0 <= posicion_personaje[1] + altura_salto - offset_nivel < nivel1.get_height():
                if nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + altura_salto - offset_nivel)) == color_granate:
                    altura_salto = 0
        else:  # Fase de caída
            if 0 <= posicion_personaje[1] + persona.get_height() + altura_salto - offset_nivel < nivel1.get_height():
                if nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() + altura_salto - offset_nivel)) == color_granate:
                    salto = False
                    altura_salto = 0

    else:  # Verificar colisión cuando no está en salto
        if 0 <= posicion_personaje[1] + persona.get_height() - offset_nivel < nivel1.get_height():
            if nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() - offset_nivel)) == color_granate:
                altura_salto = 0

    # Dibujar el nivel y el personaje en la pantalla
    pantalla.blit(nivel1, (0, -offset_nivel))  # Ajustar la posición del nivel para mostrarlo correctamente
    pantalla.blit(persona, (posicion_personaje[0], posicion_personaje[1] + altura_salto))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el tiempo
    pygame.time.Clock().tick(60)



