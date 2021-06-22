from Circle import *

def setup():
    size(640, 420)
    global c, c1
    c = Circulo(210, 210, 25)
    c1 = Circulo(50, 50, 30, 10, 10)
    c1.color(0, 0, 127)
    
def draw():
    background(255)
    c.show()
    c1.show()
    c.move()
    c1.move()
    c.check_edges()
    c1.check_edges()
