// Utiliza as bibliotecas:
#include <OneWire.h> 
#include <DallasTemperature.h> 

// Numero do PIN
#define DS18B20 10 

// Ativar sensor
OneWire ourWire(DS18B20); 
DallasTemperature sensors(&ourWire);

void setup(){
  Serial.begin(9600);
  sensors.begin(); 
  delay(1000); 
}

// Ler Valores 
void loop(){
  sensors.requestTemperatures();
  Serial.print("Temperatura: "); 
  Serial.print(sensors.getTempCByIndex(0)); 
  Serial.println("°C"); 
  delay(250);
}