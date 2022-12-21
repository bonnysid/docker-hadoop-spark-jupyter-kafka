from kafka import KafkaProducer
from time import sleep
from datetime import date, time, datetime
import json

# channel
topic = 'topic'

# producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x: json.dumps(x).encode('utf-8'),
                         api_version=(0, 11, 5))

for e in range(1000):
    print('number', e)
    data = {
        'id': e,
        'cloudId': (e % 7) + 1,
        'date': date(2022, 12, e % 30 + 1).strftime('%m/%d/%Y'),
        'cost': 1000
    }
    producer.send(topic, value=data)
    sleep(1)