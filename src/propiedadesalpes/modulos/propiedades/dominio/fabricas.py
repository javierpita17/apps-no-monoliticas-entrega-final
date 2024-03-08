""" Fábricas para la creación de objetos del dominio de propiedades

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de propiedades

"""

from .entidades import Reserva
from propiedadesalpes.seedwork.dominio.repositorios import Mapeador
from propiedadesalpes.seedwork.dominio.fabricas import Fabrica
from propiedadesalpes.seedwork.dominio.entidades import Entidad
from propiedadesalpes.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaReserva(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador ) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            reserva: Reserva = mapeador.dto_a_entidad(obj)

            return reserva

@dataclass
class FabricaPropiedades(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Reserva.__class__:
            fabrica_reserva = _FabricaReserva()
            return fabrica_reserva.crear_objeto(obj, mapeador)
        else:
            return fabrica_reserva.crear_objeto(obj, mapeador) # colocar una Excepcion si es necesario

