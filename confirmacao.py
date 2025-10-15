import pygame
from consts import *

def confirmacao(personagem) -> pers:
    
    fonte = pygame.font.SysFont(None, 28)
    fonte_titulo = pygame.font.SysFont(None, 48)
    
    texto_titulo = fonte_titulo.render("Confirmar Personagem?", True, (255, 255, 255))
    texto_instrucao = fonte.render("ENTER = Confirmar    ESC = Cancelar", True, (200, 200, 200))
    
    def quebrar_50_chars(texto):
        linhas = []
        for i in range(0, len(texto), 50):
            linhas.append(texto[i:i+50])
        return linhas
    
    linhas_descricao = quebrar_50_chars(personagem.desc_imagem)
    
    titulo_rect = texto_titulo.get_rect(center=(LARGURA//2, 80))
    instrucao_rect = texto_instrucao.get_rect(center=(LARGURA//2, ALTURA - 80))
    
    personagem_rect = personagem.image.get_rect(center=(LARGURA//3, ALTURA//2))
    
    textos_descricao = []
    for i, linha in enumerate(linhas_descricao):
        texto_linha = fonte.render(linha, True, (255, 255, 255))
        texto_rect = texto_linha.get_rect(center=(2*LARGURA//3, ALTURA//2 - len(linhas_descricao)*15 + i*30))
        textos_descricao.append((texto_linha, texto_rect))
    
    if textos_descricao:
        largura_max = max([texto[1].width for texto in textos_descricao])
        altura_total = len(linhas_descricao) * 30
        fundo_descricao = pygame.Surface((largura_max + 40, altura_total + 20))
        fundo_descricao.set_alpha(180)
        fundo_descricao.fill((0, 0, 0))
        fundo_rect = fundo_descricao.get_rect(center=(2*LARGURA//3, ALTURA//2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return personagem
                elif event.key == pygame.K_ESCAPE:
                    return None
        
        JANELA.blit(IMG_FUNDO, (X_INI, Y_INI))
        
        JANELA.blit(texto_titulo, titulo_rect)
        
        JANELA.blit(personagem.image, personagem_rect)
        
        if textos_descricao:
            JANELA.blit(fundo_descricao, fundo_rect)
            for texto, rect in textos_descricao:
                JANELA.blit(texto, rect)
        
        JANELA.blit(texto_instrucao, instrucao_rect)
        
        pygame.display.flip()
        CLOCK.tick(FPS)
