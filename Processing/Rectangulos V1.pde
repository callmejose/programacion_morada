size(800, 600);
background(random(255),random(255),random(255));
for(int i=0; i<1000; i++) {
  fill(random(0, 255), random(0, 255), random(0, 255));
  int px = (int) random(0, 800);
  int py = (int) random(0, 600);
  int ax = (int) random(0,400);
  int ay = (int) random(0,400);
  rect(px,py,ax,ay); 
}
