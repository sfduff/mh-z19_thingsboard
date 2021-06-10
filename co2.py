import mh_z19
import os
import sys
import paho.mqtt.client as mqtt
import json
import time

THINGSBOARD_HOST = '192.168.1.101'
ACCESS_TOKEN = '1vB0HkdQwXOd2xhMirVS'
# sensordata = {'temperature': 11, 'pressure' : 11, 'humidity': 11}

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()

try:
  while True:
    sensordata = mh_z19.read()
    client.publish('v1/devices/me/telemetry', json.dumps(sensordata), 1)
    time.sleep(30)

except KeyboardInterrupt:
  pass

client.loop_stop()
client.disconnect()
