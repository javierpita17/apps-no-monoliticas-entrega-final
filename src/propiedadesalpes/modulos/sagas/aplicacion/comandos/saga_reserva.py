from .comandos.manejar_reserva import CrearReservaCommand, CancelarReservaCommand
from .eventos.eventos_reserva import ReservaCreadaEvent, ReservaFallidaEvent

class ReservaSaga:
    def __init__(self, command_handler, event_publisher, repository):
        self.command_handler = command_handler
        self.event_publisher = event_publisher
        self.repository = repository

    def ejecutar_saga(self, datos_reserva):
        # Paso 1: Intentar crear la reserva
        crear_reserva_cmd = CrearReservaCommand(datos_reserva)
        reserva_id = self.command_handler.handle(crear_reserva_cmd)
        
        # Paso 2: Publicar evento de reserva creada
        reserva_creada_event = ReservaCreadaEvent(reserva_id=reserva_id)
        self.event_publisher.publish(reserva_creada_event)

        # Si algún paso falla, revertir los cambios anteriores
        try:
            # Supongamos que este es el punto donde algo podría fallar, por ejemplo,
            # el envío de una notificación falla y no queremos confirmar la reserva
            self.enviar_notificacion(datos_reserva)
        except Exception as e:
            # Paso 3: Si hay un error, cancelar la reserva y publicar el evento de fallo
            cancelar_reserva_cmd = CancelarReservaCommand(reserva_id)
            self.command_handler.handle(cancelar_reserva_cmd)
            
            reserva_fallida_event = ReservaFallidaEvent(reserva_id=reserva_id, razon=str(e))
            self.event_publisher.publish(reserva_fallida_event)
            raise

    def enviar_notificacion(self, datos_reserva):
        # Lógica para enviar notificación
        pass
