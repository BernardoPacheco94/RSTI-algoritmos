from math import pi

class FormaGeometrica:
    cor_fundo = None
    cor_borda = None
    espessura_borda = None
    
class Triangulo(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
        return (self.base*self.altura) / 2
    
class Quadrilatero(FormaGeometrica):
    base = None
    altura = None
    
    def calcular_area(self):
        return self.base*self.altura

class Circulo(FormaGeometrica):
    raio = None
    
    def calcular_area(self):
        return pi*self.raio**2

triangulo_a = Triangulo()
triangulo_a.cor_fundo = 'vermelho'
triangulo_a.cor_borda = 'preto'
triangulo_a.espessura_borda = 3
triangulo_a.base = 100
triangulo_a.altura = 150


quadrado = Quadrilatero()
quadrado.cor_fundo = 'transparente'
quadrado.cor_borda = 'preto'
quadrado.espessura_borda = 2
quadrado.base = 8
quadrado.altura = 16


bolinha = Circulo()
bolinha.cor_borda = 'azul'
bolinha.cor_fundo = 'branca'
bolinha.espessura_borda = 3
bolinha.raio = 10

