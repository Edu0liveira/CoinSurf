# Coin Surf
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config_coin_surf import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen_coin_surf import init_screen
from game_screen_coin_surf import game_screen

pygame.init()
pygame.mixer.init()
pygame.display.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pikachu_coin_surf.png')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
#