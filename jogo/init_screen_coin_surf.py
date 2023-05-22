import pygame
import random
from os import path
import config_coin_surf
import assets_coin_surf

def init_screen(screen):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(config_coin_surf.IMG_DIR, 'tela_inicio_coin_surf.jpg')).convert()
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
                state = config_coin_surf.GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(config_coin_surf.BLACK)
        screen.blit(background, background_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state