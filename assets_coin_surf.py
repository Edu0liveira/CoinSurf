import pygame
import os
from config_coin_surf import SHARPEDO_WIDTH, SHARPEDO_HEIGHT, MOEDA_AMARELA_WIDTH, MOEDA_AMARELA_HEIGHT, IMG_DIR, WIDTH, HEIGHT, FNT_DIR, SHARPEDO_BOOST_WIDTH, SHARPEDO_BOOST_HEIGHT, SURFISTA_HEIGHT, SURFISTA_WIDTH, SURFISTA_UP_HEIGHT,SURFISTA_UP_WIDTH, SURFISTA_DOWN_HEIGHT,SURFISTA_DOWN_WIDTH, MOEDA_NOVA_HEIGHT, MOEDA_NOVA_WIDTH

BACKGROUND = 'onda_coin_surf.jpg'
BACKGROUND2 = 'onda_tarde_coin_surf'
BACKGROUND3 = 'onda_noite__coin_surf'
SHARPEDO_IMG = 'sharpedo_coin_surf'
SHARPEDO_BOOST_IMG = 'sharpedo_boost_coin_surf'
MOEDA_AMARELA_IMG = 'moeda_amarela_coin_surf'
SCORE_FONT = 'score_font'
SURFISTA_IMG = 'surfista1'
SURFISTA_UP_IMG = 'surfista2'
SURFISTA_DOWN_IMG = 'surfista3'
MOEDA_AMARELA_FRAMES = 'moeda_amarela_frames'

pygame.display.init()
pygame.font.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))

f1 = pygame.image.load(os.path.join(IMG_DIR, 'moeda1.png')).convert_alpha()
f2 = pygame.image.load(os.path.join(IMG_DIR, 'moeda2.png')).convert_alpha()
f3 = pygame.image.load(os.path.join(IMG_DIR, 'moeda3.png')).convert_alpha()
f4 = pygame.image.load(os.path.join(IMG_DIR, 'moeda4.png')).convert_alpha()
f5 = pygame.image.load(os.path.join(IMG_DIR, 'moeda5.png')).convert_alpha()
f6 = pygame.image.load(os.path.join(IMG_DIR, 'moeda6.png')).convert_alpha()

def load_assets():
    assets = {}
    
    assets[SURFISTA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'surfista1.png')).convert_alpha()
    assets[SURFISTA_IMG] = pygame.transform.scale(assets[SURFISTA_IMG], (SURFISTA_WIDTH, SURFISTA_HEIGHT))
    
    assets[SURFISTA_UP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'surfista2.png')).convert_alpha()
    assets[SURFISTA_UP_IMG] = pygame.transform.scale(assets[SURFISTA_UP_IMG], (SURFISTA_UP_WIDTH, SURFISTA_UP_HEIGHT))
    
    assets[SURFISTA_DOWN_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'surfista3.png')).convert_alpha()
    assets[SURFISTA_DOWN_IMG] = pygame.transform.scale(assets[SURFISTA_DOWN_IMG], (SURFISTA_DOWN_WIDTH, SURFISTA_DOWN_HEIGHT))

    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR, 'onda_coin_surf.jpg')).convert()
    assets[BACKGROUND] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BACKGROUND2] = pygame.image.load(os.path.join(IMG_DIR, 'onda_tarde_coin_surf.jpg')).convert()
    assets[BACKGROUND2] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    assets[BACKGROUND3] = pygame.image.load(os.path.join(IMG_DIR, 'onda_noite__coin_surf.jpg')).convert()
    assets[BACKGROUND3] = pygame.transform.scale(assets[BACKGROUND], (WIDTH, HEIGHT))
    
    assets[SHARPEDO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'sharpedo_coin_surf.png')).convert_alpha()
    assets[SHARPEDO_IMG] = pygame.transform.scale(assets[SHARPEDO_IMG], (SHARPEDO_WIDTH, SHARPEDO_HEIGHT))
    assets[SHARPEDO_BOOST_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'sharpedo_boost_coin_surf.png')).convert_alpha()
    assets[SHARPEDO_BOOST_IMG] = pygame.transform.scale(assets[SHARPEDO_IMG], (SHARPEDO_BOOST_WIDTH, SHARPEDO_BOOST_HEIGHT))

    assets[MOEDA_AMARELA_FRAMES] = [f1, f2, f3, f4, f5, f6]
    assets[MOEDA_AMARELA_FRAMES] = [pygame.transform.scale(image, (MOEDA_NOVA_WIDTH, MOEDA_NOVA_HEIGHT)) for image in assets[MOEDA_AMARELA_FRAMES]]

       
    assets[MOEDA_AMARELA_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'moeda_amarela_coin_surf.png')).convert_alpha()
    assets[MOEDA_AMARELA_IMG] = pygame.transform.scale(assets[MOEDA_AMARELA_IMG], (MOEDA_AMARELA_WIDTH, MOEDA_AMARELA_HEIGHT))

    assets[SCORE_FONT] = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28)
    return assets

assets = load_assets()
print(assets)  