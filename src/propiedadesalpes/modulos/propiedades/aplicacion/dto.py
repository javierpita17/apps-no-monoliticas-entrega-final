from dataclasses import dataclass, field
from propiedadesalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ReservaDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)


@dataclass(frozen=True)
class PropiedadDTO(DTO):
    ubicacion: str = field(default_factory=str)
    valorMercado: float = field(default_factory=float)
    estadoActual: str = field(default_factory=str)
    tipo: str = field(default_factory=str)