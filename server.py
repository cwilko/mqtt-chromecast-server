import sys
import subprocess
import configparser
import paho.mqtt.client as mqtt

config = configparser.ConfigParser()
config.read('server.ini')

MQTT_HOST = config.get("MQTT","host")
MQTT_PORT = config.getint("MQTT","port")
MQTT_TOPIC = config.get("MQTT","topic")

CAST_DEVICE = config.get("CHROMECAST","device")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(MQTT_TOPIC+"/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	msg_received = str(msg.payload.decode("utf-8"))
	print(msg.topic + " " + msg_received)

	if (msg.topic.endswith("stop")):
		print("Stopping cast...")
		subprocess.run(["catt", "stop"])
	elif (msg.topic.endswith("start")):
		print("Casting to device...")
		subprocess.run(["catt", "-d", CAST_DEVICE, "cast_site", msg_received])
    	

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, MQTT_PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()