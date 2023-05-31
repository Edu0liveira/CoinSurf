#Coin Surf
# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config_coin_surf import WIDTH, HEIGHT, INIT, MANUAL, GAME, FINAL, QUIT
from init_screen_coin_surf import init_screen
from game_screen_coin_surf import game_screen
from manual_screen import manual_screen
from final_screen_coin_surf import final_screen

pygame.init()
pygame.mixer.init()
pygame.display.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('COIN SURF')


class Score:
    def __init__(self): 
        self.points = 0

score = Score()

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    if state == MANUAL:
        state = manual_screen(window)
    if state == GAME:
        state = game_screen(window, score)
    if state == FINAL:
        state = final_screen(window, score)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados