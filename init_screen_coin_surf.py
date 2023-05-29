import pygame
from os import path
from config_coin_surf import WIDTH, HEIGHT
import config_coin_surf
pygame.mixer.init()
musica=pygame.mixer.music.load('musica_padrao.mp3')
pygame.mixer.music.set_volume(.6)
pygame.mixer.music.play()

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(config_coin_surf.IMG_DIR, 'tela_inicio_coin_surf.jpg')).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(config_coin_surf.FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = config_coin_surf.QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = config_coin_surf.INIT2
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(config_coin_surf.BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state