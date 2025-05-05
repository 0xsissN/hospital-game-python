import pygame
import sys

from src.menu import main_menu
from src.entities.hospital import Hospital
from src.entities.player import Player
from src.entities.patient import Patient
from src.entities.doctor import Doctor
from src.entities.pharmacy import Pharmacy

pygame.init()

WIDTH, HEIGHT = 1100, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital RPG")

hospital = Hospital("Hospital central")
drPepe = Doctor("Dr. Pepe", "PEDIATRIA")
drKiko = Doctor("Dr. Kiko", "CARDIOLOGIA")
drGoomba = Doctor("Dr. Goomba", "NEUROLOGIA")
drBowser = Doctor("Dr. Bowser", "MEDICINA GENERAL")
fChavo = Pharmacy()

button_honguito = False
button_chavo = False
button_pepe = False
button_kiko = False
button_goomba = False
button_bowser = False

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLUE = (100, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

speed = 5

spawn = pygame.Rect(0, HEIGHT // 2, 40, 40)

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

dynamic_player = [
    mario,
    luigi,
    kamek,
    kong,
    peach,
    rosalina,
    waluigi,
    wario
]

create_player = pygame.Rect(((WIDTH // 2 + 200) + (WIDTH - (WIDTH // 2 + 200)) // 2) - 80, 50, 160, 50)  
des_create_player = True

players = [
    Player(pygame.Rect(0, HEIGHT // 2, 40, 40))
]

honguito = pygame.image.load('./assets/images/cstatic/honguito.png')
honguito = pygame.transform.scale(honguito, (50, 60))
honguito_rect = pygame.Rect(130, 30, 50, 60)

chavo = pygame.image.load('./assets/images/cstatic/chavo.png')
chavo = pygame.transform.scale(chavo, (70, 70))
chavo_rect = pygame.Rect(130, 575, 70, 70)

pepe = pygame.image.load('./assets/images/cstatic/pepe.png')
pepe = pygame.transform.scale(pepe, (60, 80))
pepe_rect = pygame.Rect(600, 50, 60, 80)

kiko = pygame.image.load('./assets/images/cstatic/kiko.png')
kiko = pygame.transform.scale(kiko, (60, 80))
kiko_rect = pygame.Rect(600, 220, 60, 80)

goomba = pygame.image.load('./assets/images/cstatic/goomba.png')
goomba = pygame.transform.scale(goomba, (50, 70))
goomba_rect = pygame.Rect(600, 400, 50, 70)

bowser = pygame.image.load('./assets/images/cstatic/bowser.png')
bowser = pygame.transform.scale(bowser, (60, 80))
bowser_rect = pygame.Rect(600, 580, 60, 80)

static_player = [
    {"player": honguito, "coordinate": honguito_rect.topleft},
    {"player": goomba, "coordinate": goomba_rect.topleft},
    {"player": pepe, "coordinate": pepe_rect.topleft},
    {"player": kiko, "coordinate": kiko_rect.topleft},
    {"player": chavo, "coordinate": chavo_rect.topleft},
    {"player": bowser, "coordinate": bowser_rect.topleft}
]

selected_player = 0

clock = pygame.time.Clock()

def draw_hospital():
    screen.fill(GRAY)
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH // 2 + 200, HEIGHT)) 

    pygame.draw.rect(screen, BLUE, (0, (HEIGHT // 4) - 20, 300, 20))     
    pygame.draw.rect(screen, BLUE, (300, 0, 20, (HEIGHT // 4)))
    pygame.draw.rect(screen, WHITE, (((850 - (WIDTH - (WIDTH // 2 + 100))) // 2) - 20, (HEIGHT // 4) - 20, 70, 20))
    
    pygame.draw.rect(screen, GREEN, (0, ((HEIGHT // 4) * 3) - 20, 300, 20))
    pygame.draw.rect(screen, GREEN, (300, ((HEIGHT // 4) * 3) - 20, 20, (HEIGHT // 4) + 20))
    pygame.draw.rect(screen, WHITE, (((850 - (WIDTH - (WIDTH // 2 + 100))) // 2) - 20, ((HEIGHT // 4) * 3) - 20, 70, 20))

    pygame.draw.rect(screen, RED, (450, 0, 20, HEIGHT))
    pygame.draw.rect(screen, RED, (450, (HEIGHT // 4) - 20, 300, 20))
    pygame.draw.rect(screen, RED, (450, ((HEIGHT // 4) * 2) - 20, 300, 20))
    pygame.draw.rect(screen, RED, (450, ((HEIGHT // 4) * 3) - 20, 300, 20))

    pygame.draw.rect(screen, WHITE, (450, 50, 20, 60))
    pygame.draw.rect(screen, WHITE, (450, 220, 20, 60))
    pygame.draw.rect(screen, WHITE, (450, 400, 20, 60))
    pygame.draw.rect(screen, WHITE, (450, 580, 20, 60))
    
    font = pygame.font.SysFont(None, 24)
    
    txtReception = font.render("RECEPCION", True, (0, 0, 0))
    screen.blit(txtReception, (10, 10))

    txtPediatrics = font.render("PEDIATRIA", True, (0, 0, 0))
    screen.blit(txtPediatrics, (600, 10))
    
    txtCardiology = font.render("CARDIOLOGIA", True, (0, 0, 0))
    screen.blit(txtCardiology, (600, 185))
    
    txtNeurology = font.render("NEUROLOGIA", True, (0, 0, 0))
    screen.blit(txtNeurology, (600, 360))
    
    txtGeneralMedicine = font.render("MEDICINA GENERAL", True, (0, 0, 0))
    screen.blit(txtGeneralMedicine, (575, 535))
    
    txtPharmacy = font.render("FARMACIA", True, (0, 0, 0))
    screen.blit(txtPharmacy, (10, 675))

    if des_create_player:
        pygame.draw.rect(screen, WHITE, create_player)
        txtButton = font.render('Crear personaje', True, (0, 0, 0))
        screen.blit(txtButton, (create_player.x + 15, create_player.y + 18))

    if button_honguito:
        pygame.draw.rect(screen, WHITE, create_player)
        txtInteraction = font.render('Iniciar registro', True, (0, 0, 0))
        screen.blit(txtInteraction, (create_player.x + 15, create_player.y + 18))

    if button_chavo:
        pygame.draw.rect(screen, WHITE, create_player)
        txtInteraction = font.render('Realizar compra', True, (0, 0, 0))
        screen.blit(txtInteraction, (create_player.x + 15, create_player.y + 18))
    
    if button_pepe:
        pygame.draw.rect(screen, WHITE, create_player)
        txtInteraction = font.render('Hablar con Pepe', True, (0, 0, 0))
        screen.blit(txtInteraction, (create_player.x + 15, create_player.y + 18))

    if button_kiko:
        pygame.draw.rect(screen, WHITE, create_player)
        txtInteraction = font.render('Hablar con Kiko', True, (0, 0, 0))
        screen.blit(txtInteraction, (create_player.x + 15, create_player.y + 18))

    if button_goomba:
        pygame.draw.rect(screen, WHITE, create_player)
        txtInteraction = font.render('Hablar con Goomba', True, (0, 0, 0))
        screen.blit(txtInteraction, (create_player.x + 10, create_player.y + 18))

    if button_bowser:
        pygame.draw.rect(screen, WHITE, create_player)
        txtInteraction = font.render('Hablar con Bowser', True, (0, 0, 0))
        screen.blit(txtInteraction, (create_player.x + 5, create_player.y + 18))

def draw_dinamyc_player():
    for i, player in enumerate(players):
        image = dynamic_player[i % len(dynamic_player)]
        screen.blit(image, player.rect.topleft)

def draw_static_player():
    for i in static_player:
        screen.blit(i["player"], i["coordinate"])
    
def player_interaction():
    global button_honguito, button_chavo, button_pepe, button_kiko, button_goomba, button_bowser, des_create_player

    player = players[selected_player]
    
    button_honguito = player.rect.colliderect(honguito_rect)
    button_chavo = player.rect.colliderect(chavo_rect)
    button_pepe = player.rect.colliderect(pepe_rect)
    button_kiko = player.rect.colliderect(kiko_rect)
    button_goomba = player.rect.colliderect(goomba_rect)
    button_bowser = player.rect.colliderect(bowser_rect)

    des_create_player = not any([button_honguito, button_chavo, button_pepe, button_kiko, button_goomba, button_bowser])
    
def move_player():
    global selected_player

    keys = pygame.key.get_pressed()
    player = players[selected_player]
    rect = player.rect

    new_x = rect.x
    new_y = rect.y

    if keys[pygame.K_LEFT]:
        new_x -= speed
    if keys[pygame.K_RIGHT]:
        new_x += speed
    if keys[pygame.K_UP]:
        new_y -= speed
    if keys[pygame.K_DOWN]:
        new_y += speed

    if 0 <= new_x <= WIDTH - rect.width:
        rect.x = new_x
    if 0 <= new_y <= HEIGHT - rect.height:
        rect.y = new_y

def register_patient():
    name = input("Ingrese su nombre: ")
    age = int(input("Ingrese su edad: "))
    money = int(input("Con cuanto dinero va a entrar: "))
    
    player = players[selected_player]
    player.patient = Patient(name, age, money)

    if player.patient.age < 18:
        print("Doctor asignado Dr. Pepe, especialidad PEDIATRIA")
        drPepe.assignedPatient(player.patient)
    else:
        print("Tomando sintomas:")
        doctor = hospital.assignedDoctor()

        if doctor.name == "Dr. Kiko":
            print(f"Doctor asignado {doctor.name}, especialidad {doctor.speciality}")
            drKiko.assignedPatient(player.patient)
        elif doctor.name == "Dr. Goomba":
            print(f"Doctor asignado {doctor.name}, especialidad {doctor.speciality}")
            drGoomba.assignedPatient(player.patient)
        elif doctor.name == "Dr. Bowser":
            print(f"Doctor asignado {doctor.name}, especialidad {doctor.speciality}")
            drBowser.assignedPatient(player.patient)
        else:
            print("No existe esa especialidad")
        
def select_player():
    global selected_player, button_honguito, button_chavo, button_pepe, button_kiko, button_goomba, button_bowser, des_create_player

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_1:
                if len(players) >= 1:
                    selected_player = 0
            if event.key == pygame.K_2:
                if len(players) >= 2:
                    selected_player = 1
            if event.key == pygame.K_3:
                if len(players) >= 3:
                    selected_player = 2
            if event.key == pygame.K_4:
                if len(players) >= 4:
                    selected_player = 3
            if event.key == pygame.K_5:
                if len(players) >= 5:
                    selected_player = 4
            if event.key == pygame.K_6:
                if len(players) >= 6:
                    selected_player = 5
            if event.key == pygame.K_7:
                if len(players) >= 7:
                    selected_player = 6
            if event.key == pygame.K_8:
                if len(players) >= 8:
                    selected_player = 7
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if des_create_player and create_player.collidepoint(event.pos):
                if len(players) < 8:  
                    new_player = Player(pygame.Rect(spawn.x, spawn.y, 40, 40))
                    players.append(new_player)

            if button_honguito and create_player.collidepoint(event.pos):
                player = players[selected_player]
                if player.patient is None:
                    register_patient()
                else:
                    print(f"{player.patient.name} ya está registrado.")

            if button_chavo and create_player.collidepoint(event.pos):
                player = players[selected_player]
                if player.patient is None:
                    print("No se ha registrado en el hospital")
                else:
                    fChavo.processPurchase(player.patient)
            
            if button_pepe and create_player.collidepoint(event.pos):
                drPepe.attendPatient()

            if button_kiko and create_player.collidepoint(event.pos):
                drKiko.attendPatient()
                
            if button_goomba and create_player.collidepoint(event.pos):
                drGoomba.attendPatient()
                
            if button_bowser and create_player.collidepoint(event.pos):
                drBowser.attendPatient()
                
while True:
    action = main_menu()
    if action == "play":
        while True:
            select_player()
            move_player()

            draw_hospital()
            draw_dinamyc_player()
            draw_static_player()
            player_interaction()

            pygame.display.flip()

            clock.tick(60)

    elif action == "exit":
        pygame.quit()
        break



