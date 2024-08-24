import pika
import json
from typing import Dict
from time import sleep

class RabbitMqPublisher:
    def __init__(self, excharge='minha_exchanges', routing_key='', host = 'localhost', port = 5672, username = 'guest', password = 'guest') -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password    
        self.__channel = self.__create_channel()
        self.exchange = excharge
        self.routing_key = routing_key
    
    def __create_channel(self):
        self.conect = pika.ConnectionParameters(host=self.host, port=self.port, 
                                           credentials=pika.PlainCredentials(username=self.username, password=self.password))
        channel = pika.BlockingConnection(self.conect).channel()
        return channel
    
    def send_message(self, msg: Dict):
        self.__channel.basic_publish(exchange=self.exchange, routing_key=self.routing_key, body=json.dumps(msg),
                                     properties=pika.BasicProperties(delivery_mode=2)) 





publishermq = RabbitMqPublisher()
x = 0
while True:
    sleep(1)
    publishermq.send_message(msg={'msg': 'minha mensagem', 'numero': x})
    x += 1