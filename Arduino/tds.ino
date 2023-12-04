// Utiliza as bibliotecas:
#include <EEPROM.h>
#include "GravityTDS.h"

// Numero do PIN
#define TdsSensorPin A4

GravityTDS gravityTds;

// Valor medio temperatura e valor minimo TDS
float media = 25, tdsValue = 0;

void setup()
{
  Serial.begin(9600);  
  gravityTds.setPin(TdsSensorPin);
  // Tensão 5v
  gravityTds.setAref(5.0);  
  // Valor máximo de arduino
  gravityTds.setAdcRange(1024);  
  // Ativar sensor
  gravityTds.begin(); 
}

// Ler valores
void loop()
{ 
  gravityTds.setTemperature(media);  
  gravityTds.update();  
  tdsValue = gravityTds.getTdsValue();   
  Serial.print(tdsValue,0);
  Serial.println("ppm");
  delay(100);
}
