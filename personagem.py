import pygame

class Personagem:

    def __init__(self, image, x_pos, y_pos, ataque, vida, defesa, sorte, desc_imagem, nome="Padrao"):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ataque = ataque
        self.vida = vida
        self.defesa = defesa
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.sorte = sorte
        self.desc_imagem = desc_imagem
        self.nome = nome
        self.vida_atual = vida #Na construção a vida atual é igual a vida
        self.x_pos_atual = x_pos
        self.y_pos_atual = y_pos
        self.vivo = True

    def update(self, janela):
        janela.blit(self.image, self.rect)

    def draw_at_position(self, janela, pos_x, pos_y):
        self.x_pos_atual = pos_x
        self.y_pos_atual = pos_y
        self.rect = self.image.get_rect(center=(self.x_pos_atual, self.y_pos_atual))
        self.update(janela)

    def reduz_vida(self, dano): #Adicionar sorte aqui!
        dano_total = dano * (50/(50+self.defesa))
        self.vida_atual -= dano_total
        if self.vida_atual <= 0:
            self.vivo = False 
    
    def reset(self):
        self.vida_atual = self.vida
        self.vivo = True