import pulsar
from pulsar.schema import *

class ReservaCitaEventConsumer:
    def __init__(self, client, topic_name, subscription_name):
        self.client = client
        self.topic_name = topic_name
        self.subscription_name = subscription_name

    def consume(self):
        # Suscribirse al tópico con el nombre dado y la suscripción dada
        consumer = self.client.subscribe(
            topic=self.topic_name,
            subscription_name=self.subscription_name,
            # Suponiendo que el evento está definido con un AvroSchema
            schema=AvroSchema(ReservaCitaEvent)
        )

        try:
            while True:
                # Esperar por el próximo mensaje
                msg = consumer.receive()
                try:
                    # Procesar el mensaje
                    event_data = msg.value()
                    self.process_event(event_data)
                    # Reconocer el mensaje como procesado
                    consumer.acknowledge(msg)
                except Exception as e:
                    # Manejar excepción sin reconocer el mensaje
                    print(f"Error al procesar el mensaje: {e}")
                    consumer.negative_acknowledge(msg)
        except Exception as e:
            print(f"Error al consumir mensajes: {e}")
        finally:
            # Cerrar el consumidor
            consumer.close()

    def process_event(self, event_data):
        # Implementar la lógica para procesar el evento
        # Por ejemplo, enviar una notificación al cliente o al agente
        print(f"Procesando evento: {event_data}")
        # Aquí iría la lógica para enviar notificaciones basadas en event_data

# Definir la estructura del evento con un esquema Avro
class ReservaCitaEvent(Record):
    cliente_id = String()
    propiedad_id = String()
    fecha_hora = String()
    agente_id = String()

# Crear una instancia del cliente Pulsar
client = pulsar.Client('pulsar://localhost:6650')

# Crear una instancia del consumidor de eventos
consumer = ReservaCitaEventConsumer(
    client=client,
    topic_name='persistent://public/default/reservas-citas',
    subscription_name='reserva-cita-subscription'
)

# Iniciar el consumo de eventos
consumer.consume()
