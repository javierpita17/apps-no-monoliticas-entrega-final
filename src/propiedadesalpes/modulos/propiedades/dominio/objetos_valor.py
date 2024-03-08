"""Objetos valor del dominio de propiedades

En este archivo usted encontrará los objetos valor del dominio de propiedades

"""

from __future__ import annotations

from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.objetos_valor import ObjetoValor, Codigo, Ruta, Locacion
from datetime import datetime
from enum import Enum


class EstadoReserva(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    CANCELADA = "Cancelada"
    PAGADA = "Pagada"