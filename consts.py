import pygame
from botao import Botao as bt
from personagem import Personagem as pers

CLOCK = pygame.time.Clock()
FPS = 60

SOUND_MENU_PATH = "workshop-pygame/sessao1/sounds/Title Screen - Pokémon FireRed & Pokémon LeafGreen (OST).mp3"
SOUND_CHARACTERS = "workshop-pygame/sessao1/sounds/select_characters.wav"
SOUND_GROUP = "workshop-pygame/sessao1/sounds/select_group.wav"
SOUND_FIGHT = "workshop-pygame/sessao1/sounds/fight.mp3"

SOUNDS_BATTLE = ["workshop-pygame/sessao1/sounds/When rushjet1 and danooct1 get bored..mp3",
                 "workshop-pygame/sessao1/sounds/Famitracker Means Business!.mp3",
                 "workshop-pygame/sessao1/sounds/battle_audio_1.mp3",
                 "workshop-pygame/sessao1/sounds/battle_audio_2.mp3",
                 "workshop-pygame/sessao1/sounds/battle_audio_3.mp3",
                 "workshop-pygame/sessao1/sounds/battle_audio_4.mp3",
                 ]

LARGURA, ALTURA = 1024, 768

JANELA = pygame.display.set_mode((LARGURA, ALTURA))

IMG_MENU = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/menu.png").convert_alpha()
IMG_MENU = pygame.transform.scale(IMG_MENU, (LARGURA, ALTURA))

IMG_VITORIA = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/vitoria.png").convert_alpha()
IMG_VITORIA = pygame.transform.scale(IMG_VITORIA, (LARGURA, ALTURA))

IMG_FUNDO = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/fundo.jpeg").convert_alpha()
IMG_FUNDO = pygame.transform.scale(IMG_FUNDO, (LARGURA, ALTURA))

IMG_BATALHA_PRIMEIRA = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/primeira_batalha.png").convert_alpha()
IMG_BATALHA_PRIMEIRA = pygame.transform.scale(IMG_BATALHA_PRIMEIRA, (LARGURA, ALTURA))

IMG_BATALHA_SEGUNDA = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/segunda_batalha.png").convert_alpha()
IMG_BATALHA_SEGUNDA = pygame.transform.scale(IMG_BATALHA_SEGUNDA, (LARGURA, ALTURA))

IMG_BATALHA_TERCEIRA = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/terceira_batalha.png").convert_alpha()
IMG_BATALHA_TERCEIRA = pygame.transform.scale(IMG_BATALHA_TERCEIRA, (LARGURA, ALTURA))

IMG_BATALHA_QUARTA = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/quarta_batalha.png").convert_alpha()
IMG_BATALHA_QUARTA = pygame.transform.scale(IMG_BATALHA_QUARTA, (LARGURA, ALTURA))

IMG_BATALHA_QUINTA = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/quinta_batalha.png").convert_alpha()
IMG_BATALHA_QUINTA = pygame.transform.scale(IMG_BATALHA_QUINTA, (LARGURA, ALTURA))

IMG_LOGO_FIGHT = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/fight.png").convert_alpha()
IMG_LOGO_FIGHT = pygame.transform.scale(IMG_LOGO_FIGHT, (300, 200))

IMGS_BATALHA = [IMG_BATALHA_PRIMEIRA, IMG_BATALHA_SEGUNDA, IMG_BATALHA_TERCEIRA,
                IMG_BATALHA_QUARTA, IMG_BATALHA_QUINTA]

X_INI = 0
Y_INI = 0

X_VEL_INI = 0
Y_VEL_INI = 0
VEL_MOD = 5

IMG_QUADRO = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/quadro.png").convert_alpha()
IMG_QUADRO = pygame.transform.scale(IMG_QUADRO, (180, 200))

IMG_CURSOR = pygame.image.load("workshop-pygame/sessao1/imagem/fundo/cursor.png")
IMG_CURSOR =  pygame.transform.scale(IMG_CURSOR, (150, 75))

