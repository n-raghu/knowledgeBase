from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers': '10.0.0.10',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()
