from ursina import *
app = Ursina()
import random as r
background = Entity(model='quad', color=color.white , z=1, scale=(20,10))
T_rex = Entity(model='quad', texture='t rex', y=-0.5, x=-5, collider='box')
terra = Entity(model='quad', texture='terra' , scale=(25,0.2),  z=-1 , y=-1)
cactus = Entity(model='quad', texture='pianta' , collider='box', y=-0.5 , x=10)
game_over = Entity(model='quad', texture='game over' , scale=(7,1), y=2 , visible=False)
ricomincia = Entity(model='quad', texture='ricomincia' , visible=False)
nuvola = Entity(model='quad' , texture='nuvola' , scale=(2,1),y=2,x=5)
Testo= Text(text=f'Punti:{0}',  color=color.black, position=(-0.6, 0.4))
T_rex.collider = BoxCollider(T_rex, center=Vec3(0, 0, 0), size=Vec3(0.5, 0.5, 0.5))
salto = Audio('poing.mp3', loop = False, Autoplay = False, volume = .5)
morte = Audio('morte.mp3', loop = False, Autoplay = False, volume = 0.5)
salto.stop()
morte.stop()
CACTUS = []

nuvola2=duplicate(nuvola)
pair1 = [nuvola2, nuvola]

terra2 = duplicate(terra)
pair = [terra, terra2]

def newCactus():
    molti_cactus = duplicate(cactus, x=10+r.randint(0,5))
    CACTUS.append(molti_cactus)
    invoke(newCactus, delay=r.randint(1,2))
newCactus()

def update():
    global PUNTI
    PUNTI +=1
    Testo.text = f'Punti: {PUNTI}'
    for terra in pair:
        terra.x -= 11.5*time.dt
        if terra.x < -5:
            terra.x += 9
    for nuvola in pair1:
        nuvola.x -= 11.5 * time.dt
        if nuvola.x < -10:
            nuvola.x += 20*r.randint(1,3)
    for MIO in CACTUS:
        MIO.x -= 11*time.dt
    if T_rex.intersects().hit:
        T_rex.texture= 'morto'
        game_over.visible = True
        ricomincia.visible = True
        morte.play()
        application.pause()


PUNTI=0
def input(key):
    if key == 'space':
        if T_rex.y <= -0.4:
            T_rex.animate_y(2, duration=0.2, curve = curve.out_sine)
            T_rex.animate_y(-0.5, delay=0.2, duration=0.4, curve=curve.out_sine)
            salto.play()


# TODO: Put sprite animation

app.run()