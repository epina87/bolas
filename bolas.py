from random import randint
import  pygame as pg


class Cuadrado:
    def __init__(self,x,y,w=25,h=25,color = (255,255,255)) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color

        self.vx = 0
        self.vy = 0

    def velocidad(self,vx,vy):
        self.vx = vx
        self.vy = vy

    def mover(self,xmax,ymax):
        self.x += self.vx
        self.y += self.vy

        if self.x >= (xmax-self.w) or self.x<=0:
            self.vx= self.vx*-1   
        if self.y >= (ymax-self.w) or self.y<=0:
            self.vy= self.vy*-1

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Bolitas rebotando")

n_cuadrado = randint(-10,10)

cuadrado = Cuadrado(400,300,color=(255,255,0))
cuadrado2 = Cuadrado(300,300,35,35,(0,255,0))

cuadrado.velocidad(1,1)
cuadrado2.velocidad(randint(-10,10),randint(-10,10))


game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0,0,255))

    cuadrado.mover(800,600)
    cuadrado2.mover(800,600)

    pg.draw.rect(pantalla_principal,cuadrado.color, (cuadrado.x,cuadrado.y,cuadrado.w,cuadrado.h))
    pg.draw.rect(pantalla_principal,cuadrado.color, (cuadrado2.x,cuadrado2.y,cuadrado2.w,cuadrado2.h))
    
    pg.display.flip()
pg.quit()


