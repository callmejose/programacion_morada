
float yoff = 0.0;
float xoff = 10.0;
int numbarcos = 1;
int[] xbarcos = new int[10];
int sealevel;

void setup() {
  size(800, 600);
  noStroke();
  xbarcos[0] = width/2;
  sealevel = height/2;
}

void draw() {
  fill(150,225,250, 30);
  rect(0,0,width,height);
  xoff += 0.01;
  yoff += 0.02;
  for (int i = 0; i < numbarcos; i++){
    pintarBarco(xbarcos[i],sealevel);
  }
  float ynoise = noise(yoff) * height/30 + sealevel + 3;
  fill(27,44,170, 100);
  rect(0,ynoise, width, height - ynoise);
}

void pintarBarco(int x,int y) {
  x = int(noise(xoff) * width/30 + x);
  y = int(noise(yoff) * height/60 + y);
  fill(15,15,12);
  rect(x,y-60,3,60);
  fill(195,199,81);
  triangle(x,y-10, x,y-60, x-50,y-10);
  fill(106,99,54);
  quad(x-50,y, x+50,y, x+30,y+20, x-30,y+20);
}

void mousePressed(){
  if (numbarcos < 10){
    xbarcos[numbarcos] = mouseX;
    numbarcos++;
  }
}
