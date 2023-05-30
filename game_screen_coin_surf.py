import pygame
from config_coin_surf import FPS, WIDTH, HEIGHT, BLACK, YELLOW
from assets_coin_surf import load_assets, BACKGROUND, SCORE_FONT
from sprites_coin_surf import Pikachu, Sharpedo, Moeda_amarela, Moeda_verde, Moeda_vermelha

score2 = 0 

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Criando um grupo do Sharpedo e das moedas
    all_sprites = pygame.sprite.Group()
    all_sharpedo = pygame.sprite.Group()
    all_moedas_amarelas  = pygame.sprite.Group()
    all_moedas_verdes  = pygame.sprite.Group()
    all_moedas_vermelhas  = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_sharpedo'] = all_sharpedo
    groups['all_moedas_amarelas'] = all_moedas_amarelas
    groups['all_moedas_verdes'] = all_moedas_verdes
    groups['all_moedas_vermelhas'] = all_moedas_vermelhas

    # Carrega o fundo do jogo
    background = assets[BACKGROUND]
    # Redimensiona o fundo
    background_rect = background.get_rect()

    # Criando o Surfista
    player = Pikachu(groups, assets)
    all_sprites.add(player)
    # Criando os Sharpedos
    for i in range(1):
        sharpedo = Sharpedo(assets)
        all_sprites.add(sharpedo)
        all_sharpedo.add(sharpedo)
    # Criando as moedas amarelas
    for i in range(6):
        moeda_amarela = Moeda_amarela(assets)
        all_sprites.add(moeda_amarela)
        all_moedas_amarelas.add(moeda_amarela)

    DONE = 0
    PLAYING = 1
    CAIU = 2
    state = PLAYING

    keys_down = {}
    score = 0
    lives = 3
    
    green_coin_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(green_coin_timer, 10000)

    quantidade_de_moedas = 0

    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_UP:
                        player.speedy -= 5
                    if event.key == pygame.K_DOWN:
                        player.speedy += 5

                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_UP:
                            player.speedy += 5
                        if event.key == pygame.K_DOWN:
                            player.speedy -= 5
 
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos Sharpedos e moedas
        all_sprites.update()

        if state == PLAYING:
            # Verifica se houve colisão entre a moeda amarela e o Pikachu 
            hits = pygame.sprite.spritecollide(player, all_moedas_amarelas, True, pygame.sprite.collide_mask)
            for m in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                #assets[DESTROY_SOUND].play() DESCOMENTA DEPOIS
                m = Moeda_amarela(assets)
                all_sprites.add(m)
                all_moedas_amarelas.add(m)

                # Ganhou pontos!
                score += 1
                quantidade_de_moedas += 1
                if quantidade_de_moedas % 50 == 0:
                    lives += 1

            hits = pygame.sprite.spritecollide(player, all_moedas_verdes, True, pygame.sprite.collide_mask)
            for v in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                #assets[DESTROY_SOUND].play() DESCOMENTA DEPOIS
                v = Moeda_verde(assets)
                all_sprites.add(v)
                all_moedas_verdes.add(v)

                # Você ganhou uma vida!
                lives += 1

            hits = pygame.sprite.spritecollide(player, all_moedas_vermelhas, True, pygame.sprite.collide_mask)
            for vm in hits: # As chaves são os elementos do primeiro grupo (meteoros) que colidiram com alguma bala
                # O meteoro e destruido e precisa ser recriado
                #assets[DESTROY_SOUND].play() DESCOMENTA DEPOIS
                vm = Moeda_vermelha(assets)
                all_sprites.add(vm)
                all_moedas_vermelhas.add(vm)

                # A pontuação e a velocidade dobram!
                

                    

            # Verifica se houve colisão entre o Pikachu e o Sharpedo
            hits = pygame.sprite.spritecollide(player, all_sharpedo, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                player.kill()
                lives -= 1
                state = CAIU
                keys_down = {}

                # Cria um novo Sharpedo
                sharpedo = Sharpedo(assets)
                all_sprites.add(sharpedo)
                all_sharpedo.add(sharpedo)

        elif state == CAIU:
                if lives == 0:
                    state = DONE
                else:
                    state = PLAYING
                    player = Pikachu(groups, assets)
                    all_sprites.add(player)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        # Atualiza a posição da imagem de fundo.
        background_rect.x += -4
        # Se o fundo saiu da janela, faz ele voltar para dentro.
        if background_rect.right < 0:
            background_rect.x += background_rect.width
        # Desenha o fundo e uma cópia para a direita.
        # Assumimos que a imagem selecionada ocupa pelo menos o tamanho da janela.
        # Além disso, ela deve ser cíclica, ou seja, o lado esquerdo deve ser continuação do direito.
        window.blit(background, background_rect)
        # Desenhamos a imagem novamente, mas deslocada da largura da imagem em x.
        background_rect2 = background_rect.copy()
        background_rect2.x += background_rect2.width
        window.blit(background, background_rect2)

        # Desenhando sharpedo
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador