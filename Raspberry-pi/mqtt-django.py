import paho.mqtt.client as mqtt 
import requests
import json


# Broker MQTT Mosquito
broker = 'localhost'
port = 18083
client_id = 'aqua2'
# username = '*****'
# password = '*****'

# Topicos MQTT
topic_temp = "sensores/temperatura-plantas"
topic_hum = "sensores/umidade"
topic_ldr = "sensores/ldr"
topic_tds= "sensores/tds"
topic_temp_agua = "sensores/temperatura-agua"
topic_nivel = "sensores/nivel"

def on_message(client, userdata, message): 
  # Temperatura Plantas
  if message.topic == topic_temp:      
    nome = "Temperatura"
    tipo = "Plantas"
    grupo = "Grupo P"
    temperatura = str(message.payload.decode("utf-8"))
    unidade_medida = "graus" 
    temperatura_plantas = {'nome': nome, 'tipo': tipo, 'grupo': grupo, 'temperatura': temperatura, 'unidade_medida': unidade_medida}
    headers = {'Authorization': 'Token 2d75140c068049278f9cb7d39b1a20f05aecdc56'}
    url_temperatura_plantas = "http://127.0.0.1:8000/api/temperatura-plantas/"
    send_temperatura_plantas = requests.post(url_temperatura_plantas, headers = headers, json = temperatura_plantas)
    print(send_temperatura_plantas)
    print("Temperatura Plantas enviado com suceso")
  # Umidade
  if message.topic == topic_hum:    
    nome = "Umidade"
    tipo = "Plantas"
    grupo = "Grupo P"
    umidade = str(message.payload.decode("utf-8"))
    unidade_medida = "porcentagem" 
    umidade = {'nome': nome, 'tipo': tipo, 'grupo': grupo, 'umidade': umidade, 'unidade_medida': unidade_medida}
    headers = {'Authorization': 'Token 2d75140c068049278f9cb7d39b1a20f05aecdc56'}
    url_umidade = "http://127.0.0.1:8000/api/umidade/"
    send_umidade = requests.post(url_umidade, headers = headers, json = umidade)
    print(send_umidade)
    print("Umidade enviado com suceso")
  # LDR
  if message.topic == topic_ldr:
    nome = "LDR"
    tipo = "Plantas"
    grupo = "Grupo P"
    luminosidade = str(message.payload.decode("utf-8"))
    media_luminosidade = 30
    unidade_medida = "lumen" 
    luminosidade = {'nome': nome, 'tipo': tipo, 'grupo': grupo, 'luminosidade': luminosidade, 'media_luminosidade': media_luminosidade,'unidade_medida': unidade_medida}
    headers = {'Authorization': 'Token 2d75140c068049278f9cb7d39b1a20f05aecdc56'}
    url_ldr = "http://127.0.0.1:8000/api/ldr/"
    send_luminosidade = requests.post(url_ldr, headers = headers, json = luminosidade)
    print(send_luminosidade)
    print("LDR enviado com suceso")
  # TDS
  if message.topic == topic_tds:
    nome = "TDS"
    tipo = "Acuario"
    grupo = "Grupo A"
    tds = str(message.payload.decode("utf-8"))
    media_tds = 100
    unidade_medida = "ppm" 
    tds = {'nome': nome, 'tipo': tipo, 'grupo': grupo, 'tds': tds, 'media_tds': media_tds,'unidade_medida': unidade_medida}
    headers = {'Authorization': 'Token 2d75140c068049278f9cb7d39b1a20f05aecdc56'}
    url_tds = "http://127.0.0.1:8000/api/tds/"
    send_tds = requests.post(url_tds, headers = headers, json = tds )
    print(send_tds)
    print("TDS enviado com suceso")
  # Temperatura Acuario
  if message.topic == topic_temp_agua:
    nome = "Temperatura"
    tipo = "Acuario"
    grupo = "Grupo A"
    temperatura = str(message.payload.decode("utf-8"))
    unidade_medida = "graus" 
    temperatura_aquario = {'nome': nome, 'tipo': tipo, 'grupo': grupo, 'temperatura': temperatura, 'unidade_medida': unidade_medida}
    headers = {'Authorization': 'Token 2d75140c068049278f9cb7d39b1a20f05aecdc56'}
    url_temperatura_aquario = "http://127.0.0.1:8000/api/temperatura-aquario/"
    send_temperatura_aquario  = requests.post(url_temperatura_aquario, headers = headers, json = temperatura_aquario )
    print(send_temperatura_aquario)
    print("Temperatura Aquario enviado com suceso")
  # Nivel agua
  if message.topic == topic_nivel:
    nome = "Nível de Água"
    tipo = "Acuario"
    grupo = "Grupo A"
    nivel = str(message.payload.decode("utf-8"))
    nivel_minimo = 30
    unidade_medida = "centímetros" 
    nivel = {'nome': nome, 'tipo': tipo, 'grupo': grupo, 'nivel': nivel, 'nivel_minimo': nivel_minimo,'unidade_medida': unidade_medida}
    headers = {'Authorization': 'Token 2d75140c068049278f9cb7d39b1a20f05aecdc56'}
    url_nivel = "http://127.0.0.1:8000/api/nivel/"
    send_nivel  = requests.post(url_nivel, headers = headers, json = nivel )
    print(send_nivel)
    print("Nível Água enviado com suceso")
  
# Conexão com Broker MQTT Mosquito
def on_connect(client, userdata, flags, rc):     
  if rc==0:
     print("Conetado ao broker")     
     client.subscribe(topic_temp)
     client.subscribe(topic_hum)
     client.subscribe(topic_ldr)
     client.subscribe(topic_tds)
     client.subscribe(topic_temp_agua)
     client.subscribe(topic_nivel)

# Assinatura topicos do Broker MQTT Mosquito
def on_subscribe(client, userdata, mid, granted_qos):
    print(f'Cliente assinado a {topic_temp}')
    print(f'Cliente assinado a {topic_hum}')
      
      
client = mqtt.Client(client_id)            
client.on_connect=on_connect
client.on_subscribe = on_subscribe
client.on_message=on_message   
client.connect(broker)       
client.loop_forever()


    




