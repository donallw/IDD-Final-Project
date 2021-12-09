import json
import paho.mqtt.client as mqtt
import uuid


topic = 'IDD/pilldispenser'

#this is the callback that gets called once we connect to the broker. 
#we should add our subscribe functions here as well
def on_connect(client, userdata, flags, rc):
	print(f"connected with result code {rc}")
	client.subscribe(topic)


# this is the callback that gets called each time a message is recived
def on_message(client, userdata, msg):
    if msg.topic == topic:
        val = msg.payload.decode('UTF-8')
        val = json.loads(val)
        with open('data.txt', 'w') as outfile:
            json.dump(val, outfile)
        

# Every client needs a random ID
client = mqtt.Client(str(uuid.uuid1()))
# configure network encryption etc
client.tls_set()
# this is the username and pw we have setup for the class
client.username_pw_set('idd', 'device@theFarm')

# attach out callbacks to the client
client.on_connect = on_connect
client.on_message = on_message

#connect to the broker
client.connect(
    'farlab.infosci.cornell.edu',
    port=8883)

# this is blocking. to see other ways of dealing with the loop
#  https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php#network-loop
client.loop_forever()