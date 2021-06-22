float x, dx;
float y, dy;
int d, r;

void setup() {
  size(840, 420);

  d = 25;
  r = d/2;
  x = 420;
  y = 210;
  dx = 5;
  dy = 5;
}

void draw() {
  background(128);
  ellipse(x, y, d, d);

  if (x >= (width - r) || x <= r)
    dx *= -1;

  if (y >= (height - r) || y <= r)
    dy *= -1;

  x += dx;
  y += dy;

  println("X: "+x+" dx: "+dx+" Y: "+y+" dy: "+dy);
}
