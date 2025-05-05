import pygame

pygame.init()

WIDTH, HEIGHT = 1100, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hospital RPG")

PASTEL_BLUE = (173, 216, 230) 
WHITE = (255, 255, 255)
BUTTON_GREEN = (100, 200, 150)
BUTTON_RED = (220, 100, 100)
BUTTON_BLUE = (70, 130, 180)
TEXT_COLOR = (50, 50, 80)

try:
    source_title = pygame.font.Font(None, 72)
    button_font = pygame.font.Font(None, 42)
except:
    source_title = pygame.font.SysFont('arial', 72, bold=True)
    button_font = pygame.font.SysFont('arial', 42)

class Button:
    def __init__(self, x, y, width, height, text, normal_color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.current_color = normal_color
        self.surface_text = button_font.render(text, True, TEXT_COLOR)
        self.rect_text = self.surface_text.get_rect(center=self.rect.center)
        self.shade = pygame.Rect(x+4, y+4, width, height)
    
    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0, 30), self.shade, border_radius=10)
        pygame.draw.rect(surface, self.current_color, self.rect, border_radius=10)
        pygame.draw.rect(surface, (255, 255, 255, 50), self.rect, 2, border_radius=10)
        surface.blit(self.surface_text, self.rect_text)

    def verify_hover(self, pos):
        if self.rect.collidepoint(pos):
            self.current_color = self.hover_color
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            return True
        
        self.current_color = self.normal_color
        return False

def main_menu():
    start_button = Button(WIDTH//2 - 180, HEIGHT//2 - 50, 360, 70, "INICIAR JUEGO", BUTTON_GREEN, (120, 220, 170))
    exit_button = Button(WIDTH//2 - 180, HEIGHT//2 + 70, 360, 70, "SALIR", BUTTON_RED, (240, 120, 120))
    clock = pygame.time.Clock()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "exit"
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(mouse_pos):
                    return "play"
                
                if exit_button.rect.collidepoint(mouse_pos):
                    return "exit"

        start_button.verify_hover(mouse_pos)
        exit_button.verify_hover(mouse_pos)

        screen.fill(PASTEL_BLUE) 
        
        title = source_title.render("HOSPITAL ", True, TEXT_COLOR)
        shade_title = source_title.render("HOSPITAL", True, (100, 100, 150))
        
        screen.blit(shade_title, (WIDTH//2 - title.get_width()//2 + 3, HEIGHT//4 - 50 + 3))
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4 - 50))
        
        subtitle = button_font.render("Gestión de pacientes y recursos", True, TEXT_COLOR)
        screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, HEIGHT//4 + 40))
        
        start_button.draw(screen)
        exit_button.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
