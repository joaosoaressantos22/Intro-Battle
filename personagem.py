import pygame

class Personagem:

    def __init__(self, image, x_pos, y_pos, ataque, vida, defesa):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.ataque = ataque
        self.vida = vida
        self.defesa = defesa
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, janela):
        janela.blit(self.image, self.rect)
    
    