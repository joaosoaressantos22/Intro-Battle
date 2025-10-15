import pygame
from consts import * 

def vitoria():
     
    fonte_titulo = pygame.font.SysFont(None, 36)  
    frase = fonte_titulo.render(f"VOCE FINALMENTE GANHOU ALGUMA COISA!", True, (0, 0, 0))
    frase_de_aviso = fonte_titulo.render(f"PRESSIONE QUALQUER TECLA PARA SAIR!", True, (0, 0, 0))

    pos_y_base = ALTURA - 150 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                    return

        JANELA.blit(IMG_VITORIA, (X_INI, Y_INI))

        JANELA.blit(frase, (LARGURA // 2 - frase.get_width() // 2, pos_y_base + 80))
        JANELA.blit(frase_de_aviso, (LARGURA // 2 - frase_de_aviso.get_width() // 2, pos_y_base + 120))

        pygame.display.flip()