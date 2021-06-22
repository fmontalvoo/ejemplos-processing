class Gato:
    
    def __init__(self, pos_x, pos_y, nombre, tamanno, apariencia, dx=1, dy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.nombre = nombre
        self.tamnno = tamanno
        self.apariencia = loadImage(apariencia)
        self.dx = dx
        self.dy = dy
        
    def mostrar(self):
        image(self.apariencia, self.pos_x, self.pos_y, self.tamnno, self.tamnno)
        noFill()
        rect(self.pos_x, self.pos_y, self.tamnno, self.tamnno)

    def mostrar_nombre(self):
        textSize(16)
        fill(0, 0, 0)
        text(self.nombre, self.pos_x+self.tamnno/2, self.pos_y)
        
    def maullar(self, r=0, g=0, b=0):
        textSize(21)
        fill(r, g, b)
        text('miau', self.pos_x+self.tamnno/2, self.pos_y+self.tamnno+20)
        
    def mover(self):
        self.pos_x = self.pos_x + self.dx
        self.pos_y= self.pos_y + self.dy
        print('X:',self.pos_x, 'Y:', self.pos_y, 'dx:', self.dx, 'dy:', self.dy)
        
    def verificar_bordes(self):
        if self.pos_x >= width-self.tamnno or self.pos_x <= 0:
            self.dx = self.dx * -1
        
        if self.pos_y >= height-self.tamnno or self.pos_y <= 0:
            self.dy = self.dy * -1
