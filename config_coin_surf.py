from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets_coin_surf', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets_coin_surf', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets_coin_surf', 'font')

# Dados gerais do jogo.
WIDTH = 770 # Largura da tela
HEIGHT = 410 # Altura da tela
FPS = 90 # Frames por segundo

# Define tamanhos
SHARPEDO_WIDTH = 85
SHARPEDO_HEIGHT = 85
SHARPEDO_BOOST_WIDTH = 80
SHARPEDO_BOOST_HEIGHT = 80
PIKACHU_WIDTH = 62
PIKACHU_HEIGHT = 62
PIKACHU_BOOST_HEIGHT = 62
PIKACHU_BOOST_WIDTH = 62
MOEDA_AMARELA_WIDTH = 50
MOEDA_AMARELA_HEIGHT = 50
MOEDA_VERDE_WIDTH = 50
MOEDA_VERDE_HEIGHT = 50
MOEDA_VERMELHA_WIDTH = 50
MOEDA_VERMELHA_HEIGHT = 50

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
INIT2 = 1
GAME = 2
QUIT = 3