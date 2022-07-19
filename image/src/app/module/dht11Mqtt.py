import time
import board
import adafruit_dht
import paho.mqtt.client as mqttClient
import json


# Initialisieren Sie das dht-Ger  t, wobei der Datenpin mit Pin 16 (GPIO 23) des Raspberry Pi verbunden ist:
dhtDevice = adafruit_dht.DHT11(board.D23)

# Sie k  nnen DHT22 use_pulseio=False   bergeben, wenn Sie pulseio nicht verwenden m  chten.
# Dies kann auf einem Linux-Einplatinencomputer wie dem Raspberry Pi notwendig sein,
# aber es wird nicht in CircuitPython funktionieren.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

def on_connect(client, userdata, flags, return_code):
    '''
    Connect to the MQTT broker
    '''
    if return_code == 0:
        print("Connected to broker")
        global CONNECTED
        CONNECTED = True
    else:
        print("Connection failed")
        

CONNECTED = False
BROKER_ADDRESS = "localhost"
PORT = 1883

# connect with client 
print("connecting to MQTT")
client = mqttClient.Client()
client.on_connect = on_connect
client.connect(host=BROKER_ADDRESS, port=PORT)

while True:
    try:
        # Drucken der Werte   ber die serielle Schnittstelle
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        timestamp = time.time()
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
        client.publish("rpi_temp", '{"temp_data" : %s, "timestamp" :  %s }' % (temperature_c, timestamp))
        client.publish("rpi_humidity", '{"humidity_data" : %s, "timestamp" :  %s }' % (humidity, timestamp))

    except RuntimeError as error:
        # Fehler passieren ziemlich oft, DHT's sind schwer zu lesen, einfach weitermachen
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(1.0)

  