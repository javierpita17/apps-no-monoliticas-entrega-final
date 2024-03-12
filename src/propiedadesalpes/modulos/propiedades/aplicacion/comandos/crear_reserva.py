from propiedadesalpes.seedwork.aplicacion.comandos import Comando
from propiedadesalpes.modulos.propiedades.aplicacion.dto import ReservaDTO
from .base import CrearReservaBaseHandler
from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from propiedadesalpes.modulos.propiedades.dominio.entidades import Reserva
from propiedadesalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto

