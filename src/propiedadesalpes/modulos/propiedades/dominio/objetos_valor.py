"""Objetos valor del dominio de propiedades

En este archivo usted encontrará los objetos valor del dominio de propiedades

"""

from __future__ import annotations

from dataclasses import dataclass, field
from propiedadesalpes.seedwork.dominio.objetos_valor import ObjetoValor, Ciudad
from datetime import datetime
from enum import Enum


class EstadoReserva(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    CANCELADA = "Cancelada"
    PAGADA = "Pagada"

@dataclass(frozen=True)
class Ubicacion(ObjetoValor):
    ubicacion: str
    ciudad: Ciudad


@dataclass(frozen=True)
class ValorMercado(ObjetoValor):
    valor: float
    moneda: str    