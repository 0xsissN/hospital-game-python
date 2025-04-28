import pygame
import sys

pygame.init()

ANCHO, ALTO = 1300, 900
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hospital RPG")

BLANCO = (255, 255, 255)
GRIS = (200, 200, 200)
AZUL = (100, 100, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

velocidad = 5

jugadores = [
    pygame.Rect(0, ALTO // 2, 40, 40)  
]

mario = pygame.image.load('./assets/images/mario.png')  
mario = pygame.transform.scale(mario, (40, 40)) 

jugador_seleccionado = 0

reloj = pygame.time.Clock()

def dibujar_hospital():
    pantalla.fill(GRIS)
    pygame.draw.rect(pantalla, BLANCO, (0, 0, ANCHO // 2 + 200, ALTO)) 

    pygame.draw.rect(pantalla, AZUL, (0, (ALTO // 4) - 30, 850 - (ANCHO - (ANCHO // 2 + 100)), 30))     
    pygame.draw.rect(pantalla, AZUL, (850 - (ANCHO - (ANCHO // 2 + 100)), 0, 30, (ALTO // 4)))
    pygame.draw.rect(pantalla, BLANCO, (((850 - (ANCHO - (ANCHO // 2 + 100))) // 2) - 30, (ALTO // 4) - 30, 70, 30))
    
    pygame.draw.rect(pantalla, VERDE, (0, ((ALTO // 4) * 3) - 30, 850 - (ANCHO - (ANCHO // 2 + 100)), 30))
    pygame.draw.rect(pantalla, VERDE, (850 - (ANCHO - (ANCHO // 2 + 100)), ((ALTO // 4) * 3) - 30, 30, (ALTO // 4) + 30))
    pygame.draw.rect(pantalla, BLANCO, (((850 - (ANCHO - (ANCHO // 2 + 100))) // 2) - 30, ((ALTO // 4) * 3) - 30, 70, 30))

    pygame.draw.rect(pantalla, ROJO, (ANCHO - (ANCHO // 2 + 100) - 30, 0, 30, ALTO))
    pygame.draw.rect(pantalla, ROJO, (ANCHO - (ANCHO // 2 + 100), (ALTO // 4) - 30, 850 - (ANCHO - (ANCHO // 2 + 100)), 30))
    pygame.draw.rect(pantalla, ROJO, (ANCHO - (ANCHO // 2 + 100), ((ALTO // 4) * 2) - 30, 850 - (ANCHO - (ANCHO // 2 + 100)), 30))
    pygame.draw.rect(pantalla, ROJO, (ANCHO - (ANCHO // 2 + 100), ((ALTO // 4) * 3) - 30, 850 - (ANCHO - (ANCHO // 2 + 100)), 30))

    pygame.draw.rect(pantalla, BLANCO, (ANCHO - (ANCHO // 2 + 100) - 30, (((ALTO // 4) - 30) // 2) - 30, 30, 60))
    pygame.draw.rect(pantalla, BLANCO, (ANCHO - (ANCHO // 2 + 100) - 30, (((((ALTO // 4) * 2) - 30) // 2) - 30) + 110, 30, 60))
    pygame.draw.rect(pantalla, BLANCO, (ANCHO - (ANCHO // 2 + 100) - 30, (((((ALTO // 4) * 2) - 30) // 2) - 30) + 335, 30, 60))
    pygame.draw.rect(pantalla, BLANCO, (ANCHO - (ANCHO // 2 + 100) - 30, (((((ALTO // 4) * 2) - 30) // 2) - 30) + 575, 30, 60))

def dibujar_jugadores():
    for _, jugador in enumerate(jugadores):
        pantalla.blit(mario, jugador.topleft)  

def mover_jugador():
    global jugador_seleccionado

    teclas = pygame.key.get_pressed()

    jugador = jugadores[jugador_seleccionado]

    nueva_x = jugador.x
    nueva_y = jugador.y

    if teclas[pygame.K_LEFT]:
        nueva_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        nueva_x += velocidad
    if teclas[pygame.K_UP]:
        nueva_y -= velocidad
    if teclas[pygame.K_DOWN]:
        nueva_y += velocidad

    if 0 <= nueva_x <= ANCHO - jugador.width:
        jugador.x = nueva_x
    if 0 <= nueva_y <= ALTO - jugador.height:
        jugador.y = nueva_y

    for i, otro_jugador in enumerate(jugadores):
        if i != jugador_seleccionado and jugador.colliderect(otro_jugador):
            return

    jugadores[jugador_seleccionado] = jugador

def seleccionar_jugador():
    global jugador_seleccionado

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if evento.key == pygame.K_1:
                jugador_seleccionado = 0
            if evento.key == pygame.K_2:
                jugador_seleccionado = 1
            if evento.key == pygame.K_3:
                jugador_seleccionado = 2

while True:
    seleccionar_jugador()
    mover_jugador()

    dibujar_hospital()
    dibujar_jugadores()

    pygame.display.flip()

    reloj.tick(60)
