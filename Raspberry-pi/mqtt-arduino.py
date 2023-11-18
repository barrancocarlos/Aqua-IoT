import paho.mqtt.client as mqtt 
import serial
import time
from textwrap import wrap

broker = 'localhost'
port = 18083
topic = "sensores/temperatura"
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
    line = ser.readline()   # Ler sensor
    if line:
        string = line.decode()     
        temp, hum = wrap(string, 5)  # Dividir os valores
        print(temp)            
        client.publish(topic, temp) # Publicar no MQTT
        # Mostrar os valores
        print("Temperatura") 
        print(hum)  
        client.publish(topic, hum)
        print("Umidade") 
ser.close()
           
