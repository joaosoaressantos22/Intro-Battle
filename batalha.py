from consts import *
from utils import *
import random

def batalha(personagens): #Lista de personagens que estão no jogo
    lista_personagens_mortos = [False, False, False] #Lista vazia NAO PRECISO
    if pygame.mixer.get_init():
        pygame.mixer.fadeout(1000)
    
    imagem_batalha = random.choice(IMGS_BATALHA)
    
    prim_pos_x = ter_pos_x = 90
    prim_pos_y = 300
    segun_pos_x = 120
    segun_pos_y = 430
    ter_pos_y = 560

    if imagem_batalha == IMG_BATALHA_PRIMEIRA:
        prim_pos_x = ter_pos_x = 90
        prim_pos_y = 450
        segun_pos_x = 120
        segun_pos_y = 580
        ter_pos_y = 710

    if imagem_batalha == IMG_BATALHA_TERCEIRA:
        prim_pos_x = ter_pos_x = 90
        prim_pos_y = 300
        segun_pos_x = 120
        segun_pos_y = 430
        ter_pos_y = 560

    if imagem_batalha == IMG_BATALHA_QUINTA:
        prim_pos_x = ter_pos_x = 90
        prim_pos_y = 300
        segun_pos_x = 120
        segun_pos_y = 430
        ter_pos_y = 560

    musica_batalha = random.choice(SOUNDS_BATTLE)
    inimigo = random.choice(list(BOSSES.values()))
    play_sound(musica_batalha)

    prim_per = personagens[0]
    segun_per = personagens[1]
    ter_per = personagens[2]

    play_sound(SOUND_FIGHT, 10)

    turno_do_personagem = 0
    atacou = [False, False, False]
    ataques_realizados = 0
    personagens_mortos = 0
    
    while True:

        JANELA.blit(imagem_batalha, (X_INI, Y_INI))
        JANELA.blit(IMG_LOGO_FIGHT, (LARGURA//2 - 125, 0))
        rect_to_draw = JANELA.blit(IMG_QUADRO, (0, 0))
        personagens[turno_do_personagem].draw_at_position(JANELA, rect_to_draw.centerx, rect_to_draw.centery)
        
        if not inimigo.vivo:
            inimigo.reset()
            for p in personagens:
                p.reset()
            return True  # Jogador venceu
        
        # Verificar se todos os personagens estão mortos
        personagens_vivos = [p for p in personagens if p.vivo]
        if not personagens_vivos:
            for p in personagens:
                p.reset()
            return False  # Jogador perdeu
        
        if ataques_realizados < (3 - personagens_mortos):
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        atacou[turno_do_personagem] = True
                        ataques_realizados += 1
                        inimigo.reduz_vida(calcula_dano(personagens[turno_do_personagem]))
                        turno_do_personagem = encontrar_proximo_personagem_livre(turno_do_personagem, atacou, personagens)  
                        
                        print(f"Vida do inimigo: {inimigo.vida_atual}")
                        
                    elif event.key == pygame.K_ESCAPE:
                        #virar um botao de pause ja ja
                        return False
                    
                    elif event.key == pygame.K_RIGHT and personagens_mortos < 2 and ataques_realizados < 2:
                        play_sound(SOUND_GROUP)
                        turno_do_personagem = encontrar_proximo_personagem_direita(turno_do_personagem, atacou, personagens)

                    elif event.key == pygame.K_LEFT and personagens_mortos < 2 and ataques_realizados < 2:
                        play_sound(SOUND_GROUP)
                        turno_do_personagem = encontrar_proximo_personagem_esquerda(turno_do_personagem, atacou, personagens)
                    
        # ATAQUE DO INIMIGO  
        else:
            print("ZEIREI - Inimigo atacando")
            
            pos_alvo = encontrar_proximo_personagem_vivo(random.randint(0,2), personagens)
            personagem_alvo = personagens[pos_alvo]
            personagem_alvo.reduz_vida(calcula_dano(inimigo))

            if not personagem_alvo.vivo:
                personagens_mortos += 1 
                atacou[pos_alvo] = True
                lista_personagens_mortos[pos_alvo] = True
                turno_do_personagem = encontrar_proximo_personagem_vivo(pos_alvo, personagens)
            
            for i in range(3):
                if lista_personagens_mortos[i] == False:
                    atacou[i] = False
                
        
            ataques_realizados = 0

        if prim_per.vivo:
            prim_per.draw_at_position(JANELA, prim_pos_x, prim_pos_y)
        if segun_per.vivo:
            segun_per.draw_at_position(JANELA, segun_pos_x, segun_pos_y)
        if ter_per.vivo:
            ter_per.draw_at_position(JANELA, ter_pos_x, ter_pos_y)
        if inimigo.vivo:
            inimigo.draw_at_position(JANELA, LARGURA - 100, ALTURA - 200)
        elif inimigo.vivo and imagem_batalha == IMG_BATALHA_QUINTA:
            inimigo.draw_at_position(JANELA, LARGURA - 300, ALTURA - 200)

        if not pygame.mixer.get_busy():
            musica_batalha = random.choice(SOUNDS_BATTLE)
            play_sound(musica_batalha)

        pygame.display.flip()

# FUNCOES DE ARRAY CIRCULAR - MODIFICADAS PARA CONSIDERAR APENAS PERSONAGENS VIVOS
def encontrar_proximo_personagem_livre(atual, atacou, personagens):
    proximo = (atual + 1) % 3
    tentativas = 0
    
    # Procura por um personagem vivo que não atacou
    while (atacou[proximo] or not personagens[proximo].vivo) and tentativas < 3:
        proximo = (proximo + 1) % 3
        tentativas += 1
    
    # Se encontrou um personagem válido, retorna ele
    if not atacou[proximo] and personagens[proximo].vivo:
        print("SAI NO PRIMEIRO")
        return proximo
    
    # Se não encontrou, procura por QUALQUER personagem vivo que não atacou
    for i in range(3):
        print(i)
        if i != atual and personagens[i].vivo and not atacou[i]:
            print("SAI NO ANTIPENULTIMO")
            return i
    
    # Se ainda não encontrou, procura por QUALQUER personagem vivo (exceto o atual)
    for i in range(3):
        if i != atual and personagens[i].vivo:
            print(" SAI NO PENULTIMO")
            return i
    
    # Se chegou aqui, todos os outros personagens estão mortos ou não há opções válidas
    # Neste caso, força a retornar um personagem diferente do atual, mesmo que seja inválido
    for i in range(3):
        if i != atual:
            print("SAI NO ULTIMO")
            return i
    
    return (atual + 1) % 3

def encontra_posicao_livre(lista_personagens_mortos, pos_alvo):
    atual = pos_alvo
    if lista_personagens_mortos[pos_alvo]:
        proximo = (atual + 1) % 3
        tentativas = 0
    
        while lista_personagens_mortos[proximo] == False and tentativas < 3:
            proximo = (proximo + 1) % 3
            tentativas += 1
    
    # Se não encontrou nenhum personagem vivo, procura qualquer personagem vivo       
        return proximo

    return -1

def encontrar_proximo_personagem_direita(atual, atacou, personagens):
    proximo = (atual + 1) % 3
    tentativas = 0
    
    while tentativas < 3 and atacou[proximo] == True:
        proximo = (proximo + 1) % 3
        if proximo > 2:
            proximo = 0
        elif proximo < 2:
            proximo += 1

    if tentativas < 3:
        return proximo 
    if tentativas >= 3:
        return atual

def encontrar_proximo_personagem_esquerda(atual, atacou, personagens):

    proximo = (atual - 1) % 3
    if proximo < 0:
        proximo = 2
    tentativas = 0
    
    while tentativas < 3 and atacou[proximo] == True:
        proximo = (proximo - 1) % 3
        if proximo < 0:
            proximo = 2
        elif proximo> 0:
            proximo -= 1
        tentativas += 1
    print(f"NA ESQUERDA ENCONTROU: {proximo}\n")
    if tentativas < 3:
        return proximo 
    if tentativas >= 3:
        return atual

def encontrar_proximo_personagem_vivo(atual, personagens, direcao=1):
    total = len(personagens)

    if direcao == 1:
        proximo = (atual + 1) % total
        tentativas = 0
        while not personagens[proximo].vivo and tentativas < total:
            proximo = (proximo + 1) % total
            tentativas += 1
    else:
        proximo = (atual - 1) % total
        tentativas = 0
        while not personagens[proximo].vivo and tentativas < total:
            proximo = (proximo - 1) % total
            proximo = proximo % total
            tentativas += 1

    return proximo 

def calcula_dano(personagem):
    critical = random.randint(1, 100 + personagem.sorte)
    return (personagem.ataque + personagem.ataque*(critical/100))