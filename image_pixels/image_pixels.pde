PImage img;

void setup() {
  size(910, 512);
  img = loadImage("image.jpg");
}

void draw() {
  loadPixels();
  img.loadPixels();
  for (int x = 0; x < width; x++) {
    for (int y = 0; y < height; y++) {
      int index = x + y * width;
      float r = red(img.pixels[index]);
      float g = green(img.pixels[index]);
      float b = blue(img.pixels[index]);
      float d = dist(mouseX, mouseY, x, y);
      float factor = map(d, 0, 200, 2, 0);
      pixels[index] = color(r*factor, g*factor, b*factor);
      //pixels[index] = color(g,r,b);
    }
  }
  updatePixels();
}
