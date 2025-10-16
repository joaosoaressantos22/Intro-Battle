import pygame
from menu import menu
from selecao import selecao
from batalha import batalha
from consts import *
from utils import *
from vitoria import vitoria
from derrota import derrota

def jogo():

    pygame.init()

    menu() 
    personagens = selecao()
    
    for i in range(0, 3): #Definindo que serão 5 batalhas
        var = batalha(personagens, i + 1)
        if not var:
            with open ("workshop-pygame/sessao1/recordes/phase.txt", 'r') as f:
                max = int(f.read())
                if i > max: 
                    with open ("workshop-pygame/sessao1/recordes/phase.txt", 'w') as fw:
                        fw.write(f"{i + 1}")
            with open ("workshop-pygame/sessao1/recordes/enemies_killed.txt", 'r') as f:
                killed = int(f.read())
            with open ("workshop-pygame/sessao1/recordes/enemies_killed.txt", 'w') as fw:
                fw.write(f"{killed + i + 1}")
            break

    with open ("workshop-pygame/sessao1/recordes/phase.txt", 'w') as fw:
        fw.write(f"{i + 1}")

    with open ("workshop-pygame/sessao1/recordes/enemies_killed.txt", 'r') as f:
        killed = int(f.read())
    
    with open ("workshop-pygame/sessao1/recordes/enemies_killed.txt", 'w') as fw:
        fw.write(f"{killed + i + 1}")
    if var:
        vitoria()
    else:
        derrota()
    jogo()


