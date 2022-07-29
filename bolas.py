import pygame as pg
import random

class Cuadrao:
    def __init__(self, x, y, w=25, h=25, color = (255, 255, 255)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 0
        self.vy = 0

    def velocidad(self, vx, vy):
        self.vx = vx
        self.vy = vy

    def mover(self, xmax, ymax):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= xmax - self.w:
            self.vx *= -1 

        if self.y <= 0 or self.y >= ymax - self.h:
            self.vy *= -1 

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))

pg.display.set_caption("Bolitas rebotando")

cuadrao = Cuadrao(400, 300, h=50, color=(255, 255, 0))
cuadrao.velocidad(5, 5)
cuadrao2 = Cuadrao(300, 300, 35, 35, (0, 255, 0))
cuadrao2.velocidad(random.randint(-10, 10), random.randint(-10, 10))

game_over = False
while not game_over:
    lista_eventos = pg.event.get()
    for evento in lista_eventos:
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0, 0, 255))
    cuadrao.mover(800, 600)
    cuadrao2.mover(800, 600)

    pg.draw.rect(pantalla_principal, cuadrao.color, (cuadrao.x, cuadrao.y, cuadrao.w, cuadrao.h))
    pg.draw.rect(pantalla_principal, cuadrao2.color, (cuadrao2.x, cuadrao2.y, cuadrao2.w, cuadrao2.h))
    pg.display.flip()


pg.quit()