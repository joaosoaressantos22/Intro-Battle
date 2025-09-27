import pygame

class Botao:

    def __init__(self, image, x_pos, y_pos, indice, img_cursor):
        self.image = image
        self.x_pos = x_pos 
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.indice = indice 
        self.img_cursor = img_cursor

    def update(self, janela):
        janela.blit(self.image, self.rect)

    def checkInput(self, posicao):
        if posicao[0] in range (self.rect.left , self.rect.right) and posicao[1] in range(self.rect.top, self.rect.bottom):
            print("CLICOU!!!")
            return True
        return False
    
    def desenharCursor(self, janela, indice):
        if indice == self.indice:
            janela.blit(self.img_cursor, (self.rect.x, self.rect.y))

    def checkInputCursor(self, indice):
        if indice == self.indice:
            print("BOTAO PRESSIONADO!")
            return True
        return False