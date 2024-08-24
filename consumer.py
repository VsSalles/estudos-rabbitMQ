import pika 

class RabbitMqConsumer:
    def __init__(self, callback, queue = 'minha_fila', host = 'localhost', port = 5672, username = 'guest', password = 'guest') -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.queue = queue
        self.callback = callback        
        self.__channel = self.__create_channel()
    
    def __create_channel(self):
        self.conect = pika.ConnectionParameters(host=self.host, port=self.port, 
                                           credentials=pika.PlainCredentials(username=self.username, password=self.password))
        channel = pika.BlockingConnection(self.conect).channel()
        channel.queue_declare(queue="minha_fila",  durable=True, arguments={'x-overflow': 'reject-publish'})
        channel.basic_consume(queue="minha_fila", auto_ack=True, on_message_callback=self.callback)
        return channel
    
    def start(self):
        print(f'Listen RabbitMQ on Port 5672')
        self.__channel.start_consuming()  


def minha_callback(ch, method, properties, body):
    print(body)

consumerMQ = RabbitMqConsumer(callback=minha_callback)
consumerMQ.start()

