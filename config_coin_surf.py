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
SHARPEDO_WIDTH = 95
SHARPEDO_HEIGHT = 95
SHARPEDO_BOOST_WIDTH = 80
SHARPEDO_BOOST_HEIGHT = 80

SURFISTA_WIDTH = 62
SURFISTA_HEIGHT = 62

SURFISTA_UP_WIDTH = 62
SURFISTA_UP_HEIGHT = 62

SURFISTA_DOWN_WIDTH = 62
SURFISTA_DOWN_HEIGHT = 62

MOEDA_AMARELA_WIDTH = 50
MOEDA_AMARELA_HEIGHT = 50
MOEDA_NOVA_WIDTH = 50
MOEDA_NOVA_HEIGHT = 50

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
MANUAL = 1
GAME = 2
FINAL = 3
QUIT = 4