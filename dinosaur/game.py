import pygame
import random

WIDTH, HEIGHT = 900, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GROUND_HEIGHT =300

def run_game(player_name):
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dino Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    #dinosaur
    gravity = 1
    velocity = 0
    is_jumping = False
    dino_img = pygame.image.load("img/dino1.gif")
    dino_img = pygame.transform.scale(dino_img, (50, 50))
    dino = dino_img.get_rect()
    dino.topleft = (50, GROUND_HEIGHT - 50)

    #obstacles
    obstacles = []
    obstacle_timer = 0
    spawn_delay = random.randint(60, 120)

    #score 
    score = 0

    running = True
    while running:
        screen.fill(WHITE)
        pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quitI()
                return score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not is_jumping:
                    velocity = -15
                    is_jumping = True

        #dinosaur physics
        velocity += gravity
        dino.y += velocity
        if dino.y >= GROUND_HEIGHT - 50:
            dino.y = GROUND_HEIGHT - 50
            is_jumping = False

