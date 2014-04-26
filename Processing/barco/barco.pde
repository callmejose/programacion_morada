
float yoff = 0.0;   //inicialización de variables para el ruido
float xoff = 10.0;
int numbarcos = 1;   //inicialización del conteo de barcos
int[] xbarcos = new int[10];   //coordenadas de los barcos
int sealevel;   //nivel del mar

void setup() {   //esta función se ejecuta una vez al principio
  size(800, 600);   //creación del lienzo de 800x600
  noStroke();   //las figuras que creare no tendrán bordes
  xbarcos[0] = width/2;   //el primer barco estará en la mitad
  sealevel = height/2;   //y el nivel del mar estará en la mitad
}

void draw() {   //esta función se ejecuta todo el tiempo
  fill(150,225,250, 30);   //color de fondo con alfa bajo
  rect(0,0,width,height);  //rectángulo de fondo
  xoff += 0.01;   //desplazamiento en el ruido
  yoff += 0.02;
  for (int i = 0; i < numbarcos; i++){   //ciclo que se ejecuta "numbarcos" veces
    pintarBarco(xbarcos[i],sealevel);   //llamado a la función pintar barco
  }
  float ynoise = noise(yoff) * height/30 + sealevel + 3;   //calculo de la altura a la que se pintará el mar
  fill(27,44,170, 100);   //color del mar, alfa bajo
  rect(0,ynoise, width, height - ynoise);   //el mar sera un rectángulo
}

void pintarBarco(int x,int y) {   //definición de la función 'pintarBarco'
  x = int(noise(xoff) * width/30 + x);   //calculo de las posiciones x , y con ruido
  y = int(noise(yoff) * height/60 + y);
  fill(15,15,12);   //colores del barco y figuras que lo componen (un rectángulo, un triangulo y un cudrilatero)
  rect(x,y-60,3,60);
  fill(195,199,81);
  triangle(x,y-10, x,y-60, x-50,y-10);
  fill(106,99,54);
  quad(x-50,y, x+50,y, x+30,y+20, x-30,y+20);
}

void mousePressed(){   //función que se ejecuta al presionar el mouse
  if (numbarcos < 10){  //se valida que el número de barcos permanezca en un máximo de 10
    xbarcos[numbarcos] = mouseX;   //se guarda la coordenada del mouse como la posición del nuevo barco
    numbarcos++;   //y se incrementa el conteo de barcos
  }
}
