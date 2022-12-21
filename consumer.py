import json
from kafka import KafkaConsumer

# channel
topic = 'topic'

# consumer
consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'], api_version=(0, 11, 5),
                         auto_offset_reset='earliest', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    message = message.value
    print(message['number'])