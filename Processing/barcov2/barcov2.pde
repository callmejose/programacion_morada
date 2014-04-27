
float yoff = 0.0;   //inicialización de variables para el ruido
float[] xoff = new float[10];
int numbarcos = 1;   //inicialización del conteo de barcos
int[] xbarcos = new int[10];   //coordenadas de los barcos
int sealevel;   //nivel del mar
float tetha = 0.0;   //inicialización de angulo
float inc = TWO_PI/100.0;   //incremento del angulo

void setup() {   //esta función se ejecuta una vez al principio
  size(800, 600);   //creación del lienzo de 800x600
  noStroke();   //las figuras que creare no tendrán bordes
  xbarcos[0] = width/2;   //el primer barco estará en la mitad
  xoff[0] = random(1000);   //inicialización aleatoria del ruido
  sealevel = height/2;   //y el nivel del mar estará en la mitad
}

void draw() {   //esta función se ejecuta todo el tiempo
  fill(150,225,250, 50);   //color de fondo con alfa bajo
  rect(0,0,width,height);  //rectángulo de fondo
  yoff += 0.01;   //desplazamiento de la función de ruido
  tetha += inc;   //desplazamiento de la función sinosoidal
  sealevel = int(sin(tetha) * height/80 + height/2 - height/160);
  for (int i = 0; i < numbarcos; i++){   //ciclo que se ejecuta "numbarcos" veces
    xoff[i] += 0.005;   //desplazamiento de la función de ruido para cada barco
    xbarcos[i] = pintarBarco(xbarcos[i],sealevel,xoff[i]);   //llamado a la función pintar barco
  }
  fill(27,44,170, 100);   //color del mar, alfa bajo
  rect(0,sealevel, width, height - sealevel);   //el mar sera un rectángulo
}

int pintarBarco(int x,int y, float myxoff) {   //definición de la función 'pintarBarco'
  x = int(noise(myxoff) * width/100 + x - width/200);   //calculo de las posiciones x , y con ruido
  y = int(noise(yoff) * height/50 + y - height/100 - 10);
  fill(106/2,99/2,54/2);   //colores del barco y figuras que lo componen (un rectángulo, un triangulo y un cudrilatero)
  rect(x,y-60,3,60);
  fill(195,199,81);
  triangle(x,y-10, x,y-60, x-50,y-10);
  fill(106,99,54);
  quad(x-50,y, x+50,y, x+30,y+20, x-30,y+20);
  return x;   //retorno de x que sera la nueva posición del barco
}

void mousePressed(){   //función que se ejecuta al presionar el mouse
  if (numbarcos < 10){  //se valida que el número de barcos permanezca en un máximo de 10
    xoff[numbarcos] = random(1000);   //inicialización aleatoria de la función de ruido
    xbarcos[numbarcos] = mouseX;   //se guarda la coordenada del mouse como la posición del nuevo barco
    numbarcos++;   //y se incrementa el conteo de barcos
  }
}
