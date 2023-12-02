import paho.mqtt.client as mqtt 
import requests
import json


broker = 'localhost'
port = 18083
topic = "sensores/temperatura"
client_id = 'aqua2'
# username = '*****'
# password = '*****'

def on_message(client, userdata, message):  
  print("mensagem =",str(message.payload.decode("utf-8")))
  url = 'http://127.0.0.1:8000/api/temperatures/'
  tempobj = {'value': str(message.payload.decode("utf-8"))}
  x = requests.post(url, json = tempobj)
  print("Enviar para Django =", x.text)
  

def on_connect(client, userdata, flags, rc):     
  if rc==0:
     print("Conetado ao broker")     
     client.subscribe(topic)

def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Cliente assinado a {topic}')
      
      
client = mqtt.Client(client_id)            
client.on_connect=on_connect
client.on_subscribe = on_subscribe
client.on_message=on_message   
client.connect(broker)       
client.loop_forever()


    




