from consts import *
from utils import *
import random
import pygame

# Estrutura de dados para armazenar as posições dos personagens por cenário
POSICOES_BATALHA = {
    IMG_BATALHA_PRIMEIRA: {
        "personagens": [(90, 450), (120, 580), (90, 710)],
        "inimigo": (LARGURA - 100, ALTURA - 200)
    },
    IMG_BATALHA_TERCEIRA: {
        "personagens": [(90, 300), (120, 430), (90, 560)],
        "inimigo": (LARGURA - 100, ALTURA - 200)
    },
    IMG_BATALHA_QUINTA: {
        "personagens": [(90, 300), (120, 430), (90, 560)],
        "inimigo": (LARGURA - 300, ALTURA - 200)
    }
}

# Posições padrão, caso a imagem não esteja no dicionário
POSICOES_PADRAO = {
    "personagens": [(90, 300), (120, 430), (90, 560)],
    "inimigo": (LARGURA - 100, ALTURA - 200)
}

def desenhar_barra_de_vida(superficie, x, y, personagem):
    """Desenha a barra de vida de um personagem na tela."""
    vida_atual = max(0, personagem.vida_atual)
    
    try:
        percentual_vida = vida_atual / personagem.vida
    except ZeroDivisionError:
        percentual_vida = 0
        
    largura_vida_atual = LARGURA_BARRA_VIDA * percentual_vida
    
    pygame.draw.rect(superficie, VERMELHO, (x, y, LARGURA_BARRA_VIDA, ALTURA_BARRA_VIDA))
    
    if largura_vida_atual > 0:
        pygame.draw.rect(superficie, VERDE, (x, y, largura_vida_atual, ALTURA_BARRA_VIDA))
    
    texto_vida = FONTE_VIDA.render(f'{int(vida_atual)}/{personagem.vida}', True, BRANCO)
    pos_texto_x = x + (LARGURA_BARRA_VIDA - texto_vida.get_width()) / 2
    pos_texto_y = y + (ALTURA_BARRA_VIDA - texto_vida.get_height()) / 2
    
    superficie.blit(texto_vida, (pos_texto_x, pos_texto_y))


