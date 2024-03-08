"""Entidades del dominio de propiedades

En este archivo usted encontrará las entidades del dominio de propiedades

"""

from __future__ import annotations
from dataclasses import dataclass, field
import datetime

import propiedadesalpes.modulos.propiedades.dominio.objetos_valor as ov
from propiedadesalpes.modulos.propiedades.dominio.eventos.reservas import ReservaCreada, ReservaAprobada, ReservaCancelada, ReservaPagada
from propiedadesalpes.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad


@dataclass
class Reserva(AgregacionRaiz):
    id_cliente: uuid.UUID = field(hash=True, default=None)
    estado: ov.EstadoReserva = field(default=ov.EstadoReserva.PENDIENTE)

    def crear_reserva(self, reserva: Reserva):
        self.id_cliente = reserva.id_cliente
        self.estado = reserva.estado
        self.fecha_creacion = datetime.datetime.now()

        self.agregar_evento(ReservaCreada(id_reserva=self.id, id_cliente=self.id_cliente, estado=self.estado.name, fecha_creacion=self.fecha_creacion))
        # TODO Agregar evento de compensación        
