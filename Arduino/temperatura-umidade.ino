// Utiliza as bibliotecas:
// - DHT Sensor Library: https://github.com/adafruit/DHT-sensor-library
// - Adafruit Unified Sensor Lib: https://github.com/adafruit/Adafruit_Sensor

#include "DHT.h"

// Numero do PIN
#define DHTPIN 2     

// Tipo de sensor
#define DHTTYPE DHT11   

// Ativar sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  Serial.println(F("Sensor Ativado"));

  dht.begin();
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
}
