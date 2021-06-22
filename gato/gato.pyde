from Gato import *

def setup():
    size(620, 430)
    global gato, gato1
    gato = Gato(50, 50, "Lucas", 128, "gato.png", 2, 2)
    gato1 = Gato(300, 200, "Rigoberto", 64, "gato1.png", 5, 5)
    
def draw():
    background(255)
    gato.mostrar()
    gato.mostrar_nombre()
    gato.maullar(r=random(255), g=random(255), b=random(255))
    gato.mover()
    gato.verificar_bordes()
    
    gato1.mostrar()
    gato1.mostrar_nombre()
    gato1.maullar(r=255, g=0, b=0)
    gato1.mover()
    gato1.verificar_bordes()
      
    
