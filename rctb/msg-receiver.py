#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='rc-events', exchange_type='topic')

result = channel.queue_declare(queue='client-test1', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='rc-events', queue=queue_name, routing_key='testkey')

def callback(ch, method, properties, body):
    print(body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()

