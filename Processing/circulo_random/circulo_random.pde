void setup() {
  size(800, 600);
}

void draw() {
}

void mousePressed() {
  int x = mouseX;
  int y = mouseY;
  int rojo = int(random(255));
  int verde = int(random(255));
  int azul = int(random(255));
  background(rojo,verde,azul);
  ellipse(x,y, 80,80);
}
