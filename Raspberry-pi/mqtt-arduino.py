import paho.mqtt.client as mqtt 
import serial
import time
from textwrap import wrap

broker = 'localhost'
port = 18083
topic_temp = "sensores/temperatura"
topic_hum = "sensores/umidade"
topic_ldr = "sensores/ldr"
topic_tds= "sensores/tds"
topic_temp_agua = "sensores/temperatura-agua"
topic_nivel = "sensores/nivel"
client_id = 'aqua'
# username = '*****'
# password = '*****'

def on_connect(client, userdata, flags, rc):
   if rc==0:
     print("Conetado ao broker")
     
# Conexao USB com Arduino
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)
      
client = mqtt.Client(client_id)            
client.on_connect=on_connect 
client.connect(broker) 

#Loop
i = 0

while i < 1:
  # Ler sensor
    line = ser.readline()   
    if line:
        string = line.decode() 
        # Dividir os valores    
        temp, hum, ldr, tds, temp_agua, nivel = wrap(string, 5)
        # Temperatura  
        print(temp)                  
        client.publish(topic_temp, temp) # Publicar Temperatura no broker MQTT         
        print("Temperatura") # Mostrar Temperatura
        # Umidade 
        print(hum)  
        client.publish(topic_hum, hum) # Publicar Umidade no broker MQTT 
        print("Umidade") # Mostrar Umidade
        # LDR 
        print(ldr)  
        client.publish(topic_ldr, ldr) # Publicar LDR no broker MQTT 
        print("LDR") # Mostrar LDR
        # TDS
        print(tds)  
        client.publish(topic_tds, tds) # Publicar LDR no broker MQTT 
        print("TDS") # Mostrar TDS
        # Temperatura Agua
        print(temp_agua)                  
        client.publish(topic_temp_agua, temp_agua) # Publicar Temperatura Agua no broker MQTT         
        print("Temperatura Agua") # Mostrar Temperatura Agua
        # Nivel Agua
        print(nivel)                  
        client.publish(topic_nivel, nivel) # Publicar Nivel Agua no broker MQTT         
        print("Nivel Agua") # Mostrar Nivel Agua
ser.close()
           
