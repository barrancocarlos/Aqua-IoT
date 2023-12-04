// Utiliza as bibliotecas:
#include "DHT.h"
#include <OneWire.h> 
#include <DallasTemperature.h> 
#include <EEPROM.h>
#include "GravityTDS.h"

//LDR
#define DELAY 500 
// Tensão 5v
#define VIN 5 
// Resistor
#define R 10000 

// Numero do PIN
#define DHTPIN 2  
#define DS18B20 10    
#define TdsSensorPin A4
const int echo=4;
const int trigger=6;
const int sensorPin = A0; 

// Tipo de sensor
#define DHTTYPE DHT11   

// Ativar sensor
DHT dht(DHTPIN, DHTTYPE);
OneWire ourWire(DS18B20); 
DallasTemperature sensors(&ourWire);

GravityTDS gravityTds;
// Valor medio temperatura e valor minimo TDS
float media = 25, tdsValue = 0;

// Variáveis ​​de cálculo
long tempo;
float distancia;

// Variáveis LDR
int sensorVal; 
int lux; 

void setup() {
  Serial.begin(9600);
  Serial.println(F("Sensor Ativado"));

  dht.begin();

  sensors.begin(); 

  gravityTds.setPin(TdsSensorPin);
  // Tensão 5v
  gravityTds.setAref(5.0);  
  // Valor máximo de arduino
  gravityTds.setAdcRange(1024);  
  // Ativar sensor
  gravityTds.begin(); 

  pinMode(echo,INPUT);
  pinMode(trigger,OUTPUT);
  Serial.begin(9600);
  delay(100);
}

void loop() {
  // Aguardar 2 segundos
  delay(2000);

  // Ler umidade
  float h = dht.readHumidity();
  // Ler temperatura em Celsius
  float t = dht.readTemperature();
  // Ler temperatura em Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Messagem erro
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Erro na leitura do sensor"));
    return;
  }

  // Mostrar valores
  Serial.print(F("Umidade: "));
  Serial.print(h);
  Serial.print(F("%  Temperatura: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.println(F("°F"));

  // Temp Agua
  sensors.requestTemperatures();
  Serial.print("Temperatura: "); 
  Serial.print(sensors.getTempCByIndex(0)); 
  Serial.println("°C"); 

  // TDS
  gravityTds.setTemperature(media);  
  gravityTds.update();  
  tdsValue = gravityTds.getTdsValue();   
  Serial.print(tdsValue,0);
  Serial.println("ppm");
  delay(100);

  // Nivel Agua
  calculo();
  
  Serial.print("Distância: ");
  Serial.print(distancia);     
  Serial.print("cm");
  Serial.println();

  // LDR
  sensorVal = analogRead(sensorPin);
  lux=sensorRawToPhys(sensorVal);
  Serial.print(F("O valor do sensor é = "));
  Serial.println(sensorVal); 
  Serial.print(F("O valor físico é = "));
  Serial.print(lux); 
  Serial.println(F(" lumen"));
  delay(DELAY);


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

// Convertidor LDR
int sensorRawToPhys(int raw){  
  // Conversão analógico para tensão
  float Vout = float(raw) * (VIN / float(1024));
  // Conversão de tensão em resistência
  float RLDR = (R * (VIN - Vout))/Vout;
  // Resistência à conversão em lúmen 
  int phys=500/(RLDR/1000); 
  return phys;
}
