import pygame
from menu import menu
from confirmacao import confirmacao
from consts import *
from utils import *

def desenhar_status(janela, personagem, pos_quadro, fonte):
    
    cor_texto = (255, 255, 255) # Branco
    x_inicial = pos_quadro[0] + 15
    y_inicial = pos_quadro[1] + 125 # Posição Y inicial, abaixo da imagem
    
    status = [
        f"Vida: {personagem.vida}",
        f"Ataque: {personagem.ataque}",
        f"Defesa: {personagem.defesa}",
        f"Sorte: {personagem.sorte}"
    ]
    
    espacamento = 18 # Espaço entre as linhas de texto
    
    for i, texto in enumerate(status):
        texto_surface = fonte.render(texto, True, cor_texto)
        janela.blit(texto_surface, (x_inicial, y_inicial + (i * espacamento)))

def criar_quadro_vazio():
    superficie = pygame.Surface((180, 200), pygame.SRCALPHA)

    for y in range(200):
        alpha = 100 + int(50 * (y / 200))
        pygame.draw.line(superficie, (80, 80, 80, alpha), (0, y), (180, y))
    pygame.draw.rect(superficie, (255, 255, 255), (0, 0, 180, 200), 3)
    return superficie

def selecao():
    selecionados = []
    indice = 1
    selecionou = False

    IMG_QUADRO_VAZIO = criar_quadro_vazio()
    
    posicoes_quadros = [
        (LARGURA - 220, 70),    # Primeiro quadro
        (LARGURA - 220, 300),    # Segundo quadro  
        (LARGURA - 220, 530)     # Terceiro quadro
    ]
    
    fonte_selecionados = pygame.font.SysFont(None, 36)
    fonte_instrucoes = pygame.font.SysFont(None, 24)
    fonte_numero = pygame.font.SysFont(None, 72)
    fonte_status = pygame.font.SysFont(None, 22) # <<< FONTE NOVA
    
    texto_selecionados = fonte_selecionados.render("Selecionados", True, (255, 255, 255))
    
    while True:
        CLOCK.tick(FPS)

        # Input 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    indice += 1
                if event.key == pygame.K_LEFT:
                    indice -= 1
                if event.key == pygame.K_UP:
                    indice -= 2
                if event.key == pygame.K_DOWN:
                    indice += 2
                if event.key == pygame.K_RETURN:
                    selecionou = True
                if event.key == pygame.K_ESCAPE:
                    if len(selecionados) > 0:
                        selecionados.clear()
                    else:
                        menu()
                if event.key == pygame.K_s and len(selecionados) == 3:
                    play_sound(SOUND_GROUP)
                    return selecionados


        # Atualizacao
        if indice > 5:
            indice = 1
        elif indice < 1:
            indice = 5

        # Renderizacao 
        JANELA.blit(IMG_FUNDO, (X_INI, Y_INI))
        
        texto_rotacionado = pygame.transform.rotate(texto_selecionados, 0)
        JANELA.blit(texto_rotacionado, (LARGURA - 210, 20))
        
        for i, pos in enumerate(posicoes_quadros):

            if i < len(selecionados):
                # Desenha o quadro com o personagem selecionado
                JANELA.blit(IMG_QUADRO, pos)
                # Centraliza a imagem do personagem no quadro (posição Y ajustada)
                selecionados[i].draw_at_position(JANELA, pos[0] + 90, pos[1] + 65)
                # Número do slot (no canto superior esquerdo do quadro)
                texto_numero = fonte_numero.render(str(i+1), True, (255, 255, 0))
                JANELA.blit(texto_numero, (pos[0] + 10, pos[1] + 10))
                
                # <<< MOSTRA OS STATUS DO PERSONAGEM >>>
                desenhar_status(JANELA, selecionados[i], pos, fonte_status)
                
            else:

                JANELA.blit(IMG_QUADRO_VAZIO, pos)

                texto_numero = fonte_numero.render(str(i+1), True, (150, 150, 150))
                JANELA.blit(texto_numero, (pos[0] + 10, pos[1] + 10))
                
                texto_vazio = fonte_instrucoes.render("Vazio", True, (200, 200, 200))
                JANELA.blit(texto_vazio, (pos[0] + 65, pos[1] + 90))
        
        if selecionou == False:
            # Desenha os botões dos personagens disponíveis
            for bt in BT_PERSONAGENS:
                bt.update(JANELA)
                bt.desenharCursor(JANELA, indice)

            for personagem in ICONES_PERSONAGENS:
                JANELA.blit(personagem[0], personagem[1])
                
            # Desenha instruções
            instrucoes1 = fonte_instrucoes.render("Use as setas para navegar e ENTER para selecionar", True, (255, 255, 255))
            instrucoes2 = fonte_instrucoes.render(f"Selecionados: {len(selecionados)}/3", True, (255, 255, 255))
            instrucoes3 = fonte_instrucoes.render("ESC: Voltar ao menu ou remover todos os personagens", True, (255, 200, 200))
            
            JANELA.blit(instrucoes1, (LARGURA//2 - instrucoes1.get_width()//2, ALTURA - 80))
            JANELA.blit(instrucoes2, (LARGURA//2 - instrucoes2.get_width()//2, ALTURA - 50))
            JANELA.blit(instrucoes3, (LARGURA//2 - instrucoes3.get_width()//2, ALTURA - 20))

        if selecionou == True:

            if PERSONAGENS[indice] not in selecionados:

                conf = confirmacao(PERSONAGENS[indice])

                if conf != None:

                    play_sound(SOUND_CHARACTERS)

                    if len(selecionados) < 3:

                        selecionados.append(conf)

                    else:

                        selecionados.pop(2)
                        selecionados.insert(2, conf)

            selecionou = False
        
        if len(selecionados) == 3:

            texto_pronto = fonte_selecionados.render("Pronto para começar! Pressione 'S'", True, (0, 255, 0))
            
            JANELA.blit(texto_pronto, (LARGURA//2 - texto_pronto.get_width()//2, ALTURA - 120))
                
            
        pygame.display.flip()