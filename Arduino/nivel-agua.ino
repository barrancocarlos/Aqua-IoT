// Numero do PIN
const int echo=4;
const int trigger=6;
// Variáveis ​​de cálculo
long tempo;
float distancia;

// Ativar sensor
void setup() 
{  
  pinMode(echo,INPUT);
  pinMode(trigger,OUTPUT);
  Serial.begin(9600);
  delay(100);
}

// Ler Valores
void loop() 
{
  calculo();
  
  Serial.print("Distância: ");
  Serial.print(distancia);     
  Serial.print("cm");
  Serial.println();
  
}

// Calculo
void calculo()
{
  digitalWrite(trigger,LOW);
  delayMicroseconds(2);
  digitalWrite(trigger,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger,LOW);
  
  tempo=pulseIn(echo,HIGH);
  // fórmula distância dividida pela velocidade do som
  distancia = float(tempo*0.0343)/2; 
  delay(10);
}
 
