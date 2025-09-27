import pygame

pygame.init()

CLOCK = pygame.time.Clock()
FPS = 60

LARGURA, ALTURA = 1024, 768

JANELA = pygame.display.set_mode((LARGURA, ALTURA))

IMG_PERSONAGEM = pygame.image.load("imagem/personagem/amigo/0.png").convert_alpha()
IMG_FUNDO = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/selecao_fundo.webp").convert_alpha()
IMG_FUNDO = pygame.transform.scale(IMG_FUNDO, (LARGURA, ALTURA))


X_INI = 100
Y_INI = 300

X_VEL_INI = 0
Y_VEL_INI = 0
VEL_MOD = 5

def jogo():
    
    x_pos = X_INI
    y_pos = Y_INI
    x_vel = X_VEL_INI
    y_vel = Y_VEL_INI

    while(True):
        
        CLOCK.tick(FPS)

        #Input 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_vel = VEL_MOD
                if event.key == pygame.K_LEFT:
                    x_vel = -VEL_MOD
                if event.key == pygame.K_UP:
                    y_vel = -VEL_MOD
                if event.key == pygame.K_DOWN:
                    y_vel = VEL_MOD
                if event.key == pygame.K_SPACE:
                    y_vel += 1
                    x_vel += 1
                if event.key == pygame.K_s:
                    y_vel -= 0
                    x_vel -= 0
            
        #Atualizacao

        x_pos += x_vel
        y_pos += y_vel

        #Renderizacao 
        JANELA.blit(IMG_FUNDO, (0, 0))
        JANELA.blit(IMG_PERSONAGEM, (x_pos, y_pos))
        pygame.display.flip()

        if(y_pos >= (ALTURA - 80) or y_pos <= (0 - 80)):
            y_vel *= -1

        if(x_pos >= (LARGURA -80) or x_pos <= (0 - 80)):
            x_vel *= -1

jogo()