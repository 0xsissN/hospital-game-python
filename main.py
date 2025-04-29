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

spawn = pygame.Rect(0, ALTO // 2, 40, 40)

mario = pygame.image.load('./assets/images/cdynamic/mario.png')  
mario = pygame.transform.scale(mario, (40, 40)) 

luigi = pygame.image.load('./assets/images/cdynamic/luigi.png')
luigi = pygame.transform.scale(luigi, (40, 40))

kamek = pygame.image.load('./assets/images/cdynamic/kamek.png')
kamek = pygame.transform.scale(kamek, (40, 40))

kong = pygame.image.load('./assets/images/cdynamic/kong.png')
kong = pygame.transform.scale(kong, (40, 40))

peach = pygame.image.load('./assets/images/cdynamic/peach.png')
peach = pygame.transform.scale(peach, (40, 40))

rosalina = pygame.image.load('./assets/images/cdynamic/rosalina.png')
rosalina = pygame.transform.scale(rosalina, (40, 40))

waluigi = pygame.image.load('./assets/images/cdynamic/waluigi.png')
waluigi = pygame.transform.scale(waluigi, (40, 40))

wario = pygame.image.load('./assets/images/cdynamic/wario.png')
wario = pygame.transform.scale(wario, (40, 40))

jugador_dinamico = [
    mario,
    luigi,
    kamek,
    kong,
    peach,
    rosalina,
    waluigi,
    wario
]

crear_personaje = pygame.Rect(ANCHO // 2 + 220, 50, 150, 50)  

jugadores = [
    pygame.Rect(0, ALTO // 2, 40, 40)  
]

honguito = pygame.image.load('./assets/images/cstatic/honguito.png')
honguito = pygame.transform.scale(honguito, (50, 60))
honguito_rect = pygame.Rect(130, 30, 50, 60)

chavo = pygame.image.load('./assets/images/cstatic/chavo.png')
chavo = pygame.transform.scale(chavo, (70, 70))
chavo_rect = pygame.Rect(130, 750, 70, 70)

pepe = pygame.image.load('./assets/images/cstatic/pepe.png')
pepe = pygame.transform.scale(pepe, (60, 80))
pepe_rect = pygame.Rect(700, 50, 60, 80)

kiko = pygame.image.load('./assets/images/cstatic/kiko.png')
kiko = pygame.transform.scale(kiko, (60, 80))
kiko_rect = pygame.Rect(700, 280, 60, 80)

goomba = pygame.image.load('./assets/images/cstatic/goomba.png')
goomba = pygame.transform.scale(goomba, (50, 70))
goomba_rect = pygame.Rect(700, 500, 50, 70)

bowser = pygame.image.load('./assets/images/cstatic/bowser.png')
bowser = pygame.transform.scale(bowser, (60, 80))
bowser_rect = pygame.Rect(700, 750, 60, 80)

jugador_estatico = [
    {"personaje": honguito, "coordenada": honguito_rect.topleft},
    {"personaje": goomba, "coordenada": goomba_rect.topleft},
    {"personaje": pepe, "coordenada": pepe_rect.topleft},
    {"personaje": kiko, "coordenada": kiko_rect.topleft},
    {"personaje": chavo, "coordenada": chavo_rect.topleft},
    {"personaje": bowser, "coordenada": bowser_rect.topleft}
]

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
    
    pygame.draw.rect(pantalla, VERDE, crear_personaje)
    font = pygame.font.SysFont(None, 24)
    texto_boton = font.render('Crear personaje', True, (0, 0, 0))
    pantalla.blit(texto_boton, (crear_personaje.x + 10, crear_personaje.y + 15))

def personajes_dinamicos():
    for i, jugador in enumerate(jugadores):
        imagen = jugador_dinamico[i % len(jugador_dinamico)]  
        pantalla.blit(imagen, jugador.topleft)

def personajes_estaticos():
    for i in jugador_estatico:
        pantalla.blit(i["personaje"], i["coordenada"])
    
def interaccion_personajes():
    jugador = jugadores[jugador_seleccionado]
    if jugador.colliderect(honguito_rect):
        print("Honguito") 
    elif jugador.colliderect(goomba_rect):
        print("Gommba")
    elif jugador.colliderect(pepe_rect):
        print("Pepe")
    elif jugador.colliderect(kiko_rect):
        print("Kiko")
    elif jugador.colliderect(chavo_rect):
        print("Chavo")
    elif jugador.colliderect(bowser_rect):
        print("Bowser")
    
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
            if evento.key == pygame.K_4:
                jugador_seleccionado = 3
            if evento.key == pygame.K_5:
                jugador_seleccionado = 4
            if evento.key == pygame.K_6:
                jugador_seleccionado = 5
            if evento.key == pygame.K_7:
                jugador_seleccionado = 6
            if evento.key == pygame.K_8:
                jugador_seleccionado = 7

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if crear_personaje.collidepoint(evento.pos):
                if len(jugadores) < 8:  
                    nuevo = pygame.Rect(spawn.x, spawn.y, 40, 40)
                    jugadores.append(nuevo)
    
while True:
    seleccionar_jugador()
    mover_jugador()

    dibujar_hospital()
    personajes_dinamicos()
    personajes_estaticos()
    interaccion_personajes()

    pygame.display.flip()

    reloj.tick(60)
