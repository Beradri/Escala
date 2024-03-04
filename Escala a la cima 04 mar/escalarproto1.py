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
posicion_personaje = [300, 522]

# Velocidad del personaje
velocidad_personaje = 0
velocidad_horizontal = 5
velocidad_salto = 10
gravedad = 0.5  # Factor de gravedad

# Colores
color_granate = (136, 0, 21)

# Variables de salto
salto = False
altura_salto = 0

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
        elif evento.type == KEYUP:
            if evento.key == K_a or evento.key == K_LEFT or evento.key == K_d or evento.key == K_RIGHT:
                velocidad_personaje = 0

    # Movimiento horizontal del personaje
    posicion_personaje[0] += velocidad_personaje

    # Verificar colisión horizontal
    if (posicion_personaje[0] <= 0 and velocidad_personaje < 0) or \
            (posicion_personaje[0] + persona.get_width() >= ancho_pantalla and velocidad_personaje > 0):
        velocidad_personaje = 0
    elif velocidad_personaje > 0:  # Movimiento hacia la derecha
        if not salto and nivel1.get_at((posicion_personaje[0] + persona.get_width(), posicion_personaje[1] + persona.get_height() // 2 + int(altura_salto))) == color_granate:
            velocidad_personaje = 0
    elif velocidad_personaje < 0:  # Movimiento hacia la izquierda
        if not salto and nivel1.get_at((posicion_personaje[0], posicion_personaje[1] + persona.get_height() // 2 + int(altura_salto))) == color_granate:
            velocidad_personaje = 0

    # Movimiento vertical del personaje (salto)
    if salto:
        altura_salto -= velocidad_salto
        velocidad_salto -= gravedad  # Aplicar gravedad

        # Nueva condición para detener la caída cuando toca el color granate por debajo
        if velocidad_salto <= 0 and nivel1.get_at((posicion_personaje[0] + persona.get_width() // 2, posicion_personaje[1] + persona.get_height() + 1)) == color_granate:
            salto = False
            altura_salto = 0
            velocidad_salto = 10  # Reiniciar velocidad de salto

        # Resto del código de salto sin cambios

    # Dibujar el nivel y el personaje en la pantalla
    pantalla.fill((0, 0, 0))  # Limpiar pantalla
    pantalla.blit(nivel1, (0, alto_pantalla - nivel1.get_height()))  # Mostrar nivel
    pantalla.blit(persona, (posicion_personaje[0], posicion_personaje[1] + int(altura_salto)))  # Mostrar personaje

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el tiempo
    pygame.time.Clock().tick(60)

#la colisión horizontal no funciona, y al saltar, la fase de caida no detecta que toca el color granate y por lo tanto cae fuera de loslímites de la pantalla


