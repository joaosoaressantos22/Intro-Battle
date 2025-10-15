import pygame
from consts import *
from utils import *

def menu():

    with open("workshop-pygame/sessao1/recordes/bosses_killed.txt") as f:
        bosses_killed = f.read()
    
    with open("workshop-pygame/sessao1/recordes/enemies_killed.txt") as f:
        enemies_killed = f.read()
    
    with open("workshop-pygame/sessao1/recordes/phase.txt") as f:
        phases = f.read()
    
    if pygame.mixer.get_init():
        pygame.mixer.stop()

    play_sound(SOUND_MENU_PATH)
    
    fonte_titulo = pygame.font.SysFont(None, 36)  
    
    recorde_bosses = fonte_titulo.render(f"Bosses derrotados: {bosses_killed}", True, (0, 0, 0))
    recorde_inimigos = fonte_titulo.render(f"Inimigos derrotados: {enemies_killed}", True, (0, 0, 0))
    recorde_fases = fonte_titulo.render(f"Fase máxima: {phases}", True, (0, 0, 0))
    frase_de_aviso = fonte_titulo.render(f"Precione 'Enter' para continuar ou 'ESC'para sair", True, (0, 0, 0))


    pos_y_base = ALTURA - 150 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        # Desenhar o fundo do menu
        JANELA.blit(IMG_MENU, (X_INI, Y_INI))
        
        # Desenhar os recordes na parte inferior
        JANELA.blit(recorde_bosses, (LARGURA // 2 - recorde_bosses.get_width() // 2, pos_y_base))
        JANELA.blit(recorde_inimigos, (LARGURA // 2 - recorde_inimigos.get_width() // 2, pos_y_base + 40))
        JANELA.blit(recorde_fases, (LARGURA // 2 - recorde_fases.get_width() // 2, pos_y_base + 80))
        JANELA.blit(frase_de_aviso, (LARGURA // 2 - frase_de_aviso.get_width() // 2, pos_y_base + 120))

        pygame.display.flip()