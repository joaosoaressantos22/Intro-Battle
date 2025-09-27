import pygame
from botao import Botao as bt
from personagem import Personagem as pers

pygame.init()

CLOCK = pygame.time.Clock()
FPS = 60

LARGURA, ALTURA = 1024, 768

JANELA = pygame.display.set_mode((LARGURA, ALTURA))

IMG_FUNDO = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/selecao_fundo.webp").convert_alpha()
IMG_FUNDO = pygame.transform.scale(IMG_FUNDO, (LARGURA, ALTURA))

X_INI = 0
Y_INI = 0

X_VEL_INI = 0
Y_VEL_INI = 0
VEL_MOD = 5

IMG_QUADRO = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/quadro.png")
IMG_CURSOR = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/cursor.png").convert_alpha()

BOTAO_PERSONAGEM_FIRST = bt(IMG_QUADRO, 150, 135, 1, IMG_CURSOR)
BOTAO_PERSONAGEM_SECOND = bt(IMG_QUADRO, 360, 135, 2, IMG_CURSOR)
BOTAO_PERSONAGEM_THIRD = bt(IMG_QUADRO, 150, 385, 3, IMG_CURSOR)
BOTAO_PERSONAGEM_FORTH = bt(IMG_QUADRO, 360, 385, 4, IMG_CURSOR)
BOTAO_PERSONAGEM_FIFTH = bt(IMG_QUADRO, 150, 635, 5, IMG_CURSOR)

BT_PERSONAGENS = [BOTAO_PERSONAGEM_FIRST, BOTAO_PERSONAGEM_SECOND, BOTAO_PERSONAGEM_THIRD, BOTAO_PERSONAGEM_FORTH, BOTAO_PERSONAGEM_FIFTH]

IMG_ADIBURAI = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/adiburai/0.png")
IMG_ADIBURAI_RECT = IMG_ADIBURAI.get_rect(center=(150, 135))
IMG_AMIGO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/amigo/0.png")
IMG_AMIGO_RECT = IMG_AMIGO.get_rect(center=(360, 135))
IMG_BICHO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/bicho/0.png")
IMG_BICHO_RECT = IMG_BICHO.get_rect(center=(150, 385))
IMG_ICO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/ico/0.png")
IMG_ICO_RECT = IMG_ICO.get_rect(center=(360, 385))
IMG_ROGERIO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/rogerio/0.png")
IMG_ROGERIO_RECT = IMG_ROGERIO.get_rect(center=(150, 635))

ICONES_PERSONAGENS = [(IMG_ADIBURAI, IMG_ADIBURAI_RECT), (IMG_AMIGO, IMG_AMIGO_RECT),(IMG_BICHO, IMG_BICHO_RECT), (IMG_ICO, IMG_ICO_RECT), (IMG_ROGERIO, IMG_ROGERIO_RECT)]

def jogo():
    

    indice = 1
    while(True):
        
        clicou = False

        CLOCK.tick(FPS)

        #Input 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicou = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    indice += 1
                if event.key == pygame.K_LEFT:
                    indice -= 1
                if event.key == pygame.K_UP:
                    indice -= 2
                if event.key == pygame.K_DOWN:
                    indice += 2

        #Atualizacao
        
        if clicou:
            for bt in BT_PERSONAGENS:
                bt.checkInput(pygame.mouse.get_pos())
        if indice > 5:
            indice = 1
        elif indice < 1:
            indice = 5

        #Renderizacao 
        JANELA.blit(IMG_FUNDO, (X_INI, Y_INI))
        
        for bt in BT_PERSONAGENS:
            bt.update(JANELA)
            bt.desenharCursor(JANELA, indice)

        for personagem in ICONES_PERSONAGENS:
            JANELA.blit(personagem[0], personagem[1])

        pygame.display.flip()

jogo()