class Circulo:
    def __init__(self, pos_x=10, pos_y=10, radius=1, dx=5, dy=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.diameter = 2 * self.radius
        self.dx = dx
        self.dy = dy
        self.color()
   
    def color(self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b
   
    def show(self):
        fill(self.r, self.g, self.b)
        ellipse(self.pos_x, self.pos_y, self.diameter, self.diameter)
        
    def move(self):
        self.pos_x += self.dx
        self.pos_y += self.dy
    
    def check_edges(self):
        if self.pos_x >= (width - self.radius) or self.pos_x <= self.radius:
            self.dx *= -1;
        if self.pos_y >= (height - self.radius) or self.pos_y <= self.radius:
            self.dy *= -1;