BOTAO_PERSONAGEM_FIRST = bt(IMG_QUADRO, 150, 135, 1, IMG_CURSOR)
BOTAO_PERSONAGEM_SECOND = bt(IMG_QUADRO, 360, 135, 2, IMG_CURSOR)
BOTAO_PERSONAGEM_THIRD = bt(IMG_QUADRO, 150, 385, 3, IMG_CURSOR)
BOTAO_PERSONAGEM_FORTH = bt(IMG_QUADRO, 360, 385, 4, IMG_CURSOR)
BOTAO_PERSONAGEM_FIFTH = bt(IMG_QUADRO, 150, 635, 5, IMG_CURSOR)

BT_PERSONAGENS = [BOTAO_PERSONAGEM_FIRST, BOTAO_PERSONAGEM_SECOND, BOTAO_PERSONAGEM_THIRD, BOTAO_PERSONAGEM_FORTH, BOTAO_PERSONAGEM_FIFTH]

IMG_ADIBURAI = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/adiburai/0.png").convert_alpha()
IMG_ADIBURAI = pygame.transform.scale(IMG_ADIBURAI, (80, 120))
IMG_ADIBURAI_RECT = IMG_ADIBURAI.get_rect(center=(150, 135))

IMG_AMIGO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/amigo/0.png").convert_alpha()
IMG_AMIGO = pygame.transform.scale(IMG_AMIGO, (80, 120))
IMG_AMIGO_RECT = IMG_AMIGO.get_rect(center=(360, 135))

IMG_BICHO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/bicho/0.png").convert_alpha()
IMG_BICHO = pygame.transform.scale(IMG_BICHO, (80, 120))
IMG_BICHO_RECT = IMG_BICHO.get_rect(center=(150, 385))

IMG_ICO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/ico/0.png").convert_alpha()
IMG_ICO = pygame.transform.scale(IMG_ICO, (80, 120))
IMG_ICO_RECT = IMG_ICO.get_rect(center=(360, 385))

IMG_ROGERIO = pygame.image.load("workshop-pygame/sessao1/imagem/personagem/rogerio/0.png").convert_alpha()
IMG_ROGERIO = pygame.transform.scale(IMG_ROGERIO, (80, 120))
IMG_ROGERIO_RECT = IMG_ROGERIO.get_rect(center=(150, 635))

ICONES_PERSONAGENS = [(IMG_ADIBURAI, IMG_ADIBURAI_RECT), (IMG_AMIGO, IMG_AMIGO_RECT),(IMG_BICHO, IMG_BICHO_RECT), (IMG_ICO, IMG_ICO_RECT), (IMG_ROGERIO, IMG_ROGERIO_RECT)]
#Ok, Alice vai ter quanto de vida? 250? Defesa? ok Sorte?
PERSONAGENS = {
    1: pers(IMG_ADIBURAI, 150, 160, 300, 250, 300, 20, "Alice - Boa em quase tudo"), 
    2: pers(IMG_AMIGO, 360, 135, 50, 100, 110, 500, "Xandinho - Nn é confiável, mas as vezes sortudo"), 
    3: pers(IMG_BICHO, 150, 385, 350, 200, 200, 10, "Maria - Ela não perde uma trocacao"),
    4: pers(IMG_ICO, 360, 385, 100, 1000, 500, 1, "Joao - Pensa num bixo que é azarado e apanha da vida"),
    5: pers(IMG_ROGERIO, 150, 635, 1000, 1000, 1000, 5, "Karla - Roubada demais não use!")
}

IMG_CAPETA = pygame.image.load("workshop-pygame/sessao1/imagem/inimigos/capeta/capeta-removebg-preview.png").convert_alpha()
IMG_CAPETA = pygame.transform.scale(IMG_CAPETA, (160, 240))

IMG_LAGARTO = pygame.image.load("workshop-pygame/sessao1/imagem/inimigos/lagarto/lagarto_esquisito-removebg-preview.png").convert_alpha()
IMG_LAGARTO = pygame.transform.scale(IMG_LAGARTO, (160, 240))

IMG_ALIEN = pygame.image.load("workshop-pygame/sessao1/imagem/inimigos/alien/alien.png").convert_alpha()
IMG_ALIEN = pygame.transform.scale(IMG_ALIEN, (160, 240))

BOSSES = {
    1: pers(IMG_CAPETA, 200, 300, 125, 2000, 500, 100, " "), 
    2: pers(IMG_LAGARTO, 200, 300, 1000, 150, 200, 100, " "),
    3: pers(IMG_ALIEN, 200, 300, 500, 500, 300, 100, " ") 
}