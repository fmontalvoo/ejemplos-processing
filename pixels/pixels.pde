size(421, 421);

loadPixels();
for (int x = 0; x < width; x++) {
  for (int y = 0; y < height; y++) {
    int index = x + y * width;
    float d = dist(x, y, width/2, height/2);
    //println("I: "+index+" D: "+d);
    pixels[index] = color(d);
  }
}
updatePixels();
