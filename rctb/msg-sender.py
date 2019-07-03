#!/usr/bin/env python3
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='rc-events', exchange_type='topic')

message = ' '.join(sys.argv[1:]) or "testmsg"
channel.basic_publish(exchange='rc-events', routing_key='testkey', body=message)
connection.close()

