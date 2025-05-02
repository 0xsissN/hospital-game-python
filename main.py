import pygame
import sys

from src.entities.hospital import Hospital
from src.entities.player import Player
from src.entities.patient import Paciente
from src.entities.doctor import Doctor
from src.entities.pharmacy import Farmacia

pygame.init()

ANCHO, ALTO = 1300, 900
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Hospital RPG")

hospital = Hospital("Hospital central")
drPepe = Doctor("Dr Pepe", "PEDIATRIA")
drKiko = Doctor("Dr. Kiko", "CARDIOLOGIA")
drGoomba = Doctor("Dr. Goomba", "NEUROLOGIA")
drBowser = Doctor("Dr. Bowser", "MEDICINA GENERAL")
fChavo = Farmacia()

boton_honguito = False
boton_chavo = False
boton_pepe = False
boton_kiko = False
boton_goomba = False
boton_bowser = False

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

crear_personaje = pygame.Rect(((ANCHO // 2 + 200) + (ANCHO - (ANCHO // 2 + 200)) // 2) - 80, 50, 160, 50)  
des_crear_personaje = True

jugadores = [
    Player(pygame.Rect(0, ALTO // 2, 40, 40))
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
    
    font = pygame.font.SysFont(None, 24)
    
    if des_crear_personaje:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_boton = font.render('Crear personaje', True, (0, 0, 0))
        pantalla.blit(texto_boton, (crear_personaje.x + 15, crear_personaje.y + 18))

    if boton_honguito:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_interaccion = font.render('Iniciar registro', True, (0, 0, 0))
        pantalla.blit(texto_interaccion, (crear_personaje.x + 15, crear_personaje.y + 18))

    if boton_chavo:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_interaccion = font.render('Realizar compra', True, (0, 0, 0))
        pantalla.blit(texto_interaccion, (crear_personaje.x + 15, crear_personaje.y + 18))
    
    if boton_pepe:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_interaccion = font.render('Hablar con Pepe', True, (0, 0, 0))
        pantalla.blit(texto_interaccion, (crear_personaje.x + 15, crear_personaje.y + 18))

    if boton_kiko:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_interaccion = font.render('Hablar con Kiko', True, (0, 0, 0))
        pantalla.blit(texto_interaccion, (crear_personaje.x + 15, crear_personaje.y + 18))

    if boton_goomba:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_interaccion = font.render('Hablar con Goomba', True, (0, 0, 0))
        pantalla.blit(texto_interaccion, (crear_personaje.x + 10, crear_personaje.y + 18))

    if boton_bowser:
        pygame.draw.rect(pantalla, BLANCO, crear_personaje)
        texto_interaccion = font.render('Hablar con Bowser', True, (0, 0, 0))
        pantalla.blit(texto_interaccion, (crear_personaje.x + 5, crear_personaje.y + 18))

def personajes_dinamicos():
    for i, jugador in enumerate(jugadores):
        imagen = jugador_dinamico[i % len(jugador_dinamico)]
        pantalla.blit(imagen, jugador.rect.topleft)

def personajes_estaticos():
    for i in jugador_estatico:
        pantalla.blit(i["personaje"], i["coordenada"])
    
def interaccion_personajes():
    global boton_honguito, boton_chavo, boton_pepe, boton_kiko, boton_goomba, boton_bowser, des_crear_personaje

    jugador = jugadores[jugador_seleccionado]
    
    boton_honguito = jugador.rect.colliderect(honguito_rect)
    boton_chavo = jugador.rect.colliderect(chavo_rect)
    boton_pepe = jugador.rect.colliderect(pepe_rect)
    boton_kiko = jugador.rect.colliderect(kiko_rect)
    boton_goomba = jugador.rect.colliderect(goomba_rect)
    boton_bowser = jugador.rect.colliderect(bowser_rect)

    des_crear_personaje = not any([boton_honguito, boton_chavo, boton_pepe, boton_kiko, boton_goomba, boton_bowser])
    
def mover_jugador():
    global jugador_seleccionado

    teclas = pygame.key.get_pressed()
    jugador = jugadores[jugador_seleccionado]
    rect = jugador.rect

    nueva_x = rect.x
    nueva_y = rect.y

    if teclas[pygame.K_LEFT]:
        nueva_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        nueva_x += velocidad
    if teclas[pygame.K_UP]:
        nueva_y -= velocidad
    if teclas[pygame.K_DOWN]:
        nueva_y += velocidad

    if 0 <= nueva_x <= ANCHO - rect.width:
        rect.x = nueva_x
    if 0 <= nueva_y <= ALTO - rect.height:
        rect.y = nueva_y

def registrar_paciente():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    dinero = int(input("Con cuanto dinero va a entrar: "))
    sintomas = []

    while True:
        x = int(input("Agregar sintoma 1. Si | 2. No: "))
        if x == 1:
            s = input("Ingrese sintoma: ")
            sintomas.append(s)
        elif x == 2:
            break
        else:
            print("Esa opcion no existe")
    
    jugador = jugadores[jugador_seleccionado]
    jugador.patient = Paciente(nombre, edad, dinero, sintomas)
    doctor = hospital.asignarDoctor(jugador.patient)

    if doctor.nombre == "Dr. Pepe":
        print(f"Doctor asignado {doctor.nombre}, especialidad {doctor.especialidad}")
        drPepe.pacienteAsignado(jugador.patient)

def seleccionar_jugador():
    global jugador_seleccionado, boton_honguito, boton_chavo, boton_pepe, boton_kiko, boton_goomba, boton_bowser, des_crear_personaje

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
            if des_crear_personaje and crear_personaje.collidepoint(evento.pos):
                if len(jugadores) < 8:  
                    nuevo = Player(pygame.Rect(spawn.x, spawn.y, 40, 40))
                    jugadores.append(nuevo)

            if boton_honguito and crear_personaje.collidepoint(evento.pos):
                jugador = jugadores[jugador_seleccionado]
                if jugador.patient is None:
                    registrar_paciente()
                else:
                    print(f"{jugador.patient.nombre} ya está registrado.")

            if boton_chavo and crear_personaje.collidepoint(evento.pos):
                jugador = jugadores[jugador_seleccionado]
                if jugador.patient is None:
                    print("No se ha registrado en el hospital")
                else:
                    fChavo.procesarCompra(jugador.patient)
            
            if boton_pepe and crear_personaje.collidepoint(evento.pos):
                drPepe.atenderPaciente()

            if boton_kiko and crear_personaje.collidepoint(evento.pos):
                drKiko.atenderPaciente()
                
            if boton_goomba and crear_personaje.collidepoint(evento.pos):
                drGoomba.atenderPaciente()
                
            if boton_bowser and crear_personaje.collidepoint(evento.pos):
                drBowser.atenderPaciente()
                
while True:
    seleccionar_jugador()
    mover_jugador()

    dibujar_hospital()
    personajes_dinamicos()
    personajes_estaticos()
    interaccion_personajes()

    pygame.display.flip()

    reloj.tick(60)
