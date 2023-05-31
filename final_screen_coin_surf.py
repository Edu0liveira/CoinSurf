import pygame
from os import path
import config_coin_surf
from config_coin_surf import WIDTH, HEIGHT, YELLOW
from config_coin_surf import WIDTH, HEIGHT
from assets_coin_surf import load_assets, SCORE_FONT
import assets_coin_surf



def final_screen(screen):

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(config_coin_surf.IMG_DIR, 'tela_final_coin_surf.jpg')).convert()
    background_rect = background.get_rect()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    
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
                if event.key == pygame.K_r:
                    state = config_coin_surf.INIT
                    running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(config_coin_surf.BLACK)
        screen.blit(background, background_rect)

        # Mostrando o score
        text_surface = assets_coin_surf.assets[SCORE_FONT].render("Sua pontuação foi de:", True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        screen.blit(text_surface, text_rect)

        '''text_surface = assets_coin_surf.assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  180)
        screen.blit(text_surface, text_rect)'''

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state