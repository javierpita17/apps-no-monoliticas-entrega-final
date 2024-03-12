from propertiesalpes.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass, field

from .objetos_valor import Ubicacion, ValorMercado

@dataclass
class User(Entidad):
    username: Username = field(default_factory=Ubicacion)
    password: Password = field(default_factory=ValorMercado)
    estadoActual: str = field(default_factory=str)
    tipo: str = field(default_factory=str)
