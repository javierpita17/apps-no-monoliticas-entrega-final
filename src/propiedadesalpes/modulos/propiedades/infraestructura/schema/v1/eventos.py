from pulsar.schema import *
from propiedadesalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
from propiedadesalpes.seedwork.infraestructura.utils import time_millis
import uuid

class ReservaCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()



class EventoReservaCreada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ReservaCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)