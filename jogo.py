import pygame
from menu import menu
from selecao import selecao
from batalha import batalha
from consts import *
from utils import *
from vitoria import vitoria

def jogo():

    pygame.init()

    menu() 
    personagens = selecao()
    
    for i in range(0, 20): #Definindo que serão 5 batalhas
        print(i)
        var = batalha(personagens)
        if not var:
            with open ("workshop-pygame/sessao1/recordes/phase.txt", 'r') as f:
                max = int(f.read())
                if i > max: 
                    with open ("workshop-pygame/sessao1/recordes/phase.txt", 'w') as fw:
                        fw.write(f"{i + 1}")

            #Chamada recursiva
            #CHAMARIAMOS DERROTA AQUI
            jogo()

    with open ("workshop-pygame/sessao1/recordes/phase.txt", 'w') as fw:
        fw.write(f"{i + 1}")

    vitoria()
    jogo()