def batalha(personagens, turno):
    if pygame.mixer.get_init():
        pygame.mixer.fadeout(1000)
    
    imagem_batalha = random.choice(IMGS_BATALHA)
    
    posicoes = POSICOES_BATALHA.get(imagem_batalha, POSICOES_PADRAO)
    posicoes_personagens = posicoes["personagens"]
    pos_inimigo_x, pos_inimigo_y = posicoes["inimigo"]

    musica_batalha = random.choice(SOUNDS_BATTLE)
    inimigo = random.choice(list(BOSSES.values()))
    play_sound(musica_batalha)
    play_sound(SOUND_FIGHT, 10)

    turno_do_personagem = 0
    while not personagens[turno_do_personagem].vivo:
        turno_do_personagem = (turno_do_personagem + 1) % len(personagens)

    atacou = [not p.vivo for p in personagens]
    ataques_realizados = 0
    personagens_mortos = sum(1 for p in personagens if not p.vivo)
    
    inimigo_iniciou_turno = False
    tempo_inicio_delay_inimigo = 0
    
    while True:
        JANELA.blit(imagem_batalha, (X_INI, Y_INI))
        JANELA.blit(IMG_LOGO_FIGHT, (LARGURA // 2 - 125, 0))
        rect_quadro = JANELA.blit(IMG_QUADRO, (0, 0))
        personagens[turno_do_personagem].draw_at_position(JANELA, rect_quadro.centerx, rect_quadro.centery)
        
        if not inimigo.vivo:
            for p in personagens: p.reset()
            inimigo.reset()
            return True

        if personagens_mortos >= len(personagens):
            for p in personagens: p.reset()
            return False
        
        personagens_vivos_count = len(personagens) - personagens_mortos
        
        # --- Turno do Jogador ---
        if ataques_realizados < personagens_vivos_count:
            inimigo_iniciou_turno = False # Reseta a flag do inimigo durante o turno do jogador
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        atacou[turno_do_personagem] = True
                        ataques_realizados += 1
                        inimigo.reduz_vida(calcula_dano(personagens[turno_do_personagem]))
                        
                        if ataques_realizados < personagens_vivos_count:
                            turno_do_personagem = encontrar_proximo_personagem_livre(turno_do_personagem, atacou, personagens)
                        
                    elif event.key == pygame.K_ESCAPE:
                        return False
                    
                    elif event.key == pygame.K_RIGHT and ataques_realizados < personagens_vivos_count -1:
                        play_sound(SOUND_GROUP)
                        turno_do_personagem = encontrar_proximo_personagem_direita(turno_do_personagem, atacou, personagens)

                    elif event.key == pygame.K_LEFT and ataques_realizados < personagens_vivos_count -1:
                        play_sound(SOUND_GROUP)
                        turno_do_personagem = encontrar_proximo_personagem_esquerda(turno_do_personagem, atacou, personagens)
        
        # --- Turno do Inimigo (com delay) ---
        else:
            # Se for o primeiro frame do turno do inimigo, inicia o timer
            if not inimigo_iniciou_turno:
                tempo_inicio_delay_inimigo = pygame.time.get_ticks()
                inimigo_iniciou_turno = True

            # Verifica se o delay de 3 segundos já passou
            if pygame.time.get_ticks() - tempo_inicio_delay_inimigo > DELAY_INIMIGO_MS:
                # Delay acabou, executa o ataque
                pos_alvo = encontrar_proximo_personagem_vivo(random.randint(0, 2), personagens)
                personagem_alvo = personagens[pos_alvo]
                personagem_alvo.reduz_vida(calcula_dano(inimigo))

                if not personagem_alvo.vivo:
                    personagens_mortos += 1 
                
                ataques_realizados = 0
                atacou = [not p.vivo for p in personagens]
                if personagens_mortos < len(personagens):
                    turno_do_personagem = encontrar_proximo_personagem_vivo(pos_alvo, personagens)
        
        if ataques_realizados < personagens_vivos_count:
            texto_turno_atual = FONTE_TURNO.render(f"Rodada: {turno}", True, (0,0,0))
            JANELA.blit(texto_turno_atual, (LARGURA//2, ALTURA - 100))

        else:

            texto_turno_inimigo = FONTE_TURNO.render("Turno do Inimigo", True, VERMELHO)
            rect_texto = texto_turno_inimigo.get_rect(center=(LARGURA // 2, 400))
            JANELA.blit(texto_turno_inimigo, rect_texto)

        for i, p in enumerate(personagens):
            if p.vivo:
                pos_x, pos_y = posicoes_personagens[i]
                p.draw_at_position(JANELA, pos_x, pos_y)
                desenhar_barra_de_vida(JANELA, pos_x + 30, pos_y - 50, p)
        
        if inimigo.vivo:
            inimigo.draw_at_position(JANELA, pos_inimigo_x, pos_inimigo_y)
            desenhar_barra_de_vida(JANELA, pos_inimigo_x - 30, pos_inimigo_y - 150, inimigo)

        if not pygame.mixer.get_busy():
            musica_batalha = random.choice(SOUNDS_BATTLE)
            play_sound(musica_batalha)

        pygame.display.flip()

# Funções Auxiliares de Lógica de Turno 
def encontrar_proximo_personagem_livre(atual, atacou, personagens):
    proximo = (atual + 1) % 3
    for _ in range(3):
        if not atacou[proximo] and personagens[proximo].vivo:
            return proximo
        proximo = (proximo + 1) % 3
    return atual

def encontrar_proximo_personagem_direita(atual, atacou, personagens):
    proximo = (atual + 1) % 3
    for _ in range(3):
        if not atacou[proximo] and personagens[proximo].vivo:
            return proximo
        proximo = (proximo + 1) % 3
    return atual

def encontrar_proximo_personagem_esquerda(atual, atacou, personagens):
    proximo = (atual - 1 + 3) % 3
    for _ in range(3):
        if not atacou[proximo] and personagens[proximo].vivo:
            return proximo
        proximo = (proximo - 1 + 3) % 3
    return atual

def encontrar_proximo_personagem_vivo(atual, personagens):
    proximo = (atual + 1) % len(personagens)
    for _ in range(len(personagens)):
        if personagens[proximo].vivo:
            return proximo
        proximo = (proximo + 1) % len(personagens)
    return -1

def calcula_dano(personagem):
    critical_multiplier = (1 + personagem.sorte / 100) * random.random()
    return personagem.ataque * (1 + critical_multiplier)