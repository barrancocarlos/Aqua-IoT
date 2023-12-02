
#define DELAY 500 
// Tensão 5v
#define VIN 5 
// Resistor
#define R 10000 

// Numero do PIN
const int sensorPin = A0; 

// Variáveis
int sensorVal; 
int lux; 

void setup(void) {
  Serial.begin(9600);
}

// Ler Valores
void loop(void) {
  sensorVal = analogRead(sensorPin);
  lux=sensorRawToPhys(sensorVal);
  Serial.print(F("O valor do sensor é = "));
  Serial.println(sensorVal); 
  Serial.print(F("O valor físico é = "));
  Serial.print(lux); 
  Serial.println(F(" lumen"));
  delay(DELAY);
}

// Convertidor
int sensorRawToPhys(int raw){  
  // Conversão analógico para tensão
  float Vout = float(raw) * (VIN / float(1024));
  // Conversão de tensão em resistência
  float RLDR = (R * (VIN - Vout))/Vout;
  // Resistência à conversão em lúmen 
  int phys=500/(RLDR/1000); 
  return phys;
}