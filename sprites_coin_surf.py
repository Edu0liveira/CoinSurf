import random
import pygame
import math 
from config_coin_surf import SHARPEDO_WIDTH, SHARPEDO_HEIGHT, MOEDA_AMARELA_WIDTH, MOEDA_VERDE_WIDTH, MOEDA_VERMELHA_WIDTH, MOEDA_AMARELA_HEIGHT, MOEDA_VERDE_HEIGHT, MOEDA_VERMELHA_HEIGHT, IMG_DIR, WIDTH, HEIGHT, SURFISTA_HEIGHT,  SURFISTA_WIDTH, SURFISTA_UP_WIDTH, SURFISTA_UP_HEIGHT, SURFISTA_DOWN_WIDTH, SURFISTA_DOWN_HEIGHT
from assets_coin_surf import PIKACHU_IMG, PIKACHU_BOOST_IMG, SHARPEDO_IMG, SHARPEDO_BOOST_IMG, MOEDA_AMARELA_IMG, MOEDA_VERDE_IMG, MOEDA_VERMELHA_IMG, SURFISTA_IMG, SURFISTA_UP_IMG, SURFISTA_DOWN_IMG, load_assets

assets = load_assets()

class Pikachu(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[SURFISTA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        self.rect.bottom = ((HEIGHT/2)+40) 
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição do pikachu
        self.rect.y += self.speedy

        # Lógica para alterar o sprite do Pikachu dependendo da direção
        if self.speedy < 0:  # Se o Pikachu está se movendo para cima
            self.image = self.assets['surfista2']
        elif self.speedy > 0:  # Se o Pikachu está se movendo para baixo
            self.image = self.assets['surfista3']
        else:  # Se o Pikachu não está se movendo verticalmente
            self.image = self.assets['surfista1']

        # Mantém dentro da tela
        if self.rect.bottom < HEIGHT/2 + 60:
            self.rect.bottom = HEIGHT/2 + 60
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Pikachu_boost(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[PIKACHU_BOOST_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = 60
        self.rect.bottom = ((HEIGHT/2)+40) 
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
        # Atualização da posição do pikachu boost
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.bottom < HEIGHT/2 + 60:
            self.rect.bottom = HEIGHT/2 + 60
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Sharpedo(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets[SHARPEDO_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint(HEIGHT // 2, HEIGHT - SHARPEDO_HEIGHT)
        self.speedx = -6
        self.speedy = 0
        self.amplitude = 50  # Amplitude do movimento senoidal
        self.frequency = 0.1  # Frequência do movimento senoidal
        self.initial_y = self.rect.y  # Posição inicial em y

    def update(self):
        # Atualizando a posição do Sharpedo
        self.image = self.assets[SHARPEDO_IMG]
        self.rect.x += self.speedx

        # Movimento senoidal em y
        time = pygame.time.get_ticks() / 500  # Tempo em segundos
        self.rect.y = self.initial_y + self.amplitude * math.sin(self.frequency * 2 * math.pi * time)

        # Se o Sharpedo passar do final da tela, volta para a direita e sorteia
        # novas posições e velocidades
        if self.rect.right < 0:
            self.rect.x = WIDTH
            self.rect.y = random.randint(HEIGHT // 2, HEIGHT - SHARPEDO_HEIGHT)
            self.speedx = -6
            self.speedy = 0

class Sharpedo_boost(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[SHARPEDO_BOOST_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint((HEIGHT/2), HEIGHT-SHARPEDO_HEIGHT)
        self.speedx = -9
        self.speedy = 0

    def update(self):
        # Atualizando a posição do sharpedo
        self.image = assets[SHARPEDO_BOOST_IMG]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o sharpedo passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.image = assets[SHARPEDO_IMG]
            self.rect.x = WIDTH
            self.rect.y = random.randint((HEIGHT/2), HEIGHT - SHARPEDO_HEIGHT)
            self.speedx = -9
            self.speedy = 0

class Moeda_amarela(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MOEDA_AMARELA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint((HEIGHT/2), HEIGHT- MOEDA_AMARELA_HEIGHT)
        self.speedx = -5
        self.speedy = 0

    def update(self):
        # Atualizando a posição da moeda amarela
        self.image = assets[MOEDA_AMARELA_IMG]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se  a moeda amarela passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.image = assets[MOEDA_AMARELA_IMG]
            self.rect.x = WIDTH
            self.rect.y = random.randint((HEIGHT/2), HEIGHT- MOEDA_AMARELA_HEIGHT)
            self.speedx = -5
            self.speedy = 0

class Moeda_verde(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MOEDA_VERDE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint((HEIGHT/2), HEIGHT- MOEDA_AMARELA_HEIGHT)
        self.speedx = -5
        self.speedy = 0

    def update(self):
        # Atualizando a posição da moeda verde
        self.image = assets[MOEDA_VERDE_IMG]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a moeda verde passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.image = assets[MOEDA_VERDE_IMG]
            self.rect.x = WIDTH
            self.rect.y = random.randint((HEIGHT/2), HEIGHT- MOEDA_AMARELA_HEIGHT)
            self.speedx = -5
            self.speedy = 0

class Moeda_vermelha(pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MOEDA_VERMELHA_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.randint((HEIGHT/2), HEIGHT- MOEDA_AMARELA_HEIGHT)
        self.speedx = -3
        self.speedy = 0

    def update(self):
        # Atualizando a posição da moeda vermelha
        self.image = assets[MOEDA_VERMELHA_IMG]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se a moeda vermelha passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.image = assets[MOEDA_VERMELHA_IMG]
            self.rect.x = WIDTH
            self.rect.y = random.randint((HEIGHT/2), HEIGHT- MOEDA_AMARELA_HEIGHT)
            self.speedx = -3
            self.speedy = 0
