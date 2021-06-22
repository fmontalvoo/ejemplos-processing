int x;
int y;
int azul = 0;
int contador = 0;
PImage mario;

void setup(){
  size(720,720);
  x = 210;
  y = 210;
  mario = loadImage("mario.png");
  println(mario);
}

void draw(){
  background(0,0, azul);
  println(contador);
  image(mario, x, y, 82, 128);
  //fill(200,0,0);
  //circle(x,y, 120);
  if(contador % 20 == 0)
    azul = (int) random(255);
  contador++;
}

void keyPressed(){
  
  if(keyCode == 65)
    x = x - 10;
  if(keyCode == 68)
    x = x + 10;
    
  if(keyCode == 87)
    y = y - 10;
    
  if(keyCode == 83)
    y = y + 10;
}
