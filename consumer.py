from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'ftl',
    'auto.offset.reset': 'earliest',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'admin',
    'sasl.password': 'admin',
    'security.protocol': 'sasl_plaintext'
})

c.subscribe(['test']) # topic 'test'

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

c.close()