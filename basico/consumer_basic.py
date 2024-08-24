import pika

#consumer só se relaciona com uma queue

def minha_callback(ch, method, properties, body):
    '''função que toma a ação de quando eu receber a mensagem'''
    print(body)

connection_parameters = pika.ConnectionParameters( #informações para a conexao com o rabbitMQ
    host="localhost", 
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()  #cria um canal e se connecta ao rabbitMQ
channel.queue_declare(      #informa qual é a fila que ele esta se relacionado e espera consumir mensagens, essa fila foi criada na interface web do rabbitMQ                             # 
    queue="minha_fila",     #foi criado tambem uma excharge(que manda as msg para a fila) fazendo o bind(conexao) a essa fila
    durable=True
)
channel.basic_consume(      #informa a fila como sera consumida a fila, auto_ak é a confirmação automatica 
    queue="minha_fila",     #que ele devolvera para o rabbitmq informando que ele consumiu a msg
    auto_ack=True,
    on_message_callback=minha_callback
)

print(f'Listen RabbitMQ on Port 5672')
channel.start_consuming()       #esperando msgs da fila