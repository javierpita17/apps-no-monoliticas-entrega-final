from propiedadesalpes.config.db import db 
from propiedadesalpes.modulos.propiedades.dominio.repositorios import RepositorioReservas, RepositorioEventosReservas
from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import EstadoReserva
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad, Reserva
from propiedadesalpes.modulos.propiedades.dominio.fabricas import FabricaPropiedades
from .dto import Reserva as ReservaDTO
from .dto import EventosReserva
from .mapeadores import MapeadorReserva, MapadeadorEventosReserva
from uuid import UUID
from pulsar.schema import *



class RepositorioReservasSQLAlchemy(RepositorioReservas):

    def __init__(self):
        self._fabrica_propiedades: FabricaPropiedades = FabricaPropiedades()

    @property
    def fabrica_propiedades(self):
        return self._fabrica_propiedades

    def obtener_por_id(self, id: UUID) -> Reserva:
        reserva_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(reserva_dto, MapeadorReserva())

    def obtener_todos(self) -> list[Reserva]:
        # TODO
        raise NotImplementedError

    def agregar(self, reserva: Reserva):
        reserva_dto = self.fabrica_propiedades.crear_objeto(reserva, MapeadorReserva())

        db.session.add(reserva_dto)

    def actualizar(self, reserva: Reserva):
        # TODO
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        # TODO
        raise NotImplementedError

class RepositorioEventosReservaSQLAlchemy(RepositorioEventosReservas):



    def obtener_por_id(self, id: UUID) -> Reserva:
        reserva_dto = db.session.query(ReservaDTO).filter_by(id=str(id)).one()
        return self.fabrica_propiedades.crear_objeto(reserva_dto, MapadeadorEventosReserva())

    def obtener_todos(self) -> list[Reserva]:
        raise NotImplementedError

    def agregar(self, evento):
        reserva_evento = self.fabrica_propiedades.crear_objeto(evento, MapadeadorEventosReserva())

        parser_payload = JsonSchema(reserva_evento.data.__class__)
        json_str = parser_payload.encode(reserva_evento.data)

        evento_dto = EventosReserva()
        evento_dto.id = str(evento.id)
        evento_dto.id_entidad = str(evento.id_reserva)
        evento_dto.fecha_evento = evento.fecha_creacion
        evento_dto.version = str(reserva_evento.specversion)
        evento_dto.tipo_evento = evento.__class__.__name__
        evento_dto.formato_contenido = 'JSON'
        evento_dto.nombre_servicio = str(reserva_evento.service_name)
        evento_dto.contenido = json_str

        db.session.add(evento_dto)

    def actualizar(self, reserva: Reserva):
        raise NotImplementedError

    def eliminar(self, reserva_id: UUID):
        raise NotImplementedError


