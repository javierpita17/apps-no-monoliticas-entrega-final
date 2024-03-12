from propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from propiedadesalpes.seedwork.infraestructura.utils import unix_time_millis
from propiedadesalpes.modulos.propiedades.dominio.objetos_valor import Ciudad, Ubicacion, EstadoReserva
from propiedadesalpes.modulos.propiedades.dominio.entidades import Propiedad, Reserva, ReservaCreada
from propiedadesalpes.modulos.propiedades.dominio.eventos.reservas import ReservaAprobada, ReservaCancelada, ReservaAprobada, ReservaPagada, ReservaCreada, EventoReserva

from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion

from .dto import Reserva as ReservaDTO

from pulsar.schema import *


class MapadeadorEventosReserva(Mapeador):

    
    # Versiones aceptadas
    versions = ('v1',)

    LATEST_VERSION = versions[0]

    def __init__(self):
        self.router = {
            ReservaCreada: self._entidad_a_reserva_creada
        }

    def obtener_tipo(self) -> type:
        return EventoReserva.__class__

    def es_version_valida(self, version):
        for v in self.versions:
            if v == version:
                return True
        return False

    def _entidad_a_reserva_creada(self, entidad: ReservaCreada, version=LATEST_VERSION):
        def v1(evento):
            from .schema.v1.eventos import ReservaCreadaPayload, EventoReservaCreada

            payload = ReservaCreadaPayload(
                id_reserva=str(evento.id_reserva), 
                id_cliente=str(evento.id_cliente), 
                estado=str(evento.estado), 
                fecha_creacion=int(unix_time_millis(evento.fecha_creacion))
            )
            evento_integracion = EventoReservaCreada(id=str(evento.id))
            evento_integracion.id = str(evento.id)
            evento_integracion.time = int(unix_time_millis(evento.fecha_creacion))
            evento_integracion.specversion = str(version)
            evento_integracion.type = 'ReservaCreada'
            evento_integracion.datacontenttype = 'AVRO'
            evento_integracion.service_name = 'aeroalpes'
            evento_integracion.data = payload

            return evento_integracion
                    
        if not self.es_version_valida(version):
            raise Exception(f'No se sabe procesar la version {version}')

        if version == 'v1':
            return v1(entidad)       

    def _entidad_a_reserva_aprobada(self, entidad: ReservaAprobada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError
    
    def _entidad_a_reserva_cancelada(self, entidad: ReservaCancelada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError
    
    def _entidad_a_reserva_pagada(self, entidad: ReservaPagada, version=LATEST_VERSION):
        # TODO
        raise NotImplementedError

    def entidad_a_dto(self, entidad: EventoReserva, version=LATEST_VERSION) -> ReservaDTO:
        if not entidad:
            raise NoExisteImplementacionParaTipoFabricaExcepcion
        func = self.router.get(entidad.__class__, None)

        if not func:
            raise NoExisteImplementacionParaTipoFabricaExcepcion

        return func(entidad, version=version)

    def dto_a_entidad(self, dto: ReservaDTO, version=LATEST_VERSION) -> Reserva:
        raise NotImplementedError


class MapeadorReserva(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'


    def obtener_tipo(self) -> type:
        return Reserva.__class__

    def entidad_a_dto(self, entidad: Reserva) -> ReservaDTO:
        
        reserva_dto = ReservaDTO()
        reserva_dto.fecha_creacion = entidad.fecha_creacion
        reserva_dto.fecha_actualizacion = entidad.fecha_actualizacion
        reserva_dto.id = str(entidad.id)

        itinerarios_dto = list()
        
        for itinerario in entidad.itinerarios:
            itinerarios_dto.extend(self._procesar_itinerario(itinerario))

        reserva_dto.itinerarios = itinerarios_dto

        return reserva_dto

    def dto_a_entidad(self, dto: ReservaDTO) -> Reserva:
        reserva = Reserva(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        reserva.itinerarios = list()

        return reserva

