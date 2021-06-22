PImage img;

void setup(){
  size(910, 512);
  img = loadImage("image.jpg");
}

void draw(){
  for(int i = 0; i < 240; i++){
    float x = random(width);
    float y = random(height);
    color c = img.get(int(x), int(y));
    
    noStroke();
    //fill(c, 70);
    fill(c);
    ellipse(x, y, 5, 5);
  }
}
