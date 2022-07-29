from random import randint
import  pygame as pg

pan_Altura = 800

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

    def dibujar(self,pantalla_principal):
        pg.draw.rect(pantalla_principal,self.color, (self.x,self.y,self.w,self.h))    

pg.init()

pantalla_principal = pg.display.set_mode((800, 600))
pg.display.set_caption("Bolitas rebotando")

n_cuadrado = randint(3,10)
list_cuadrado = []

pos_poner_velcidad = 0 
while n_cuadrado> 0 :
        
    list_cuadrado.append(Cuadrado(randint(0,800),randint(0,60),25,25,(randint(0,255),randint(0,255),randint(0,255))))
    list_cuadrado[pos_poner_velcidad].velocidad(randint(1,3),randint(1,3))

    pos_poner_velcidad +=1
    n_cuadrado-=1

game_over = False
while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill((0,0,255))

    for pos,caracter in enumerate(list_cuadrado):
        list_cuadrado[pos].mover(800,600)
        list_cuadrado[pos].dibujar(pantalla_principal)               
    pg.display.flip()
pg.quit()


