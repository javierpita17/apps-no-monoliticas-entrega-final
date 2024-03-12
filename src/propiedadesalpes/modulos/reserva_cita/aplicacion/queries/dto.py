from dataclasses import dataclass, field
from propertiesalpes.seedwork.aplicacion import DTO

@dataclass(frozen=True)
class ReservaCitaDTO(DTO):
    cliente_id: str = field(default_factory=str)
    propiedad_id: str = field(default_factory=str)
    fecha_hora: str = field(default_factory=str)
    agente_id: str = field(default_factory=str)  # ID del agente que muestra la propiedad
