import pika

#publisher só se relaciona com excharge

connection_parameters = pika.ConnectionParameters(  #conexao
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="guest",
        password="guest"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel() #cria um canal e se conecta de fato

channel.basic_publish(
    exchange="minha_exchanges",  #informa o nome da excharge que ele vai mandar msg
    routing_key="",             
    body="estouMandandoUmaMensagem",
    properties=pika.BasicProperties(
        delivery_mode=2  #garante que a mensagem sera entregue/persistencia/durabilidade maior das mensagem/usado para exemplo:dados de transações
    )
)
